# Write a Python program to count the number 4 in a given list. 
l = [4, 6, 7, 8, 9, 4, 2, 1, 3, 4, 6, 4, 9, 4, 4, 4, 4]
count = 0
for i in l:
    if i == 4:
        count += 1
print(count)
