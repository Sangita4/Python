a = 4
b = "4"
print(a is b)          # Is operator compare exact location of object in memory
print(a == b)          #  == operator compare value of the object

a = [1, 2, 3]
b = [1, 2, 3]
print("List = ", a is b)     # False  Mutable objects locations are different in memory for same value
print("List = ", a == b)

a = 8
b = 8
print(a is b)
print(a == b)


a = "Sangita"
b = "Sangita"
print(a is b)               # True, Immutable objects locations are same in memory for same value
print(a == b)


a = None
b = None
print(a is b)
print(a == b)
print(a is None)

