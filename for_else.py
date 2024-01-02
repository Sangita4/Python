for i in range(10):
    print(i)
else:
    print("Sorry, value not found")


l = []
for i in l:
    print(i)
else:
    print("Empty list")


i = 6
while i <=5:
    print(i)
else:
    print(f'{i} is greater than 5')

while i <= 10:
    if i == 6:
        break
    i+=1
else:
    print("Loop Break")                      # If loop Break then else statement not working.


for i in range(5):                           # Else statement only run when loop completed successfully.
    if i == 1:
        break
else:
    print(i)
