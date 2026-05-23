num = int(input("Enter your number : "))

if num<=1:
    print("Given number is not prime")
    
else:
    for i in range(2,num):
        if num%i == 0:
            print("Given number is not prime number")
            break
    else:
        print("Given number is prime")