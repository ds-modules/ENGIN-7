
# coding: utf-8

# # E7: Introduction to Computer Programming for Scientists and Engineers

# ## Lab Assignment 4

# For each question, you will have to fill in one or more Python functions. We provide an autograder with a number of test cases that you can use to test your function. Note that the fact that your function works for all test cases thus provided does necessarily guarantee
# that it will work for all possible test cases relevant to the question. It is your responsibility
# to test your function thoroughly, to ensure that it will also work in situations not covered
# by the test cases provided

# In[1]:


# Please run this cell, and do not modify the contets
import numpy as np
import math
np.seterr(all='ignore');
# %run lab4_ag.py


# ## Question 1: Interest
# 
# The interest rate, $r$, on a principal, $P_0$, is a payment for allowing the bank to use
# an investor's money. Compound interest is accumulated according to the recursive
# formula $P_n = (1 + r)P_{n-1}$, where $P_n$ is the balance after n compounding periods (e.g.
# years), and $P_{n-1}$ is the balance after the previous period. The interest rate $r$ is given
# in decimal, e.g. 0.1, which is 10%. 
# 
# Write a recursive function `mySavingsPlan(P0, rate, goal)` with output `years`. `years` is the number of years it will require for an investor to reach the investment goal defined by `goal` while investing an original amount `P0` at the annual interest rate, and
# specified by the variable `rate`. For the purpose of this problem, consider the investment
# balance to change only once per year (i.e. the output years should be a whole number).

# In[2]:


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


# ## Question 2: Searching
# 
# Write a Python function `myMin(P)` with output `value, location`, where `P` is a class double (numeric) array. The output value is the minimum value in the array `P` and location is the index of the minimum value. Note that the minimum
# value could appear more than once. If this is the case, location should specify the
# indices of all occurrences of the minimum value. You may NOT use the built-in
# Python command `min` in your function.

# In[3]:


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


# ## Question 3: Rainfall Totals
# 
# Design a function that computes the total rainfall at a location using daily rainfall
# measurements entered by a user. The list may contain the number -999 indicating
# the end of the data from a given period. There may be negative numbers other than
# -999 in the list which represent erroneous measurements which should be neglected.
# Produce the total and average of the non-negative values in the list up to the first -999
# (if there is a -999 value). 
# 
# Your function `myRainfall(rainData)` should return `rainTot, rainAvg`,
# where `rainData` is a double array of daily rainfall data, `rainTot` is the total rainfall
# in the period represented by either the entire array `rainData` or the period from the
# beginning until the first occurrence of -999. `rainAvg` is the average daily rainfall during
# this period (not counting days with neglected measurements).

# In[4]:


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


# ## Question 4: Random Walk Vacuum Robot
# 
# In this problem, we are going to study the displacement of a random walk vacuum
# cleaner robot that randomly wanders around a closed room.
# 
# - The room is represented by a square grid $[0, L]$ ft x $[0, L]$ ft, so there are $(L+1)^2$ "grid points," each of size 1 ft$^2$ in the room. Each grid point is represented by
# $(x, y)$ coordinates, where $x$ and $y$ are both integers.
# 
# - The robot cleans the room by randomly moving from one grid point to another.
# Whenever the robot stops on a grid point, the area around that grid point is
# cleaned. The robot also cleans as it moves, meaning that if it moves from $(x, y) =
# (1, 1)$ to $(x, y) = (1; 3)$, then the points defined by $(x, y) = (1, 1)$, $(1, 2)$, and $(1, 3)$
# have now all been cleaned. The robot starts in the bottom left corner of the room
# $((x, y) = (0, 0))$.
# 
# - The direction and length of each robot movement is determined by two random
# numbers, which are provided in the input argument `rmat`. The first movement is
# determined by the first row of rmat, the second movement is determined by the
# second row, and so on. The first number in each row determines the direction (see
# table below), and the second number in each row determines the length of each
# movement. If all rows of rmat have been used and the robot still has not cleaned
# the entire room, then the values of `rmat` are recycled, starting with the first row.
# For example, if the robot's current position is $(x, y) = (2; 3)$ and the next row in
# `rmat` is `1, 3`, then the robot's next position is $(x, y) = (2, 6)$ (if $L \ge 6$).
# 
# - If a step would cause the robot to hit a wall, then the robot should not take that
# step but instead go to the next row of rmat.

# Write a function `RandomWalk(L, rmat)` that outputs `N, path`,
# where `L` determines the size of the room as described above and `rmat` is a $M$ x $2$
# matrix of random integers 1 through 4, which will tell the robot where to move.
# Your function will output `N`, the number of steps it takes for the robot to cover the
# entire room, as well as `path`, a $(N +1)$ x $2$ matrix where each row contains $(x, y)$
# coordinates of every step. The first row of path will be `0, 0`, and the second row
# will have the $(x, y)$ coordinates of the robot after the first step.
# 
# | Number | Direction |
# |--------|-----------|
# | 1      | up (+y)   |
# | 2      | down (-y) |
# | 3      | right(+x) |
# | 4      | left (-x) |

# You can experiment with the command `something` to see how to generate your own
# matrix of random values. For instance, `randi([1 4], 100, 2)` will give a 100 x
# 2 matrix filled with randomly selected integers between 1 and 4. When testing
# your code, make sure that `rmat` is big enough that the robot doesn't get "stuck"
# in a repeating path that doesn't cover the entire room. The larger `L` you use, the
# more rows rmat should have. Reasonable values for `L` should range from about 5
# to 10, along with a few hundred rows in `rmat`.
# 
# You may also wish to plot the path of the robot to confirm that it has covered
# all the squares in the room. You do not need to submit this plot.
# 
# ## find python equiv

# In[5]:


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


