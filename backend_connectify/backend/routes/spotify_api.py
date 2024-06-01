# backend_connectify/spotify_api.py
import requests
from routes.spotify_auth import get_token

def search_track(track_name):
    token = get_token()
    search_url = 'https://api.spotify.com/v1/search'
    headers = {
        'Authorization': f'Bearer {token}'
    }

    params = {
        'q': track_name,
        'type': 'track',
        'limit': 1
    }

    response = requests.get(search_url, headers=headers, params=params)
    response_data = response.json()

    if response_data['tracks']['items']:
        track = response_data['tracks']['items'][0]
        track_info = {
            'name': track['name'],
            'artist': track['artists'][0]['name'],
            'id': track['id'],
            'url': track['external_urls']['spotify']
        }
        return track_info
    else:
        return None

if __name__ == '__main__':
    track_name = 'Imagine'
    track_info = search_track(track_name)
    if track_info:
        print(f"Track Name: {track_info['name']}")
        print(f"Artist: {track_info['artist']}")
        print(f"Track ID: {track_info['id']}")
        print(f"Spotify URL: {track_info['url']}")
    else:
        print("Track not found.")
