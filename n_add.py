#  Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
# Sample value of n is 5
# Expected Result : 615

num = int(input("Enter a number: "))
n1 = num 
n2 = str(num) + str(num)
n3 = str(n2) + str(n1)

add = int(n1) + int(n2) + int(n3)
print(add)


n1 = int("%s" % num)
n2 = int("%s%s" % (num, num))
n3 = int("%s%s%s" % (num, num, num))
print(n1+n2+n3)
