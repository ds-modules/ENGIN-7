import math
import numpy as np
import cmath
import scipy.io as sio
import matplotlib.pyplot as plt

def q1():
    """
    doctest here
    """
    a, b, c, x = 3., -6., 4., 2.
    E1 = math.sqrt(a*a+b*b+c*c)
    E2 = (-b-cmath.sqrt(b*b-4*a*c))/(2*a)
    E3 = math.log(3*x-a)
    E4 = math.log(3*abs(b)+c/5,10)
    E5 = math.pow(a*x+a*b/c,1./3)
    E6 = (x*x+1)/((a*x-1)*abs(b-math.exp(x)))
    E7 = math.cos(math.sqrt(a)/3*math.pi)**2 + \
         math.cos((math.sqrt(a)/3*math.pi)**2)
    E8 = cmath.exp(cmath.pi*cmath.sqrt(-1))
    E9 = math.acos(math.cos(x))
    E10 = (a+2*c)/(math.sin((b+2*c)/math.sqrt(a**2+b**2+c**2)))

    return E1,E2,E3,E4,E5,E6,E7,E8,E9,E10

def q2():
    # Q2A
    year = list(range(2007,2016))
    wins, losses = [7,9,8,5,7,3,1,5,8], [6,4,2,7,6,9,11,7,5]
    # print(year, wins, losses)

    # Q2B
    losses[2] = 5

    # Q2C
    mat_contents = sio.loadmat('CALFB_HistoricalData.mat')
    # print(mat_contents)
    Y_all = np.append(np.ndarray.flatten(mat_contents['Y']), year)
    W_all = np.append(np.ndarray.flatten(mat_contents['W']), wins)
    L_all = np.append(np.ndarray.flatten(mat_contents['L']), losses)
    # print(Y_all.shape, W_all.shape, L_all.shape)

    # Q2D
    fig, ax = plt.subplots()
    plt.xlabel('Year')
    plt.ylabel('Wins and Losses')
    plt.title('Cal Football Data')
    ax.set_ylim([0,15])
    ax.plot(Y_all, W_all, label='wins', linestyle='dashed')
    ax.plot(Y_all, L_all, label='losses', linestyle='dashed')
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles, labels)
    plt.show()

q2()
