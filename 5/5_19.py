arr = [2, 3, 2, 5, 8, 1, 9, 8]
unique_arr = []

for i in arr:
    if arr.count(i) < 2:
        unique_arr.append(i)

string_arr = ' '.join(str(e) for e in arr)
string_unique = ' '.join(str(e) for e in unique_arr)

print(f'array: {string_arr}')
print(f'unique array: {string_unique}')