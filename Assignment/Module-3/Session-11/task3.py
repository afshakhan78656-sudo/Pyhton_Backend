import pymysql

mydb = pymysql.connect(host="localhost", user="root", password="", database="music_stream")

mycursor = mydb.cursor()

mycursor.execute("SELECT name, song_count FROM playlists WHERE song_count > 10")

data = mycursor.fetchall()

for row in data:
    print("Playlist:", row[0], "Song Count:", row[1])

mycursor.close()
mydb.close()