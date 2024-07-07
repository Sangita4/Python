def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n * fact(n-1)    # 5*fact(4) ==> 5*4*fact(3) ==> 5*4*3*fact(2) ==> 5*4*3*2*fact(1) ==> 5*4*3*2*1*fact(0) ==> 5*4*3*2*1*1
print(fact(5))
print(fact(6))



def fab(n):
    if n <= 1:
        return n
    else:
        return(fab(n-1) + fab(n-2))

nterms = 10
if nterms <= 0:
    print("Please enter positive number")
else:
    print("Fabonacci Squence:")
    for i in range(nterms):
        print(fab(i))
    

