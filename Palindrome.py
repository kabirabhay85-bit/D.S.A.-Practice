n = int(input("Enter your number: "))
num = n
Total = 0
while num>0:
    ld = num%10
    Total =ld + (Total*10)
    num = num//10
    n == Total
print(Total)

