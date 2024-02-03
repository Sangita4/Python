def prime(n):
    for i in range(2, n):
        if n % i == 0:
            return "Number is not prime"
            break
    else:
        return "Number is prime"
print(prime(30))
