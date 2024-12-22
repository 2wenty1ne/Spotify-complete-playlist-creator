from utils.getToken import get_token
from spotify.createPlaylist import create_playlist
from spotify.retrieveSongs import retrieve_songs_from_artist_id

token = get_token()

# artist_id = "2n6A4lZ0HPaY3qY4eFYMG2"  # ivorydespair
# artist_id = "3YQKmKGau1PzlVlkL1iodx"  # twentyOnePilots
# artist_id = "0uCCBpmg6MrPb1KY2msceF"  # burial
# artist_id = "3QaxveoTiMetZCMp1sftiu"  # waterparks
artist_id = "3Fl31gc0mEUC2H0JWL1vic"  # paula <3
# artist_id = "2p2uE4i92Dn4DkThfoKIB9" # double test
retrieve_songs_from_artist_id(token, artist_id)
create_playlist(token)
