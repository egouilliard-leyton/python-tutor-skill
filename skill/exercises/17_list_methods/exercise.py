"""Solution variants for Lesson 17: List Methods"""

def add_song(playlist, song):
    playlist.append(song)
    return playlist

def remove_song(playlist, song):
    if song in playlist:
        playlist.remove(song)
    return playlist

def get_top_3(playlist):
    return playlist[:3]

def sort_playlist(playlist):
    return sorted(playlist)
