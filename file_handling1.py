'''
f = open('myfile2.txt', 'r')
while True:
    line = f.readlines()
    print(line)
    if not line:
        print(line, type(line))
        break
'''

f = open('text.txt', 'w')
line = ('Hey Sangita!!!\n', 'How are you?\n')
f.writelines(line)
f.close()
