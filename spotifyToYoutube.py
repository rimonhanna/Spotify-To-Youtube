#coding: utf-8

# Spotify library.
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
# google library
from ytmusicapi import YTMusic
import requests
import functools

class SpotifyToYoutube():

    def login_to_google(self, ytmusic_headers):
        session = requests.Session()
        session.request = functools.partial(session.request, timeout=60)
        ytmusic = YTMusic(ytmusic_headers, requests_session=session)
        return ytmusic
        
    def add_to_playlist(self, ytmusic, video_name, target_playlist):
        search_results = ytmusic.search(video_name, "songs") or ytmusic.search(video_name, "videos")
        if len(search_results) > 0:
            ytmusic.add_playlist_items(target_playlist, [search_results[0]['videoId']])

    def get_tracks(self, playlist_url, spotify_client_id, spotify_client_secret):
        # Creating and authenticating our Spotify app.
        client_credentials_manager = SpotifyClientCredentials(spotify_client_id, spotify_client_secret)
        spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

        track_list = []

        # Getting a playlist.
        results = spotify.user_playlist_tracks(user="", playlist_id=playlist_url)
        
        tracks = results['items']
        while results['next']:
            results = spotify.next(results)
            tracks.extend(results['items'])

        # For each track in the playlist.
        for track in tracks:
            if(track == None or track["track"] == None):
                print(track)
            elif(track["track"]["artists"] == None):
                print(track["track"])
                track_list.append(track["track"]["name"])
            # In case there's only one artist.
            elif (len(track["track"]["artists"]) == 1):
                # We add trackName - artist.
                track_list.append(track["track"]["name"] + " - " + track["track"]["artists"][0]["name"])
            # In case there's more than one artist.
            else:
                name_string = ""
                # For each artist in the track.
                for index, artist in enumerate(track["track"]["artists"]):
                    name_string += (artist["name"])
                    # If it isn't the last artist.
                    if (len(track["track"]["artists"]) - 1 != index):
                        name_string += ", "
                # Adding the track to the list.
                track_list.append(track["track"]["name"] + " - " + name_string)
           

        return track_list
