try:
    l = [1, 2, 3, 4, 5, 6]
    print(l[9])
except Exception as e:
    print(f'Exception: {e}')
finally:
    print(f'Display list {l}')



try:
    a = input("Enter a number:")
    for i in range(1, 11):
        print(f'{a} X {i} = {int(a)*i}')
except:
    print("Invalid Input")
finally:
    print(f'Display user input {a}')


def function():
    try:
        s = int(input("Enter input:"))
        if s == 4:
            print(i)
            return 1
    except:
        print(f'Input is not equal to 4')
        return 0
    finally:
        print('I am always execuated') 
print(function())


def fun():
    try:
        num = int(input("Enter input:"))
        l = [2, 4, 5, 6]
        print(l[num])
        return 0
    except ValueError:
        print("Number is not interger")
        return 1
    except IndexError:
        print("Out off index")
        return 2
    #finally:
        #print(f'List: {l}')
    print("I am always execuated")               # This print statement will not executed when user return value.

print(fun())
