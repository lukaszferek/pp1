#multiplication table
number = int(input('enter a number: '))
for i in range(1, 11):
    print(f'{number} * {i} = ' + str(number * i))