'''
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
'''

def pattern(n):
    for i in range(n):
        for j in range(i+1):
            print("*", end=" ")
        for j in range(n-i-1):
            print(end=" ")
        print("\r")
    for i in range(n):
        for j in range(n-i-1):
            print("*", end=" ")
        for j in range(i+1):
            print(end=" ")
        print("\r")
pattern(5)