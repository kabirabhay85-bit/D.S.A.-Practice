matrix = [
    [1, 2, 3, 4],
    [5, 0, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
def rotate_matrix(matrix):
    n = len(matrix)
    result= [[0 for _ in range(n)] for _ in range(n)]
    for i in range(0,n):
        for j in range(0,n):
            result[j][(n-1) - i] = matrix [i][j]
    return result
result = rotate_matrix(matrix)
for row in result:
    print(row)
    
# For counterclockwise

matrix = [
    [1, 2, 3, 4],
    [5, 0, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
def rotate_matrix(matrix):
    n = len(matrix)
    result= [[0 for _ in range(n)] for _ in range(n)]
    for i in range(0,n):
        for j in range(0,n):
            result[i][(n-1) - j] = matrix [i][j]
    return result
result = rotate_matrix(matrix)
for row in result:
    print(row)