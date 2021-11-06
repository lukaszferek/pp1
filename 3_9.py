### check if at least one of the numbers given from the keyboard is positve
number1 = int(input('enter 1st number: '))
number2 = int(input('enter 2nd number: '))

if (number1 > 0 or number2 > 0):
    print('at least one given number is positive')
else:
    print('none of the given numbers are positive')