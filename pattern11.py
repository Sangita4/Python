'''
0 0 0 0
1 1 1
2 2
3
'''
def pattern(n):
    k = n - 1
    num = 0
    for i in range(n):
        for j in range(k):
            print(num, end=" ")
        k = k - 1
        num = num + 1 
        print("\r")
pattern(6)
