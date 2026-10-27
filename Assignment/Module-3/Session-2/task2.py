def read_next_line(filename):
    f = open(filename, "r")

    f.seek(20)
    print(f.readline())

    f.close()


read_next_line("lyrics.txt")