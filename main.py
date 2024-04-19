import base64
from dotenv import dotenv_values

from retrieveSongs import retrieve_songs_from_artist_id
from sendRequest import send_request

env_vars = dotenv_values(".env")
client_id = env_vars["CLIENT_ID"]
client_secret = env_vars["CLIENT_SECRET"]


#? Get token
url = "https://accounts.spotify.com/api/token"
headers = {'Authorization': 'Basic ' + base64.b64encode((client_id + ':' + client_secret).encode()).decode()}
data = {'grant_type': 'client_credentials'}

token = send_request("post", url, headers=headers, data=data)['access_token']
if token:
    print("Got token \n")

# artist_id = "2n6A4lZ0HPaY3qY4eFYMG2"  # ivorydespair
# artist_id = "3YQKmKGau1PzlVlkL1iodx"  # twentyOnePilots
# artist_id = "0uCCBpmg6MrPb1KY2msceF"  # burial
# artist_id = "3QaxveoTiMetZCMp1sftiu"  # waterparks
artist_id = "3Fl31gc0mEUC2H0JWL1vic"  # paula
retrieve_songs_from_artist_id(token, artist_id)

