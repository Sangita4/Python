# Write a Python program to sum two given integers. However, if the sum is between 15 and 20 it will return 20.

def sum(x, y):
    s = x + y
    if 15 < s < 20:
        return 20
    else:
        return s
print(sum(10, 17))
print(sum(4, 8))
print(sum(12, 7))
