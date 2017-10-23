
# coding: utf-8

# # E7: Introduction to Computer Programming for Scientists and Engineers

# ## Lab Assignment 9

# For each question, you will have to fill in one or more Python functions. We provide an autograder with a number of test cases that you can use to test your function. Note that the fact that your function works for all test cases thus provided does necessarily guarantee
# that it will work for all possible test cases relevant to the question. It is your responsibility
# to test your function thoroughly, to ensure that it will also work in situations not covered
# by the test cases provided

# In[3]:


# Please run this cell, and do not modify the contets
import math
import numpy as np
import matplotlib.pyplot as plt
import cmath
np.seterr(all='ignore')
# %run lab2_ag.py


# ## Question 1: Systems of Linear Equations
#
# Write a function `mySols(A,b)` which returns `x`,
# to solve the system $Ax = b$, where $A$ is a $m \times n$ matrix, $x$ is a $n \times 1$ vector, and $b$ is a
# $m \times 1$ vector.
# - If there is no solution, `x` should be empty (defined as `[]`) and the function should
# display: `"There is no solution"`.
# - If there is one solution, `x` should contain this solution and the function should display:
# `"There is one solution"`.
# - If there is an infinite number of solutions, x should contain one of the solutions and
# the function should display: `"There is an infinite number of solutions"`. Note that the
# solution you show can be different than the one shown below in the test case.

# In[4]:


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
        return np.linalg.solve(A, b)


# ## Question 2: Polynomial derivatives
#
# Let $f(x) = a_0 +a_1x+a_2x^2 +a_3x^3$ be an arbitrary 3rd degree polynomial. If you think about
# it, the coefficients completely determine this polynomial, and so we can package all relevant
# information about $f(x)$ in a convenient column vector form $f = [a_0, a_1, a_2, a_3]^T$ . Why might
# this be convenient? Well, we can represent common operations like differentiation with a
# simple matrix multiplication, as you'll have a chance to show below.

# ### 2.1
#
# Write a Python function `cubicPolyDiff(f)` which returns the tuple `(cubicDf, cubicD)`
# which differentiates an arbitrary $3^{rd}$ degree polynomial $f(x) = a_0 +a_1x+a_2x^2 +a_3x^3$,
# as represented by the input argument `f = [[a0], [a1], [a2], [a3]]`. The output `cubicDf`
# should also be a length 4 column vector, and should be the coefficient vector of the
# polynomial $f'(x)$. The output `cubicD` should be the differentiation matrix, such that
# `isequal(cubicD*f, cubicDf)` evaluates to `true`.

# In[5]:


def cubicPolyDiff(f):
    n = len(f)
    D = np.concatenate(
        (np.zeros((3, 1)), np.diag([x for x in range(1, 4)])), axis=1)
    D = np.concatenate((D, np.zeros((1, 4))), axis=0)
    Df = np.dot(D, f)
    return Df, D


# In[6]:


print(cubicPolyDiff([[1], [2], [3], [4]]))
cubicPolyDiff([[4], [4], [21], [0]])


# ### 2.2
#
# Write a Python function `polyDiff(f)` which returns the tuple `(Df, D)`
# which differentiates an arbitrary $n^{th}$ degree polynomial $f(x) = a_0 +a_1x+a_2x^2+\dots+a_nx^n$,
# as represented by the input argument `f = [[a_0], [a_1], [a_2], ..., [an]]` (the length of
# `f` will be $n + 1$). The output `Df`
# should also be a length $n+1$ column vector, and should be the coefficient vector of the
# polynomial $f'(x)$. The output `D` should be the differentiation matrix, such that
# `isequal(D*f, Df)` evaluates to `true`.

# In[28]:


def polyDiff(f):
    n = len(f)
    D = np.concatenate(
        (np.zeros((n - 1, 1)), np.diag([x for x in range(1, n)])), axis=1)
    D = np.concatenate((D, np.zeros((1, n))), axis=0)
    Df = np.dot(D, f).T
    return Df, D


# In[29]:


polyDiff(np.array([0, 6, 3, 0, 9, 4]).T)


# ### 2.3
#
# Write a Python function `polyDiffm(f, m)` which returns the tuple `(Dmf, Dm)`
# which finds the $m^{th}$ derivative of the arbitrary $n^{th}$ degree polynomial $f(x) = a_0 +a_1x+a_2x^2+\dots+a_nx^n$, as represented by its coefficient vector, `f = [[a_0], [a_1], [a_2], ..., [an]]`
# (the length of
# `f` will be $n + 1$). The output, `Dmf` should also be a length $n + 1$, and
# should be the coefficient vector of the polynomial $f^m(x)$. The output, `Dm` should be
# the $m^{th}$ derivative matrix, such that `isequal(Dm*f, Dmf)` evaluates to `true`.
#
# [Hint: use your function `polyDiff` to solve this problem].

