class Content:
    def display(self, title):
        print("Title:", title)

class Movie(Content):
    def display(self, title, year):
        super().display(title)
        print("Year:", year)

obj= Movie()
obj.display("Jawan", 2023)