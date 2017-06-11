import math
import numpy as np

def solve_quadratic(a, b, c):
    """
    >>> solve_quadratic(1, -7, 10)
    (5.0, 2.0)
    >>> solve_quadratic(5, -23, 2)
    (4.511334438749598, 0.08866556125040184)
    """
    disc = math.sqrt(b*b-4.*a*c)
    return (-b+disc)/(2.*a), (-b-disc)/(2.*a)

def euclidean_distance(x1, y1, x2, y2):
    """
    >>> euclidean_distance(np.array([0,0]),np.array([0,0]),np.array([3,5]),np.array([4,12]))
    array([  5.,  13.])
    """
    x = x1 - x2
    y = y1 - y2
    return np.sqrt(x*x+y*y)

def c14_dating(time):
    """
    >>> c14_dating(10000)
    0.29828675203393595
    >>> c14_dating(5730)
    0.49999454030978113
    """
    return math.e**(-time*0.00012097)

def proj_time(y0, v0, theta):
    """
    >>> proj_time(0, 15, 40)
    1.9657
    """
    b = v0 *



