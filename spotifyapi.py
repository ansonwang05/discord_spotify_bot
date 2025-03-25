import spotapi

def convert_url_to_data(playlist_url):
    '''
    Converts spotify playlist into useable data 
    and returns it 

    Args:
        playlist_url (str) : url of the playlist

    Returns:
        Playlist information in the form of a mapping[str, Any]
    '''
    playlist = spotapi.PublicPlaylist(playlist_url)
    playlist_data = playlist.get_playlist_info()
    return playlist_data

def size_of_playlist(playlist_url):
    '''
    Returns the size of the spotify playlist

    Args:
        playlist_url (str) : url of the playlist 

    Returns:
        Size of the playlist as an int
    '''
    playlist_data = convert_url_to_data(playlist_url)
    return len(playlist_data['data']['playlistV2']['content']['items'])

def get_playlist_owner(playlist_url):
    '''
    Returns the owner of the playlist 

    Args:
        playlist_url (str) : url of the playlist

    Returns: 
        Owner of the playlist as a string
    '''
    playlist_data = convert_url_to_data(playlist_url)
    return playlist_data['data']['playlistV2']['content']['items'][0]['addedBy']['data']['name']

def get_playlist_song(playlist_url, index):
    '''
    Returns the song at a certain index of the playlist 

    Args:
        playlist_url (str) = url of the playlist 
        index (int) = index of the song 

    Returns:
        The song at the specific requested index as a string
    '''
    playlist_data = convert_url_to_data(playlist_url)
    return playlist_data['data']['playlistV2']['content']['items'][index]['itemV2']['data']['name']
