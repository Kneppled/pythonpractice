"""
vampires.py

Find vampire numbers for n fangs.

A vampire number n*2 digit number that is the product of n 2-digit numbers 
called fangs, such that there is a one-to-one match between the digits in the
fangs and the digits in the vampire number.

Functions:
find_vampires: Find vampire numbers (list of tuple of int)
show_vampires: Pretty print data on vampire numbers. (None)
"""

import itertools, functools, operator

def find_vampires(fang_count):
    """
    Find vampire numbers (list of tuple of int)

    The items in the output are the vampire number followed by the fangs that
    made it.

    Parameters:
    fang_count: The number of fangs for the vampire number. (int)
    """
    vampires = []
    # check all possible combinations of fangs
    for fangs in itertools.combinations(range(10, 100), fang_count):
        possible = functools.reduce(operator.mul, fangs, 1)
        # make sure character lists match
        possible_chars = sorted(str(possible))
        fang_chars = sorted(''.join([str(fang) for fang in fangs]))
        if possible_chars == fang_chars:
            vampires.append((possible, ) + fangs)
    return sorted(vampires)

def show_vampires(vampires):
    """
    Pretty print data on vampire numbers. (None)

    Paramters:
    vampires: A list of vampires with fangs, as output by find_vampires. (list)
    """
    for vampire_data in vampires:
        fang_text = '*'.join([str(fang) for fang in vampire_data[1:]])
        print('{}={}'.format(vampire_data[0], fang_text))

if __name__ == '__main__':
    vampire_data = find_vampires(3)
    show_vampires(vampire_data)
