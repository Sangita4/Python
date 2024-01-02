t = (1, 2, 3)
print(type(t))
print(t)

t1 = (1)    # This is integer
print(type(t1), t1)

t2 = (1,)   # This is tuple
print(type(t2), t2)

t = ('Sangita', 'Rahul', 4, 8, 1, 3)
print(len(t))
print(t[:4])
print(t[-1])
print(t[1:3])
print(t[-4:-1])
print(t[::-1])
print(t[1])
# print(t[6])     Outoff index


for i in t:
    print(i)

for i in range(len(t)):
    print(t[i])

t1 = t
print(t1)

l = list(t1)
print("Tuple to List:", l)

t = tuple(l)
print("List to Tuple:", t)

t2 = ('Sangita', 'Rahul', 'Kakade', 'Kalane', 1998, 1992)
t3 = t1 + t2
print(t3)

c = t3.count('Sangita')
print("Count:", c)

i = t3.index('Sangita', 1, 8)
print("Index of given element:", i)

i1 = t3.index(1998)
print("Index of 1998:", i1)
