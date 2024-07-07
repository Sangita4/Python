s = '''Hey Sangita,
How are you?'''
print(s)

s1 = """Hey Sangita, How are you?
What are you doing"""
print(s1)

name = 'sangita!'
l_name = 'Kalane'
print(name + l_name)
print(name + " " + l_name)

print(name[0])
print(name[:3])
print(name[0:4])
print(name[-1])
print(name[:-4])
print(name[::-1])
print(name[::-2])
# print(name[7]) # Out of index

print(len(name))
print(name.upper())
print(name.lower())
print(name.isupper())
print(name.islower())
# print(name.isalphanumeric())
print(s1.capitalize())
print(name.rstrip('!'))
a = name.replace("sangita!", "Sangs")
print(a)
print(s.split(" "))
b = s.center(50)
print(len(b))
print(len(s))
print(s1.count('you'))
print(s.endswith('?'))
print(s.find('Sangita'))
print(s1.index('doing'))
print(name.isalnum())
print(l_name.isalpha())
print(name.isprintable())

spc = "                   "
print(spc.isspace())
print(name.isspace())
print(s.istitle())
print(s.startswith('Hey'))
print(s.swapcase())
print(s.title())