# ## Question 5: Fibonacci and Golden Ratio
# 
# The Fibonacci Sequence can be defined by the recursive relationship $F_N = F{N-1}+F_{N-2}$,
# where the first two numbers of the sequence by convention are $F1 = 0$ and $F2 = 1$. The
# sequence is defined for any positive integer $N$. The Fibonacci sequence can also be
# written using an iterative relationship.
# 
# (a) Using **recursion**, write a function `FibRec(N)` with output `F`,
# that returns the Nth number in the Fibonacci sequence, $F_N$. If the input `N` is not
# a positive integer (positive means that $N > 0$, and integer means the number has
# no fractional component), the output `F` should be the string "N must be a positive integer".
# If the class of the input `N` is not double, the output `F` should be the string:
# "N must be of class double"

# In[6]:


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


# (b) Using a **for loop** (no recursion), write a function `FibIter(N)` that returns `F`, the Nth number in the Fibonacci sequence, $F_N$. If the input `N` is not
# a positive integer (see above), the output `F` should be the string "N must be a positive integer".
# If the class of the input `N` is not double, the output `F` should be the string:
# "N must be of class double"

# In[7]:


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


# (c) Write a function to compute the ratio $r = \frac{F_N}{F_{N-1}}$. Your function `FibRatio(N)` should return `r`,
# where `r` is the ratio defined above for the values of the Fibonacci Sequence defined
# by `N`. If `N` is a not an integer greater than or equal to 2, the output `r` should be the
# string "N must be an integer greater than 1." Your function `FibRatio`
# should call one of the functions from earlier in this problem. Which one you use
# is up to you.

# You do not have to submit any answer to the following questions to complete this
# assignment, but you should think about the answers to improve your understand-
# ing: How does the computational speed of the iterative and recursive functions
# compare? How does the speed of each one change for N = 5; 10; 50? Why do you
# think that is? Compute `FibRatio(N)` for N = 5, 10, 20, 50, and 100. What
# do you notice?

# In[8]:


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


# (d) Actually, $r = \frac{F_N}{F_{N-1}}$ converges to a limit called the Golden Ratio whose exact value
# is $\phi = (1 + \sqrt{5}/2)$
# 
# Write a function `FibApprox(e)` returning `N`, 
# where N is the smallest integer such that $|\phi - \frac{F_N}{F_{N-1}}| \le e$.

# In[9]:


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


# ## Question 6: Number guessing game
# 
# This game begins with player one saying something like, "I'm thinking of an integer between forty and sixty." Following a guess by player two, player one responds
# 'higher', 'lower', or 'correct!' as might be the case. Supposing that `N` is the number
# of possible values (here, twenty-one, since we will consider inclusive intervals), then at
# most $\lfloor \log_2 \rfloor + 1$ questions should be necessary to determine the number, since each
# question can halve the search space.
# 
# Suppose player one selects a number between 1 and 30 to be the "secret number". Since
# player one tells player two whether a guess is too low, too high, or correct, player two
# can start off by guessing in the middle, 15. If the secret number is less than 15, then
# because player two knows that 15 is too high, player two can eliminate all the numbers
# from 15 to 30 from further consideration. If the secret number is greater than 15, then
# player two can eliminate 1 through 15. Either way, player two can eliminate about
# half the numbers. On the next guess, player two again eliminates half of the remaining
# numbers, then keeps going, always eliminating half of the remaining numbers until the
# number is guessed. We call this halving approach a binary search algorithm, and no
# matter which number from 1 to 30 is the secret number, player two should be able to
# find the number in at most 5 guesses with this technique (for the range 1 to 30).
#  
# The function `player1` simulates the actions of player one and has been made available
# to you to help you familiarize yourself with the game. The function has two input
# arguments, nmin and nmax which define the range of possible values. To play the game
# with the range described above, call the function with the command `player1(40, 60)`
# and enter your guesses when prompted. The only output argument of `player1` is
# `N_guess`, which is the number of guesses it took to guess the secret number.
# 
# Your job is to write a **recursive** function that simulates the actions of player two
# in this game. Since the function `player1` requires user interaction in order to run,
# two difierent functions, `player1initialize` and `player1response` have also been
# provided. Note that these functions have been encrypted so they cannot be read or
# edited, but they can be run just like a regular function.
# 
# The function `player1initialize(nmin, nmax)` returns `secret`where `nmin` and `nmax` define the range for the game (just like in `player1`). The output secret is a randomly
# selected secret number from within the specified range, stored in an encrypted form
# which can be read by `player1response`.
# 
# The function `player1response(guess, secret)` returns `msg`. `guess` is a double representing the guess. The input argument `secret` is an encrypted secret number created
# by `player1initialize`. The output `msg` is a string with three potential values:
# 'higher', 'lower', 'correct', which indicate the relationship between the secret
# number and the guessed number. Note that when `player1response` is called it will
# also print a message to the screen telling you if your guess is too high, low or correct,
# to help you keep track of what is going on; `msg` will only have the three possible values
# listed above.
# 
# The function you write is `player2(nmin, nmax, N_guess, secret)`, with output `N_guess`.
# The inputs `nmin` and `nmax` are integers of class double which define the range of the
# game just like before. The input argument `N_guess` represents the number of guesses
# which have taken place. Hint: when you call the function from the command window,
# the input `N_guess` will always be 0 since no guesses have been used yet. Only when
# you make recursive calls will it be different. The input argument secret should be
# taken directly from the output of `player1initialize`. The output argument `N_guess`
# is the number of guesses which was required to guess the secret number.
# 
# Note that the statements printed to the screen are a result of calls to `player1response`
# and do not need to be created by you in your `player2` function. Also note that because
# the secret number is selected randomly in `player1initialize`, your results won't
# exactly match the test cases.

# In[10]:


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

