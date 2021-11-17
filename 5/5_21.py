arr = [5, 1, 9, 6, 1]
max1 = 0
max2 = 0

for i in range(len(arr) - 1):
    if arr[i] > max1:
        max1 = arr[i]
        index = i

temp = arr.pop(arr.index(max1))

for i in range(len(arr) - 1):
    if arr[i] > max2:
        max2 = arr[i]
        
arr.insert(index, max1)

print(f'array: {arr}')
print(f'result: {max2}')