from math import pi
from math import factorial
from math import sin
import numpy as np

def my_sin_approx_fixed(x, n):
    """
    >>> my_sin_approx_fixed(0, 0)
    0.0
    >>> my_sin_approx_fixed(2*pi/3, 2)
    0.8990450164363117
    >>> my_sin_approx_fixed(2*pi/3, 4)
    0.8661082667623468
    >>> my_sin_approx_fixed(5*pi/2, 3)
    -189.61411535680674
    >>> my_sin_approx_fixed(5*pi/2, 10)
    1.0135363227206775
    
    :param x: value of x, well defined double
    :param n: either zero or positive int
    :return: approx of sin(x)
    """
    sum = 0.0
    for i in range(n+1):
        sum += ((-1)**i * x**(2*i+1)) / factorial(2*i + 1)
    return sum

def my_sin_approx_tolerance(x, tolerance):
    """
    >>> my_sin_approx_tolerance(pi/3, 1e-2)
    (0.8662952837868347, 2)
    >>> my_sin_approx_tolerance(4*pi/5, 1e-3)
    (0.5883934857193339, 4)
    >>> my_sin_approx_tolerance(pi/3, 1e-10)
    (0.8660254037859597, 6)
    >>> my_sin_approx_tolerance(11*pi/2, 1e-5)
    (-0.9999916736842261, 26)
        
    :param x: same as before
    :param tolerance: greater than zero, not NaN, inf
    :return: tuple (smallest possible n such that approx of sin(x) is within tolerance of actual, approx is part 1)
    """
    def within(a):
        return abs(a - actual) <= tolerance

    actual = sin(x)
    n = 0
    approx = 0.0
    while not within(approx):
        n+=1
        approx = my_sin_approx_fixed(x,n)
    return (approx, n)


def my_minimum_index(vector):
    """
    >>> my_minimum_index(np.array([5]))
    (5, 0)
    >>> my_minimum_index(np.array([5, 6, 1]))
    (1, 2)
    >>> my_minimum_index(np.array([5, 6, 1, -1, 1]))
    (-1, 3)
    >>> my_minimum_index(np.array([4, 10, np.nan, 2, 5, 50]))
    (2.0, 3)
    >>> my_minimum_index(np.array([1, 2]))
    (1, 0)
    
    :param vector: numpy array with at least one entry
    :return: (smallest value in vector, index of first occurrence)
    """
    index = 0
    min = vector[0]
    for i in range(len(vector)):
        if np.isnan(vector[i]):
            continue
        if vector[i] < min or np.isnan(min):
            min = vector[i]
            index = i
    return (min, index)


def my_sort(vector):
    """
    >>> my_sort(np.array([0]))
    [0]
    >>> my_sort(np.array([2,1]))
    [1, 2]
    >>> my_sort(np.array([2,1,9,-10,pi]))
    [-10.0, 1.0, 2.0, 3.1415926535897931, 9.0]
    >>> my_sort(np.array([6, 3, 7, 1, 0, 1, 7]))
    [0, 1, 1, 3, 6, 7, 7]
    >>> my_sort(np.array([6, 3, 7, 1, np.NaN, 0, 1, 7]))
    [0.0, 1.0, 1.0, 3.0, 6.0, 7.0, 7.0, nan]
    
    
    :param vector: same as part 1
    :return: sorted version of vector
    """
    for i in range(len(vector)):
        smallest, index = my_minimum_index(vector[i:])
        vector[index + i] = vector[i]
        vector[i] = smallest

    #vector.sort()
    return list(vector)

def my_reverse_without_recursion(vector):
    """
    >>> my_reverse_without_recursion([True, True, False, True])
    [True, False, True, True]
    >>> my_reverse_without_recursion([1,2,3,4,5])
    [5, 4, 3, 2, 1]
    >>> my_reverse_without_recursion([1,2,3,4])
    [4, 3, 2, 1]
    
    :param vector: some possibly empty numpy array
    :return: reversed vector
    """
    stk = []
    while len(vector)>0:
        stk.append(vector.pop())
    # newvector = []
    # while len(stk)>0:
    #     newvector.append(stk.pop())
    return stk

def my_reverse_with_recursion(vector):
    """
    >>> my_reverse_without_recursion([True, True, False, True])
    [True, False, True, True]
    >>> my_reverse_without_recursion([1,2,3,4,5])
    [5, 4, 3, 2, 1]
    >>> my_reverse_without_recursion([1,2,3,4])
    [4, 3, 2, 1]
    
    :param vector: same as before
    :return: reversed vector
    """
    def helper(start, end):
        if start == end:
            return vector
        temp = vector[start]
        vector[start] = vector[end]
        vector[end] = temp
        return helper(start+1, end-1)
    return helper(0, len(vector)-1)


def my_parser(string, delimiters):
    """
    >>> my_parser("Hello+World", list("+"))
    ('+', 'Hello', 'World')
    >>> my_parser("Another-test", list(",-"))
    ('-', 'Another', 'test')
    >>> my_parser("NO DELIMITER??", list("!()"))
    ('', 'NO DELIMITER??', '')
    
    :param string: string to split
    :param delimiters: array of chars, each value is a delimiter
    :return: (first delimiter that appears in string, stuff to left of delim, stuff to right of delim)
    """
    for delim in delimiters:
        index = -1
        for i in range(len(string)):
            if string[i] == delim:
                index = i
        if index == -1:
            continue
        return (delim, string[:index], string[index+1:])
    return ("", string, "")


def my_calculator_inverse_precedence(expression):
    """
    >>> my_calculator_inverse_precedence("4-3.14")
    0.8600
    >>> my_calculator_inverse_precedence("4-2-2")
    0
    >>> my_calculator_inverse_precedence("3+5*2")
    16
    >>> my_calculator_inverse_precedence("2^3/3")
    2
    >>> my_calculator_inverse_precedence("8-2-2*4^2")
    256
    
    :param expression: string representing arithmetic expression
    :return: eval of expression using new order of operations
    """
    return 0

def my_calculator_with_undo(expression):
    """
    >>> my_calculator_with_undo("2.5-2")
    0.500
    >>> my_calculator_with_undo("2.5-2!")
    2.500
    
    :param expression: same as before
    :return: see above
    """
    return 0