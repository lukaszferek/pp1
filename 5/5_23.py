def median(array):
    array.sort()
    
    if len(array) % 2 != 0:
        result = array[int(len(array) / 2)]
        
    elif len(array) % 2 == 0:
        n1 = array[int(len(array) / 2)]
        n2 = array[int(len(array) / 2 - 1)]
        result = (n1 + n2) / 2
        
    print(array)
    print(result)
        
median([1, 0, 9, 4, 6])
median([6, 8, 3, 1, 0, 5, 7])