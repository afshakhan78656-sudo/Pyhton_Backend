f = open("my_fav_songs.txt", "r")

songs = f.readlines()

i = 1
for song in songs:
    print(i, song.strip())
    i = i + 1

f.close()