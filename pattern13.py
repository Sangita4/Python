'''
* * * * * * 
* * * * * 
* * * * 
* * * 
* * 
* 
'''

def pattern(n):
    k = n
    for i in range(n):
        for j in range(k):
            print('*', end=" ")
        k = k - 1
        print("\r")
pattern(6)
