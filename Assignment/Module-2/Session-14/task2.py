playlists = {}

def add_song(user, playlist, song, artist):

    if user not in playlists:
        playlists[user] = {}

    if playlist not in playlists[user]:
        playlists[user][playlist] = []

    playlists[user][playlist].append(song)

    print(song, "-", artist)


add_song("raj", "Favourites", "Kesariya", "Arijit Singh")
add_song("raj", "Favourites", "Believer", "Imagine Dragons")
add_song("simran", "Chill", "Heeriye", "Jasleen Royal")

print(playlists)