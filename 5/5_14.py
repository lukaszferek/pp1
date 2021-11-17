names = ['Genowefa', 'Onufry', 'Celestyna', 'Alojzy', 'Pankracy']
max_char = len(names[0])
max_word = names[0]

for n in names:
    if len(n) > max_char:
        max_word = n