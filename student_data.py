student1 = ("Amelie", 92)
student2 = ("Lucas", 62)
student3 = ("Sofia", 47)
student4 = ("Daniel", 29)

students = [student1, student2, student3, student4]

for student in students:
    name = student[0]
    mark = student[1]

    if mark >= 40:
        result = "Pass"
    else:
        result = "Fail"

    if mark >= 80:
        grade = "A"
    elif mark >= 70:
        grade = "B"
    elif mark >= 60:
        grade = "C"
    elif mark >= 50:
        grade = "D"
    elif mark >= 40:
        grade = "E"
    else:
        grade = "F"

    print("Name:", name)
    print("Mark:", mark)
    print("Result:", result)
    print("Grade:", grade)
    print()