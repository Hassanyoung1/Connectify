# Connectify - Connect Through Music

Connectify is an engaging online music player platform that bridges the gap between friends through real-time musical connectivity. Users are encouraged to collaborate on playlists, explore vast musical libraries, and vibe to the same beats synchronously, no matter where they are.

## Description

Connectify is a full-stack web application built using Flask for the backend and a combination of HTML, CSS, and JavaScript for the frontend. It allows users to register, log in, create and manage playlists, search for and add tracks, create and participate in chatrooms, and enjoy a synchronized music listening experience with friends.

## Tech Stack

### Backend

- **Language**: Python
- **Framework**: Flask
- **Database**: SQLite (for development) or MySQL (for production)
- **ORM**: SQLAlchemy
- **Authentication**: Flask-Login
- **Other Dependencies**: Werkzeug, Flask-Cors

### Frontend

- **Languages**: HTML, CSS, JavaScript
- **Framework**: None (Vanilla JavaScript)
- **Libraries**: None

## Features

- User Registration and Authentication
- Music Integration with Spotify API
- Playlist Creation and Management
- Real-time Music Playback and Synchronization
- User Chatrooms and Voice Notes

## Installation

1. Clone the repository:



git clone https://github.com/your-username/connectify.git


2. Navigate to the project directory:



cd connectify


3. Install the required Python packages:



pip install -r requirements.txt


4. Set up the environment variables:

- For the backend:
  - `CONNECTIFY_MYSQL_USER`: Your MySQL username
  - `CONNECTIFY_MYSQL_PWD`: Your MySQL password
  - `CONNECTIFY_MYSQL_HOST`: Your MySQL host (e.g., `localhost`)
  - `CONNECTIFY_MYSQL_DB`: Your MySQL database name
  - `CONNECTIFY_TYPE_STORAGE`: Set to `db` for MySQL storage or `file` for file storage
  - `CONNECTIFY_ENV`: Set to `development` or `production`
- For the frontend:
  - `SECRET_KEY`: A secret key for Flask
  - `SPOTIPY_CLIENT_ID`: Your Spotify API client ID
  - `SPOTIPY_CLIENT_SECRET`: Your Spotify API client secret

## Running the Application

### Backend

1. Navigate to the `backend_connectify` directory:



cd backend_connectify


2. Run the Flask application:



python backend/app.py


The backend server will start running on `http://localhost:5010`.

### Frontend

1. Navigate to the `frontend_connectify` directory:



cd frontend_connectify


2. Run the Flask application:



python app.py


The frontend server will start running on `http://localhost:5000`.

3. Open your web browser and navigate to `http://localhost:5000` to access the Connectify application.

## Usage

1. Register a new account or log in with an existing account.
2. Create a new playlist or search for existing tracks to add to your playlists.
3. Invite friends to join your playlist sessions and enjoy synchronized music playback.
4. Participate in chatrooms and send voice notes to your friends.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).