from DOMAIN.requestHandling.sendRequest import send_request

def checkArtistID(accessToken, artistID):
    artistURL = f"https://api.spotify.com/v1/artists/{artistID}"

    artist_respone = send_request("get", artistURL, accessToken)

    print(f"ID check code: {artist_respone.status_code}")
    print(f"Artist response: {artist_respone.json()}")

    if artist_respone.status_code == 404 or artist_respone.status_code == 400:
        return False, None
    
    artist_name = artist_respone.json()["name"]

    return True, artist_name
