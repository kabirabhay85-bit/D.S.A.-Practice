nums = [1,1,0,1,0,1,1,1,1,0,1,1]

def consecutive_ones(nums):
    n = len(nums)
    count = 0
    max_count = 0
    for i in range(0,n):
        if nums[i] == 1:
            count +=1
        else:
            max_count = max(max_count,count)
            count = 0
    return max(max_count,count)
print(consecutive_ones(nums))