#fibonacci
a = 0
b = 1
temp = 0
c = 0

print(f'{a}')

for i in range(50):
    c = a + b
    print(f'{c}')
    temp = a
    a = c
    b = temp
    
    