def occurs(number, array):
    if number in array:
        return True
    else:
        return False
    
arr = [15, 38, 7, 23, 14]    
print(occurs(int(input('enter a number: ')), arr))