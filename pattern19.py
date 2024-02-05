'''
    *
   **
  ***
 ****
*****
 ****
  ***
   **
    *
'''

def pattern(n):
    for i in range(n):
        for j in range(n-i-1):
            print(end=" ")
        for k in range(i+1):
            print("*", end="")
        print("\r")

    for i in range(n):
        for j in range(i+1):
            print(end=" ")
        for k in range(n-1-i):
            print("*", end="")
        print("\r")
pattern(5)
