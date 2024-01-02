s = {1, 2, 5, 4, 8, 4, 8, 'Sangita', 'Kalane'}
print(s)                     # Sets are unchanged
print(type(s))               # Ordered 
d = s.pop()
print(s)
print(d)

s1 = set()                   # Empty set
print(type(s1))

for i in s:
    print(i)

s1 = {2, 4, 6, 8, 9}
s2 = {3, 5, 7, 9, 1}
print(s1.union(s2))          # Combine both set

s1.update(s2)                # concatinate 
print(s1, s2)

s1.intersection_update(s2)    # Common elements only
print(s1, s2)

s2.update(s1)
print(s2, s1)


a = {1, 4, 3, 2, 5, 6}
b = {2, 4, 6}

c = a.symmetric_difference(b)   # Only different elements
print(c)

print(a.issuperset(b))          # a is superset of b

print(b.issubset(a))            # b is subset of a

a.add(8)
print(a)

a.remove(6)                     # Remove element. If not found element then is shows error.
print(a)

a.discard(6)                    # If element not found then is is not showing any error.
print(a)

del b                           # Delete entired set

a.clear()                       # Remove all element from set
print(a)
