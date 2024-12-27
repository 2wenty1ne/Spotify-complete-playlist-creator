from DOMAIN.requestHandling.sendRequest import send_request

def checkArtistID(accessToken, artistID):
    artistURL = f"https://api.spotify.com/v1/artists/{artistID}"

    authed_headers = {'Authorization': f'Bearer {accessToken}'}

    artist_respone = send_request("get", artistURL, headers=authed_headers)

    if artist_respone.status_code == 404:
        return False
    
    return True
