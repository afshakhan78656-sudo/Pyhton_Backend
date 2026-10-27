def add_song(song_name, playlist):
    playlist.append(song_name)
    return playlist


def remove_song(song_name, playlist):
    if song_name in playlist:
        playlist.remove(song_name)

    return playlist