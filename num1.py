# Write a Python program to calculate the difference between a given number and 17. If the number is greater than 17, return twice the absolute difference. 

def difference(n):
    if n > 17:
        return (n - 17) *2
    else:
        return 17-n

print(difference(20))
print(difference(10))

