'''
A
B B
C C C
D D D D
E E E E E
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
