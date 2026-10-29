class InstaStory:
    def share(self):
        print("Sharing an image story")

class WhatsAppStory(InstaStory):
    def share(self):
        super().share()
        print("Sharing a text status")

obj = WhatsAppStory()

obj.share()
