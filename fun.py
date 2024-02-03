def function():
    print("Sangita")
function()

def addd(n):
    print("Addition:", n+n)
addd(10)

def cal(a, b):
    mean = (a*b)/(a+b)
    print("Mean:", mean)

    if a > b:
        print("a:", a)
    elif b > a:
        print("b:", b)
    else:
        print("both", a, b)

cal(10, 9)
cal(10, 20)

def average(a=16, b=32):
    print("Default argument average: ", (a+b)/2)
average()

def name(a, b='Rahul ', c='K'):
    print("My name is", a + b + c)
name('Sangita ', 'Sanjivan ')

def default(a, b=None):
    print("Hey", a)
default('Sangita')

def ave(a, b):
    print(a+b, a-b)
ave(b=8, a=4)

def arg_fun(*numbers):
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum += i
    print("Average of numbers:", sum/len(numbers))
arg_fun(4, 8, 4, 8)

def karg_fun(**f_name):
    print(type(f_name))
    print("Hello,", f_name['m_name'], f_name['h_name'], f_name['s_name'])
karg_fun(m_name='Sangita', h_name='Rahul', s_name='Kakade')

def addition(a, b):
    return a+b
print(addition(4, 8))

def sub(a, b):
    return a-b
c = sub(8, 4)
print(c)

