# Write a Python program to get a newly-generated string from a given string where "Is" has been added to the front. Return the string unchanged if the given string already begins with "Is". 

def strings(s):
    if s.startswith("Is"):
        return s
    else:
        return "Is" + s
print(strings("IsEmpty"))
print(strings("It"))
