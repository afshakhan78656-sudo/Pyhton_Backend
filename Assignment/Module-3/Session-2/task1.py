f = open("lyrics.txt", "r")

print("Position:", f.tell())

data = f.read(10)
print("First 10 characters:", data)

print("Position:", f.tell())

f.close()