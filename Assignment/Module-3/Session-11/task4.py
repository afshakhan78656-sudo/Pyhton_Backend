import pymysql

mydb = pymysql.connect(host="localhost", user="root", password="", database="music_stream")

mycursor = mydb.cursor()

sql = "UPDATE playlists SET name=%s WHERE name=%s"

mycursor.execute(sql, ("Chill Hits", "Chill Vibes"))

mydb.commit()

if mycursor.rowcount > 0:
    print("Playlist name updated successfully")
else:
    print("Playlist not found")

mycursor.close()
mydb.close()