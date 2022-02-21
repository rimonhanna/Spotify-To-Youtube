# Spotify To Youtube ▶
A simplistic way to find songs from a Spotify playlist and add them to a YouTube Music playlist.<br>

# How does it work? 😮
After doing some simple configuration. All you gotta do is insert your <b> >>PUBLIC<< </b> <a href="http://www.spotify.com">Spotify</a> playlist URL in the configuration file, then the app will automatically search all songs from that playlist on  <a href="http://music.youtube.com">YouTube Music</a> and automatically add them to a playlist of your choice. Check below for instructions on how to make it work:

# How to use it?
1. To use the script, you gotta register an app as a developer on Spotify.
    * Go to this link https://developer.spotify.com/dashboard/
    * Log in to your spotify account
    * Click in Create an App
    * Give the app a name and a description and then create the app
2. When you finish doing that, create a JSON file named "config.json" on the project's main folder.
3. The config.json file must have the following format:
``` 
{
    "spotify":
    {
        "client_id": "your_spotify_client_id",
        "client_secret": "your_spotify_client_secret",
        "playlists": ["source_playlist_id_1", "source_playlist_id_2"]
    },
    "google":
    {
        "playlists": ["target_playlist_name_1", "target_playlist_name_2"]
    }
}
```
4. Copy Client ID from the spotify app page to the config file replacing your_spotify_client_id
5. Click on show client secret and copy the client secret from the spotify app page to the config file replacing your_spotify_client_secret
6. Replace target_playlist_name with the name of the playlist you want the tracks to be added to in YouTube music
7. Get youtube music authentication headers
    1. Open a new tab
    2. Open the developer tools (Ctrl-Shift-I) and select the “Network” tab
    3. Go to https://music.youtube.com and ensure you are logged in
    4. Find an authenticated POST request. The simplest way is to filter by /browse using the search bar of the developer tools. If you don’t see the request, try scrolling down a bit or clicking on the library button in the top bar.
    5. Verify that the request looks like this: Status 200, Method POST, Domain music.youtube.com, File browse?...
    6. Click on the Name of any matching request. In the “Headers” tab, scroll to the section “Request headers” and copy the value of cookie: to the end of the line and add it to ytmusic_headers.json
8. Finally run the script by copying this command into your terminal window `python3 spotifyToYoutube.py`

# What did you use to make it? :thinking:
I used the following libraries:<br>
  - <a href="https://github.com/plamere/spotipy">Spotipy (For handling the Spotify API)</a>
  - <a href="https://ytmusicapi.readthedocs.io/en/latest/">ytmusicapi (For adding to the YouTube playlist automation)</a>

# Why did you make it?
I wanted to migrate my playlists from Spotify to YouTube Music and I didn't find any good tools out there to do it automatically, so I decided to do it just for fun :) and I thought maybe someone else finds it useful as well.
