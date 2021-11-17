arr = [8, 2, 5, 1, 9]
pow_arr = []

for num in arr:
    pow_arr.append(num * num)

arr_string = (' '.join(str(num) for num in arr))
pow_arr_string = (' '.join(str(num) for num in pow_arr))

print(f'array: {arr_string}')
print(f'2nd power: {pow_arr_string}')