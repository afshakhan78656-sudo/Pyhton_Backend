class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

obj = User("ramesh", "ramesh@gmail.com")

print(obj.username)
print(obj.email)