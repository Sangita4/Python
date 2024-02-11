# Write a Python program that concatenates all elements in a list into a string and returns it.

def lst_str_con(lst):
    result = ""
    for i in lst:
        result += str(i)
    return result
print(lst_str_con([1, 9, 9, 8]))
