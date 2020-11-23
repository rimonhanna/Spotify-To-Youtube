#coding: utf-8
import json
import os
import time
# Spotify library.
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Selenium for automation
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class SpotifyToYoutube():

    def set_up(self):
        self.rootdir = os.path.dirname(os.path.realpath(__file__))
        self.driver = webdriver.Firefox(executable_path=self.rootdir + '/geckodriver')
        self.driver.implicitly_wait(30)
        self.verification_errors = []
        self.accept_next_alert = True

    def login_to_google(self):
        url = 'https://stackoverflow.com/users/login?ssrc=head&returnurl=https%3a%2f%2fstackoverflow.com%2f'
        self.driver.get(url)

        self.driver.find_element_by_xpath("//div[@id='openid-buttons']/button").click()
        
        self.driver.find_element_by_id("identifierId").send_keys(jsonConfig["google"]["username"])
        self.driver.find_element_by_id("identifierNext").click()

        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable((By.NAME, "password")))
        self.driver.find_element_by_name("password").send_keys(jsonConfig["google"]["password"])
        self.driver.find_element_by_id("passwordNext").click()
        time.sleep(10)
        
    def add_to_playlist(self, url):
        try:
            driver = self.driver
            driver.get(url)

            element = driver.find_element_by_xpath("//div[@id='contents']/ytmusic-responsive-list-item-renderer/div[2]/div")
            WebDriverWait(driver, 30).until(expected_conditions.visibility_of(element))
            element.click()

            element = driver.find_element_by_xpath("(//iron-icon[@id='icon'])[4]")
            WebDriverWait(driver, 10).until(expected_conditions.visibility_of(element))
            element.click()

            element = driver.find_element_by_link_text("Add to playlist")
            WebDriverWait(driver, 10).until(expected_conditions.visibility_of(element))
            element.click()

            element = driver.find_element_by_xpath("//yt-formatted-string[@title='" + jsonConfig["google"]["playlist"] + "']")
            WebDriverWait(driver, 10).until(expected_conditions.visibility_of(element))
            element.click()
            
        except ElementClickInterceptedException:
            pass
        except TimeoutException:
            pass
        except NoSuchElementException:
            pass


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

    def open_in_youtube_music(self, song_name):
        self.add_to_playlist('https://music.youtube.com/search?q=' + song_name)

# Opening our JSON configuration file (which has our tokens).
with open("config.json", encoding='utf-8-sig') as json_file:
    jsonConfig = json.load(json_file)    

if (__name__ == "__main__"):
    spotifyToYoutube = SpotifyToYoutube()
    
    playlist_url = jsonConfig["spotify"]["playlist"]
    tracks = spotifyToYoutube.get_tracks(playlist_url)
    
    print("Searching songs...")
    songs = []
    spotifyToYoutube.set_up()
    spotifyToYoutube.login_to_google()

    for i in tracks:
        print(i)
        spotifyToYoutube.open_in_youtube_music(i)
        
    print("Migration finished!")
    spotifyToYoutube.driver.quit()
