matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]

transpose = []

for j in range(len(matrix[0])): 
    row = []
    for i in range(len(matrix)): 
        row.append(matrix[i][j]) 
    transpose.append(row)

print("Transpose matrix (4x3):")

for row in transpose: 
    print(row) 