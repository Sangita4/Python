class Employee:
    company = "Google"
    def ShowDetails(self):
        print(f'My name is {self.name} and I am working in {self.company}')

    def ChangeCompany(cls, newCompany):
        cls.company = newCompany

e1 = Employee()
e1.name = "Sangita"
e1.ShowDetails()
e1.ChangeCompany("Amazon")
e1.ShowDetails()
print(Employee.company)


class Employee:
    company = "Google"
    def ShowDetails(self):
        print(f'My name is {self.name} and I am working in {self.company}')
    
    @classmethod
    def ChangeCompany(cls, newCompany):
        cls.company = newCompany

e1 = Employee()
e1.name = "Sangita"
e1.ShowDetails()
e1.ChangeCompany("Amazon")
e1.ShowDetails()
print(Employee.company)


