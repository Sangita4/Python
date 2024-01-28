class Emp:
    def __init__(self, name):
        self.name = name

    def __len__(self):
        l = 0
        for i in self.name:
            l +=1
        return l

    def __str__(self):
        return (f'Employee name is {self.name} str')

    def __repr__(self):
        return (f"Employee name is ('{self.name}') repr")

    def __call__(self):
        print("I am Good Girl")

e1 = Emp("Sangita")
e1()

print(e1)
print(str(e1))
print(repr(e1))
print(e1.name)
print(len(e1))
