# Write a Python program to sum the first n positive integers.

def sum(n):
    s = 0
    for i in range(n+1):
        s += i
    return s
print(sum(8))


n = 8
sum_num = (n * (n + 1))/2
print(sum_num)
