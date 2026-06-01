import requests
from bs4 import BeautifulSoup
import ytmusicapi
from ytmusicapi import YTMusic

URL = "https://appbrewery.github.io/bakeboard-hot-100/"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"}

# date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")
date = "2026-04-18"

response = requests.get(URL+date, headers=header)
soup = BeautifulSoup(response.content, "html.parser")

music_name = soup.find_all(name="h3", class_="chart-entry__title")

all_music_names = [music.getText() for music in music_name]

print(all_music_names)

# print(soup.prettify())

# yt = YTMusic("browser.json")
# playlists = yt.get_library_playlists()
# print(f"Found {len(playlists)} playlists in your library.")

yt = YTMusic("browser.json")

# Verify authentication works
playlists = yt.get_library_playlists()
print(f"Found {len(playlists)} playlists in your library.")

# USE TO CREATE A PLAYLIST ------------------------------------
# playlist_id = yt.create_playlist(title="Billboard 100", description="2000-08-12 Billboard 100", privacy_status="PRIVATE")
# print("Playlist criada com ID:", playlist_id)



for music in all_music_names:
    try:
        results = yt.search(music, filter="songs")
        print(results)

        if results:
            print(f"Music found {music}")
            video_id = results[0]["videoId"]
            print(f"\nVideo ID: {video_id}\n")

            try:
                yt.add_playlist_items(playlistId="PLpVK6imjLSRAoLIljSPyOTIUW4dfrz0DJ", videoIds=[video_id])
                print(f"Added {music} to your playlist.")
            except:
                print(f"Could not add {music} to your playlist.")

    except:
        print(f"Could not find {music}")
