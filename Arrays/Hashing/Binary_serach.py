nums = [2,4,6,7,9,11,18,19]
def binarysearch(nums,target):
    n = len(nums)
    low = 0
    high = n-1
    while low<=high:
        mid = (low+high)//2
        if nums[mid] == target:
            print("Required target is : ", mid)
            return mid
        elif nums[mid]<target:
            low = mid+1
        else:
            high = mid-1
    return -1
print(binarysearch(nums,6))
            
        
            