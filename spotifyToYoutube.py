#coding: utf-8
import json
import os
import time
# Spotify library.
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
# google library
from ytmusicapi import YTMusic

class SpotifyToYoutube():

    def login_to_google(self):
        ytmusic = YTMusic('ytmusic_headers.json')
        return ytmusic
        
    def add_to_playlist(self, ytmusic, video_name, target_playlist):
        search_results = ytmusic.search(video_name, "songs") or ytmusic.search(video_name, "videos")
        ytmusic.add_playlist_items(target_playlist, [search_results[0]['videoId']])

    def get_tracks(self, playlist_url):
        # Creating and authenticating our Spotify app.
        client_credentials_manager = SpotifyClientCredentials(jsonConfig["spotify"]["client_id"], jsonConfig["spotify"]["client_secret"])
        spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

        condition = True
        track_list = []
        counter = 0
        while condition:
            # Getting a playlist.
            results = spotify.user_playlist_tracks(user="", playlist_id=playlist_url)

            # For each track in the playlist.
            for i in results["items"]:
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
            counter = counter + 100
            condition = counter < results["total"]
        return track_list

# Opening our JSON configuration file (which has our tokens).
with open("config.json", encoding='utf-8-sig') as json_file:
    jsonConfig = json.load(json_file)    

if (__name__ == "__main__"):
    spotifyToYoutube = SpotifyToYoutube()
    
    sourcePlaylists = jsonConfig["spotify"]["playlists"]
    targetPlaylists = jsonConfig["google"]["playlists"]
    ytmusic = spotifyToYoutube.login_to_google()

    if(len(sourcePlaylists) != len(targetPlaylists)):
        print("Please use the same number of Source and Target playlists")
    else:
        for index, playlist_url in enumerate(sourcePlaylists):
            print(playlist_url)
            print("Getting tracks...")
            tracks = spotifyToYoutube.get_tracks(playlist_url)
            
            targetPlaylist = targetPlaylists[index]
            print(targetPlaylist)
            targetPlaylistId = ytmusic.create_playlist(targetPlaylist, targetPlaylist)

            for track in tracks:
                print(track)
                spotifyToYoutube.add_to_playlist(ytmusic, track, targetPlaylistId)
                
            print("Migration finished!")
