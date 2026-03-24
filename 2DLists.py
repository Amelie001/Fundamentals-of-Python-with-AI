matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix)

print(len(matrix))

print(len(matrix[0]))

print(matrix[1][2])

print("\n")

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(matrix[i][j], end = " ")

    print("\n")

# Take user input for creating a matrix

rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
matrix = []

for i in range(rows): 
    temp = []

    for j in range(columns):
        x = int(input("Enter your elements: "))
        temp.append(x)

    matrix.append(temp)

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(matrix[i][j], end = " ")

    print("\n")

# Square matrix and diagonal elements 

matrix = []

n = int(input("Enter the dimensions of the matrix: "))

for i in range(n):
    temp = []
    for j in range(n):
        x = int(input("Enter your elements: "))
        temp.append(x)
    matrix.append(temp)

print("Diagonal Elements: ")

for i in range(n): 
    print(matrix[i][j])

# Addition and subtraction of 2D Lists

A = [
    [1, 2], 
    [3, 4]
]

B = [
    [5, 6],
    [7, 8]
]

additionResult = [
    [0, 0],
    [0, 0]
]

subtractionResult = [
    [0, 0],
    [0, 0]
]

for i in range(2):
    for j in range(2): 
        additionResult[i][j] = A[i][j] + B[i][j]
        subtractionResult[i][j] = A[i][j] - B[i][j]

print("Addition Result: ")

for i in range(2): 
    for j in range(2): 
        print(additionResult[i][j], end = " ")
    print("\n")

print("Subtraction Result: ")

for i in range(2): 
    for j in range(2): 
        print(subtractionResult[i][j], end = " ")
    print("\n")

# Matrix multiplication

A = [
    [1, 2], 
    [3, 4]
]

B = [
    [5, 6],
    [7, 8]
]

multiplicationResult = [
    [0, 0],
    [0, 0]
]

for i in range(2): 
    for j in range(2): 
        for k in range(2):
            multiplicationResult[i][j] += A[i][k] * B[k][j]

print("Multiplication result: ")

for i in range(2):
    for j in range(2): 
        print(multiplicationResult[i][j], end = " ")
    print("\n")