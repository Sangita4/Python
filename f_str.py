def address(name, country):
    adrs = ('My name is {}. I am from {}.').format(name, country)
    print("Format:", adrs)
    print('I am from {1}. And my name is {0}.'.format(name, country))
    print(f'My name is {name}. I am from {country}.')
    print(f'My name is {{name}}. I am from {{country}}.')   # Display raw format of f-string

address("Sangita", "India")

price = 49.000986123
txt = f'For only {price:.2f}'                               # Display only 2 floter points
print(txt)
