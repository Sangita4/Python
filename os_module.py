import os

print(os.getcwd())

if not os.path.exists('data'):
    os.mkdir('data')

for i in range(0, 101):
    os.mkdir(f'data/day{i+1}')


for i in range(0, 101):
    os.rename(f'data/day{i+1}', f'data/tutorial{i+1}')


files = os.listdir('data')
print(files)


for file in files:
    print(file)
    print(os.listdir(f'data/{file}'))

os.chdir('/home')
print(os.getcwd())

