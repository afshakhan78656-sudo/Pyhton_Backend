class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

s1 = Song("Kesariya", "Arijit Singh", 240)
s2 = Song("Heeriye", "Jasleen Royal", 210)

print(s1.title, s1.artist, s1.duration)
print(s2.title, s2.artist, s2.duration)