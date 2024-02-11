# Write a Python program that prints out all colors from color_list_1 that are not present in color_list_2.
# Test Data :
# color_list_1 = set(["White", "Black", "Red"])
# color_list_2 = set(["Red", "Green"])

def color_lst(lst1, lst2):
    print(lst1.difference(lst2))

lst1 = set(["White", "Black", "Red"])
lst2 = set(["Red", "Green"])
color_lst(lst1, lst2)