# In[81]:


def polyDiffm(f, m):
    D = polyDiff(f)[1]
    Dm = np.linalg.matrix_power(D, m)
    Dfm = np.dot(Dm, f)
    return Dfm, Dm


# In[84]:


polyDiffm(np.array([0, 6, 3, 0, 9, 4]).T, 2)


# ## Question 3: Regression and model selection
#
# In engineering, model selection is the task of selecting a model among a set of candidate
# models, given a data set. This is really useful for linking a series of observations to a
# mathematical model predicting these observations.

# ### 3.1: Linear law
#
# First, we will consider observations derived from a linear model:
#
# $$y = ax$$
#
# Where $x$ and $y$ are some observable input and output, respectively, and $a$ is a coefficient to
# be determined from the observations.
#
# Write a function with header
# function `myLinearRegression(x,y)` returning the tuple `(a, RMSE)`
# that performs linear regression with inputs `x` and `y`, each of which is a column vector of
# class double. The output `a` is a scalar double which represents the best estimate for the
# coefficient `a` in Equation 1. `RMSE` is a scalar double which represents the root mean square
# error (RMSE), which is a measure of how good the fit is (the lower the RMSE, the better)
# and is calculated as follows:
#
# $$RMSE = \sqrt{\frac{1}{m} \sum_{i=1}^m (\hat{y}_i - y_i)^2}$$
#
# where $m$ is the number of points in the data set, and $\hat{y}_i$ is the estimation of $y_i$ (in this case,
# $ax_i$). To visualize the performance of your function, you can plot the data points and the
# estimation results your function outputs (see image below).
#
# You will test out your function with data related to Ohm's law, which is an example of
# such a linear law: $V = IR$, where $V$ is the voltage (in volts), $R$ the resistance (in ohms)
# and $I$ the current (in amperes). Using measurements of $I$ and $V$ contained in the `Ohm.mat`
# file, your function will find the conductance $G$ (the inverse of the resistance) using the data
# from this example electrical circuit. Your function should work on any set of data in the
# appropriate format.

# In[70]:


def myLinearRegression(x, y):
    # print(x,y)
    a = np.linalg.lstsq(x, y)
    # print(a)
    m = len(y)
    yhat = a * x
    # print(yhat[0])
    tmp = (yhat - y)**2
    print(tmp)
    print(tmp[0][3])
    RMSE = math.sqrt((1 / m) * tmp)
    return yhat, RMSE


# In[71]:


myLinearRegression(np.array([[2], [3]]), np.array([[2], [5]]))


# ### 3.2 General Model
#
# In this problem, we will consider observations to be derived from a general model:
#
# $$y = af_1(x) + bf_2(x) + c$$
#
# where the possible models are one of three options:
# 1. $f_1(x) = sin(x), f_2(x) = cos(x)$
# 2. $f_1(x) = x^2, f_2(x) = x$
# 3. $f_1(x) = \exp(x), f_2(x) = 0$
#
# Write a function `myBestRegression(x,y)` which returns the tuple `(a, b, c, modelNum)`
# where inputs `x` and `y` are column vectors of class double of observed data pairs. Your function should estimate `a`, `b`, and `c` from the general model equation for all three models listed above. Your
# function should also compute RMSE for the best fit from each of the three models. Finally,
# your function should select the best model (the one with the lowest RMSE), and return
# the three coefficients for that model, as well as identifying the best model with the output
# `modelNum`. `modelNum` is a scalar double with a value of 1, 2, or 3 corresponding to the best model from the list above. Note that for model 3, there is no coefficient $b$. If model 3 is the
# best model, the output `b` should be a scalar double whose value is zero.
#
# <img src="resources/E7_Lab9_1.jpg" style="width: 500px;"/>
# <center>*Figure 1: Ohm's law and linear regression*</center>
#

