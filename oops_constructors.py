class Person:
    def __init__(self):
        print("Hey, I am Sangita")           # This method always called whenever class called

    def info(self, name):
        print(f'My name is {name}')
obj = Person()
obj.info('Sangita')
a = Person()


class Person_info:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print(f'{self.name} is a {self.age} year old')

obj = Person_info("Sangita", 26)
obj.info()


class Person:

    def __init__(self, name, age, occupation=None):
        self.name = name
        self.age = age
        self.occupation = occupation

    def info(self, surname):
        print(f'{self.name} {surname} is a {self.age} year old.')

obj = Person("Sangita", 26)
obj.info("Kalane")


class New_Person:
    def __init__(self, occupation=None):
        self.occupation = occupation

    def person_info(name):
        print(f'My name is {name}')

    def person_details(self, name):
        print(f'My name is {name} and my occupation is {self.occupation}')

New_Person.person_info("Sangita")
obj = New_Person("Tester")
obj.person_details("Rahul")


