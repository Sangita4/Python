# Write a Python program to get n (non-negative integer) copies of the first 2 characters of a given string. Return n copies of the whole string if the length is less than 2. 

def str_copy(text, num):
    if len(text) > 2:
        return num * text[:2]
    else:
        return num * text
print(str_copy("Sangita", 1))
print(str_copy("S", 5))

