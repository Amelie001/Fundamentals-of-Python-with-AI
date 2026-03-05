students = {
    "Amelie": {"Maths": 96, "CS": 98, "Economics": 92},
    "Leo": {"Maths": 80, "CS": 85, "Economics": 78},
    "Sofia": {"Maths": 88, "CS": 90, "Economics": 84}
}

for student, marks in students.items():

    total = sum(marks.values())
    average = total / len(marks)
    highest = max(marks.values())

    print("Student:", student)
    print("Total marks:", total)
    print("Average score:", average)
    print("Highest mark:", highest)
    print()