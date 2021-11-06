#check if pin is correct
pin = '0805'
guess = '0'

for i in range(3):
    guess = input('enter the pin code: ')
    
    if guess == pin:
        print('correct!')
        break
    
    elif guess != pin and i < 2:
        print('incorrect..')
    
    else:
        print('incorrect...')
        print('your card has been blocked')