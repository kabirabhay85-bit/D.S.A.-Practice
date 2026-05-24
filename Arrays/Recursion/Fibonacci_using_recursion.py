def func(num):
    if num == 0 or num ==1:
        return num
    else:
        return func(num-1) + func(num-2)
print(func(8))