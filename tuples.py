student_details = ("Amelie", 14, "Home educated", 87, 98, 92)

for x in student_details:
    print(x, end = " ")

name, age, school, maths, computer_science, economics = student_details

print(name)
print(age)
print(school)
print(maths)
print(computer_science)
print(economics)

my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))

print(my_tuple[0][3])
print(my_tuple[1][1])