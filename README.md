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
        "playlist": "source_playlist_url"
    },
    "google":
    {
        "username": "your_youtube_username",
        "password": "your_youtube_password",
        "playlist": "target_playlist_name"
    }
}
```
4. Copy Client ID from the spotify app page to the config file replacing your_spotify_client_id
5. Click on show client secret and copy the client secret from the spotify app page to the config file replacing your_spotify_client_secret
6. Replace your_youtube_username with your google account username
7. Replace your_youtube_password with your google account password
8. Replace target_playlist_name with the name of the playlist you want the tracks to be added to in YouTube music
9. Finally run the script by copying this command into your terminal window `python3 spotifyToYoutube.py`

# What did you use to make it? :thinking:
I used the following libraries:<br>
  - <a href="https://github.com/plamere/spotipy">Spotipy (For handling the Spotify API)</a>
  - <a href="https://selenium-python.readthedocs.io/">Selenium Python (For adding to the YouTube playlist automation)</a>

# Why did you make it?
Just for fun :) and it might actually be useful to someone. 
