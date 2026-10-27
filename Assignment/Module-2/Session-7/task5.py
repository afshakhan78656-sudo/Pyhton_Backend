def char_count_dict(s):
    d = {}

    for i in s:
        d[i] = s.count(i)

    return d


s = input("Enter Name:").lower()
d = char_count_dict(s)

for i in sorted(d):
    print(i, ":", d[i])