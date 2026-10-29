class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

class Influencer(User):
    def __init__(self, username, email, followers):
        super().__init__(username, email)
        self.followers = followers

class VerifiedInfluencer(Influencer):
    def __init__(self, username, email, followers, badge):
        super().__init__(username, email, followers)
        self.badge = badge

obj = VerifiedInfluencer("ramesh", "ramesh@gmail.com", 15000, "Blue Tick")

print(obj.username)
print(obj.email)
print(obj.followers)
print(obj.badge)