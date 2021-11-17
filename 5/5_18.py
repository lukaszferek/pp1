arr = [7, 6, 4, 3, 20]

def bubblesort(array):
    for i in range((len(arr) - 1), 0, -1):
        for j in range(i):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
    
    print(arr)
    
    
    
bubblesort(arr)