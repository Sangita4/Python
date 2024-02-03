class Math:
    def __init__(self, num):
        self.num = num

    def addtonum(self, num1):
        self.num = self.num + num1
        #return self.num
    
    @staticmethod
    def add(a, b):
        return a + b

a = Math(4)
print(a.num)
a.addtonum(8)
print(a.num)

print(a.add(4, 8))

print(Math.add(4, 8))  #Static method used when we do not need to use class instance
#print(add(4, 8))
