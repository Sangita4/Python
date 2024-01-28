sum = lambda a, b: a+b
print(sum(4, 8))

sqr = lambda x: x**2
print(sqr(4))

cube = lambda x : x**3
print(cube(8))

avg = lambda a, b, c : (a+b+c)/3
print(avg(4, 8, 12))


def test(fun, value):
    return 6 + fun(value)
print(test(cube, 4))

print(test(lambda x: x**3, 5))

print(test(lambda x: x**2, 10))

