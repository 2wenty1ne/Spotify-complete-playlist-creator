import os
import string
import random
import urllib
import base64
import requests
from urllib.parse import urlencode
from flask import Flask, redirect, request, render_template, make_response

from secretAccess.userData import get_client_id, get_client_secret


CLIENT_ID = get_client_id()
CLIENT_SECRET = get_client_secret()
STATE_KEY_COOKIE = 'spotify_auth_state'
ACCESS_TOKEN_COOKIE = "spotify_access_token"
REFRESH_TOKEN_COOKIE = "spotify_refresh_token"

WEB_FOLDER_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'node_project'))

app = Flask(__name__, template_folder=WEB_FOLDER_PATH, static_folder=WEB_FOLDER_PATH)

def generate_random_string(length):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))


@app.route('/')
def home():
    homeTemplatePath = "home/home.html"
    return render_template(homeTemplatePath)


@app.route('/login')
def login():
    state = generate_random_string(16) #? State generated
    scope = 'user-read-private user-read-email'

    host = request.host_url.rstrip('/')

    REDIRECT_URI = f"{host}/callback"

    params = {
        'response_type': 'code',
        'client_id': CLIENT_ID,
        'scope': scope,
        'redirect_uri': REDIRECT_URI,
        'state': state
    }

    url = 'https://accounts.spotify.com/authorize?' + urllib.parse.urlencode(params)

    response = redirect(url)
    response.set_cookie(STATE_KEY_COOKIE, state) #? Lasts as long as the browser session

    return response


@app.route('/callback')
def callback():
    code = request.args.get('code', None) #? Code if auth successfull
    auth_error = request.args.get('error', None)
    login_gen_state = request.args.get('state', None)
    cookie_state = request.cookies.get(STATE_KEY_COOKIE) if request.cookies else None 


    #? Error redirect if theres an error
    if (auth_error is not None):
        print(f"AuthError: {auth_error}")
        query_error_params = urllib.parse.urlencode({'error': auth_error})
        return redirect(f"/err?{query_error_params}")


    #? Error redirect if state returned from spotify auth doesnt equal the state produced in login  
    if (login_gen_state is None) or (login_gen_state != cookie_state):
        query_state_mismatch_params = urllib.parse.urlencode({'error': 'state_mismatch'})
        return redirect(f"/err?{query_state_mismatch_params}")


    #? Error redirect if there is code and error is None - unknown
    if (code is None):
        query_unknown_error_params = urllib.parse.urlencode({'error': 'unknown_error'})
        return redirect(f"/err?{query_unknown_error_params}")


    response = make_response()
    response.delete_cookie(STATE_KEY_COOKIE)

    response.headers['Location'] = f"/"
    response.status_code = 302
    

    initial_access_token_url = "https://accounts.spotify.com/api/token"
    auth_header = base64.b64encode(f"{CLIENT_ID}:{CLIENT_SECRET}".encode()).decode()

    #? Redirect URI only for validation (Needs to be in the list of accepted redirect URIs)
    host = request.host_url.rstrip('/')
    REDIRECT_URI = f"{host}/callback"

    initial_access_token_payload = {
        "code": code,
        "redirect_uri": REDIRECT_URI,
        "grant_type": "authorization_code"
    }
    initial_access_token_headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": f"Basic {auth_header}"
    }

    token_response = requests.post(
        initial_access_token_url, 
        data=initial_access_token_payload, 
        headers=initial_access_token_headers)
    
    #? Redirect early to error page if an error accured getting access token
    if token_response.status_code != 200:
        access_token_err_params = urllib.parse.urlencode({'error': token_response.status_code})
        response.headers['Location'] = f"/err?{access_token_err_params}"
        return response


    tokens = token_response.json()

    access_token = tokens['access_token']
    refresh_token = tokens['refresh_token']

    response.set_cookie(ACCESS_TOKEN_COOKIE, access_token)
    response.set_cookie(REFRESH_TOKEN_COOKIE, refresh_token)

    #! Test access token
    # user_info_url = "https://api.spotify.com/v1/me"
    # user_headers = {"Authorization": f"Bearer {access_token}"}
    # user_response = requests.get(user_info_url, headers=user_headers)

    # if user_response.status_code == 200:
    #     print("User Info:", user_response.json())


    #? Redirect back home after successfully getting access token
    return response


#? ERROR
@app.route('/err')
def error():
    error_message = request.args.get('error', 'Unknown error occurred')
    errorTemplatePath = "err/error.html"
    return render_template(errorTemplatePath, error_message=error_message)


@app.route('/createPlaylist')
def createPlaylist():

    #TODO redirect back to home
    pass


if __name__ == '__main__':
    app.run(host='0.0.0.0', port="8888", debug=True)