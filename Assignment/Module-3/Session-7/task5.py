class Notification:
    def send(self):
        print("Sending notification")

class EmailNotification(Notification):
    def send(self):
        super().send()
        print("Sending Email")

class SMSNotification(Notification):
    def send(self):
        super().send()
        print("Sending SMS")

obj = EmailNotification()
obj = SMSNotification()

obj.send()
obj.send()