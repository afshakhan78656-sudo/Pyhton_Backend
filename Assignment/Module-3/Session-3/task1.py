songs = {
    "Kesariya": 4,
    "Heeriye": 3,
    "Believer": 4
}

def get_song_duration(song):
    try:
        print("Duration:", songs[song], "minutes")
    except KeyError:
        print("Song not found on Spotify!")


get_song_duration("Kesariya")
get_song_duration("Shape of You")