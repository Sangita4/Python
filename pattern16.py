'''
    0
   01
  012
 0123
01234
'''

def pattern(n):
    for i in range(n):
        for j in range(n-i-1):
            print(end=" ")
        for j in range(i+1):
            print(j, end="")
        print("\r")
pattern(5)

