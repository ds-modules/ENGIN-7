import numpy as np
import math
import cmath
import colorsys

def myLinearSolver(a1, b1, a2, b2, a3, b3):
    """
    >>> myLinearSolver([1,0,-1],1,[0,-1,1],2,[2,1,1],0)
    (1.0, -2.0, -0.0)
    >>> myLinearSolver([1,1,2],1,[0,1,2],1,[2,2,3],2)
    (0.0, 1.0, 0.0)

    """
    A = np.array([a1, a2, a3])
    b = np.array([b1, b2, b3])
    X = np.linalg.solve(A, b)
    return X[0], X[1], X[2]

def matInv(A):
    """
    >>> matInv(np.array([[1,2],[3,4]]))
    array([[-2. ,  1. ],
           [ 1.5, -0.5]])
    >>> matInv(np.array([[1,2],[3,4],[5,6]]))
    []
    >>> matInv(np.array([[1,0,1],[2,0,2],[1,2,0]]))
    []
    >>> matInv(np.array([[0,1],[-1,0]]))
    array([[-0., -1.],
           [ 1.,  0.]])

    """
    x, y = A.shape
    if x != y or math.isclose(np.linalg.det(A), 0):
        return []
    else:
        return np.linalg.inv(A)

def myCircuit(V, R1, R2, R3, R4, R5, R6, R7, R8):
    """
    >>> myCircuit(10,1,4,4,2,2,1,4,5)
    array([ 0.94594595,  0.47297297,  0.47297297,  0.27027027,  0.54054054,
            0.13513514])
    """
    A = [[1,-1,-1,0,0,0,0,0],
         [0,1,1,-1,0,0,0,0],
         [0,0,0,1,-1,-1,-1,0],
         [0,0,0,0,1,1,1,-1],
         [0,R2,-R3,0,0,0,0,0],
         [0,0,0,0,R5,-R6,0,0],
         [0,0,0,0,0,R6,-R7,0],
         [R1,R2,0,R4,R5,0,0,R8]]
    A = np.array(A)
    b = np.array([0,0,0,0,0,0,0,V])
    I = np.linalg.solve(A,b)
    return np.append(I[0:3],(I[4:7]))

def myNewton(f, df, x0, tol):
    """
    >>> f = lambda x: x**2 - 2
    >>> df = lambda x: 2*x
    >>> myNewton(f, df, 1, 1e-5)
    ([1, 1.5, 1.4166666666666667, 1.4142156862745099], [1, 0.25, 0.006944444444444642, 6.007304882871267e-06])

    >>> f = lambda x: math.sin(x) - math.cos(x)
    >>> df = lambda x: math.cos(x) + math.sin(x)
    >>> myNewton(f, df, 1, 1e-5)
    ([1, 0.782041901539138, 0.7853981759997019], [0.30116867893975674, 0.004746462127804163, 1.7822277875723103e-08])

    >>> f = lambda x: math.sinh(x) - 1
    >>> df = lambda x: math.cosh(x)
    >>> myNewton(f, df, -1, 1e-8)
    ([-1, 0.4096484296196503, 0.9430603553462776, 0.8827364259018153, 0.8813742438952269, 0.8813735870196955], [2.1752011936438014, 0.578797742601695, 0.08919683435847481, 0.001928274492311477, 9.28962716750803e-07, 2.156053113822054e-13])

    """
    R = [x0]
    E = [abs(f(x0))]
    for _ in range(100):
        if E[-1] < tol:
            break
        x0 = x0 - f(x0)/df(x0)
        R.append(x0)
        E.append(abs(f(x0)))
    return R, E