# Your function should work for any dataset involving two column vectors (`x` and `y`). Two
# example datasets can be found in the files `Projectile.mat` and `Pendulum.mat` found on
# bCourses.
#
# `Projectile.mat` contains observations of the position $(y)$ of a projectile along with the
# time of each observation $(t)$. We know projectile motion is governed by the equation $y(t) = -\frac{1}{2}gt^2 +v_0t+y_0$, and hence your function should be able to determine that model 2 is best,
# and provide estimates of $-\frac{g}{2}$, $v_0$, and $y_0$ (outputs `a`, `b`, `c`).
# 2 , v0, and y0 (outputs a, b, and c). Note that notation $y = f(x)$
# is used to describe the general relationship between model inputs and outputs, even though
# the variables can have different names (in this example we have $y = f(t)$).
#
# `Pendulum.mat` contains observations of the angle of a pendulum as observed at different
# points in time ($\theta = f(t)$). We know pendulum motion is governed by the equation $\theta(t) = a \sin(t) + b \sin(t) + \theta_0$, and hence your function should be able to determine that model
# number 1 is best, as well as provide estimates for $a$, $b$, and $\theta_0$.
#
# One example of the third model listed above is the calculation of compound interest.
# Compound interest at a constant interest rate $r$ provides exponential growth from the initial
# capital $x_0$: at a time $t$, the current value $x(t)$ is given by $x(t) = x_0(1 + r)^t = x_0 * e^{t \ln(1+r)}$.
#
# You are not provided with a dataset for this example. You are encouraged to create your
# own dataset and use it to test your function's ability to fit model 3 above.

# In[ ]:


def myBestRegression(x, y):
    pass

# In[ ]:

myBestRegression()


# ## Question 4: Stream flow recession analysis and over-determined systems
#
# Perhaps the most convenient feature in Python is the backslash operator, '\'. In this
# problem, we will use the backslash operator to solve an over-determined system and fit a
# well known model to some stream
# flow data.
#
# When rain falls on a watershed, water storage in the landscape increases and stream flow
# levels generally increase. Soon after rain stops falling, the discharge levels in streams will decline in a process known as the stream
# flow recession. Below is a plot of the volumetric
#
# flowrate (discharge) during and after a single rainfall event, from the Middle Fork of the Eel
# River in northern California. Notice that the discharge starts off rather slowly, peaks, then
# recedes gradually.
#
# <img src="resources/E7_Lab9_2.jpg" style="width: 600px;"/>
# <center>*Figure 2: Recession event from the Middle Fork of the Eel River, CA in 2011*</center>
#

# One of the most popular mathematical models for the stream
# flow recession is the so-called
# 'power-law' recession model, which defines the **rate of decline of stream
# flow** (i.e. the derivative of stream flow) as:
#
# $$-\frac{dQ}{dt} = aQ^b \;\;(3)$$
#
# Although you will not be required to obtain the solution of such an equation yourself, it can be solved to yield a highly nonlinear function for the form of the stream flow recession:
#
# $$Q(t) = \Bigg[(b-1)\Big( \frac{Q^{1-b}_0}{b-1} + at \Big)\Bigg]^{\frac{1}{1-b}} \;\; (4) $$
#
# where $Q_0$ is the initial stream
# flow value on the first day of the recession. Instead of attempting
# to fit this nonlinear model to stream
# ow data, many researchers will instead go back to
# Equation 3 and log transform the relationship:
#
# $$-\frac{dQ}{dt}=aQ^b \implies \log\big(-\frac{dQ}{dt}\big)=\log a+b\log Q \;\;(5)$$
#
# As you can see, if you were to plot $\log(-\frac{dQ}{dt})$ vs. $\log Q$, the result would be a linear function
# with a slope of $b$ and a y-intercept of $\log a$.
#
# To find $a$ and $b$ using Python we will perform four steps:
#
# 1. Compute a collection of
# values of the derivative, or time rate of change, of the discharge
# 2. Construct and solve an
# over-determined system of equations, which will tell us the best fit values for $a$ and $b$
# 3. Determine how good the fit is by calculating $R^2$
# 4. Plot the best fit equation on top of
# the stream flow recession data.

