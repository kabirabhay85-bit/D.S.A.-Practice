
nums = [1,0,2,4,4,3,0,0,3,5,1]

def move_zero(nums):
    n = len(nums)
    temp = []
    
    # Step 1: collect non-zero elements
    for i in range(0, n):
        if nums[i] != 0:
            temp.append(nums[i])
    
    nz = len(temp)  # number of non-zero elements
    
    # Step 2: put non-zero elements back in nums
    for i in range(0, nz):
        nums[i] = temp[i]
    
    # Step 3: fill the rest with zeros
    for i in range(nz, n):
        nums[i] = 0
    
    return nums

print(move_zero(nums))