student = {
    "Name" : "Amelie", 
    "Age" : 14, 
    "StudentID" : "1234A",
    "Grade" : 9, 
    "Total marks" : 99
}

# Viewing particular values

print(student)

print(student["Name"])

# Adding / updating values 

student["Gender"] = "Female"
print(student)

student["StudentID"] = 1234
print(student)

# Removing a value 

del student["StudentID"]
print(student)

student.pop("Grade")
print(student)

# Viewing keys

for key in student.keys():
    print(key)

for value in student.values(): 
    print(value)

# Getting length of dictionary 

print(len(student))