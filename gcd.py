# Write a Python program that computes the greatest common divisor (GCD) of two positive integers. 

def gcd(x, y):
    if x % y == 0:
        return y
    for i in range(int(y/2), 0, -1):
        if x % i == 0 and y % i == 0:
            return i
            break

print("GCD of 12 & 17 =", gcd(12, 17))
print("GCD of 4 & 6 =", gcd(4, 6))
print("GCD of 336 & 360 =", gcd(336, 360))
