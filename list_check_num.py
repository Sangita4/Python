# Write a Python program that checks whether a specified value is contained within a group of values. 

def lst_check(lst, num):
    print(f'List: {lst} \nNumber: {num}')
    if num in lst:
        return True
    else:
        return False
print(lst_check([4, 5, 8, 9], 4))
print(lst_check([1, 2, 3, 7], 8))
