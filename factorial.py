def fac(n):
    if n == 0 or n ==1:
        return 1
    else: 
        return fac(n-1)*n
print(fac(5))


def fac(n):
    fact = 1
    if n <= 0 or n == 1:
        return 1
    else:
        for i in range(2, n+1):
            fact = fact * i
        return fact
print(fac(1))

