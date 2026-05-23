matrix = [
    [10, 20, 30],
    [45, 5, 60],
    [25, 90, 15]
]

largest = matrix[0][0]

for row in matrix:
    for num in row:
        if num > largest:
            largest = num

print("Largest element is:", largest)