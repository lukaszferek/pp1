def minmax(array):
    maxi = 0
    mini = array[0]
    array2 = []

    for i in range(len(array) - 1):
        if array[i] < mini:
            mini = array[i]
        
        if array[i] > maxi:
            maxi = array[i]       

    array2.append(mini)
    array2.append(maxi)
    print(f'array: {array}')
    print(f'result: {array2}')

array = [4, 2, 8, 4, 7, 9, 5]
minmax(array)