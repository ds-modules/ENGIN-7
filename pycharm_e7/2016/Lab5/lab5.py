import numpy as np
import math
import heapq
import time
import matplotlib.pyplot as plt
import random
from timeit import default_timer as timer

def myBigONotation():
    return ['E', 'D', 'B']

def myBraille2Double(braille):
    """
    >>> myBraille2Double([[1,0,1,1],[1,0,0,1],[0,0,0,0]])
    24
    >>> myBraille2Double([[1,0,1,1,1,0],[1,0,0,1,0,0],[0,0,0,0,0,0]])
    241
    >>> myBraille2Double([[[1,0],[0,0],[0,0]],[[1,0],[0,1],[0,0]],[[1,1],[0,0],[0,0]],[[1,1],[1,0],[0,0]]])
    1536
    """
    braille = np.array(braille)
    one = [[1,0],[0,0],[0,0]]
    two = [[1,0],[1,0],[0,0]]
    three = [[1,1],[0,0],[0,0]]
    four = [[1,1],[0,1],[0,0]]
    five = [[1,0],[0,1],[0,0]]
    six = [[1,1],[1,0],[0,0]]
    seven = [[1,1],[1,1],[0,0]]
    eight = [[1,0],[1,1],[0,0]]
    nine = [[0,1],[1,0],[0,0]]
    zero = [[0,1],[1,1],[0,0]]

    if len(braille.shape)==2:
        n_digits = int(len(braille[2])/2)
        result = 0
        digit = -1
        for i in range(n_digits):
            sub_braille = braille[:,[i*2,i*2+1]]
            if np.array_equal(sub_braille, one):
                digit = 1
            elif np.array_equal(sub_braille, two):
                digit = 2
            elif np.array_equal(sub_braille, three):
                digit = 3
            elif np.array_equal(sub_braille, four):
                digit = 4
            elif np.array_equal(sub_braille, five):
                digit = 5
            elif np.array_equal(sub_braille, six):
                digit = 6
            elif np.array_equal(sub_braille, seven):
                digit = 7
            elif np.array_equal(sub_braille, eight):
                digit = 8
            elif np.array_equal(sub_braille, nine):
                digit = 9
            elif np.array_equal(sub_braille, zero):
                digit = 0
            else:
                raise ValueError("unrecognized braille")
            result = result + digit*(10**(n_digits-i-1))
    else:
        n_digits = len(braille)
        result = 0
        digit = -1
        for i in range(n_digits):
            sub_braille = braille[i]
            if np.array_equal(sub_braille, one):
                digit = 1
            elif np.array_equal(sub_braille, two):
                digit = 2
            elif np.array_equal(sub_braille, three):
                digit = 3
            elif np.array_equal(sub_braille, four):
                digit = 4
            elif np.array_equal(sub_braille, five):
                digit = 5
            elif np.array_equal(sub_braille, six):
                digit = 6
            elif np.array_equal(sub_braille, seven):
                digit = 7
            elif np.array_equal(sub_braille, eight):
                digit = 8
            elif np.array_equal(sub_braille, nine):
                digit = 9
            elif np.array_equal(sub_braille, zero):
                digit = 0
            else:
                raise ValueError("unrecognized braille")
            result = result + digit*(10**(n_digits-i-1))

    return result

def myBraille2ASCII(braille):
    """
    >>> myBraille2ASCII([[[1,0],[0,0],[0,0]],[[1,0],[0,1],[0,0]],[[1,1],[0,0],[0,0]],[[1,1],[1,0],[0,0]]])
    [49, 53, 51, 54]

    :param braille: braille encoding
    :return: ascii
    """
    number = myBraille2Double(braille)
    numberstr = str(number)

    n_digits = len(numberstr)
    ASCII = []

    for i in range(n_digits):
        ASCII.append(ord(numberstr[i]))

    return ASCII

def myBinary2Num(binary, representation):
    """
    >>> myBinary2Num('11001000', 'unsigned')
    200
    >>> myBinary2Num('11001000', 'sign-magnitude')
    -72
    >>> myBinary2Num('11001000', 'twos complement')
    -56
    >>> myBinary2Num('01001110', 'unsigned')
    78
    >>> myBinary2Num('11001110', 'sign-magnitude')
    -78
    >>> myBinary2Num('11001110', 'twos complement')
    -50

    :param binary: character string of length 8, binary
    :param representation: name of representation for binary
    :return: output argument result in base 10
    """
    num = str(binary)
    result = 0

    if representation == 'unsigned':
        for i in range(0, len(num)):
            if num[i] == '1':
                result += 2**(7-i)

    elif representation == 'sign-magnitude':
        sign = 1
        if num[0] == '1':
            sign = -1
        for i in range(1, len(num)):
            if num[i] == '1':
                result += 2**(7-i)
        result *= sign

    elif representation == 'twos complement':
        if num[0] == '1':
            result = result - 2**7
        for i in range(1, len(num)):
            if num[i] == '1':
                result += 2**(7-i)

    return result

