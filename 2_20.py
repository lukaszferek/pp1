### bmi calculator ###
weight = int(input('enter your weight in kg: '))
height = int(input('enter your height in cm: ')) / 100
bmi = weight / height ** 2

if bmi < 18.5:
    print(f'bmi index: {bmi}\nunderweight!')
elif bmi > 18.5 and bmi < 24.9:
    print(f'bmi index: {bmi}\nnormal weight!')
elif bmi > 25 and bmi < 29.9:
    print(f'bmi index: {bmi}\noverweight!')
elif bmi > 30 and bmi < 34.9:
    print(f'bmi index: {bmi}\nobesity class I')
elif bmi > 35 and bmi < 39.9:
    print(f'bmi index: {bmi}\nobesity class II')
else:
    print(f'bmi index: {bmi}\nobesity class III')