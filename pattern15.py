'''
 * * * *
  * * *
   * *
    *
'''

def pattern(n):
    k = n - 1
    for i in range(n):
        for j in range(i+1):
            print(end=" ")
        for j in range(k):
            print("* ", end="")
        k = k - 1
        print()
pattern(5)
