def arr_as_string(arr):
    arr_string = ','.join(str(e) for e in arr)
    
    print(f'array: {arr}')
    print(f'string: {arr_string}')
    
arr_as_string([1, 2, 3])