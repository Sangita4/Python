class Person:
    name = "Sangita"
    occupation = "Tester"
    age = 26


print(Person.age)
print(Person.occupation)

a = Person()
print(a.name)

a.name = "Rahul"
occupation = "Software Tester"
a.age = 32
print(a.name)
print(a.occupation)
print(a.age)


    
class Person_info:
    name = "Rahul"
    occupation = "Software Tester"
    age = 32

    def info(self):
        print(f'{self.name} is a {self.age} year old.')
        
obj = Person_info()
obj.info()

a = Person_info()
a.name = "Sangita"
occupation = "Software Tester"
a.age = 26

a.info()

