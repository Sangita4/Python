def kbc(q, l):
    count = 0
    for i in range(len(q)):
        quetion = q[i]
        #print(quetion)
        print(f'Question for Rs. {l[i]}')
        print(quetion[0])

        print(f'a. {quetion[1]}                     b. {quetion[2]}')
        print(f'c. {quetion[3]}                     d. {quetion[4]}')

        ans = int(input("Enter your answer (1-4):"))
        if (ans == quetion[-1]):
            print(f"Your are absolatly correct, You won Rs. {l[i]}")
            if i == 1:
                money = 2000
            else:
                money = 1000
        else:
            print(f"Wrong Answer")
            break

q = [["Who is the prime minister of India?", "Amit Shah", "Naredra Modi", "Devendra Fadanvis", "Raj Thakare", 1], ["Who won ICC world cup 2023?", "India", "Pak", "Austrulia", "Japan", 2]]

levels = [1000, 2000]

kbc(q, levels)

