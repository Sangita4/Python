'''
A
B C
D E F
G H I J
K L M N O
'''

def pattern(n):
#    k = n - 1
    c = 65
    for i in range(n): 
        for j in range(i+1): 
            ch = chr(c)
            print(ch, end=" ")
            c += 1
        print("\r")

pattern(5)
