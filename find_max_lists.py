matrix = [
    [10,25,3], 
    [45,6,17], 
    [8,90,2]
]

max_value = matrix[0][0]
max_position = (0,0)

for i in range(len(matrix)): 
    for j in range(len(matrix[0])): 
        if matrix[i][j] > max_value: 
            max_value = matrix[i][j]
            max_position = (i,j)

print("Maximum value:", max_value)
print("Maximum position:", max_position)