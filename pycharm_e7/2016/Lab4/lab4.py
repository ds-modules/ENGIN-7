import numpy as np
import math

def mySavingsPlan(p0, rate, goal):
    """
    >>> mySavingsPlan(2000, 0.15, 10000)
    12
    >>> mySavingsPlan(1000, 0.05, 10000)
    48
    """
    if p0 > goal:
        years = 0
    else:
        years = 1 + mySavingsPlan(p0*(1+rate), rate, goal)
    return years

def myMin(P):
    """
    >>> myMin([5,4,5,2,6,7,1,8,9])
    (1, 6)
    >>> myMin([2,3,5,7,2,4,3,2])
    (2, [0, 4, 7])
    >>> myMin([2,-3,5,-7,2,4,3,2])
    (-7, 3)
    >>> myMin([2,-3,5,7,2,4,-3,2])
    (-3, [1, 6])

    :param P: a float array
    :return: (min value in P, index of min value(s))
    """
    value = P[0]
    location = 0
    for i in range(1, len(P)):
        if P[i] < value:
            value = P[i]
            location = i
        elif P[i] == value:
            if np.isscalar(location):
                location = [location, i]
            else:
                location.append(i)

    return value, location

def myRainfall(rainData):
    """
    >>> myRainfall([2,4,-5,1,7,-2,8,-999,4,6,4])
    (22, 4.4)
    >>> myRainfall([2,4,-5,1,7,-2,8,0,4,6,4])
    (36, 4.0)
    >>> myRainfall([2,4,-999,1,7,-2,8,-999,4,6,4])
    (6, 3.0)
    >>> myRainfall([2.3,4.1,-5.4,1.0,7.1,-2,8.0,4.9,6,-999])
    (33.4, 4.771428571428571)
    >>> myRainfall([0,-999,-5,1,7,-2,8,-999,4,6,2])
    (0, 0.0)

    :param rainData: a float array, with positive values,
                     negative values, or -999, a delimiter
    :return: (total rainfall, average rainfall)
    """
    rainTot = 0
    count_days = 0

    for n in range(len(rainData)):
        if rainData[n] == -999:
            break

        elif rainData[n] >= 0:
            rainTot += rainData[n]
            count_days += 1

    return rainTot, rainTot / float(count_days)

def RandomWalk(L, rmat):
    """
    >>> rmat = [[4,1],[1,2],[3,2],[1,1],[4,1],[2,1],[2,2],[3,1],[1,1],[2,2]]
    >>> RandomWalk(2,rmat)
    (8, [[0, 0], [-1, 1], [1, 1], [0, 1], [0, 0], [1, 0], [1, 1], [1, -1], [0, -1]])

    :param L: room is L x L
    :param rmat: matrix of random integers that determine movement
    :return: (number of steps, path)
    """
    def all_one(mat):
        length = len(mat[0])
        for i in range(len(mat)):
            for j in range(length):
                if mat[i][j] != 1:
                    return False
        return True

    def isWall(x, y, rmat, rmat_ind, L):
        curr = rmat[rmat_ind][0]
        dist = rmat[rmat_ind][1]
        if curr == 1:
            return (y + dist) > L
        elif curr == 2:
            return (y - dist) < 0
        elif curr == 3:
            return (x + dist) > L
        elif curr == 4:
            return (x - dist) < 0

    room = np.zeros((L+1, L+1))
    x, y = 0, 0
    room[0][0] = 1
    rmat_ind = 0
    N = 0
    path = [[0, 0]]

    while(not all_one(room)):
        if rmat_ind >= len(rmat):
            rmat_ind = 0

        while isWall(x, y, rmat, rmat_ind, L):
            rmat_ind += 1
            if rmat_ind >= len(rmat):
                rmat_ind = 0

        curr = rmat[rmat_ind][0]
        dist = rmat[rmat_ind][1]

        # print(room, curr, dist, x, y)

        if curr == 1:
            for i in range(y, y+dist):
                room[i][x] = 1
            y = y + dist
        elif curr == 2:
            for i in range(y-dist, y+1):
                room[i][x] = 1
            y =  y - dist
        elif curr == 3:
            for i in range(x, x+dist):
                room[y][i] = 1
            x = x + dist
        elif curr == 4:
            for i in range(x-dist, x+1):
                room[y][i] = 1
            x = x - dist

        rmat_ind += 1
        path.append([x - 1, y - 1])
        N += 1

    # print(room, curr, dist, x, y)
    return N, path

def fibrec(N):
    """
    >>> fibrec(12)
    89
    >>> fibrec(-3)
    'N must be a positive number'
    >>> fibrec(23)
    17711

    :param N: Nth fib number
    :return: value of that number
    """
    if N < 1:
        F = 'N must be a positive number'
    elif N == 1:
        F = 0
    elif N == 2:
        F = 1
    else:
        F = fibrec(N-1) + fibrec(N-2)
    return F

def fibiter(N):
    """
    >>> fibiter(12)
    89
    >>> fibiter(-3)
    'N must be a positive integer'
    >>> fibiter(23)
    17711

    :param N: same as above
    :return: the Nth fibbo number
    """
    f1 = 0
    f2 = 1
    F = 0
    if N < 1:
        F = 'N must be a positive integer'
    elif N == 1 or N == 2:
        F = 1
    else:
        for n in range(3, N+1):
            F = f1 + f2
            f1 = f2
            f2 = F
    return F

def fibratio(N):
    """
    >>> fibratio(10)
    1.619047619047619
    >>> fibratio(1)
    'N must be an integer greater than 1'
    >>> fibratio(15)
    1.6180257510729614

    :param N: Nth fib number
    :return: ratio of Nth/N-1th fib numbers
    """
    if N < 2:
        r = 'N must be an integer greater than 1'
    else:
        r = fibiter(N)/fibiter(N-1)
    return r

def fibapprox(e):
    """
    >>> fibapprox(1e-6)
    18
    >>> fibapprox(1e-8)
    22
    >>> fibapprox(1e-4)
    13

    :param e: margin of error (abs)
    :return: smallest integer N such that fibratio converges to golden ratio
    """
    phi = (1.+math.sqrt(5))/2
    N = 2
    while abs(phi - fibratio(N)) > e:
        N += 1
    return N

def player2(nmin, nmax, N_guess, secret):
    """
    >>> player2(10, 20, 0, 19)
    3

    :param nmin: lowest possible value
    :param nmax: highest possible value
    :param N_guess: starting num of guesses
    :param secret: secret number
    :return: number of guesses
    """
    def player1(guess, secret):
        if guess < secret:
            msg = 'higher'
        elif guess > secret:
            msg = 'lower'
        else:
            msg = 'correct'
        return msg

    N_guess += 1
    guess = round((nmax + nmin)/2)

    msg = player1(guess, secret)
    if msg == 'higher':
        N_guess = player2(guess, nmax, N_guess, secret)
    elif msg == 'lower':
        N_guess = player2(nmin, guess, N_guess, secret)

    return N_guess