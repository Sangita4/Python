l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def filter_fun(a):
    return a > 4
newl = list(filter(filter_fun, l))
print(newl)



lst = list(filter(lambda x: x < 5, l))
print(lst)
