x = int(input('enter first number: '))
y = int(input('enter second number: '))


if x > 0 and y > 0:
    print(f'point P({x}, {y}) is in the first quadrant of the coordinate system')
    
elif x > 0 and y < 0:
    print(f'point P({x}, {y}) is in the second quadrant of the coordinate system')

elif x < 0 and y < 0:
    print(f'point P({x}, {y}) is in the third quadrant of the coordinate system')
    
elif x < 0 and y > 0:
    print(f'point P({x}, {y}) is in the fourth quadrant of the coordinate system')
    
elif x == 0 and y != 0:
    print(f'point P({x}, {y}) is located on X asis.')
    
elif x != 0 and y == 0:
    print(f'point P({x}, {y}) is located on Y asis.')
    
else:
    print(f'point is located in P({x}, {y}) position')