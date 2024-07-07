x = [1, 2, 3, 4]
print(dir(x))
print(x.__add__)



class Emp:
    def __init__(self, name, age):
        self.name = name
        self.age = age

obj = Emp('Sangita', 26)
print(obj.__dict__)

print(help(Emp))

print(help(str))