def myBisection(f, a, b, tol):
    """
    >>> f = lambda x: x**2 - 2
    >>> myBisection(f, 0, 2, 1e-1)
    ([1.0, 1.5, 1.25, 1.375, 1.4375], [1.0, 0.25, 0.4375, 0.109375, 0.06640625])

    >>> f = lambda x: math.sin(x) - math.cos(x)
    >>> myBisection(f, 0, 2, 1e-2)
    ([1.0, 0.5, 0.75, 0.875, 0.8125, 0.78125], [0.30116867893975674, 0.39815702328616975, 0.050050108850486774, 0.12654664407270189, 0.038323093040207756, 0.005866372111545948])

    >>> f = lambda x: math.exp(-x) - x**2
    >>> myBisection(f, 0, 1, 1e-2)
    ([0.5, 0.75, 0.625, 0.6875, 0.71875, 0.703125], [0.3565306597126334, 0.09013344725898531, 0.14463642851899028, 0.030175327970940913, 0.029240485786380888, 0.0006511313011985931])

    """
    g = lambda a, b: (a+b)/2.

    R = [g(a,b)]
    E = [abs(f(R[0]))]

    for i in range(100):
        if E[-1] < tol:
            break
        elif f(g(a,b)) * f(a) > 0.:
            a = g(a,b)
            R.append(g(a,b))
            E.append(abs(f(g(a,b))))
        else:
            b = g(a,b)
            R.append(g(a,b))
            E.append(abs(f(g(a,b))))
    return R, E

def PolynomialExactSolutions(d):
    """
    >>> PolynomialExactSolutions(3)
    [(1+0j), (-0.4999999999999998+0.8660254037844387j), (-0.5000000000000004-0.8660254037844385j)]

    >>> PolynomialExactSolutions(9)
    [(1+0j), (0.766044443118978+0.6427876096865393j), (0.17364817766693041+0.984807753012208j), (-0.4999999999999998+0.8660254037844387j), (-0.9396926207859083+0.3420201433256689j), (-0.9396926207859084-0.34202014332566866j), (-0.5000000000000004-0.8660254037844385j), (0.17364817766692997-0.9848077530122081j), (0.7660444431189778-0.6427876096865396j)]

    >>> PolynomialExactSolutions(4)
    [(1+0j), (6.123233995736766e-17+1j), (-1+1.2246467991473532e-16j), (-1.8369701987210297e-16-1j)]

    """
    roots = []
    n = [i/(d) for i in range(d+1)][:d+1]
    for i in range(d):
        phi = 2*cmath.pi*n[i]
        # print(phi/cmath.pi)
        real = cmath.cos(phi)
        img = cmath.sin(phi)
        roots.append(real + img * 1j)
    return roots

def NewtonConv(d, z, n, tol):
    """
    >>> NewtonConv(3,1+1j,5,0.001)
    (0, nan)
    >>> NewtonConv(3,1+1j,10,0.001)
    (1, (1+0j))
    >>> NewtonConv(3,10+10j,10,0.001)
    (0, nan)
    >>> NewtonConv(3, -10+10j,100,0.001)
    (1, (-0.49999999999999978+0.86602540378443871j))
    >>> NewtonConv(3,2,100,1e-10)
    (1, (1+0j))

    """
    solutions = np.array(PolynomialExactSolutions(d))
    for i in range(n):
        z = z - ((z**d)-1)/(d*(z**(d-1)))

    abs_diff = abs(z - solutions)

    # min_diff = min(abs_diff)
    # closest_ind = []
    # for i in range(len(abs_diff)):
    #     if abs_diff[i] == min_diff:
    #         closest_ind.append(i)
    closest_ind = np.argmin(abs_diff)

    # if len(closest_ind) > 0:
    #     IsConv = 1
    #     ConvTo = np.take(solutions, closest_ind)
    if abs_diff[closest_ind] <= tol:
        IsConv = 1
        ConvTo = solutions[closest_ind]
    else:
        IsConv = 0
        ConvTo = np.nan
    return IsConv, ConvTo

def NewtonFractal(d, n, tol, res, ULcorner, sqrL):
    x = np.linspace(ULcorner[0], ULcorner[0] + sqrL, res)
    y = np.linspace(ULcorner[1], ULcorner[1] + sqrL, res)
    X, Y = np.meshgrid(x, y)
    Z = X + (1j*Y)

    for i in range(n):
        Z = Z - ((Z**d)-1)/(d*Z**(d-1))

    output = []
    solutions = PolynomialExactSolutions(d)

    for i in range(d):
        root = solutions[i]
        Mj = abs(Z - root)
        mask = (Mj <= tol) * (i + 1)
        output.append(mask)

    if not len([x for x in output if x == 0]) == 0:
        MyCustomColor = [1, 1, 1, colorsys.hsv(len(np.unique(output)) - 1)]
    else:
        MyCustomColor = hsv(len(np.unique(output)))

