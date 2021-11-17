#guessing game with my module
import mymath

while mymath.read_number() != mymath.generate_number():
    print('your guess is wrong, try again')
    
print('correct!')