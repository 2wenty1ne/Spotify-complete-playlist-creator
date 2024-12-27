from flask import request, jsonify

from DOMAIN.EndpointCreatePlaylist.checkArtistID import checkArtistID
from DOMAIN.EndpointCreatePlaylist.retrieveSongs import retrieve_songs_from_artist_id
from DOMAIN.EndpointCreatePlaylist.createPlaylist import create_playlist
from DOMAIN.EndpointCreatePlaylist.addSongsToPlaylist import addSongsToPlaylist
from DOMAIN.EndpointCreatePlaylist.getUserID import getUserID

#TODO rename file
def createPlaylistRespone(ACCESS_TOKEN_COOKIE):
    data = request.get_json()
    accessToken = request.cookies.get(ACCESS_TOKEN_COOKIE) if request.cookies else None 

    if not validate_create_playlist_request(data):
        return jsonify({"error": "Invalid request body"}), 400

    artistID = data["artistID"]
    playlistName = data["playlistName"]
    isPrivate = data["isPrivate"]

    isArtistIDValid, artistName = checkArtistID(accessToken, artistID)

    if not isArtistIDValid:
        return jsonify({"error": "Invalid artist ID"}), 490

    playlistName = check_playlist_name(playlistName, artistName)
    userID = getUserID(accessToken)["id"]

    songInstancesToAdd = retrieve_songs_from_artist_id(accessToken, artistID)

    songsToAdd = [song.song_uri for song in songInstancesToAdd]

    playlist = create_playlist(accessToken, userID, playlistName, isPrivate)
    playListID = playlist["id"]

    addSongsToPlaylist(accessToken, playListID, songsToAdd)

    playlistURL = f"https://open.spotify.com/embed/playlist/{playListID}?utm_source=generator"
    return jsonify({"playlistURL": playlistURL}), 200


def validate_create_playlist_request(data):
    required_keys = {
        "playlistName": str,
        "artistID": str,
        "isPrivate": bool
    }

    for key, expected_type in required_keys.items():
        if key not in data or not isinstance(data[key], expected_type):
            return False

    return True


def check_playlist_name(playlistName, artistName):
    if not playlistName:
        return f"All {artistName} Songs"
    
    return playlistName
