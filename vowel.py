# Write a Python program to test whether a passed letter is a vowel or not. 
def vowels(letter):
    v = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    if letter not in v:
        print(f'{letter} is not vowel')
    else:
        print(f'{letter} is vowel')
vowels('S')
vowels('A')
vowels('i')
vowels('p')

