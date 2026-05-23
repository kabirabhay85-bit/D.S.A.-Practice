nums = [7,10,-3,-1,-10,6]

def rearrange(nums):
    n = len(nums)
    pos = [] 
    neg = []
    for i in range (0,n):
        if nums[i]>=0:
            pos.append(nums[i])
        else:
            neg.append(nums[i])
    for i in range(0,len(pos)):
        nums[2*i] = pos[i]
        nums[(2*i) + 1] = neg[i]
    return nums

print(rearrange(nums))

# optimal solution

nums = [5,10,-3,-1,-10,6]

def rearrange(nums):
    n = len(nums)
    result = [0]*n
    pos_index = 0
    neg_index = 1
    for i in range(0,n):
        if nums[i]>=0:
            result[pos_index] = nums[i]
            pos_index +=2
        else:
            result[neg_index] = nums[i]
            neg_index +=2
    return result
print(rearrange(nums))