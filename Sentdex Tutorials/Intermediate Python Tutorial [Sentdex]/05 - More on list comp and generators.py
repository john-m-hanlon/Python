#
# More on list comprehension and generators
# 05 - More on list comp and generators.py
#

input_list = [5, 6, 2, 10, 15, 20, 5, 2, 1, 3]


def div_by_five(num):
    ''' Function to determine if an argument is divisble by 5

    Parameters
    ==========
    num : int
        integer which is then operated on

    Returns
    =======
    value : int
        returns only arguments which are divisible by 5
    '''
    if num % 5 == 0:
        return True
    else:
        return False


xyz = [i for i in input_list if div_by_five(i)]
print(xyz)
