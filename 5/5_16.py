arr = [12, 6, 4, 9, 3]

def star(n):
    for e in n:
        print(f'{e}:', end = ' ')
        print('*' * e)
        
star(arr)