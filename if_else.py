name = input("Enter your name:")
age = int(input("Enter your age:"))
print("Hey " + name + ", " + "your age is " + str(age) + ".")

if age >= 18:
    print("You can drive.")
else:
    print("You can not drive.")


n1 = 100
n2 = 200
n3 = 30

if n1 > n2 < n3:
    print("n2 is less")
elif n2 > n1 < n3:
    print("n1 is less")
elif n2 > n3 < n1:
    print("n3 is less")
else:
    print("All are equal")

print("n1=", n1, "n2=", n2, "n3=", n3)


t = int(input("Enter time="))

if 4 <= t < 12:
    print("Good Morning")
elif 12 <= t < 16:
    print("Good Afternoon")
elif 16 <= t < 20:
    print("Good Evening")
else:
    print("Good Night")
