x = 4
print(x)

def hello():
    x = 8
    y = 10
    print(f'Local x is {x}')
    print(f'Local y is {y}')

print(f'Global x is {x}')
hello()

print(f'The Global x is {x}')
# print(y)                   Local Variable



x = 8
print(f'Variable outside the function value is {x}')
def new_fun():
    global x
    x = 4
    print(f'Local x is {x}')

new_fun()

print(f'global x is {x}')
