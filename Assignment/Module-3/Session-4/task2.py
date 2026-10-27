class SongAlreadyExistsError(Exception):
    pass


def add_song_to_playlist(song_name, playlist):
    if song_name in playlist:
        raise SongAlreadyExistsError

    playlist.append(song_name)
    print("Song added successfully!")


playlist = ["Kesariya", "Heeriye"]

try:
    add_song_to_playlist("Kesariya", playlist)

except SongAlreadyExistsError:
    print("Song already exists in playlist!")