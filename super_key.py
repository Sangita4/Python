class Parent:
    def __init__(self, name, addr):
        self.name = name
        self.addr = addr
    def parent_method(self):
        print('This is parent class')

class Child(Parent):
    def parent_method(self):
        print("Sangita")
        super().parent_method()

    def child_method(self):
        print('This is child class')
        super().parent_method()

#p = Parent("Sangita", "Pune")
c = Child("S", "P")
c.child_method()
c.parent_method()


class Parent:
    def __init__(self, name, addr):
        self.name = name
        self.addr = addr
    def parent_method(self):
        print('This is parent class')

class Child(Parent):
#    def parent_method(self):
#        print("Sangita")
#        super().parent_method()

    def child_method(self):
        print('This is child class')
        super().parent_method()

#p = Parent("Sangita", "Pune")
c = Child("S", "P")
c.child_method()
c.parent_method()


