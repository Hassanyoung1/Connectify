# backend_connectify/spotify_auth.py
import requests
import base64

# Replace with your actual Client ID and Client Secret
client_id = 'b4b1caf240ff4ddb911dd550ea25fc65'
client_secret = '3bf6ff24b3204303a3c7e6ab7b86ffec'

def get_token():
    auth_url = 'https://accounts.spotify.com/api/token'
    auth_header = base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()

    headers = {
        'Authorization': f'Basic {auth_header}',
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    data = {
        'grant_type': 'client_credentials'
    }

    response = requests.post(auth_url, headers=headers, data=data)
    response_data = response.json()

    return response_data['access_token']

if __name__ == '__main__':
    token = get_token()
    print(token)
