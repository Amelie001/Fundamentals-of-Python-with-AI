A = [[1,2,3],[4,5,6],[7,8,9]]
B = [[10,11,12],[13,14,15],[16,17,18]]

# Addition
add = []
for i in range(3):
    row = []
    for j in range(3):
        row.append(A[i][j] + B[i][j])
    add.append(row)

# Subtraction
sub = []
for i in range(3):
    row = []
    for j in range(3):
        row.append(A[i][j] - B[i][j])
    sub.append(row)

# Multiplication
mul = []
for i in range(3):
    row = []
    for j in range(3):
        total = 0
        for k in range(3):
            total += A[i][k] * B[k][j]
        row.append(total)
    mul.append(row)

print("Addition:")
for r in add:
    print(r)

print("\nSubtraction:")
for r in sub:
    print(r)

print("\nMultiplication:")
for r in mul:
    print(r)