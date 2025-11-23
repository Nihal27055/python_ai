class book:
    def __init__(self, author, title):
        self.author = author
        self.title = title

    def right(self):
        print(f"A Story Name is '{self.title}' Writed by {self.author}")

a = book("Nihal", "The King")
a.right()
