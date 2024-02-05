'''   
        * 
      * * 
    * * * 
  * * * * 
* * * * * 
'''
def pattern(n):
    k = n*2 - 2
    for i in range(n):
        for j in range(k):
            print(end=" ")
        k = k - 2
        for j in range(i+1):
            print('* ', end="")
        print("\r")
pattern(5)
