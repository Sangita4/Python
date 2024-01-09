marks = [1, 4, 5, 6, 8, 9]

#index = 0
#for mark in marks:
#   print(mark)
#   if index == 4:
#       print("Hey Sangita !!!!!!!")
#   index += 1


for index, mark in enumerate(marks):
    print(mark)
    if index == 3:
        print("2nd Index")


s = "Hey Sangita"
for index, char in enumerate(s):
    print(s)
    if index == 3:
        print("Sangita")
