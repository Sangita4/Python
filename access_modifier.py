class test:
    def __init__(self):
        self.name = "Sangita"
a = test()
print(a.name)


class test:
    def __init__(self):
        self._name = "Sangita"
a = test()
print(a._name)


class test: 
    def __init__(self):
        self.__name = "Sangita"
a = test()
#print(a.__name)       # Can not access directly
print(a._test__name)   # Can be accessed indirectly
print(a.__dir__())
