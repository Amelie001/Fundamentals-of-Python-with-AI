# Movie Booking 

class MovieBooking: 
    def __init__(self, movie_name, seat_number, ticket_price): 
        # Public 
        self.movie_name = movie_name 
        # Protected 
        self._seat_number = seat_number 
        # Private 
        self.__ticket_price = ticket_price 
        self.__booking_status = "Pending"

    # Book ticket 
    def book_ticket(self): 
        if self.__booking_status == "Cancelled": 
            print("Cancelled ticket cannot be booked again.")
            return 
        if self.__booking_status == "Confirmed": 
            print("Ticket is already booked.")
            return 
        self.__booking_status = "Confirmed"
        print("Ticket booked successfully.")

    # Cancel ticket 
    def cancel_ticket(self): 
        if self.__booking_status == "Cancelled": 
            print("Ticket is already cancelled.")
        else: 
            self.__booking_status = "Cancelled"
            print("Ticket cancelled successfully.")

    # get ticket price 
    def get_price(self): 
        return self.__ticket_price

    # Get booking status 
    def get_booking_status(self): 
        return self.__booking_status

    # Display booking 
    def display_booking(self): 
        print("\nMovie Booking")
        print("--------------")
        print("Movie:", self.movie_name)
        print("Seat:", self._seat_number)
        print("Price: £", self.__ticket_price)
        print("Status:", self.__booking_status)

booking = MovieBooking("Avengers", "A12", 250)
booking.display_booking()
booking.book_ticket()
booking.display_booking()
booking.cancel_ticket()
booking.display_booking()