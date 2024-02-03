# Write a Python program that returns a string that is n (non-negative integer) copies of a given string. 

def string(text, num):
    if num > 0:
        result = ""
        for i in range(num):
            result = result + text
        return result
    else:
        return "Number is negative"
print(string("abc", 3))
print(string("xyz", -1))
