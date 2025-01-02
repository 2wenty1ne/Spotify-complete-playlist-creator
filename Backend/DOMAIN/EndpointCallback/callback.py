import time
import json
import urllib
import base64
from flask import request, make_response

from DOMAIN.requestHandling.sendRequest import send_request

#TODO rename func
#TODO Dont always redirect to /err, return to home and show error message
def callbackResponse(STATE_KEY_COOKIE, CLIENT_ID, CLIENT_SECRET, ACCESS_TOKEN_COOKIE, REFRESH_TOKEN_COOKIE):
    code = request.args.get('code', None) #? Code if auth successfull
    auth_error = request.args.get('error', None)
    login_gen_state = request.args.get('state', None)
    cookie_state = request.cookies.get(STATE_KEY_COOKIE) if request.cookies else None 


    #? Error redirect if theres an error
    if (auth_error is not None):
        print(f"AuthError: {auth_error}") #! TEST
        query_error_params = urllib.parse.urlencode({'error': auth_error})
        return redirect(f"/err?{query_error_params}") #! Err redirect


    #? Error redirect if state returned from spotify auth doesnt equal the state produced in login  
    if (login_gen_state is None) or (login_gen_state != cookie_state):
        query_state_mismatch_params = urllib.parse.urlencode({'error': 'state_mismatch'})
        return redirect(f"/err?{query_state_mismatch_params}") #! Err redirect


    #? Error redirect if there is code and error is None - unknown
    if (code is None):
        query_unknown_error_params = urllib.parse.urlencode({'error': 'unknown_error'})
        return redirect(f"/err?{query_unknown_error_params}") #! Err redirect


    response = make_response()
    response.delete_cookie(STATE_KEY_COOKIE)


    response.headers['Location'] = f"/"
    response.status_code = 302

    initial_access_token_url = "https://accounts.spotify.com/api/token"
    auth_payload = base64.b64encode(f"{CLIENT_ID}:{CLIENT_SECRET}".encode()).decode()

    #? Redirect URI only for validation (Needs to be in the list of accepted redirect URIs)
    host = request.host_url.rstrip('/')
    redirect_uri = f"{host}/callback"

    initial_access_token_payload = {
        "code": code,
        "redirect_uri": redirect_uri,
        "grant_type": "authorization_code"
    }


    token_response = send_request(
        "post", initial_access_token_url, auth_payload, 
        headerType="tokenGen",
        data=initial_access_token_payload, 
        )
    
    #? Redirect early to error page if an error accured getting access token
    if token_response.status_code != 200:
        print(f"Error getting token {token_response.text}") #! TEST
        access_token_err_params = urllib.parse.urlencode({'error': token_response.status_code})
        response.headers['Location'] = f"/err?{access_token_err_params}" #! Err redirect
        return response


    tokens = token_response.json()

    access_token = tokens['access_token']

    one_hour_in_secs = 3600
    expiration_time = time.time() + one_hour_in_secs

    access_token = json.dumps({
        'value': tokens['access_token'],
        'expiration': expiration_time
    })
    refresh_token = tokens['refresh_token']

    response.set_cookie(ACCESS_TOKEN_COOKIE, access_token)
    response.set_cookie(REFRESH_TOKEN_COOKIE, refresh_token)

    #? Redirect back home after successfully getting access token
    return response

