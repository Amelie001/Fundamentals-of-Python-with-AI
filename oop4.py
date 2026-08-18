# Library Book System 

class Book: 
    def __init__(self, title, author, available = True): 
        self.title = title
        self.author = author 
        self.available = available 

    def borrow(self): 
        if self.available: 
            self.available = False 
            print(self.title, "borrowed.")

        else: 
            print("Book is already borrowed.")

    def return_book(self): 
        self.available = True
        print(self.title, "returned.")

    def display(self): 
        print("\nTitle:", self.title)
        print("Author:", self.author)
        print("Available:", self.available)

book = Book("Python Basics", "Mark Lutz")

book.display()
book.borrow()
book.display()
book.return_book()
book.display()