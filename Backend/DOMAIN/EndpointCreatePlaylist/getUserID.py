from DOMAIN.requestHandling.sendRequest import send_request

def getUserID(token):
    userIDUrl = "https://api.spotify.com/v1/me"

    userID_respone = send_request("get", userIDUrl, token)

    return userID_respone.json()
