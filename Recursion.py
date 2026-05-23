def func(count = 0):
    if count == 8:
        return
    else: 
        print("Abhay Kabir")
        func(count + 1)
func()

#Recursion using parameters

def func (Name , n):
    if n<=0:
        return
    else:
        print(Name)
        func(Name, n-1)
func("Mithi" , 5)