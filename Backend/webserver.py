import os
from flask import Flask, request, render_template

from DOMAIN.secretAccess.userData import get_client_id, get_client_secret
from DOMAIN.EndpointLogin.login import loginResponse
from DOMAIN.EndpointCallback.callback import callbackResponse
from DOMAIN.EndpointCreatePlaylist.createPlaylistEndpoint import createPlaylistRespone


CLIENT_ID = get_client_id()
CLIENT_SECRET = get_client_secret()
SCOPE = 'playlist-modify-public playlist-modify-private'
STATE_KEY_COOKIE = 'spotify_auth_state'
ACCESS_TOKEN_COOKIE = "spotify_access_token"
REFRESH_TOKEN_COOKIE = "spotify_refresh_token"

WEB_FOLDER_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Frontend'))

app = Flask(__name__, template_folder=WEB_FOLDER_PATH, static_folder=WEB_FOLDER_PATH)


@app.route('/')
def home():
    homeTemplatePath = "home/home.html"
    return render_template(homeTemplatePath)


@app.route('/login')
def login():
    return loginResponse(CLIENT_ID, SCOPE, STATE_KEY_COOKIE)


@app.route('/callback')
def callback():
    return callbackResponse(STATE_KEY_COOKIE, CLIENT_ID, CLIENT_SECRET, ACCESS_TOKEN_COOKIE, REFRESH_TOKEN_COOKIE)


@app.route('/err')
def error():
    error_message = request.args.get('error', 'Unknown error occurred')
    errorTemplatePath = "err/error.html"
    return render_template(errorTemplatePath, error_message=error_message)


@app.route('/createPlaylist', methods=['POST'])
def createPlaylist():
    return createPlaylistRespone(ACCESS_TOKEN_COOKIE)


#? START WEBSERVER
if __name__ == '__main__':
    app.run(host='0.0.0.0', port="8888", debug=True)