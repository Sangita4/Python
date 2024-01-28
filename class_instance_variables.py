class Employee:
    def __init__(self, name):
        self.name = name
        self.raise_ammount = 10
    def ShowDetails(self):
        print(f'The name of the employee is {self.name} and the raise ammount is {self.raise_ammount}')

obj = Employee("Sangita")
obj.raise_ammount = 15
obj.ShowDetails()

obj1 = Employee("Rahul")
obj1.ShowDetails()

#Employee.ShowDetails(obj)



class Employee:
    company_name = "Google"
    def __init__(self, name):
        self.name = name
    def ShowDetails(self):
        print(f"The employee name is {self.name} and company name is {self.company_name}")

obj = Employee("Sangita")
obj.company_name = "Google India"
obj.ShowDetails()

obj1 = Employee("Rahul")
obj1.ShowDetails()

print(Employee.company_name)
Employee.company_name = "Amazon"
print(Employee.company_name)
