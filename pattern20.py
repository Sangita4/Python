def pattern(n):
    for i in range(n):
        for k in range(n-1-i):
            print(end=" ")
        for j in range(1):
            print("*", end=" ")
        print("\r")
pattern(5)
