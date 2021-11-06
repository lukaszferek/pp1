##bingo
numbers = []

for i in range(1, 31):
    numbers.append(i)
    
for i in range(30):
    if numbers[i] % 3 == 0 and numbers[i] % 5 == 0:
        numbers[i] = 'BINGO'
   
    elif numbers[i] % 5 == 0:
        numbers[i] = 'FIVE'
    
    elif numbers[i] % 3 == 0:
        numbers[i] = 'THREE'
        
print(' '.join(str(num) for num in numbers))

