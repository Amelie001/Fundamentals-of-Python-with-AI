# Online Course Enrollment System

courses = {
    "python": {"Ali", "Sara", "Ayaan"},
    "web development": {"Sara", "Kabir", "Ali"},
    "ai": {"Ayaan", "Riya", "Kabir"},
    "data science": {"Riya", "Sara", "Zoya"},
    "ui/ux": {"Zoya", "Kabir", "Ali"}
}


# Function to display all course names

def display_courses():
    print("\nAvailable Courses:")
    for course in courses:
        print("-", course.title())


# Function to display students enrolled in a course

def display_students():
    course_name = input("Enter course name: ").lower()

    if course_name in courses:
        if len(courses[course_name]) == 0:
            print("No students are enrolled in this course.")
        else:
            print(f"\nStudents enrolled in {course_name.title()}:")
            for student in courses[course_name]:
                print(student)
    else:
        print("Course not found.")


# Function to enroll a student in a course

def enroll_student():
    course_name = input("Enter course name: ").lower()

    if course_name in courses:
        student_name = input("Enter student name to enroll: ").title()

        if student_name in courses[course_name]:
            print("Student is already enrolled in this course.")
        else:
            courses[course_name].add(student_name)
            print(
                student_name,
                "enrolled in",
                course_name.title(),
                "successfully."
            )
    else:
        print("Course not found.")


# Function to remove a student from a course

def remove_student():
    course_name = input("Enter course name: ").lower()

    if course_name in courses:
        student_name = input("Enter student name to remove: ").title()

        if student_name in courses[course_name]:
            courses[course_name].remove(student_name)
            print(
                student_name,
                "removed from",
                course_name.title(),
                "successfully."
            )
        else:
            print("Student is not enrolled in this course.")
    else:
        print("Course not found.")


# Function to check whether a student is enrolled in a course

def check_student():
    course_name = input("Enter course name: ").lower()

    if course_name in courses:
        student_name = input("Enter student name to check: ").title()

        if student_name in courses[course_name]:
            print(
                student_name,
                "is enrolled in",
                course_name.title()
            )
        else:
            print(
                student_name,
                "is NOT enrolled in",
                course_name.title()
            )
    else:
        print("Course not found.")


# Function to show common students between two courses

def common_students():
    course1 = input("Enter first course name: ").lower()
    course2 = input("Enter second course name: ").lower()

    if course1 in courses and course2 in courses:
        common = courses[course1].intersection(courses[course2])

        if len(common) == 0:
            print("No students are enrolled in both courses.")
        else:
            print(
                f"\nStudents enrolled in both "
                f"{course1.title()} and {course2.title()}:"
            )

            for student in common:
                print(student)

    else:
        print("One or both course names are invalid.")


# Function to show all students from two courses

def all_students_two_courses():
    course1 = input("Enter first course name: ").lower()
    course2 = input("Enter second course name: ").lower()

    if course1 in courses and course2 in courses:
        all_students = courses[course1].union(courses[course2])

        print(
            f"\nAll students enrolled in "
            f"{course1.title()} or {course2.title()}:"
        )

        for student in all_students:
            print(student)

    else:
        print("One or both course names are invalid.")


# Function to show students only in the first course

def only_in_first_course():
    course1 = input("Enter first course name: ").lower()
    course2 = input("Enter second course name: ").lower()

    if course1 in courses and course2 in courses:
        difference = courses[course1].difference(courses[course2])

        if len(difference) == 0:
            print(
                f"No students are enrolled only in "
                f"{course1.title()}."
            )
        else:
            print(
                f"\nStudents enrolled only in {course1.title()}:"
            )

            for student in difference:
                print(student)

    else:
        print("One or both course names are invalid.")


# Function to show students enrolled in exactly one of two courses

def students_in_exactly_one():
    course1 = input("Enter first course name: ").lower()
    course2 = input("Enter second course name: ").lower()

    if course1 in courses and course2 in courses:
        result = courses[course1].symmetric_difference(
            courses[course2]
        )

        if len(result) == 0:
            print("No such students found.")
        else:
            print(
                f"\nStudents enrolled in exactly one of "
                f"{course1.title()} or {course2.title()}:"
            )

            for student in result:
                print(student)

    else:
        print("One or both course names are invalid.")


# Function to count students in a course

def count_students():
    course_name = input("Enter course name: ").lower()

    if course_name in courses:
        print(
            "Total students in",
            course_name.title(),
            "=",
            len(courses[course_name])
        )
    else:
        print("Course not found.")


# Function to show all unique students across all courses

def all_unique_students():
    unique_students = set()

    for course in courses.values():
        unique_students = unique_students.union(course)

    print("\nAll Unique Students:")

    for student in unique_students:
        print(student)

    print("Total unique students =", len(unique_students))


# Function to check whether one course is a subset of another

def check_subset():
    course1 = input("Enter first course name: ").lower()
    course2 = input("Enter second course name: ").lower()

    if course1 in courses and course2 in courses:
        if courses[course1].issubset(courses[course2]):
            print(
                f"All students in {course1.title()} are also "
                f"enrolled in {course2.title()}."
            )
        else:
            print(
                f"{course1.title()} is NOT a subset of "
                f"{course2.title()}."
            )
    else:
        print("One or both course names are invalid.")


# Main menu

while True:
    print("\n===== Online Course Enrollment System =====")
    print("1. Display all courses")
    print("2. Display students in a course")
    print("3. Enroll a student")
    print("4. Remove a student")
    print("5. Check whether a student is enrolled")
    print("6. Show common students between two courses")
    print("7. Show all students from two courses")
    print("8. Show students only in first course")
    print("9. Show students in exactly one of two courses")
    print("10. Count students in a course")
    print("11. Show all unique students")
    print("12. Check if one course is a subset of another")
    print("13. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        display_courses()

    elif choice == 2:
        display_students()

    elif choice == 3:
        enroll_student()

    elif choice == 4:
        remove_student()

    elif choice == 5:
        check_student()

    elif choice == 6:
        common_students()

    elif choice == 7:
        all_students_two_courses()

    elif choice == 8:
        only_in_first_course()

    elif choice == 9:
        students_in_exactly_one()

    elif choice == 10:
        count_students()

    elif choice == 11:
        all_unique_students()

    elif choice == 12:
        check_subset()

    elif choice == 13:
        print("Exiting Online Course Enrollment System...")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 13.")