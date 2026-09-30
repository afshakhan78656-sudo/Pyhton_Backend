fav_apps=('Instagram', 'Zomato', 'Spotify', 'WhatsApp', 'Flipkart')
print("My favorite apps are:",fav_apps)

fav_apps[0]="Snapchat"

# Error aayega because tuple is immutable.
# Tuple ke elements ko change nahi kar sakte.

#TypeError: 'tuple' object does not support item assignment