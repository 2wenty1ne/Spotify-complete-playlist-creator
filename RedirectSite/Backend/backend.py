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
    state = generate_random_string(16)
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
    response.set_cookie(STATE_KEY, state)

    return response


@app.route('/callback')
def callback():
    code = request.args.get('code', None)
    error = request.args.get('error', None)
    state = request.args.get('state', None)
    stored_state = request.cookies.get(STATE_KEY) if request.cookies else None

    if (error):
        query_error_params = urllib.parse.urlencode({'error': error})
        return redirect(f"/err?{query_error_params}")



    if (state is None) or (state != stored_state):
        query_state_mismatch_params = urllib.parse.urlencode({'error': 'state_mismatch'})
        return redirect(f"/err?{query_state_mismatch_params}")

    if (code is None):
        query_unknown_error_params = urllib.parse.urlencode({'error': 'unknown_error'})
        return redirect(f"/err?{query_error_params}")
    
    response = make_response()
    response.delete_cookie(STATE_KEY)
    
    auth_url = "https://accounts.spotify.com/api/token"
    auth_header = base64.b64encode(f"{CLIENT_ID}:{CLIENT_SECRET}".encode()).decode()

    host = request.host_url.rstrip('/')
    REDIRECT_URI = f"{host}/callback"

    auth_payload = {
        "code": code,
        "redirect_uri": REDIRECT_URI,
        "grant_type": "authorization_code"
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": f"Basic {auth_header}"
    }

    token_response = requests.post(auth_url, data=auth_payload, headers=headers)
    if token_response.status_code == 200:
        tokens = token_response.json()

        access_token = tokens['access_token']
        refresh_token = tokens['refresh_token']

        user_info_url = "https://api.spotify.com/v1/me"
        user_headers = {"Authorization": f"Bearer {access_token}"}
        user_response = requests.get(user_info_url, headers=user_headers)

        if response.status_code == 200:
            print("User Info:", user_response.json())

    return redirect(f"/")


#? ERROR
@app.route('/err')
def error():
    error_message = request.args.get('error', 'Unknown error occurred')
    errorTemplatePath = "err/error.html"
    return render_template(errorTemplatePath, error_message=error_message)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port="8888", debug=True)