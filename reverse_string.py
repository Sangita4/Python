# Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them. 

name = input("Enter a first name and last name: ")
n = name.split(" ")
n.reverse()
print(" ".join(n))

f_name = input("Enter a first name: ")
l_name = input("Enter a last name: ")
print(l_name, f_name)
