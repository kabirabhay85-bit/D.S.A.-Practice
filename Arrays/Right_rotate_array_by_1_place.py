nums = [5,-2,3,9,0,6,10,7]

def rotating_arr(nums):
    n = len(nums)
    nums[:] = [nums[n-1]] + nums[0:n-1]
    return nums
print(rotating_arr(nums))

# Right rotate array by K places

nums = [3,9,5,6,7,2]
k = 3
def rotating_arr(nums):
    n = len(nums)
    nums[:] = nums[n-k:] + nums[:n-k]
    return nums
print(rotating_arr(nums))



