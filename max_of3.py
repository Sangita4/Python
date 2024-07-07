def greater(a, b, c):
    if a < b > c:
        return b
    elif b < a > c:
        return a
    elif a < c > b:
        return c
    else:
        return "Equal"
print(greater(10, 10, 10))

