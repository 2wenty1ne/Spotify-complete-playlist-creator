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
STATE_KEY = 'spotify_auth_state'

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
    response.set_cookie(STATE_KEY, state) #? Lasts as long as the browser session

    return response


@app.route('/callback')
def callback():
    code = request.args.get('code', None) #? Code if auth successfull
    auth_error = request.args.get('error', None)
    login_gen_state = request.args.get('state', None)
    cookie_state = request.cookies.get(STATE_KEY) if request.cookies else None 

    #? Error redirect if theres an error
    if (error):
        query_error_params = urllib.parse.urlencode({'error': auth_error})
        return redirect(f"/err?{query_error_params}")

    #? Error redirect if state returned from spotify auth doesnt equal the state produced in login  
    if (login_gen_state is None) or (login_gen_state != cookie_state):
        query_state_mismatch_params = urllib.parse.urlencode({'error': 'state_mismatch'})
        return redirect(f"/err?{query_state_mismatch_params}")

    #? Error redirect if there is code and error is None - unknown
    if (code is None):
        query_unknown_error_params = urllib.parse.urlencode({'error': 'unknown_error'})
        return redirect(f"/err?{query_error_params}")
    

    response = make_response()
    response.delete_cookie(STATE_KEY) #TODO Check using dev tools if this works else "response.set_cookie(state_key, '', expires=0)"
    print(dir(response))
    
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

    token_response = requests.post(initial_access_token_url, data=initial_access_token_payload, headers=initial_access_token_headers)
    if token_response.status_code == 200:
        tokens = token_response.json()

        access_token = tokens['access_token']
        refresh_token = tokens['refresh_token']

        #! Test access token
        user_info_url = "https://api.spotify.com/v1/me"
        user_headers = {"Authorization": f"Bearer {access_token}"}
        user_response = requests.get(user_info_url, headers=user_headers)

        if response.status_code == 200: #? Should be user_response instead of response
            print("User Info:", user_response.json())


    #? Redirect back home after successfully getting access token 
    return redirect(f"/")


#? ERROR
@app.route('/err')
def error():
    error_message = request.args.get('error', 'Unknown error occurred')
    errorTemplatePath = "err/error.html"
    return render_template(errorTemplatePath, error_message=error_message)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port="8888", debug=True)