# Write a Python program that accepts a filename from the user and prints the extension of the file.
#Sample filename : abc.java 

file_name = input("Enter a file name: ")
f = file_name.split(".")
print(f[1])
