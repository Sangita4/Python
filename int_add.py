# Write a Python program to add two objects if both objects are integers. 

def add(x, y):
    if type(x) == int and type(y) == int:
        return x + y
    else:
        return "x and y are not intergers"
print(add(5, 6))
print(add(4.5, 7))
