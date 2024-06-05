# Backend Connectify

Backend Connectify is a backend service for managing users, playlists, tracks, chatrooms, and sessions. It also includes integration with the Spotify API to search for tracks.

## Features

- User Management: Create, update, delete users. Authenticate users with password hashing.
- Playlist Management: Create, update, delete playlists. Associate playlists with users.
- Track Management: Search for tracks using the Spotify API. Associate tracks with playlists.
- Chatroom Management: Create, update, delete chatrooms. Associate chatrooms with users.
- Session Management: Create, update, delete sessions. Associate sessions with users.
- Flask-Login Integration: Provides user authentication and session management using Flask-Login.
- SQLAlchemy Integration: Uses SQLAlchemy ORM for database management.
- Spotify API Integration: Allows searching for tracks on Spotify.

