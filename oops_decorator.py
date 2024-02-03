def greet(fx):
    def mfx():
        print("Good Morning")
        fx()
        print("Thanks for using this function")
    return mfx

@greet
def hello():
    print("Hello Sangita")

hello()

# ****************************************************************************************************

def greeting(fn):
    print("Hey, Good Morning")
    return fn

@greeting
def hello():
    print("Hello, Sangita")

hello()

# ****************************************************************************************************

def greeting(fn):
    print("Hey, Good Morning")
    fn()

@greeting
def hello():
    print("Hello, Sangita")

#hello()

# ****************************************************************************************************

def greeting(fn):
    print("Hey, Good Evening")
    return fn

# @greeting
def hello():
    print("Hello, Rahul")

greeting(hello)()

# ****************************************************************************************************

def greet(fn):
    print("Hey, Good Morning")
    return fn

@greet
def add(a, b):
    print(a+b)
add(4, 8)

# ****************************************************************************************************

def greeting(fn):
    def mfx(*args, **kargs):
        print("Hey, Rahul")
        fn(*args, **kargs)
        print("Thanks for using decorator")
    return mfx

@greeting
def add(a, b):
    print(a+b)

add(84, 48)

