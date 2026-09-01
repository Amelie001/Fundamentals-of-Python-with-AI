class Book: 

    def __init__(self, title, author): 
        self.title = title
        self.author = author 

    def display_book(self): 
        print("Title:", self.title)
        print("Author:", self.author)

    def read(self): 
        print("Reading", self.title)

class EBook(Book):

    def download(self): 
        print(self.title, "has been downloaded.")

    def show_file_size(self, size): 
        print("File size:", size, "MB")

ebook = EBook("Python Basics", "John Smith")

ebook.display_book()
ebook.read()
ebook.download()
ebook.show_file_size(5)