arr = [15, 8, 31, 47, 2, 19]
reverse_arr = []
i = (len(arr) - 1)

while i >= 0:
    reverse_arr.append(arr[i])
    i -= 1
    
arr_string = (' '.join(str(num) for num in arr))
reverse_arr_string = (' '.join(str(num) for num in reverse_arr))

print(f'array: {arr_string}')
print(f'reversed array: {reverse_arr_string}')