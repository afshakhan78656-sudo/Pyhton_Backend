def display_friends(friends):
    for i, j in friends.items():
        print(i + ":", j , "followers")


friends = {
    "Yushra": "2.3K",
    "Aksha": "5K",
    "Vidhya": "1.8K"
}

display_friends(friends)