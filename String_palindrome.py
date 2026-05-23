def is_palindrome(S):
    n = len(S)
    left = 0
    right = n-1
    while left<right:
        if S[left] != S[right]:
            return False
        left +=1
        right -=1
        return True
print(is_palindrome("NITIN"))