# ### 4.1
#
# For this problem, assume you are given $N$ daily stream
# flow recession values, $Q(0), Q(1), Q(2),\dots, Q(N - 1)$, represented in Python as a column vector discharge
# with $N$ entries. You can find a sample stream
# ow recession time series in the file
# `discharge.mat`, located in the assignment directory (this recession is the decreasing
# segment in the figure above).
#
# The first entry of discharge, $Q(0)$, represents
# flow on
# the first day, when $t = 0$, $Q(1)$ on the second day when $t = 1$, and so on.
#
# Write a function `getDerivative(discharge)` returning the tuple `(dQdt avgQ)`, a vector of values of the derivative, or the time rate of change, of discharge,
# and the discharge values corresponding to each computed value of the derivative.
#
# As an approximation for the derivative on day $t = \tau$ , your function should compute the
# following:
#
# $$\frac{dQ(\tau)}{dt} = \frac{Q(\tau + 1) - Q(\tau)}{(\tau + 1) - (\tau)} = Q(\tau + 1) - Q(\tau) \;\;(6)$$
#
# where the simplification in the denominator can be made because $t$ is in given in one day intervals. You should note that the length of the vector $\frac{dQ}{dt}$ will be $N - 1$, instead
# of $N$. Your function will also return the two day average of discharge (`avgQ`) for each
# computed value of $\frac{dQ}{dt}$ , that is:
#
# $$Q_{avg}(\tau) = \frac{Q(\tau+1)+Q(\tau)}{2}\;\; (7)$$
#
# which is also of length $N-1$. (Doing this simply stores the discharge at the temporal midpoint where the derivative is calculated so that $Q$ and $\frac{dQ}{dt}$ are computed at the
# same point in time.)

# In[72]:


def getDerivative(discharge):
    dQdt = discharge[1:] - discharge[0:-1]
    avgQ = (discharge[1:] + discharge[0:-1]) / 2.
    return dQdt, avgQ


# In[73]:


getDerivative()


# ### 4.2
#
# Now, let's set up the over-determined system of equations that we will solve to get the parameters of our recession model, $a$ and $b$.
#
# For each day, $t = \tau$ , we will have a single equation
#
# $\log a + b \log (Q_{avg}(\tau)) = \log \Big( -\frac{dQ(\tau)}{dt} \Big) \;\; (8)$
#
# Yielding a total of $N - 1$ equations for only two unknowns, $a$ and $b$. How can we
# convert the above system of equations into a single matrix equation? Well, the two
# unknowns we are looking to find are $b$ and $\log a$, and so we can call our vector of
# unknowns $x = \begin{bmatrix} \log a \\ b \end{bmatrix}$.
#
# Next, we need the right hand side (RHS) of the equation in vector form, which will be
#
# $$y = \begin{bmatrix} \log \big( -\frac{dQ(0)}{dt} \big) \\
#                       \log \big( -\frac{dQ(1)}{dt} \big) \\
#                       \vdots \\
#                       \log \big( -\frac{dQ(N-2)}{dt} \big) \end{bmatrix}$$
#
# Finally, to connect the left and right hand sides, we set up the full equation:
#
# $$\mathbf{Ax} = \begin{bmatrix} 1 & \log(Q_{avg}(0)) \\
#                        1 & \log(Q_{avg}(1)) \\
#                        \vdots & \vdots \\
# 1 & \log(Q_{avg}(N-2)) \big) \end{bmatrix}\mathbf{x} = \mathbf{y}$$

# Clearly such a system will generally be over-determined; there are more equations than
# unknowns. However, Matlab's backslash operator is smart! It automatically knows how
# to solve over-determined systems using least squares methods.
#
# In Matlab, the solution (in a least squares sense) to an equation like
# the system above is simply `x = A \ y`.
#
# For this second part, write `getRecessionParams(discharge)` returning the tuple `(a b)`, the power law recession parameters $a$ and $b$. You should use the function
# `getDerivative` from the previous question (make sure to carefully double check that it
# works before using it for this function).
#
# Inside the function `getRecessionParams`, you
# should set up the matrix equations demonstrated above and use the backslash operator
# to find the solutions, $\log a$ and $b$. Note that your function should return the values $a$
# and $b$, and so you will need to transform $\log a$ into a using the
# identity, $a = e^{\log a}$.

# In[74]:


def getRecessionParams(discharge):
    dQdt, avgQ = getDerivative(discharge)
    y = log(-dQdt)
    A = np.concatenate(
        (np.ones(
            len(discharge) - 1,
            1),
            math.log(avgQ)),
        axis=0)
    x = np.solve(A, y)

    a = math.exp(x[0])
    b = x[1]
    return a, b


# In[ ]:


getRecessionParams()


