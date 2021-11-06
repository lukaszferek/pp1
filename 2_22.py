### guess the number
import random

roll = random.randint(1, 6)
guess = 0

while guess != roll:
    guess = int(input('guess what number was rolled on a dice: '))
    print('the number you tried to guess is wrong. try again!')
else:
    print(f'correct answer! the number was: {roll}')