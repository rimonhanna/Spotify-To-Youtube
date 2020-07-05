# Spotify To Youtube ▶
A simplistic way to find songs from a Spotify playlist on YouTube.<br>
<b><i>IMPORTANT:</i> Please check the issue I've pinned <a href="https://github.com/saulojoab/Spotify-To-Youtube/issues">here</a>.</b>

# How does it work? 😮
All you gotta do is insert your <b> >>PUBLIC<< </b> <a href="http://www.spotify.com">Spotify</a> playlist URL when prompted, then the app will automatically search all songs from that playlist on <a href="http://music.youtube.com">YouTube Music</a> and automatically add them to a playlist of your choice. Check below for instructions on how to make it work:

# How to use it?
1 - To use the script, you gotta register an app as a developer on Spotify.<br>
2 - When you finish doing that, <b>create a JSON file</b> named <i>"config.json"</i> on the project's main folder.<br>
3 - The <i>config.json</i> file <b>must have</b> the following format:
```js
{
    "spotify":
    {
        "client_id": "your_spotify_client_id",
        "client_secret": "your_spotify_client_secret"
    },
    "google":
    {
        "username": "your_youtube_username",
        "password": "your_youtube_password",
        "playlist": "target_playlist_name"
    }
}
```

# What did you use to make it? :thinking:
I used the following libraries:<br>
  - <a href="https://github.com/plamere/spotipy">Spotipy (For handling the Spotify API)</a>
  - <a href="https://selenium-python.readthedocs.io/">Selenium Python (For adding to the YouTube playlist automation)</a>

# Why did you make it?
Just for fun :) and it might actually be useful to someone. I think <a href="http://discord.app">Discord</a> bots could use that to queue songs and stuff. 
