nums = [-2,1,-3,4,-1,2,1,-5,4]
def max_sum(nums):
    n = len(nums)
    maxi = float("-inf")
    for i in range(0,n):
        total = 0
        for j in range (i,n):
            total = total + nums[j]
            maxi = max(maxi,total)
    return maxi
    
print(max_sum(nums))