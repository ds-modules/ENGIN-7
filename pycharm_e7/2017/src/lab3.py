import numpy as np
np.seterr(all='ignore');

def my_consumer_helper(value):
    """
    >>> my_consumer_helper(60)
    ('1', 54.0)
    >>> my_consumer_helper(550)
    ('1', 495.0)
    
    :param value: cost of item
    :return: tuple (coupon number, price after discount)
    """
    c1 = value * .1
    c2 = 25 if (value >= 200) else 0
    c3 = 50 if (value >= 400) else 0
    best = max(c1,c2,c3)
    if best == c1:
        return ("1", value * .9)
    elif best == c2:
        return ("2", value - 25)
    else:
        return ("3", value - 50)

def my_water_quality(ph, do):
    """
    >>> my_water_quality(7, 4)
    (4.0, False)
    >>> my_water_quality(6.2, 3)
    (1.5, True)
    >>> my_water_quality(8.5, 2)
    (2.0, True)
    >>> my_water_quality(15, 10)
    (nan, True)
    
    
    :param ph: ph level of water
    :param do: dissolved oxygen concentration in water
    :return: tuple (score, warning)
    """
    if ph < 0 or ph > 14:
        phScore = np.nan
    elif ph >= 6.5 and ph <= 7.5:
        phScore = np.float64(5)
    elif ph > 7.5 and ph <= 8:
        phScore = np.float64(4)
    elif ph > 8 and ph <= 8.5:
        phScore = np.float64(3)
    elif (ph>=6 and ph<6.5) or (ph>8.5 and ph<=9):
        phScore = np.float64(2)
    elif(ph >= 5.5 and ph < 6) or (ph > 9 and ph <= 9.5):
        phScore = np.float64(1)
    else:
        phScore = np.float64(0)

    if 7 <= do <= 11:
        doScore = 5
    elif 4 <= do < 7:
        doScore = 3
    elif 2 <= do < 4:
        doScore = 1
    elif 0 <= do < 2:
        doScore = 0
    else:
        doScore = np.nan

    score = (doScore + phScore) / 2
    warning = False
    if np.isnan(doScore) or np.isnan(phScore):
        warning = True
    elif phScore < 3 or doScore < 3:
        warning = True

    return (score, warning)

def my_array_resize(array_in, dimension):
    """
    >>> my_array_resize(np.array([[2,3,5],[4,6,7]]), 'row')
    array([[2, 3, 5],
           [4, 6, 7],
           [0, 0, 0],
           [0, 0, 0]])
    >>> my_array_resize(np.array([[2, 3, 5], [4, 6, 7]]), 'col')
    array([[2, 3, 5, 0, 0, 0],
           [4, 6, 7, 0, 0, 0]])
    >>> my_array_resize(np.array([[2, 3, 5], [4, 6, 7]]), 'both')
    array([[2, 3, 5, 0, 0, 0],
           [4, 6, 7, 0, 0, 0],
           [0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0]])
    >>> my_array_resize(np.array([[2, 3, 5], [4, 6, 7]]), '1234')
    array([[2, 3, 5],
           [4, 6, 7]])
    
    :param array_in: m x n numpy array to be resized
    :param dimension: which axis to resize
    :return: resized array
    """
    x, y = array_in.shape
    #array_in = array_in.copy()
    if dimension == 'row':
            array_out = np.pad(array_in, ((0,x),(0,0)), mode='constant', constant_values=0)
    elif dimension == 'col':
        array_out = np.pad(array_in, ((0,0),(0,y)), mode='constant', constant_values=0)
    elif dimension == 'both':
        array_out = np.pad(array_in, ((0,x),(0,y)), mode='constant', constant_values=0)
    else:
        array_out = array_in.copy()
    return array_out

import operator
def my_sequence_id(a, b, c):
    """
    >>> my_sequence_id(1, 1, 2)
    3
    >>> my_sequence_id(3, 7, 21)
    147
    >>> my_sequence_id(2, 2, 4)
    >>> my_sequence_id(3, 5, 2)
    -3
    
    :param a: first integer
    :param b: second integer
    :param c: third integer
    :return: next term in sequence
    """
    possible = set()

    # def sequence(op):
    #     if c == op(a,b):
    #         return op(b,c)
    #     else:
    #         return np.nan

    if c == b + a:
        possible.add(c + b)
    if c == b - a:
        possible.add(c - b)
    if c == b * a:
        possible.add(c * b)

    if len(possible) != 1:
        return None
    else:
        return possible.pop()

def my_elevator(loc_caller, loc_one, dest_one, loc_two, dest_two):
    """
    >>> my_elevator(2, 1, -1, 2, 5)
    2
    >>> my_elevator(2, -2, 4, 1, 0)
    1
    >>> my_elevator(5, -2, None, 1, None)
    2
    >>> my_elevator(0, -1, -5, 2, 10)
    1
    >>> my_elevator(0, 3, 5, 2, None)
    2
    >>> my_elevator(10, 12, 10, 8, 10)
    1
    
    :param loc_caller: location of caller
    :param loc_one: location of elevator 1
    :param dest_one: destination of elevator 1
    :param loc_two: location of elevator 2
    :param dest_two: destination of elevator 2
    :return: 
    """
    dict = {True: 1, False: 2}
    if loc_one == loc_caller != loc_two == loc_caller:
        return dict[loc_one == loc_caller]


    moving1 = dest_one != None
    moving2 = dest_two != None
    direction1 = moving1 and (loc_one < loc_caller < dest_one or dest_one < loc_caller < loc_one)
    direction2 = moving2 and (loc_two < loc_caller < dest_two or dest_two < loc_caller < loc_two)
    if direction1 != direction2:
        return dict[direction1 == True]

    if moving1 != moving2:
        return dict[moving1 == False]

    bothMoving = moving1 and moving2
    if bothMoving:
        dist1 = abs(dest_one - loc_caller)
        dist2 = abs(dest_two - loc_caller)
        if dist1 != dist2:
            return dict[dist1 < dist2]

    distElv1 = abs(loc_one - loc_caller)
    distElv2 = abs(loc_two - loc_caller)
    return dict[distElv1 <= distElv2]