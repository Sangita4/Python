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
    k = n - 1
    for i in range(n):
        for j in range(k):
            print(end=" ")
        k = k - 1
        for j in range(i+1):
            print("* ", end="")
        print('\r')
    
    for i in range(n-1):
        for j in range(i+1):
            print(end=" ") 
        for j in range(n-i-1):
            print("*", end=" ")
        print("\r")
pattern(5)
