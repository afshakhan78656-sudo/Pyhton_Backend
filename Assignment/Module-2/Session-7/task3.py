def word_freq_dict(s):
    d={}

    for i in s.split():
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    return d
s= "Virat scored 100 Rohit scored 80 Gill scored 50"
print(word_freq_dict(s))
