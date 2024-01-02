l = ['Sangita', 'Rahul', 'Kalane']
print(type(l))

for i in l:
    print(i)

for i in range(len(l)):
    print(l[i])

l = ['Sangita', 'Rahul', 'Kakade', 4, 8, 1, 3]
print("List:", l)
print(l[0])
print(l[:3])
print(l[-4:-1])
print(l[-1])
print(l[0:5])
#print(l[10])  #Outoff index

print("Length of list:", len(l))
l.append(1992)                  # Append at the end
print("Append:", l)  
l.insert(7, 1998)               # Insert for given index
print("Insert:", l)
l1 = [2022, 2023, 2024]
l.extend(l1)                    # Extend list by list
print("Extend:", l)
l2 = l + l1                     # List concatinate
print("Concatinate:", l2)
l.reverse()                     # Reverse list
print("Reverse:", l)
#l.sort()                        # Not supported between instances of 'str' and 'int'
#print("Sort:", l)
p = l.pop()                     # Pop last
print("Pop:", p)
p1 = l.pop(0)                   # Pop by index
print("Pop by index:", p1)
del(l[6])                       # Delete by index
print("Delete:", l)
l.remove('Kakade')              # Remove by value
print("Remove:", l)
l.clear()                       # Clear list
print("Clear:", l)


lst1 = [i for i in range(10)]
print("Original List:", lst1)

lst2 = lst1
lst2[0] = 15
print("Copied list:", lst2)
print("First List:", lst1)

lst3 = []
for i in lst2:
    if i%2 == 0:
        lst3.append(i)
print(lst3)

lst1 = [i for i in range(10) if i%2 == 1]
print("List comprehension:", lst1)
