# app/routes.py
from flask import request, jsonify
from app import app
from backend_connectify.backend.routes.spotify_api import search_track

@app.route('/search', methods=['GET'])
def search():
    track_name = request.args.get('track_name')
    if not track_name:
        return jsonify({'error': 'Track name is required'}), 400
    
    track_info = search_track(track_name)
    if track_info:
        return jsonify(track_info), 200
    else:
        return jsonify({'error': 'Track not found'}), 404

