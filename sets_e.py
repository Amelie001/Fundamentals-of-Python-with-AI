# Student Club Management System using Set 

# Dictionary to store club names and their students 
clubs = {
    "coding": {"Ayaan", "Sara", "Riya"}, 
    "music": {"Sara", "Kabir", "Riya"},
    "sports": {"Ayaan", "Kabir", "Vihaan"}
}

# Function to display all club names 
def display_clubs(): 
    print("\nAvailable Clubs:")
    for club in clubs: 
        print("-", club.capitalize())

# Function to display students of a particular club 
def display_students(): 
    club_name = input("Enter club name: ").lower()

    if club_name in clubs: 
        if len(clubs[club_name]) == 0: 
            print("No students in this club.")
        else: 
            print(f"\nStudents in {club_name.capitalize()} Club:")
            for student in clubs[club_name]: 
                print(student)
    else: 
        print("Club not found.")

# Function to add a student to a club 
def add_student(): 
    club_name = input("Enter club name: ").lower()

    if club_name in clubs:
        student_name = input("Enter student name to add: "). title()

        if student_name in clubs[club_name]: 
            print("Student already exists in this club.")
        else: 
            clubs[club_name].add(student_name)
            print(student_name, "added to", club_name.capitalize(), "Club successfully.")
    else: 
        print("Club not found.")

# Function to remove a student from a club 
def remove_student(): 
    club_name = input("Enter club name: ").lower()

    if club_name in clubs: 
        student_name = input("Enter student name to remove: ").title()

        if student_name in clubs[club_name]: 
            clubs[club_name].remove(student_name)
            print(student_name, "removed from", club_name.capitalize(), "Club successfully.")
        else: 
            print("Student not found in this club.")
    else: 
        print("Club not found.")

# Function to check whether a student is in a club
def check_student(): 
    club_name = input("Enter club name: ").lower()

    if club_name in clubs: 
        student_name = input("Enter student name to check: ").title()

        if student_name in clubs[club_name]: 
            print(student_name, "is a member of", club_name.capitalize(), "Club.")
        else: 
            print(student_name, "is NOT a member of", club_name.capitalize(), "Club.")
    else: 
        print("Club not found.")

# Function to show common students between two clubs 
def common_students(): 
    club1 = input("Enter first club name: ").lower()
    club2 = input("Enter second club name: ").lower()

    if club1 in clubs and club2 in clubs: 
        common = clubs[club1].intersection(clubs[club2])

        if len(common) == 0: 
            print("No common students in both clubs.")
        else:
            print(f"\nCommon students in {club1.capitalize()} and {club2.capitalize()} Clubs:")
            for student in common: 
                print(student)
    else: 
        print("One or both club names are invalid.")

# Function to show all students from two clubs (union)
def all_students_two_clubs(): 
    club1 = input("Enter first club name: ").lower()
    club2 = input("Enter second club name: ").lower()

    if club1 in clubs and club2 in clubs: 
        all_students = clubs[club1].union(clubs[club2])

        print(f"\nAll students in {club1.capitalize()} and {club2.capitalize()} Clubs:")
        for student in all_students: 
            print(student)
    else: 
        print("One or both club names are invalid.")

# Function to show students only in the first club (difference)
def only_in_first_club(): 
    club1 = input("Enter first club name: ").lower()
    club2 = input("Enter second club name: ").lower()

    if club1 in clubs and club2 in clubs: 
        diff = clubs[club1].difference(clubs[club2])

        if len(diff) == 0: 
            print(f"No students are exclusively in {club1.capitalize()} Club.")
        else: 
            print(f"\nStudents only in {club1.capitalize()} Club:")
            for student in diff: 
                print(student)
    else: 
        print("One or both club names are invalid.")

# Function to show students in exactly one of two clubs (symmetric difference)
def students_in_exactly_one(): 
    club1 = input("Enter first club name: ").lower()
    club2 = input("Enter second club name: ").lower()

    if club1 in clubs and club2 in clubs: 
        result = clubs[club1].symmetric_difference(clubs[club2])

        if len(result) == 0: 
            print("No such students are found.")
        else: 
            print(f"\nStudents in exactly one of {club1.capitalize()} or {club2.capitalize()} Clubs:")
            for student in result: 
                print(student)
    else:
        print("One or both club names are invalid.")

# Function to count students in a club 
def count_students(): 
    club_name = input("Enter club name: ").lower()

    if club_name in clubs: 
        print("Total students in", club_name.capitalize(), "Club =", len(clubs[club_name]))
    else:
        print("Club not found.")

# Function to show all unique students in all clubs
def all_unique_students(): 
    unique_students = set()

    for club in clubs.values(): 
        unique_students = unique_students.union(club)

    print("\nAll unique students in all clubs:")
    for student in unique_students: 
        print(student)

    print("Total unique students =", len(unique_students))

# Function to check subset 
def check_subset(): 
    club1 = input("Enter first club name: ").lower()
    club2 = input("Enter second club name: ").lower()

    if club1 in clubs and club2 in clubs: 
        if clubs[club1].issubset(clubs[club2]): 
            print(f"All students of {club1.capitalize()} Club are present in {club2.capitalize()} Club.")
        else: print(f"{club1.capitalize()} Club is NOT a subset of {club2.capitalize()} Club.")
    else: 
        print("One or both club names are invalid.")

# Main menu 
while True: 
    print("\n===== Student Club Management System =====")
    print("1. Display all clubs")
    print("2. Display all students of a club")
    print("3. Add a student to a club")
    print("4. Remove a student from a club")
    print("5. Check whether a student is in a club")
    print("6. Show common students between two clubs")
    print("7. Show all students from two clubs")
    print("8. Show students only in first club")
    print("9. Show students in exactly one of two clubs")
    print("10. Count students in a club")
    print("11. Show all unique students in all clubs")
    print("12. Check if one club is a subset of another")
    print("13. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        display_clubs()
    
    elif choice == 2: 
        display_students()

    elif choice == 3: 
        add_student()

    elif choice == 4:
        remove_student()

    elif choice == 5: 
        check_student()

    elif choice == 6: 
        common_students()

    elif choice == 7: 
        all_students_two_clubs()

    elif choice == 8: 
        only_in_first_club()

    elif choice == 9: 
        students_in_exactly_one()

    elif choice == 10: 
        count_students()

    elif choice == 11: 
        all_unique_students()

    elif choice == 12: 
        check_subset()

    elif choice == 13: 
        print("Exiting Student Club Management System...")
        break

    else: 
        print("Invalid choice. Please enter a number between 1 and 13.")