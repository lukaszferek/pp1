arr = [5, 1, 9, 6, 1]
maxi = 0
mini = arr[0]

for i in range(len(arr) - 1):
    if arr[i] > maxi:
        maxi = arr[i]
    
    if arr[i] < mini:
        mini = arr[i]
        
print(f'array: {arr}')
print(f'result: {maxi} - {mini} = {maxi - mini}')