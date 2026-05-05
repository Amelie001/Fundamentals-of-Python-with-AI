def view_seats(seats):
    print("\nSeat Status")
    for number, status, name in seats:
        if status == "Available":
            print(f"Seat {number}: Available")
        else:
            print(f"Seat {number}: Booked by {name}")


def book_seat(seats):
    seat_choice = int(input("Enter seat number: "))
    name = input("Enter your name: ")

    for i in range(len(seats)):
        number, status, passenger = seats[i]

        if number == seat_choice:
            if status == "Available":
                seats[i] = (number, "Booked", name)
                print("Booking successful!")
            else:
                print("Seat already booked by", passenger)
            return

    print("Invalid seat number.")


def main():
    seats = [
        (1, "Available", ""),
        (2, "Booked", "Lucas"),
        (3, "Available", ""),
        (4, "Available", ""),
        (5, "Booked", "Sofia"),
        (6, "Available", "")
    ]

    while True:
        print("\nBus Reservation System")
        print("1. View Seats")
        print("2. Book Seat")
        print("3. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            view_seats(seats)
        elif choice == 2:
            book_seat(seats)
        elif choice == 3:
            print("Exiting system...")
            break
        else:
            print("Invalid choice.")


main()