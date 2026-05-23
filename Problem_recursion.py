#print 1 to N using recursion

def func(i,n):
    if i>n:
        return
    else :
        print(i)
        func(i+1,n)
func(1,5)

#Sum 1 to n parameterized & functional recursion

def func(sum , i , n):
    if i>n:
        return
    else :
        print(sum)
        func(sum+i,i+1, n)
func(0,1,10)

# functional recursion

def func(n):
    if n == 8:
        return 8
    else:
        return n+ func(n+1)
print(func(1))
    
