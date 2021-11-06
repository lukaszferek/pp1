### area of a triangle ###
import math

print('the program will calculate the area of a triangle. enter the sides')
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))

circuit = (a + b + c) / 2
area = math.sqrt(circuit * (circuit - a) * (circuit - b) * (circuit - c))

print(f'the area is {area}')