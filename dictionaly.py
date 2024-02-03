dic = {"name":"Sangita", "age":26, "Location":"Pune"}
print(dic)
print(type(dic))

print("Get value by key:", dic["name"])
print(dic.get("age"))
print(dic.get("xyz"))                             # Display None as output
# print(dic["xyz"])                               # Display error

print(dic.keys())
print(dic.values())
# print(dic[key])

for k,v in dic.items():
    print("Key:", k, "Value:", v)

for key in dic.keys():
    print(f'Above dic key and values are as Key: "{key}"')
    print(f'Display values of above keys "{dic[key]}"')

dic1 = {}
print(dic1)

emp = {'001':'Sangita', '002':'Rahul', '003':'Swapnali', '004':'Rutuja'}
new = {'005':'Samadhan', '006':'Vishesh'}

emp1 = emp.copy()
print(f'Copy: {emp1}')

emp.update(new)
print(f'Update: {emp}')

new.clear()
print(f'Clear: {new}')

emp.popitem()                                   # Remove last key-value pair
print(f'pop by popitem {emp}')

emp.pop('005')                                  # Remove by Key
print(f'pop by key {emp}')

del emp
# print(emp)                # Deleted sucessfully so it is showing error


a = (1, 2, 3, 4)
b = (8)
c = dict.fromkeys(a, b)
print(c)                           # Return dic with a items as key and b as value

