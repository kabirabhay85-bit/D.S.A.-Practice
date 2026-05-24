# Reverse of an array using recursion
nums = [2,4,1,3,6,7,3,8,9,5]

def func(nums , left , right):
    if left>= right:
        return
    else:
        nums[left] , nums[right] = nums[right] , nums[left]
        func(nums , left+1 , right-1)
        
def reverseArray(nums , L , R):
    func(nums,L,R)
    return nums

print(reverseArray(nums,0,len(nums)-1))

nums = [1,50,98,35,6,5,978,74]

def func(nums , left , right):
    if left>=right:
        return
    else:
        nums[left] , nums[right] = nums[right] , nums[left]
        func(nums , left+1 , right-1)
        
def reversearray(nums , L, R):
    func(nums,L,R)
    return nums
print(reverseArray(nums , 0 , len(nums) - 1))                               
