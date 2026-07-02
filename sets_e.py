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

        if student_name in clubs[club_name]; 
            clubs[club_name].remove(student_name)
            print(student_name, "removed from", club_name.capitalize(), "Club successfully.")
        else: 
            print("Student not found in this club.")
    else: 
        print("Club not found.")