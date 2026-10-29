import pymysql

def delete_playlist(playlist_id):
    mydb = None
    mycursor = None

    try:
        mydb = pymysql.connect(host="localhost", user="root", password="", database="music_stream")

        mycursor = mydb.cursor()

        sql = "DELETE FROM playlists WHERE id=%s"
        mycursor.execute(sql, (playlist_id,))

        if mycursor.rowcount > 0:
            mydb.commit()
            print("Playlist deleted successfully")
        else:
            print("Playlist ID not found")

    except pymysql.MySQLError as e:
        print("Error:", e)

    finally:
        if mycursor:
            mycursor.close()

        if mydb:
            mydb.close()


playlist_id = int(input("Enter playlist ID: "))

delete_playlist(playlist_id)