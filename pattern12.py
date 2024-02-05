'''
0 1 2 3 4 5
0 1 2 3 4
0 1 2 3
0 1 2
0 1
0
'''

def pattern(n):
    k = n
    for i in range(n):
        for j in range(k):
            print(j, end=" ")
        k = k - 1
        print("\r")
pattern(6)
