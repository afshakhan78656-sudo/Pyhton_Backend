playlists = {"user1": {"Favourites": ["Song1", "Song2"]}}

if "user2" not in playlists:
    playlists["user2"] = {}

if "Chill" not in playlists["user2"]:
    playlists["user2"]["Chill"] = []

playlists["user2"]["Chill"].append("Song3")

print(playlists)