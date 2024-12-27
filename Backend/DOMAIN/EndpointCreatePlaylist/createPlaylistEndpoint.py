from flask import request, jsonify

from DOMAIN.EndpointCreatePlaylist.validateRequest import validate_create_playlist_request
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

    if not checkArtistID(accessToken, artistID):
        return jsonify({"error": "Invalid artist ID"}), 490

    userID = getUserID(accessToken)["id"]

    songInstancesToAdd = retrieve_songs_from_artist_id(accessToken, artistID)

    songsToAdd = [song.song_uri for song in songInstancesToAdd]

    playlist = create_playlist(accessToken, userID, playlistName, isPrivate)
    playListID = playlist["id"]
    playListURL = playlist["external_urls"]["spotify"]

    addSongsToPlaylist(accessToken, playListID, songsToAdd)

    return jsonify({"message": "Request is valid!"}), 200
