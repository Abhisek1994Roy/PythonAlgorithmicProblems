import json
import time

import spotipy
from spotify_client_credentials import *
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


# Function to extract all the trackids from your playlist
def get_track_ids(playlist_id):
    music_id_list = []
    playlist = sp.playlist(playlist_id)
    for item in playlist['tracks']['items']:
        music_track = item['track']
        music_id_list.append(music_track['id'])
    return music_id_list


# Function to extract all the details of each track by passing its id
def get_track_data(track_id):
    meta = sp.track(track_id)
    track_details = {"name": meta['name'], "album": meta['album']['name'],
                     "artist": meta['album']['artists'][0]['name'],
                     "release_date": meta['album']['release_date'],
                     "duration_in_mins": round((meta['duration_ms'] * 0.001) / 60.0, 2)}
    return track_details


# Get the ids for all the songs in your playlist
playlist_id = input('Enter the playlist id')
track_ids = get_track_ids(playlist_id)
print(len(track_ids))
print(track_ids)
# track_ids = get_track_ids('7MXI9ecivGngCDv2IH05ne')

# loop over track ids and get their data points
tracks = []
for i in range(len(track_ids)):
    time.sleep(.5)
    track = get_track_data(track_ids[i])
    tracks.append(track)

# Saving the data collected in a json file
with open('spotify_data.json', 'w') as outfile:
    json.dump(tracks, outfile, indent=4)
