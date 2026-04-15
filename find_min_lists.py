matrix = [
    [10,25,3], 
    [45,6,17], 
    [8,90,2]
]

min_value = matrix[0][0]
min_position = (0,0)

for i in range(len(matrix)): 
    for j in range(len(matrix[0])): 
        if matrix[i][j] < min_value: 
            min_value = matrix[i][j]
            min_position = (i,j)

print("Minimum value:", min_value)
print("Minimum position:", min_position)