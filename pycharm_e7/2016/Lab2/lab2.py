import math
import numpy as np
import matplotlib.pyplot as plt

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

g = 9.81

def proj_time(y0, v0, theta):
    """
    >>> proj_time(0, 15, 40)
    1.9657113446071535
    """
    b = v0 * math.sin(np.deg2rad(theta))
    time = -(-b - math.sqrt(b**2+2.*g*y0))/g
    return time

def proj_distance(y0, v0, theta):
        """
        >>> proj_distance(0, 15, 40)
        22.587333784683665
        """
        time = proj_time(y0, v0, theta)
        dist = v0 * time * math.cos(np.deg2rad(theta))
        return dist

def draw_circle(xc, yc, rc):
    circle = plt.Circle((xc, yc), rc, fill=False)
    fig, ax = plt.subplots()
    ax.set_xlim((-5,5))
    ax.set_ylim((-5,5))
    ax.add_artist(circle)
    plt.show()

def triangulate(y2,x3,y3,r1,r2,r3):
    yCell = (r1*r1-r2*r2+y2*y2)/(2*y2)
    c = x3*x3 + (yCell-y3)**2 - r3*r3
    xCell = (2*x3 - math.sqrt(4*x3*x3-4*c))/2
    fig, ax = plt.subplots()
    ax.set_xlim((-20, 20))
    ax.set_ylim((-20, 20))
    circle1 = plt.Circle((0,0), r1, fill=False)
    circle2 = plt.Circle((0,y2), r2, fill=False)
    circle3 = plt.Circle((x3,y3), r3, fill=False)
    ax.plot((xCell), (yCell), '^', color = 'blue')
    ax.add_artist(circle1)
    ax.add_artist(circle2)
    ax.add_artist(circle3)
    plt.show()

triangulate(3,8,1,2.24,1.41,7.07)
