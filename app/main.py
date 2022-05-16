#coding: utf-8
import json
import os
import time
# Spotify library.
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
# google library
from ytmusicapi import YTMusic
import requests
import functools
from flask import Flask, render_template, request


class SpotifyToYoutube():

    def login_to_google(self):
        session = requests.Session()
        session.request = functools.partial(session.request, timeout=60)
        ytmusic = YTMusic('ytmusic_headers.json', requests_session=session)
        return ytmusic
        
    def add_to_playlist(self, ytmusic, video_name, target_playlist):
        search_results = ytmusic.search(video_name, "songs") or ytmusic.search(video_name, "videos")
        ytmusic.add_playlist_items(target_playlist, [search_results[0]['videoId']])

    def get_tracks(self, playlist_url, args):
        # Creating and authenticating our Spotify app.
        client_credentials_manager = SpotifyClientCredentials(args.get("spotify_client_id") or jsonConfig["spotify"]["client_id"], args.get("spotify_client_secret") or jsonConfig["spotify"]["client_secret"])
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

def parse_arguments():
    import argparse
    parser = argparse.ArgumentParser(description='Configuration argments for the migration')

    parser.add_argument('--spotify-client-id', '-i', required=False, help='Spotify development app client id')
    parser.add_argument('--spotify-client-secret', '-s', required=False, help='Spotify development app client secret')
    parser.add_argument('--spotify-playlists', '-sp', required=False, help='Spotify playlists ids')
    parser.add_argument('--ytmusic-playlists', '-yp', required=False, help='Youtube music playlists names')
    parser.add_argument('--ytmusic-headers', '-yh', required=False, help='Youtube music headers')

    args = parser.parse_args()

    return args

# Opening our JSON configuration file (which has our tokens).
with open("config.json", encoding='utf-8-sig') as json_file:
    jsonConfig = json.load(json_file)    
    
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')


@app.route('/migrate', methods=['POST'])
def migrate():
    args = request.form
        
    spotify_to_youtube = SpotifyToYoutube()

    source_playlists = args.get("spotify_playlists") or jsonConfig["spotify"]["playlists"]
    target_playlists = args.get("ytmusic_playlists") or jsonConfig["google"]["playlists"]

    if args.get("ytmusic_headers"):
        with open('ytmusic_headers.json', 'w', encoding='utf-8') as ytmusic_headers_file:
            json.dump(json.loads(args.get("ytmusic_headers")), ytmusic_headers_file, ensure_ascii=False, indent=4)
    ytmusic = spotify_to_youtube.login_to_google()

    if(len(source_playlists) != len(target_playlists)):
        print("Please use the same number of Source and Target playlists")
    else:
        for index, playlist_url in enumerate(source_playlists):
            print(playlist_url)
            print("Getting tracks...")
            tracks = spotify_to_youtube.get_tracks(playlist_url, args)
            
            target_playlist = target_playlists[index]
            print(target_playlist)
            target_playlist_id = ytmusic.create_playlist(target_playlist, target_playlist)

            for track in tracks:
                print(track)
                spotify_to_youtube.add_to_playlist(ytmusic, track, target_playlist_id)
                
            print("Migration finished!")
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 