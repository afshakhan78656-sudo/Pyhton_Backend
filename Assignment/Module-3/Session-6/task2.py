class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

class Influencer(User):
    def __init__(self, username, email, followers):
        super().__init__(username, email)
        self.followers = followers

obj = Influencer("ramesh", "ramesh@gmail.com", 5000)

print(obj.username)
print(obj.email)
print(obj.followers)