from insta.likes import like_count
from insta.comment import comment_count

likes = like_count(100, 5)
comments = comment_count(20, 3)

print("Total likes:", likes)
print("Total comments:", comments)