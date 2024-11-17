import os
import string
import random
import urllib
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
    state = request.args.get('state', None)
    stored_state = request.cookies.get(state_key) if request.cookies else None


    print(f"callback:") #!TEST
    print(f"Code: {code}") #!TEST
    print(f"Req state: {state} - Stored state: {stored_state}") #!TEST

    if (state is None) or (state != stored_state):
        print("State mismatch :(")
        query_params = urllib.parse.urlencode({'error': 'state_mismatch'})
        return redirect(f"/err?{query_params}")
    else:
        print("No state mismatch")

    return render_template('login-callback/login-callback.html')


#? ERROR
@app.route('/err')
def error():
    error_message = request.args.get('error', 'Unknown error occurred')
    errorTemplatePath = "err/error.html"
    return render_template(errorTemplatePath, error_message=error_message)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port="8888", debug=True)