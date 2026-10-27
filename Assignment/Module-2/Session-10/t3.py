from task3 import add_song, remove_song

playlist = []

playlist = add_song("Kesariya", playlist)
playlist = add_song("Tune Kya Kiya", playlist)
playlist = add_song("O Sanam", playlist)

playlist = remove_song("Kesariya", playlist)

print(playlist)