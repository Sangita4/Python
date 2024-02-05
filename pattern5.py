'''
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
'''
def pattern(n):
#    k = n - 1
    c = 1
    for i in range(n): 
        for j in range(i+1): 
            print(c, end=" ")
            c += 1
        print("\r")

pattern(5)
