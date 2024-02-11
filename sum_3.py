#  Write a Python program to sum three given integers. However, if two values are equal, the sum will be zero. 

def summation(x, y, z):
    if x == y or x == z or y == z:
        sum = 0
        return sum
    else:
        sum = x + y + z
        return sum
print(summation(3, 4, 7))
print(summation(8, 8, 4))
