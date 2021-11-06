#dog's age
dog_human_years = int(input('enter the dog\'s age in human years: '))
dog_years1 = 0
dog_years2 = 0

if dog_human_years <= 2:
    dog_years1 = dog_human_years * 10.5
else:
    dog_years1 = 2 * 10.5
    dog_years2 = (dog_human_years - 2) * 4

result = int(dog_years1 + dog_years2)
print(f'The dog\'s age in dog’s years is {result}')