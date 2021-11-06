#sum and mean from keyboard
choice = 1
numbers = []

while choice != 0:
    choice = int(input('enter number: '))
    numbers.append(choice)
    
numbers.pop()

quantity = len(numbers)
suma = sum(numbers)
mean = (suma /quantity)

print('result: quantity = %d, sum = %.1f, mean = %.1f' % (quantity, suma, mean))