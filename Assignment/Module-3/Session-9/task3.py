import re

def extract_hashtags(text):
    return re.findall(r"#[a-zA-Z0-9_]+", text)

caption = input("Enter Instagram caption: ")

print(extract_hashtags(caption))