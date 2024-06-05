# backend_connectify/spotify_api.py
"""
Spotify API Module
==================

This module provides functions to interact with the Spotify API.

Functions:
----------
    search_track: Search for a track on Spotify by its name.

Usage:
------
    from spotify_api import search_track
    track_name = 'Imagine'
    track_info = search_track(track_name)
    if track_info:
        print(f"Track Name: {track_info['name']}")
        print(f"Artist: {track_info['artist']}")
        print(f"Track ID: {track_info['id']}")
        print(f"Spotify URL: {track_info['url']}")
    else:
        print("Track not found.")
"""

import requests
from routes.spotify_auth import get_token

def search_track(track_name):
    """
    Search for a track on Spotify by its name.

    Args:
    -----
        track_name (str): The name of the track to search for.

    Returns:
    --------
        dict or None: A dictionary containing information about the track if found,
                      otherwise None.

    Example:
    --------
        track_name = 'Imagine'
        track_info = search_track(track_name)
        if track_info:
            print(f"Track Name: {track_info['name']}")
            print(f"Artist: {track_info['artist']}")
            print(f"Track ID: {track_info['id']}")
            print(f"Spotify URL: {track_info['url']}")
        else:
            print("Track not found.")
    """
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
