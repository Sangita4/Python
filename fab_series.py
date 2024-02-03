# Fiboncci Series 
# Ex. 0, 1, 1, 2, 3, 5, 8, 13, 21..........

'''
n = 10
a = 0
b = 1
c = b
count = 1
while count <= n:
    print(c)
    count += 1
    a, b = b, c
    c = a + b

'''
def fab(n):
    if n == 0 or n == 1:
        return n
    else:
        return (fab(n-1) + fab(n-2))

n = 10
if n < 0:
    print("Please enter positive number")
else:
    for i in range(n):
        print(fab(i))
