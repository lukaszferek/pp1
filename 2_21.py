### 3 dice rolls
import random

roll1 = random.randint(1, 6)
roll2 = random.randint(1, 6)
roll3 = random.randint(1, 6)

sum_of_rolls = roll1 + roll2 + roll3
print(f'numbers from the dice were: {roll1}, {roll2} and {roll3}.')
print(f'sum of dice rolls is equal to {sum_of_rolls}.')