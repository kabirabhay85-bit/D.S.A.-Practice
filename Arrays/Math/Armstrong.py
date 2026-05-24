n = int(input("Enter your number: "))
num = n
Total = 0
nod = len(str(n))
while n > 0:
    ld = num%10
    Total = Total + (ld**nod)
    num = num//10
    Total == n
print(Total)