#lambda + map() — Song Duration

durations = input("Enter durations: ").split()
durations = list(map(int, durations))
seconds = list(map(lambda x: x * 60, durations))

print(seconds)