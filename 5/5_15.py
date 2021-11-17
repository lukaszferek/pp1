colors = ['white', 'black', 'blue', 'yellow', 'red', 'green']

with open('colors.txt', 'w') as f:
    for color in colors:
        f.write(f'{color}\n')