matrix = [
    [1, 2, 3, 4],
    [5, 0, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

def set_matrix_zero(matrix):
    row = len(matrix)
    col = len(matrix[0])
    zero_row = set()
    zero_col = set()
    
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 0:
                zero_row.add(i)
                zero_col.add(j)
                
    for i in range(col):
        for j in range(row):
            if i in zero_row or j in zero_col:
                matrix [i][j] = 0
    return matrix 
result = set_matrix_zero(matrix)
print(result)    
for row in result :
    print(row)     