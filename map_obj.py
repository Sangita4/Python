def cube(x):
    return x**3

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
newl = list(map(cube, lst))
print(newl)


l = list(map(lambda x: x**2, lst))
print(l)
