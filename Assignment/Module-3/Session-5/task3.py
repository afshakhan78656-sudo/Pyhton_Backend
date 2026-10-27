class InstagramPost:
    def __init__(self, caption, likes, comments):
        self.caption = caption
        self.likes = likes
        self.comments = comments

    def add_comment(self, comment_text):
        self.comments.append(comment_text)
        self.likes = self.likes + 1


p1 = InstagramPost("My Photo", 10, ["Nice photo"])

p1.add_comment("Amazing!")

print("Caption:", p1.caption)
print("Likes:", p1.likes)
print("Comments:", p1.comments)