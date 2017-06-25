import numpy as np
import math
import cmath

def mySols(A, b):
    """
    >>> mySols(np.array([[1,2,3],[0,3,1],[1,14,7]]), np.array([[1],[2],[3]]))
    There is no solution
    []

    >>> mySols(np.array([[1,2,3],[0,3,1],[-1,14,7]]), np.array([[1],[2],[3]]))
    There is one solution
    array([[ 3.        ],
           [ 1.14285714],
           [-1.42857143]])

    >>> mySols(np.array([[1,2,3,4,5,6],[2,3,4,5,6,7],[3,4,5,6,7,8]]), np.array([[21],[27],[33]]))
    There is an infinite number of solutions
    array([[ 1.],
           [ 1.],
           [ 1.],
           [ 1.],
           [ 1.],
           [ 1.]])

    """
    rank_ab = np.linalg.matrix_rank(np.concatenate((A, b), axis=1))
    rank_a = np.linalg.matrix_rank(A)
    if rank_ab > rank_a:
        print("There is no solution")
        return []
    elif rank_ab == rank_a and rank_a != A.shape[1]:
        print("There is an infinite number of solutions")
        return np.dot(np.linalg.pinv(A), b)
    else:
        print("There is one solution")
        return np.linalg.solve(A,b)

def cubicPolyDiff(f):
    """
    >>> cubicPolyDiff([1,2,3,4])

    >>> cubicPolyDiff([4,4,21,0])


    """




