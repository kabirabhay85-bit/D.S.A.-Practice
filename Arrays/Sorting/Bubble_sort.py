nums = [5,8,1,6,9,2,4]
def selection_sort(nums):
    n = len(nums)
    for i in range(n):
        is_swap = False
        for j in range (0,n-i-1):
            if nums[j]>nums[j+1]:
                nums[j] , nums[j+1] = nums[j+1] , nums[j]
                is_swap = True
        if not is_swap:
            break
    return nums
print(selection_sort(nums))