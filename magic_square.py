matrix = [
    [2,7,6],
    [9,5,1],
    [4,3,8]
]

target_sum = sum(matrix[0])
is_magic = True 

for row in matrix: 
    if sum(row) != target_sum: 
        is_magic = False 

for col in range(len(matrix[0])): 
    col_sum = 0 
    for row in range(len(matrix)): 
        col_sum += matrix[row][col]
    if col_sum != target_sum: 
        is_magic = False 

diag1 = 0

for i in range(len(matrix)): 
    diag1 += matrix[i][i]

diag2 = 0 

for i in range(len(matrix)): 
    diag2 += matrix[i][len(matrix) - 1 - i]

if diag1 != target_sum or diag2 != target_sum:
    is_magic = False

if is_magic: 
    print("It is a magic square.")
else: 
    print("Not a magic square.")