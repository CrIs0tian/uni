def print_r(i): 
    if i >= 0:
        print('dio\t'*i+'dio') 
        print_r(i-1)

print_r(3)