# Book Recommendation System

books = {
    "fantasy": {
        "Harry Potter",
        "The Hobbit",
        "Percy Jackson"
    },

    "dystopian": {
        "The Maze Runner",
        "The Hunger Games",
        "1984"
    },

    "mystery": {
        "A Good Girl's Guide To Murder",
        "Sherlock Holmes",
        "Gone Girl"
    },

    "romance": {
        "The Fault In Our Stars",
        "The Notebook",
        "Pride And Prejudice"
    },

    "read": {
        "The Maze Runner",
        "1984",
        "Harry Potter"
    }
}


# Function to display all available genres
def display_genres():
    print("\nAvailable genres:")

    for genre in books:
        if genre != "read":
            print("-", genre.capitalize())


# Function to display books from a selected genre
def display_books():
    genre_name = input("Enter genre name: ").lower()

    if genre_name in books and genre_name != "read":

        if len(books[genre_name]) == 0:
            print("There are no books in this genre.")

        else:
            print(f"\nBooks in the {genre_name.capitalize()} genre:")

            for book in books[genre_name]:
                print("-", book)

    else:
        print("Genre not found.")


# Function to add a book to a genre
def add_book():
    genre_name = input("Enter genre name: ").lower()

    if genre_name in books and genre_name != "read":

        book_name = input("Enter book name to add: ").title()

        if book_name in books[genre_name]:
            print("This book already exists in this genre.")

        else:
            books[genre_name].add(book_name)

            print(
                book_name,
                "added to the",
                genre_name.capitalize(),
                "genre successfully."
            )

    else:
        print("Genre not found.")


# Function to remove a book from a genre
def remove_book():
    genre_name = input("Enter genre name: ").lower()

    if genre_name in books and genre_name != "read":

        book_name = input("Enter book name to remove: ").title()

        if book_name in books[genre_name]:

            books[genre_name].remove(book_name)

            print(
                book_name,
                "removed from the",
                genre_name.capitalize(),
                "genre successfully."
            )

        else:
            print("Book not found in this genre.")

    else:
        print("Genre not found.")


# Function to mark a book as read
def mark_as_read():
    book_name = input("Enter the name of the book you have read: ").title()

    if book_name in books["read"]:
        print("This book is already marked as read.")

    else:
        books["read"].add(book_name)

        print(book_name, "has been marked as read.")


# Function to remove a book from the read set
def mark_as_unread():
    book_name = input("Enter the name of the book: ").title()

    if book_name in books["read"]:

        books["read"].remove(book_name)

        print(book_name, "has been removed from your read books.")

    else:
        print("This book is not marked as read.")


# Function to display all books that have been read
def display_read_books():

    if len(books["read"]) == 0:
        print("You have not marked any books as read.")

    else:
        print("\nBooks you have read:")

        for book in books["read"]:
            print("-", book)


# Function to check whether a book has been read
def check_if_read():
    book_name = input("Enter a book name: ").title()

    if book_name in books["read"]:
        print(book_name, "has been read.")

    else:
        print(book_name, "has not been read.")


# Function to recommend unread books from a genre
def recommend_books():
    genre_name = input("Enter a genre: ").lower()

    if genre_name in books and genre_name != "read":

        recommendations = books[genre_name].difference(books["read"])

        if len(recommendations) == 0:
            print("You have already read all the books in this genre!")

        else:
            print(
                f"\nRecommended unread books from the "
                f"{genre_name.capitalize()} genre:"
            )

            for book in recommendations:
                print("-", book)

    else:
        print("Genre not found.")


# Function to show common books between two genres
def common_books():
    genre1 = input("Enter the first genre: ").lower()
    genre2 = input("Enter the second genre: ").lower()

    if (
        genre1 in books
        and genre2 in books
        and genre1 != "read"
        and genre2 != "read"
    ):

        common = books[genre1].intersection(books[genre2])

        if len(common) == 0:
            print("There are no common books in these genres.")

        else:
            print(
                f"\nBooks found in both {genre1.capitalize()} "
                f"and {genre2.capitalize()}:"
            )

            for book in common:
                print("-", book)

    else:
        print("One or both genre names are invalid.")


# Function to show all books from two genres
def combine_genres():
    genre1 = input("Enter the first genre: ").lower()
    genre2 = input("Enter the second genre: ").lower()

    if (
        genre1 in books
        and genre2 in books
        and genre1 != "read"
        and genre2 != "read"
    ):

        combined_books = books[genre1].union(books[genre2])

        print(
            f"\nAll books from {genre1.capitalize()} "
            f"and {genre2.capitalize()}:"
        )

        for book in combined_books:
            print("-", book)

    else:
        print("One or both genre names are invalid.")


# Function to show books only in the first genre
def books_only_in_first_genre():
    genre1 = input("Enter the first genre: ").lower()
    genre2 = input("Enter the second genre: ").lower()

    if (
        genre1 in books
        and genre2 in books
        and genre1 != "read"
        and genre2 != "read"
    ):

        different_books = books[genre1].difference(books[genre2])

        if len(different_books) == 0:
            print(
                f"There are no books exclusively in "
                f"{genre1.capitalize()}."
            )

        else:
            print(
                f"\nBooks only in the {genre1.capitalize()} genre:"
            )

            for book in different_books:
                print("-", book)

    else:
        print("One or both genre names are invalid.")


# Main menu
while True:

    print("\n--- BOOK RECOMMENDATION SYSTEM ---")

    print("1. Display all genres")
    print("2. Display books in a genre")
    print("3. Add a book to a genre")
    print("4. Remove a book from a genre")
    print("5. Mark a book as read")
    print("6. Mark a book as unread")
    print("7. Display read books")
    print("8. Check whether a book has been read")
    print("9. Recommend unread books")
    print("10. Find common books between two genres")
    print("11. Combine books from two genres")
    print("12. Show books only in the first genre")
    print("13. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        display_genres()

    elif choice == "2":
        display_books()

    elif choice == "3":
        add_book()

    elif choice == "4":
        remove_book()

    elif choice == "5":
        mark_as_read()

    elif choice == "6":
        mark_as_unread()

    elif choice == "7":
        display_read_books()

    elif choice == "8":
        check_if_read()

    elif choice == "9":
        recommend_books()

    elif choice == "10":
        common_books()

    elif choice == "11":
        combine_genres()

    elif choice == "12":
        books_only_in_first_genre()

    elif choice == "13":
        print("Thank you for using the Book Recommendation System!")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 13.")