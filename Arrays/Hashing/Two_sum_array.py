nums = [5,9,1,2,4,15,6,3]
def sum(nums):
    n = len(nums)
    target = 13
    for i in range (0,n-1):
        for j in range(i+1,n):
            if nums[i] + nums[j] == target:
                return[nums[i],nums[j]]
    return None
print(sum(nums))

#optimal solution

nums = [5,9,1,2,4,15,6,3]
def sum(nums):
    n = len(nums)
    target = 13
    hash_map = {}
    for i in range(0,n):
        remaining = target - nums[i]
        if remaining in hash_map:
            return [remaining,i]
        hash_map[nums[i]] = i #Dictionary me store krne ke liye
    return None
print(sum(nums))