def extract_artist(song_title):
    dash=song_title.index("-")
    return song_title[dash+2:]

print(extract_artist("Tum hi ho - Arijit Singh"))