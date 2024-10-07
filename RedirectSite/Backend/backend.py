import os
import string
import random
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
    print(f'\nState in login: {state}\n\n')
    scope = 'user-read-private user-read-email'

    host = request.host_url.rstrip('/')
    
    REDIRECT_URI = f"{host}/callback"

    # params = {
    #     'response_type': 'code',
    #     'client_id': CLIENT_ID,
    #     'scope': scope,
    #     'redirect_uri': REDIRECT_URI,
    #     'state': state
    # }

    # url = 'https://accounts.spotify.com/authorize?' + urllib.parse.urlencode(params)

    # return redirect(url)

    response = make_response(redirect('https://accounts.spotify.com/authrize?' +
    urlencode({
        'response_type': 'code',
        'client_id': CLIENT_ID,
        'scope': scope,
        'redirect_uri': REDIRECT_URI,
        'state': state
    })))
    print(f"Redirect URI: {REDIRECT_URI}")

    response.set_cookie(STATE_KEY, state)
    return response


@app.route('/callback')
def callback():
    code = request.args.get('code')
    state = request.args.get('state')
    stored_state = request.cookies.get(STATE_KEY)

    print(f"callback:")
    print(f"Code: {code}")
    print(f"Req state: {state} - Stored state: {stored_state}")

    if stored_state == state:
        print("No state mismatch")
    else:
        print("State mismatch :(")

    return render_template('login-callback/login-callback.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port="8888", debug=True)