import requests
from bs4 import BeautifulSoup
import spotipy
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# SPOTIPY_CLIENT_ID = 'ef81c85887394ab39cf601d45d35c594'
# SPOTIPY_CLIENT_SECRET = 'ed0c4b7b632c4e869f379e8f61192fda'
# SPOTIPY_REDIRECT_URI = 'http://localhost:3000'
# SONGS_PLAYLIST = "31qfwf6toctbaobee4ffxbsbnfki"


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    scope="playlist-modify-private",
    client_id='ef81c85887394ab39cf601d45d35c594',
    client_secret='ed0c4b7b632c4e869f379e8f61192fda',
    redirect_uri='http://localhost:3000',
    show_dialog=True,
    cache_path="token.txt"
))
user_id = sp.current_user()["id"]
print(user_id)
yyyymmdd = input(
    "Which year would you want to travel to? Type the date in this format: YYYY-MM-DD: ")
top_hundred_songs = requests.get(
    f"https://www.billboard.com/charts/hot-100/2009-06-13/")

soup = BeautifulSoup(top_hundred_songs.text, 'html.parser')

song_names = [i.get_text().strip() for i in soup.select("li ul li h3")]

song_uris = []
year = yyyymmdd.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type='track')
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} does not exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(
    user=user_id, name=f"{yyyymmdd} Billboard 100", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
