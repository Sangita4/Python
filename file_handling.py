f = open('myfile.txt', 'w')      # Create new file if not available
f.write("Hello Sangita")         # Override text if available
f.close()

f1 = open('myfile1.txt', 'a')
f1.write("\n Hey Sangita!!!")    # Append text without removing previous data
f1.close()

f2 = open('myfile2.txt', 'r')
text = f2.read()
print(text)
f2.close()

#f3 = open('myfile3.txt', 'x')   # Show error if file already available


with open('myfile.txt', 'a') as f:
    f.write('\nHey Sangita')
