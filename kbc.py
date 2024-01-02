def kbc(l):
    count = 0
    for i in l:
        print(i)
        # for j in l:
        ans = input("Enter your answer:")
        if ans != i[2]:
            print("Sorry, Wrong answer")
            break
        else:
            count += i[5]
    print("You won:", count)

q = [["Who is the prime minister of India?", "1. Amit Shah", "2. Naredra Modi", "3. Devendra Fadanvis", "4. Raj Thakare", 1000], ["Who won ICC world cup 2023?", "1. India", "2. Austrulia", "3. Pak", "4. Japan", 2000]]

kbc(q)

