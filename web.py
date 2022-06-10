#coding: utf-8
import json
from flask import Flask, render_template, request, jsonify, make_response
from spotifyToYoutube import SpotifyToYoutube
    
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')


@app.route('/migrate', methods=['POST'])
def migrate():
    args = request.json
    
    if not args.get("spotify_playlists") or not args.get("ytmusic_playlists"):
        return make_response(jsonify(success= False, message= 'Missing source or destination playlists'), 500)

    try:
        source_playlists = json.loads(args.get("spotify_playlists"))
        target_playlists = json.loads(args.get("ytmusic_playlists"))
    except Exception as e:
        print("An exception occurred:", e)
        return make_response(make_response(jsonify(success= False, message= str(e) + ', make sure that spotify_playlists and ytmusic_playlists are in the correct format ["playlist_1", "playlist_2"] including the square brackets, qoutes and comma separators'), 500))
    
    try:  
        if not args.get("ytmusic_headers"):
            return make_response(jsonify(success= False, message= 'Missing YouTube Music Headers'), 500)
        
        spotify_to_youtube = SpotifyToYoutube()
        ytmusic = spotify_to_youtube.login_to_google(args.get("ytmusic_headers"))

        if len(source_playlists) != len(target_playlists):
            print("Please use the same number of Source and Target playlists")
            return make_response(jsonify(success= False, message= 'Please use the same number of Source and Target playlists'), 500)
        else:
            for index, playlist_url in enumerate(source_playlists):
                print(playlist_url)
                print("Getting tracks...")
                tracks = spotify_to_youtube.get_tracks(playlist_url, args.get("spotify_client_id"), args.get("spotify_client_secret"))
                
                target_playlist = target_playlists[index]
                print(target_playlist)
                target_playlist_id = ytmusic.create_playlist(target_playlist, target_playlist)

                for track_index, track in enumerate(tracks):
                    print("Track", track_index + 1, "out of", len(tracks))
                    spotify_to_youtube.add_to_playlist(ytmusic, track, target_playlist_id)
                    
            print("Migration finished!")
            return jsonify(success= True)
    
    except Exception as e:
        print("An exception occurred:", e)
        return make_response(make_response(jsonify(success= False, message= str(e)), 500))