def generate_spiral(matrix):
    if not matrix:
        return[]
    n = len(matrix)
    top , left , bottom , right = 0,0,n-1,n-1
    result []
    
    for i in range (left , right):
    
        print(matrix[top][i])
    top += 1
    for j in range(top , bottom):
        print(matrix[i][right])
    right -=1
    for i in range(right , left):
        print(matrix[bottom][i])
    bottom -=1
    for i in range(bottom , top):
        print(matrix[i][left])
    left +=1
    return result
print(result)