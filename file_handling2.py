with open('text.txt', 'r') as f:
    print(type(f))
    f.seek(10)                     # Skip first 10 characters reading
    print(f.tell())                # Show Current position of reading

    line = f.read(5)
    print(line)


with open('text.txt', 'w') as f:
    f.write("Hello Sangita\n")
    f.truncate(11)                  # Only 5 character write in file and other remove

