students = [
    ["Amelie", 95],
    ["Leo", 82],
    ["Sofia", 88]
]

print("Original 2D list:")
for row in students:
    print(row)

# Updated
students[1][1] = 89

# Deleted
del students[2]

# Inserted
students.insert(1, ["Mia", 85])

print("\n2D List after update, delete and insert:")
for row in students:
    print(row)

