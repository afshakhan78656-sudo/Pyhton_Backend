def format_follower_count(no):
    if no >= 1000000:
        return str(no / 1000000) + "M"
    elif no >= 1000:
        return str(no / 1000) + "K"
    else:
        return str(no)

no = int(input("Enter followers: "))

print(format_follower_count(no))

