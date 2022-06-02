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
2. Go to https://spotify-ytmusic.herokuapp.com/
4. Copy Client ID from the spotify app page to spotify-ytmusic page
5. Click on show client secret and copy the client secret from the spotify app page to spotify-ytmusic page
6. Add your Spotify source artist, track, album IDs you want to migrate in this format ["6rqhFgbbKwnb9MLmUQDhG6", "abWkfFgbbKwnUQDhG6"] - you can find it at the end of the Spotify URI for an artist, track, album, etc. Example: 6rqhFgbbKwnb9MLmUQDhG6
7. Add the names of the playlists you want to be created in youtube music in the same chronological order of the source spotify playlists this format ["target_playlist_name_1", "target_playlist_name_2"]
8. Get youtube music authentication headers
    1. Open a new tab
    2. Open the developer tools (Ctrl-Shift-I) and select the “Network” tab
    3. Go to https://music.youtube.com and ensure you are logged in
    4. Find an authenticated POST request. The simplest way is to filter by /browse using the search bar of the developer tools. If you don’t see the request, try scrolling down a bit or clicking on the library button in the top bar.
    5. Verify that the request looks like this: Status 200, Method POST, Domain music.youtube.com, File browse?...
    6. Click on the Name of any matching request. In the “Headers” tab, scroll to the section “Request headers” and copy the value of cookie: to the end of the line and add it to ytmusic music headers field in the spotify-ytmusic page
9. Finally press submit and wait a few minutes until the migration is done (this can take a while depending on how big your playlists are)

# What did you use to make it? :thinking:
I used the following libraries:<br>
  - <a href="https://github.com/plamere/spotipy">Spotipy (For handling the Spotify API)</a>
  - <a href="https://ytmusicapi.readthedocs.io/en/latest/">ytmusicapi (For adding to the YouTube playlist automation)</a>

# Why did you make it?
I wanted to migrate my playlists from Spotify to YouTube Music and I didn't find any good tools out there to do it automatically, so I decided to do it just for fun :) and I thought maybe someone else finds it useful as well.
