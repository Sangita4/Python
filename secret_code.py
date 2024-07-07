# Coding:

# If word contains at least 3 characters, 
#    remove the first letter and append it at the end now append three random characters at the starting and the end.
# Else:
#    Simply reverse the string

# Decoding:

# If the word conatins less than 3 characters, reverse it.
# Else:
#    Remove 3 random characters from start and end. Now remove the last letter and append it to the begineeg.


def Coding():
    s = input("Enter a input: ")
    l = s.split(" ")
    print(l)
    for i in l:
        if len(i) >= 3:
            f = i[0]
            w = i[1:]
            print(w + f)
        else:
            print(i[::-1])
            

Coding()
