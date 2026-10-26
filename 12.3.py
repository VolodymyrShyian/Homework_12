def is_even(number):
    num = str(number)
    num_1 = num[-1]
    my_tuple = (2, 4, 6, 8, 0)
    if int(num_1) in my_tuple:
        return True
    else:
        return False

assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'
