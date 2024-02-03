def mini(a, b, c):
    print("Numbers:", a, b, c)
    if b > a < c:
        return a 
    elif a > b < c:
        return b
    elif a > c < b:
        return c
    else:
        return "Equal"
print(mini(5, 6, 7))
print(mini(9, 0, 1))
print(mini(8, 6, 4))
print(mini(4, 4, 4))
