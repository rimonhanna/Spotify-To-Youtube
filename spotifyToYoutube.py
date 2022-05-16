#coding: utf-8

# Spotify library.
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
# google library
from ytmusicapi import YTMusic
import requests
import functools


class SpotifyToYoutube():

    def login_to_google(self):
        session = requests.Session()
        session.request = functools.partial(session.request, timeout=60)
        ytmusic = YTMusic('ytmusic_headers.json', requests_session=session)
        return ytmusic
        
    def add_to_playlist(self, ytmusic, video_name, target_playlist):
        search_results = ytmusic.search(video_name, "songs") or ytmusic.search(video_name, "videos")
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
        for i in tracks:
            # In case there's only one artist.
            if (i["track"]["artists"].__len__() == 1):
                # We add trackName - artist.
                track_list.append(i["track"]["name"] + " - " + i["track"]["artists"][0]["name"])
            # In case there's more than one artist.
            else:
                name_string = ""
                # For each artist in the track.
                for index, b in enumerate(i["track"]["artists"]):
                    name_string += (b["name"])
                    # If it isn't the last artist.
                    if (i["track"]["artists"].__len__() - 1 != index):
                        name_string += ", "
                # Adding the track to the list.
                track_list.append(i["track"]["name"] + " - " + name_string)
           

        return track_list
