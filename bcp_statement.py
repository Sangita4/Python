l = ["Sangita", "Rahul", "Shivam"]
for i in l:
    # print(i)
    if i == "Rahul":
        break
    print(i)

for i in range(15):
    # print(i)
    if i%2 == 0:
        continue 
    print(i)


i = 10
while i%2 == 0:
    break
print("While loop:", i)

while i%2 ==1:
    continue
i -= 1
print("While loop for continue:", i)

for i in range(100):
    pass
