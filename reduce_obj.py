from functools import reduce

numbers = [1, 2, 3, 4, 5]
sum = reduce(lambda x, y: x+y, numbers)
print(sum)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def mysum(x, y):
    return x + y

sum = reduce(mysum, numbers)
print(sum)
