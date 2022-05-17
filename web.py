#coding: utf-8
import json
from flask import Flask, render_template, request
from spotifyToYoutube import SpotifyToYoutube
    
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')


@app.route('/migrate', methods=['POST'])
def migrate():
    args = request.json
        
    response_content_type = {'ContentType':'application/json'}
    
    if(not args.get("spotify_playlists") or not args.get("ytmusic_playlists")):
        return json.dumps({'success':False, 'message': 'Missing source or destination playlists'}), 500, response_content_type

    source_playlists = json.loads(args.get("spotify_playlists"))
    target_playlists = json.loads(args.get("ytmusic_playlists"))
    
    if args.get("ytmusic_headers"):
        with open('ytmusic_headers.json', 'w', encoding='utf-8') as ytmusic_headers_file:
            json.dump(json.loads(args.get("ytmusic_headers")), ytmusic_headers_file, ensure_ascii=False, indent=4)
    else: 
        return json.dumps({'success':False, 'message': 'Missing YouTube Music Headers'}), 500, response_content_type
    
    
    spotify_to_youtube = SpotifyToYoutube()
    ytmusic = spotify_to_youtube.login_to_google()

    if(len(source_playlists) != len(target_playlists)):
        print("Please use the same number of Source and Target playlists")
        return json.dumps({'success':False, 'message': 'Please use the same number of Source and Target playlists'}), 500, response_content_type
    else:
        for index, playlist_url in enumerate(source_playlists):
            print(playlist_url)
            print("Getting tracks...")
            tracks = spotify_to_youtube.get_tracks(playlist_url, args.get("spotify_client_id"), args.get("spotify_client_secret"))
            
            target_playlist = target_playlists[index]
            print(target_playlist)
            target_playlist_id = ytmusic.create_playlist(target_playlist, target_playlist)

            for track in tracks:
                print(track)
                spotify_to_youtube.add_to_playlist(ytmusic, track, target_playlist_id)
                
            print("Migration finished!")
            return json.dumps({'success':True}), 200, response_content_type