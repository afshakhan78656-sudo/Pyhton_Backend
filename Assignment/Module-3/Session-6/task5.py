class VerifiedInfluencer:
    def __init__(self, username, followers, badge):
        self.username = username
        self.followers = followers
        self.badge = badge

    def display_profile(self):
        if self.followers >= 1000000:
            count = str(self.followers / 1000000) + "M"
        elif self.followers >= 1000:
            count = str(self.followers / 1000) + "K"
        else:
            count = str(self.followers)

        print("Username:", self.username)
        print("Followers:", count)
        print("Badge:", self.badge)


obj= VerifiedInfluencer("ramesh", 1500, "Verified")
obj.display_profile()
