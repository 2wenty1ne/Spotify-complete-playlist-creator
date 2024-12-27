from DOMAIN.requestHandling.sendRequest import send_request

def getUserID(token):
    userIDUrl = "https://api.spotify.com/v1/me"
    authed_headers = {'Authorization': f'Bearer {token}'}

    userID_respone = send_request("get", userIDUrl, headers=authed_headers)

    return userID_respone.json()
