import spotipy
from spotipy.oauth2 import SpotifyOAuth
from decouple import config

# Spotify API credentials
client_id = config('SPOTIFY_CLIENT_ID')
client_secret = config('SPOTIFY_CLIENT_SECRET')
uri = config('SPOTIFY_REDIRECT_URI')
username = config('SPOTIFY_USERNAME')

# Spotify API authentication
scope = 'playlist-modify-public'
token = SpotifyOAuth(scope=scope, username=username, client_id=client_id, client_secret=client_secret, redirect_uri=uri)
spotifyObject = spotipy.Spotify(auth_manager=token)

# Get the playlist ID
playlistURL = input('Enter the URL of the playlist you want to sort: ')
playlistID = playlistURL.split('/')[-1].split('?')[0]

# Get the playlist items
all_tracks = []
offset = 0
limit = 100

# Get all the tracks in the playlist
while True:
    response = spotifyObject.playlist_items(playlist_id=playlistID, offset=offset, limit=limit)
    all_tracks += response['items']

    if len(response['items']) == 0:
        break

    offset += limit

# Get the track details for sorting
sortedData = sorted(all_tracks, key=lambda x: (x['track']['artists'][0]['name'], x['track']['album']['name']))
sortedTrackIDs = [item['track']['id'] for item in sortedData if item['track']['id'] is not None] 

# Create a new playlist with the sorted tracks
playlistName = input('Enter the name of the new sorted playlist: ')
playlist = spotifyObject.user_playlist_create(user=username, name=playlistName, public=True)

# Get the sorted track IDs
for i in range(0, len(sortedTrackIDs), 100):
    batch = sortedTrackIDs[i:i+100]
    spotifyObject.playlist_add_items(playlist_id=playlist['id'], items=batch)




