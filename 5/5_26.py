arr = [1, 2, 3, 4, 5, 6]

for i in range((len(arr) - 1), 0, -1):
    for j in range(i):
        if arr[j] % 2 != 0:
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp