s = input("Enter Sentence:").lower()
stop = ["the", "and", "in", "of", "a", "to", "is"]
d = {}

for i in s.split():
    if i not in stop:
        d[i] = s.split().count(i)

print(d)