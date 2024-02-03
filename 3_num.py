# Write a Python program to calculate the sum of three given numbers. If the values are equal, return three times their sum. 

def numbers(n1, n2, n3):
    if n1 == n2 == n3:
        return (n1+n2+n3) * 3
    else:
        return(n1+n2+n3)

print(numbers(4, 5, 6))
print(numbers(10, 10, 10))
