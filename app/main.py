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
from ... import SpotifyToYoutube

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