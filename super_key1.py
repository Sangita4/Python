class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class Programmer(Employee):
    def __init__(self, name, id, language):
        super().__init__(name, id)
        self.language = language

emp = Employee("Rahul", 345)
pro = Programmer("Sangita", 12345, "Python")
print(emp.name)
print(pro.name)
