from pprint import pprint

from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

SP_CLIENT_ID = "dfde15631d07421d8b9ef3e7536d30b3"
SP_CLIENT_SECRET = "922e552397114facb5966f56e6619c32"
SP_REDIRECT_URI = "https://example.com/"
SP_PLAYLIST_CREATION = "playlist-modify-private"
SP_ENDPOINT = "https://api.spotify.com/v1/users/smedjan"

# date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")  # 2007-09-01
date = "2007-09-01"

billboard_url = f"https://www.billboard.com/charts/hot-100/{date}/"
billboard_webpage = requests.get(url=billboard_url).text
soup = BeautifulSoup(billboard_webpage, "html.parser")
all_songs = soup.select("li ul li h3")
all_song_names = [song.getText().strip() for song in all_songs]

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SP_CLIENT_ID,
                                               client_secret=SP_CLIENT_SECRET,
                                               redirect_uri=SP_REDIRECT_URI,
                                               scope="playlist-modify-private",
                                               username="pixu",
                                               cache_path="token.txt",
                                               show_dialog=True))

user_id = sp.current_user()["id"]

songs_uri = []

for song in all_song_names:
    result = sp.search(q=f"track:{song} year:2007", type="track", limit=1)
    try:
        songs_uri.append(result["tracks"]["items"][0]["uri"])
    except IndexError:
        pass


billboard_playlist = sp.user_playlist_create(user=user_id,
                                             name="BillBoardHot100",
                                             public=False,
                                             collaborative=False,
                                             description="Hello, Spotify111!!!")

sp.playlist_add_items(playlist_id=billboard_playlist["id"], items=songs_uri)


# for i in range(len(songs_uri)):
#     sp.playlist_add_items(playlist_id=billboard_playlist["id"], items=[songs_uri[i]])

