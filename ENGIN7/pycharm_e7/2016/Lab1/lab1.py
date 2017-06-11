import math
import numpy as np

def q1():
    a, b, c, x = 3., -6., 4., 2.
    E1 = math.sqrt(a*a + b*b + c*c)
    E2 = (-b - np.sqrt(b*b - 4*a*c)) / 2*a
    E3 = math.log(3*x - a)
    E4 = math.log(3*abs(b) + c / 5, 10)
    E5 = math.pow(a*x + a*b/c, 1./3)
    E6 = (x*x + 1) / ((a*x-1) * abs(b-math.e**x))
    E7 = math.cos(math.sqrt(a)/3*math.pi)**2 + \
         math.cos((math.sqrt(a)/3*math.pi)**2)

    return (E1,E2,E3,E4,E5,E6,E7)

q1()