f = open("playlist.txt", "w")
f.write("Kesariya\nChaleya\nTune Kya Kiya\n O sanam") 
f.close()

f = open("playlist.txt", "r")

f.readline()
f.readline()

print(f.readline().strip())

f.close()