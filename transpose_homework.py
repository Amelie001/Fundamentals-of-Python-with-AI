matrix = [
    [1, 2, 3, 4, 5, 6],
    [7, 8, 9, 10, 11, 12],
    [13, 14, 15, 16, 17, 18],
    [19, 20, 21, 22, 23, 24],
    [25, 26, 27, 28, 29, 30]
]

transpose = []

for j in range(len(matrix[0])): 
    row = []
    for i in range(len(matrix)): 
        row.append(matrix[i][j]) 
    transpose.append(row)

print("Transpose matrix (5x6):")

for row in transpose: 
    print(row) 