# Spotify To Youtube ▶
A simplistic way to find songs from a Spotify playlist and add them to a YouTube Music playlist.<br>

# How does it work? 😮
After doing some simple configuration. All you gotta do is insert your <b> >>PUBLIC<< </b> <a href="http://www.spotify.com">Spotify</a> playlist URL in the configuration file, then the app will automatically search all songs from that playlist on  <a href="http://music.youtube.com">YouTube Music</a> and automatically add them to a playlist of your choice. Check below for instructions on how to make it work:

# How to use it?
<!-- ## The easy way
1. To use the script, you gotta register an app as a developer on Spotify.
    * Go to this link https://developer.spotify.com/dashboard/
    * Log in to your spotify account
    * Click in Create an App
    * Give the app a name and a description and then create the app
2. Go to https://spotifyytmusic.pythonanywhere.com/
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
    6. Click on the Name of any matching request. In the “Headers” tab, scroll to the section “Request headers” and copy the value of **cookie**: to the end of the line and add it to the below text then copying it all to the ytmusic music headers field in the spotify-ytmusic page.
        ``` 
        {
          "accept": "*/*",
          "accept-language": "en-GB,en;q=0.9,en-US;q=0.8",
          "cookie": "REPLACE_THIS_PART",
          "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36 Edg/98.0.1108.51",
          "x-goog-authuser": "0",
          "x-origin": "https://music.youtube.com"
        }
        ``` 
9. Finally press submit and wait a few minutes until the migration is done (this can take a while depending on how big your playlists are) -->

<!-- ## The hard way -->
### Setting up the tools
1. If you don't have firefox please install it from https://www.mozilla.org/en-US/firefox/new/
2. If you don't have python installed (Mac comes with python preinstalled) then please install it from https://www.python.org/downloads/
3. Go to https://github.com/rimonhanna/Spotify-To-Youtube
4. Click on the green button called Code, then click on Download Zip, unzip/extract the file to the folder of your choosing
5. Open Terminal/Command Prompt then navigate to the folder of the extracted folder using cd path_to_folder for example cd ~/Downloads/Spotify-To-Youtube-master/ 
6. You're now all set and ready to use start migrating your playlists
### Migrating your playlists
1. To use the script, you gotta register an app as a developer on Spotify.
    * Go to this link https://developer.spotify.com/dashboard/
    * Log in to your spotify account
    * Click in Create an App
    * Give the app a name and a description and then create the app
2. Go to https://open.spotify.com/ and open the spotify playlist you intend to copy/migrate in the browser, make it public or shareable, and then copy its id (the right most part of the link/url in the address bar e.g. 7EQFI3982FGL) to the config file replacing `source_playlist_id`
3. Copy Client ID from the spotify app page to the config file replacing `your_spotify_client_id`
4. Click on show client secret and copy the client secret from the spotify app page to the config file replacing `your_spotify_client_secret`
5. Add your Spotify source IDs - you can find it at the end of the Spotify URI (see above) for an artist, track, album, etc. Example: 6rqhFgbbKwnb9MLmUQDhG6
6. Replace target_playlist_name with the name of the playlist you want the tracks to be added to in YouTube music
7. Get youtube music authentication headers
    1. Open a new tab
    2. Open the developer tools (Ctrl-Shift-I) and select the “Network” tab
    3. Go to https://music.youtube.com and ensure you are logged in
    4. Find an authenticated POST request. The simplest way is to filter by /browse using the search bar of the developer tools. If you don’t see the request, try scrolling down a bit or clicking on the library button in the top bar.
    5. Verify that the request looks like this: Status 200, Method POST, Domain music.youtube.com, File browse?...
    6. Click on the Name of any matching request. In the “Headers” tab, scroll to the section “Request headers” and copy the value of cookie: to the end of the line and add it to ytmusic_headers.json
8. Finally run the script by copying this command `./run.sh` into your command prompt if you're using windows and this command in the terminal window `./run.sh` if you're using macOS. 

If you got an error that python(3) was not found:
    *  You need to add the python 3.x you just installed to the system PATH
    *  If you're using macOS catalina or newer (using zshrc) you can use this in the terminal `echo "alias python=/usr/local/bin/python3.9" >> ~/.zshrc` 
    *  If you're using an older version of macOS then use this in the terminal instead `echo "alias python=/usr/local/bin/python3.9" >> ~/.bashrc`
    *  If you're using windows you could follow this simple guide https://datatofish.com/add-python-to-windows-path/
## Buy me coffee
If you have enjoyed using this, consider buying me a coffee?
https://paypal.me/payrimon
# What did you use to make it? :thinking:
I used the following libraries:<br>
  - <a href="https://github.com/plamere/spotipy">Spotipy (For handling the Spotify API)</a>
  - <a href="https://ytmusicapi.readthedocs.io/en/latest/">ytmusicapi (For adding to the YouTube playlist automation)</a>

# Why did you make it?
I wanted to migrate my playlists from Spotify to YouTube Music and I didn't find any good tools out there to do it automatically, so I decided to do it just for fun :) and I thought maybe someone else finds it useful as well.
