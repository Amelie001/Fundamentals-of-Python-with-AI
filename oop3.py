# oop3

class Movie:

    def __init__(self, name, seats): 
        self.name = name 
        self.seats = seats

    def book_ticket(self, tickets):
        if tickets <= self.seats: 
            self.seats -= tickets 
            print(tickets, "ticket(s) booked.")
        else:
            print("Not enough seats available.")

    def display(self): 
        print("\nMovie:", self.name)
        print("Seats remaining:", self.seats)

movie = Movie("Avengers", 50)

movie.display()
movie.book_ticket(5)
movie.display()
movie.book_ticket(10)
movie.display()