nums = [1,1,1,2,3,4,4,7,9,9,9,10]

def remove_duplicates(nums):
    n = len(nums)
    if n ==0:
        return 0
    
    if n ==1:
        return 1
    i = 0
    j = i+1
    while j<n:
        if nums[j] != nums[i]:
            i+=1
            nums[i] , nums[j] = nums[j] , nums[i]
        j +=1
    return i+1
length = remove_duplicates(nums)
print("Lenth of unique elements:",length)
print("Array after removing duplicates:" , nums[:length])


