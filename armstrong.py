num = input("Enter a number: ")
l = len(num)
s = 0
for i in num:
    s += int(i)**l
if int(num) == s:
    print("Armstrong")
else:
    print("Not Armstorng")


num = int(input("Enter a number: "))
l = len(str(num))
temp = num
sum = 0
while temp > 0:
    m = temp % 10
    sum += m **l
    temp //= 10
if num == sum:
    print("Armstrong")
else:
    print("Not Armstrong")
