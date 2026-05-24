nums = [9,6,4,2,5,7,0,1]
def missing(nums):
    n = len(nums)
    for i in range(0,n+1):
        if i not in nums:
            return i 
print(missing(nums))

#Better Solution
nums = [9,6,4,2,5,7,0,1]
def missing(nums):
    n = len(nums)
    freq = {}
    for i in range(0,n+1):
        freq[i] = 0
    for num in nums:
        freq[num] =1
    for k,v in freq.items():
        if v == 0:
            return k
    
    print(missing(nums))