def myCompareFloats(x, y, tolerance=1e-9):
    """
    >>> myCompareFloats(2+3, 5, 0)
    (True, True)
    >>> myCompareFloats(0, 0.001, 1e-2)
    (False, True)

    :param x: scalar, float
    :param y: scalar, float
    :param tolerance: absolute
    :return: if the floats are about equal
    """
    exact = (x==y)
    approx = (abs(x-y)<=tolerance)
    return exact, approx

def mySingle2Decimal(binary):
    """
    >>> mySingle2Decimal ('00111111111100000000000000000000')
    1.875
    >>> mySingle2Decimal ('10111111000000000000000000000000')
    -0.5
    >>> mySingle2Decimal ('00100000100000000000000000000001')
    2.1684046034649503e-19
    >>> mySingle2Decimal ('11111111100000000000000000000000')
    -inf
    >>> mySingle2Decimal ('11111111100000000000000000000001')
    nan
    >>> mySingle2Decimal ('10111111010000000000000000000000')
    -0.75
    >>> mySingle2Decimal ('00100000100000000000111000000001')
    2.1693310457510097e-19

    :param binary:
    :return:
    """
    num = str(binary)
    value_s = int(num[0])
    value_d = 127
    value_e = myBinary2Num(num[1:9], 'unsigned')

    value_f = 0
    for i in range(9,32):
        if num[i] == '1':
            value_f = value_f + 2**(8-i)

    if not math.isclose(value_e, 0) and not math.isclose(value_e, 255):
        result = ((-1)**value_s)*(2**(value_e-value_d))*(1+value_f)
    elif math.isclose(value_e, 0) and not math.isclose(value_f, 0):
        result = ((-1)**value_s)*(2**(1-value_d))*value_f
    elif math.isclose(value_e, 0) and math.isclose(value_f, 0):
        result = 0
    elif math.isclose(value_e, 255) and math.isclose(value_f, 0):
        result = ((-1)**value_s)*np.Inf
    else:
        result = np.NaN

    return result

def myCompareElements(element1, element2):
    """
    >>> element1, element2 = 'Hydrogen', 'Carbon'
    >>> myCompareElements (element1 , element2)
    -1
    >>> myCompareElements (element2 , element1)
    1
    >>> myCompareElements (element1 , element1)
    0
    >>> element1, element2 = 'Uranium', 'Boron'
    >>> myCompareElements (element1 , element2)
    -1
    >>> myCompareElements (element2 , element1)
    1
    >>> myCompareElements (element1 , element1)
    0
    >>> element1, element2 = 'Plutonium', 'Hydrogen'
    >>> myCompareElements (element1 , element2)
    -1
    >>> myCompareElements (element2 , element1)
    1
    >>> myCompareElements (element1 , element1)
    0

    :param element1: name of element of periodic table
    :param element2: different element
    :return: comparison
    """
    if element1 < element2:
        return 1
    elif element1 == element2:
        return 0
    else:
        return -1

def mySortElements(elements):
    """
    >>> elements=['Hydrogen' , 'Carbon' , 'Magnesium' , 'Calcium' , 'Carbon']
    >>> mySortElements(elements)
    ['Calcium', 'Carbon', 'Carbon', 'Hydrogen', 'Magnesium']
    >>> elements=['Dubnium','Bohrium','Copernicium','Meitnerium','Roentgenium']
    >>> mySortElements(elements)
    ['Bohrium', 'Copernicium', 'Dubnium', 'Meitnerium', 'Roentgenium']
    >>> elements=['Argon','Argon']
    >>> mySortElements(elements)
    ['Argon', 'Argon']

    :param elements: 1xn cell array representing list of n elements of periodic table
    :return: 1xn cell array that represents the sorted list
    """
    sorted = []
    heapq.heapify(elements)
    while len(elements) > 0:
        sorted.append(heapq.heappop(elements))
    return sorted

def myCompareSorting(n):
    """

    :param n: integer greater than 0
    :return: chart of time comparison
    """
    time_student = []
    time_gsi = []
    elems = [random.random() for _ in range(int(n))]
    # x_ax = [2**i for i in range(int(math.ceil(math.log(n, 2))))]
    x_ax = []
    i = n//10
    while i < n:
        t = time.time()
        mySortElements(elems[:i])
        time_student.append((time.time() - t)*1000)

        t = time.time()
        sorted(elems[:i])
        time_gsi.append((time.time() - t)*1000)

        x_ax.append(i)

        i += n//10

    fig, ax = plt.subplots()
    plt.xlabel('Size of list to sort')
    plt.ylabel('Wall time taken by sorted alg (ms)')
    plt.title('Comparision of sorting algs')
    print(time_student)
    print(time_gsi)
    ax.plot(x_ax, time_student, label='student')
    ax.plot(x_ax, time_gsi, label='gsi')
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles, labels)
    plt.show()

myCompareSorting(int(1e6))