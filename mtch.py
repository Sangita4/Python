n = int(input("Enter number: "))

match n:
    case 0:
        print("number is 0")
    case 4:
        print("number is 4")
    case _ if n > 8:
        print("number is greater than 8")
    case _ if n == 8:
        print("number is 8")
    case _:
        print("Default: ", n)