# If you read section 13.2 in your textbook closely, you'll see that solving the over-determined system in the previous part is exactly the equivalent of performing a linear regression. Essentially, you fit the data with a best fit linear function of the form:
#
# $$\log\Big(-\frac{dQ}{dt}\Big)=\log a + b \log Q \;\;(11)$$
#
# You can think of $\log(-\frac{dQ}{dt})$
# as the dependent variable ($y$), $\log Q$ as the independent
# variable ($x$), $\log a$ as the y-intercept of the best fit line, and $b$ as the slope.
#
# For any modeling exercise, it's good practice to report some measure of 'goodness of fit', that is, how well your model performs. There are a number of different measures
# of goodness of fit, but one of the most popular for linear regression is the coefficient of
# determination, commonly referred to as $R^2$.
#
# In practical terms, $R^2$ is simply a measure of how much better your best fit linear
# function is than a best fit constant function, or mean model, $y = \text{mean}(y_{data})$. $R^2$ is
# computed with the following equation:
#
# $$R^2=1-\frac{SSE_{linear\;model}}{SSE_{mean\;model}}\;\;(12)$$
#
# where $SSE_linear\;model$ is the sum of squared errors of the linear model, and $SSE_{mean\;model}$
# is the sum of squared errors of the mean model. Sum of squared errors is simply the
# sum of the squares of the differences between the model and the data. Looking at the
# equation for $R^2$, you can see that the smaller the errors of the linear model relative to
# the mean model, the closer $R^2$ will get to 1. So, the perfect linear fit has an $R^2 = 1$.
#
# To illustrate, consider the very simple dataset,
# `xdata = [1, 2, 3, 3.5]; ydata = [1.2, 3, 2.8, 3.9]` (blue points below).
#
# Also plotted below are both the best fit linear model (using linear regression) and the
# best fit mean model to the data:
#
# <img src="resources/E7_Lab9_3.jpg" style="width: 600px;"/>
# <center>*Figure 3: Linear model fit vs. constant (mean) model fit*</center>

# The individual errors are simply the vertical lengths of the fine black lines, representing
# the distance from the data to each model. In this case, the sum of squared errors can
# be computed as:
#
# $$ \begin{align} SSE_{linear\;model} &= e_{L1}^2 + e_{L2}^2 + e_{L3}^2 + e_{L4}^2 & (13) \\
# SSE_{mean\;model} &= e_{M1}^2 + e_{M2}^2 + e_{M3}^2 + e_{M4}^2 & (14) \end{align} $$
#
# Therefore, $R^2 = 1 - \frac{SSE_{linear\;model}}{SSE_{mean\;model}} = 0.8095$. Give it a try and see if you get the same
# numbers.
#
# For this part, you will write a function `rsquaredRecessionModel(discharge)`
# to compute the $R^2$ goodness of fit of your stream
# flow recession model. Note, for
# the data points in your $R^2$ calculation, you should use the variables `dQdt` and `avgQ`
# outputted from the function `getDerivative(discharge)`. Also, you should find
# the $R^2$ value for the *linear* fit in log-log space, that is, find
# $R^2$ for the fitted line $\log (-\frac{dQ}{dt}) = \log a + b \log Q$;
# while it is possible to compute an $R^2$ value for the non-linear form
# of the model (Equation 4), we will not do that here.

# In[75]:


def rsquaredRecessionModel(discharge):
    a, b = getRecessionParams(discharge)
    dQdt, avgQ = getDerivative(discharge)

    yhat = math.log(a) + b * math.log(avgQ)
    y_mean = mean(log(-dQdt))

    SSE_lin = sum((yhat - log(-dQdt))**2)
    SSE_mean = sum((math.log(-dQdt) - y_mean)**2)

    rsq = 1 - (SSE_lin / SSE_mean)

    return rsq


# In[ ]:


rsquaredRecessionModel()


# ### Question 4.4
#
# For the final part of this problem, you will write the function `plotRecessionModel(a, b, discharge)`
# which will take a pair of recession parameters (`a` and `b`), a discharge time series
# (`discharge`), and plot the recession model on top of the discharge data. You should
# pair Equation 4 with the recession parameter values to plot the model. The function
# should also include the values of the recession parameters in the plot title. Note that
# $Q_0$ in Equation 4 will simply be the first element in the vector discharge, and the
# independent variable $t$ will be a simple length $N$ vector, $time = 0:(N-1)$.
#
# For the
# test case above, your `plotRecessionModel` function should generate a plot similar
# to the one below. Although it does not need to look exactly the same (you can choose
# different colors, markers, etc), you should properly label your axes, the legend, and the
# title.
#
# <img src="resources/E7_Lab9_4.jpg" style="width: 400px;"/>
# <center>*Figure 4: Power law recession model fitted to discharge data.*</center>

# In[ ]:


def plotRecessionModel(a, b, discharge):
    N = len(discharge)
    Q = ((b - 1) * (discharge[0]**(1 - b)) / (b - 1) + a * t)**(1 / (1 - b))


# In[ ]:


plotRecessionModel(a, b, discharge)
