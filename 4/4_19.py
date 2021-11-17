def check_num_in_range(num, x, y):
    if num >= x and num <= y:
        return True
    else:
        return False
    
print(check_num_in_range(2, 1, 8))