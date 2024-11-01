# Spotify Playlist Sorter

## Overview

The Spotify Playlist Sorter is a Python script that allows users to sort their Spotify playlists based on artist names and album names. The script retrieves tracks from a specified playlist, sorts them, and creates a new playlist with the sorted tracks.

## Features

- Retrieve tracks from any public Spotify playlist.
- Sort tracks by artist and album names.
- Create a new playlist with the sorted tracks.
- Easy integration with the Spotify API using the Spotipy library.

## Requirements

To run this project, you'll need:

- Python 3.6 or higher
- A Spotify Developer account
- The following Python packages:
  - `spotipy`
  - `python-decouple`

## Setup

1. **Clone the repository** (if applicable):
   ```bash
   git clone https://github.com/yourusername/SortPlaylist.git
   cd SortPlaylist

2. **Install required packages
    ```bash
    pip install spotipy python-decouple

3. **Create a .env file in the project directory and add your Spotify API credentials:
   ```bash
   SPOTIFY_CLIENT_ID=your_client_id
   SPOTIFY_CLIENT_SECRET=your_client_secret
   SPOTIFY_REDIRECT_URI=http://localhost:8888/callback
   SPOTIFY_USERNAME=your_spotify_username

4. Obtain Spotify API Credentials:
    - Go to the Spotify Developer Dashboard.
    - Create a new application to get your Client ID and Client Secret.
    - Set the Redirect URI in your application settings to match the one in your .env file.

## Usage
1. **Run the script:**
   ```bash
    python script.py

2. When prompted, enter the URL of the playlist you want to sort.

3. Enter the name for the new sorted playlist.

4. The script will create a new playlist on your Spotify account with the sorted tracks.

**Example**
```bash
Enter the URL of the playlist you want to sort: https://open.spotify.com/playlist/your_playlist_id
Enter the name of the new sorted playlist: My Sorted Playlist
Successfully created playlist: My Sorted Playlist with X tracks.
```

**Contributing**
Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request.

**License**
This project is licensed under the MIT License - see the LICENSE file for details.

**Acknowledgments**
- Spotify API
- Spotipy - A lightweight Python library for the Spotify Web API.
