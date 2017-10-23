
# coding: utf-8

# # E7: Introduction to Computer Programming for Scientists and Engineers

# ## Lab Assignment 8

# For each question, you will have to fill in one or more Python functions. We provide an autograder with a number of test cases that you can use to test your function. Note that the fact that your function works for all test cases thus provided does necessarily guarantee
# that it will work for all possible test cases relevant to the question. It is your responsibility
# to test your function thoroughly, to ensure that it will also work in situations not covered
# by the test cases provided

# In[1]:


# Please run this cell, and do not modify the contets
import math
import numpy as np
import matplotlib.pyplot as plt
np.seterr(all='ignore');
# %run lab2_ag.py


# ## Question 1: Linear Systems: the Basics
# 
# ### 1.1: Solving Linear Systems
# 
# Shown below is a linear system of 3 equations with 3 unknowns, $x_1$, $x_2$, and $x_3$. The scalar
# quantities $a_{ij}$ and $b_i$ can be assumed known. Under certain conditions (which we will explore
# later), there is a unique solution for $x_1$, $x_2$, and $x_3$. Here we will assume that these conditions
# are met, so you don't have to check them.
# 
# $$ \begin{align}
# a_{11}x_1 + a_{12}x_2 + a_{13}x_3 &= b_1 \\
# a_{21}x_1 + a_{22}x_2 + a_{23}x_3 &= b_1 \\
# a_{31}x_1 + a_{32}x_2 + a_{33}x_3 &= b_1 
# \end{align} $$
# 
# Your job is to write a function `myLinearSolver(A1, b1, A2, b2, A3, b3)`
# where `A1` is a 1 x 3 double containing the three coeffficients for equation 1 ($a_{11}, a_{12}, a_{13}$) and
# `b1` is a scalar double representing $b_1$, the right-hand-side of equation 1. Similarly, `A2` and `A3`
# are 1 x 3 doubles containing the coefficients of equations 2 and 3, respectively. `b2` and `b3`
# are scalar doubles representing the right-hand-sides of equations 2 and 3, respectively.
# Your function should have 3 outputs `x1`, `x2`, and `x3`. Each output should be a scalar
# double. Together, the outputs `x1`, `x2`, and `x3` represent the solution $(x_1, x_2, x_3)$ to equations
# 1-3 above.
# 
# Your function should use the backslash n operator exactly once. Hint: This function
# can be completed in as few as 6 lines, not counting comments, header, and "end". You may
# assume that the inputs are of the appropriate class and size.

# In[ ]:


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


# ### 1.2 Matrix Inversion
# 
# Write a function `matInv(A)`
# that returns the inverse of the matrix $A$, i.e., the matrix $B$ such that $AB = I$, where $I$ is the
# identity matrix. If $A$ is not square or the determinant of $A$ is within $0 \pm 10^{-10}$, the function
# should return the empty list `[]`.

# In[ ]:


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


# ## Question 2: Linear Systems: Circuits
# 
# In this question, we will look at how to model an electric circuit using a system of linear
# equations to solve for the currents in different parts of the circuits.
# 
# Fig 1. A circuit with two resistors in series | Fig 2. A circuit with two resistors in parallel
# - | -
# ![](resources/E7_Lab8_1.jpg) | ![](resources/E7_Lab8_2.jpg)
# 
# There are two types of simple circuits, series and parallel, as shown above. $R_A$ and $R_B$
# denote the resistance of resistor $A$ and $B$, respectively. $R$ denotes the overall resistance,
# and $V$ denotes the voltage difference across the battery. $I_A$ and $I_B$ are the current 
# owing
# through $A$ and $B$, respectively, and $V_A$ and $V_B$ are the voltage differences across $A$ and $B$.
# To analyze a circuit, you start at one point in the loop and "advance" until you are back
# where you started. We will guide you through the setup of the equations you need to solve.
# The following relationships apply to this circuit in series (Figure 1):
# 
# $R = R_A + R_B$ (total resistance is the sum of the two resistors)
# 
# $I_A = I_B$ (the current through resistor $A$ is the same as through $B$)
# 
# $V = V_A + V_B = I_AR_A + I_BR_B$ (the voltage difference across the battery is
# equal to the sum of voltage differences across resistors $A$ and $B$)
# 
# Notice that voltage is equal to the product of the resistance and the current ($V = IR$).
# The following relationships apply to this circuit in parallel (Figure 2):
# 
# $ \frac{1}{R} = \frac{1}{R_A} + \frac{1}{R_B} $ (the resistances are now inversely related)
# 
# $V = V_A = V_B = I_AR_A = I_BR_B$ (the voltage difference across the battery is
# equal to the voltage difference across each resistor)
# 
# For more on serial and parallel circuits, see links [here](http://www.allaboutcircuits.com/textbook/direct-current/chpt-5/simple-series-circuits/) and [here](http://www.allaboutcircuits.com/textbook/direct-current/chpt-5/simple-parallel-circuits/).

# As an optional first step, you can solve for the currents $I_A$ and $I_B$ in these simple circuits
# by hand, for the values given here: $R_A = 3$, $R_B = 6 $, $V = 9 V$. Practice setting up
# the matrix that goes along with the equations, and see if your matrix solver from question
# 1 gives you the same answer you worked out by hand. You should find that for the circuit
# in series (Figure 1), $I_A = I_B = 1 A$, and for the circuit in parallel (Figure 2), $I_A = 3 A$,
# $I_B = 1.5 A$ (where A denotes the unit amperes).
# 
# Now you are given a more complicated circuit, shown in Figure 3. Don't worry if you
# have not encountered circuits before. You should ask for help for the physics, since physics is not the main point of the question. You are to write a function that solves for the currents
# specifically in this circuit, `MyCircuit(V, R1, R2, R3, R4, R5, R6, R7, R8)`. Return the eight currents through resistors 1 to 8, in amperes. $V$ is the battery's voltage, in volts, and $R$'s are the resistances in ohms.

# Hint: Before you start coding, use a pencil and paper to write out a system of equations. Then, also with pencil and paper, rearrange the system of equations into the form $Ax = b$,
# creating the appropriate matrix $A$ (which is a square matrix), and solution vector $b$ (which
# is a column vector). Note the order of the outputs of the function: $I_4$ and $I_8$ are not output
# because they are equal to $I_1$.
# 
# <img src="resources/E7_Lab8_3.jpg" style="width: 400px;"/>
# <center>*Figure 3: MyCircuit*</center>
# 
# Perspective: this problem shows the benefit of programming. Without a computer,
# you would need to solve a large algebraic system over again any time one of the 9 input values changed (voltage or resistance). Using Python, you can formulate the equations
# once, write one function, and solve for any variation with only one command.

# In[ ]:


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


# ## Question 3: Foot Finding: Methods
# 
# ### 3.1: Newton's Method
# 
# Write a function `myNewton(f, df, x0, tol)`
# where `f` is a function handle representing the function $f(x)$, `df` is a function handle to the
# derivative of $f$, `x0` is an initial estimate of the root, and `tol` is a strictly positive scalar double.
# The function should return a row vector `R` of class double, where `R(1)` is the initial estimate
# `x0`, and `R(k+1)` is the estimate of the root of $f$ after $k$ iterations in the Newton Method.
# 
# The function should also return the absolute error in a row vector `E`, of class double, where
# `E(k)` is the value of $\lvert f(R(k)) \rvert$. The function should return when `E(end) < tol` or after 100
# iterations have been performed. If $N$ iterations of Newton's method have been performed,
# the outputs should each have $N +1$ elements. You may assume that the derivative of `f` will
# not be 0 during any iteration for any of the test cases given. 
# 
# Do not use built-in functions to find the roots. Do not use a while loop.

# In[ ]:


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


# ### 3.2: Bisection Method
# 
# Write a function `myBisection(f, a, b, tol)`
# where `f` is a function handle, `a` and `b` are scalars such that `a < b`, and `tol` is a strictly
# positive scalar value. The function should return a row vector, `R` of class double, where
# `R(k)` is the estimation of the root of `f` after $k$ iterations of the bisection method. The first
# element of `R` should be the midpoint of the interval defined by the inputs a and b, and counts
# as the first step of the bisection method. 
# 
# The function should also return a row vector `E`
# of class double, where `E(k)` is the value of $\lvert f(R(k)) \rvert$. The function should return when
# `E(k) < tol` or after 100 iterations have been performed. If $N$ iterations of the bisection
# method are performed, the outputs should each have $N$ elements. You may assume that
# `sign(f(a)) = - sign(f(b))` for the first guess. (When you are testing your function, it
# will help to plot your function first, so you can pick appropriate values to bracket the root.)
# 
# **Note**: The inputs `a` and `b` constitute the first iteration of bisection, and therefore `R` and `E`
# should never be empty. 
# 
# Do not use built-in functions to find the roots. Do not use a while loop.

# In[ ]:


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


# ### 3.3: Further Exploration (Optional)
# 
# In this question you explored two iterative root finding methods. Each of these functions
# provides a series of $x$ values as the computer "zooms in" on the root. Experiment with
# different types of functions as well as different initial intervals and estimates, and see how
# the different root finding methods behave. Do they always converge? How quickly do they converge?
# 
# To get started, try entering the following:
# 
# ```MATLAB
# f = @(x) x.ˆ3 􀀀 3*x 􀀀 5;
# df = @(x) 3*x.ˆ2 􀀀 3;
# [rn, en] = myNewton(f, df, 3, 1e􀀀4);
# [rb, eb] = myBisection(f, 1, 3, 1e􀀀4);
# x = 2:0.1:3;
# plot(x,f(x),'r􀀀', rn,f(rn),'bo', rb,f(rb),'go')
# ```
# 
# You should see "linear convergence" for one method and "quadratic convergence" for the other (quadratic meaning that the number of correct decimal places approximately doubles with each iteration). You may want to use a log plot. This section will not be graded, but
# completing it and thinking about the concepts will help improve your understanding of root finding.

# ## Question 4: Root Finding: Fractal generation
# 
# In this question, we are exploring root finding on the complex number plane. A complex number can be written as:
# 
# $z = x + yi$
# 
# where $x$ and $y$ are two real numbers, $i$ is the imaginary number such that $i^2 = -1$, and $z$ is
# a complex number. Note that $x$ is the real part of $z$ and $y$ is the complex part of $z$.
# 
# Complex number calculations work similarly to real numbers. Below are four examples
# using $z_1$ and $z_2$ for addition, subtraction, multiplication, and division (to help refresh your
# memory):
# 
# $$ \begin{align}
# z_1 &= 1 + i \\ 
# z_2 &= 3 - 2i \\
# z_1 + z_2 &= 1 + i + 3 - 2i = 4 - i \\
# z_1 - z_2 &= 1 + i - (3 - 2i) = -2 + 3i \\
# z_1z_2 &= (1 + i)(3 - 2i) = 3 - 2i + 3i - i(2i) = 3 + i - 2(i^2) = 3 + i - 2(-1) = 5 + i \\
# \frac{z_1}{z_2} &= \frac{1+i}{3-2i} = \frac{(1+i)(3+2i)}{(3-2i)(3+2i)} = \frac{3+2i+3i-2}{9+6i-6i-4i^2} = \frac{1+5i}{13} = \frac{1}{13} + \frac{5}{13}i
# \end{align}$$
# 
# Complex numbers can be roots to a polynomial. For instance, for the equation:
# 
# $$\begin{align} z^3 + 1 &= 0 \\
# z^3 &= -1 && (7) \end{align}$$
# 
# the solutions are: $z_1 = -1$, $z_2 = \frac{1}{2} + \frac{\sqrt{3}}{2}i$, and $z_3 = \frac{1}{2} - \frac{\sqrt{3}}{2}i$. (Try plugging $z_1$, $z_2$ and $z_3$ back
# into the equation to check for yourself).

# ### 4.1: Exact complex solutions to a polynomial equation
# 
# In this section, you will learn how to solve for the exact complex solutions to a polynomial in the form of Eq. 8:
# 
# $$ z^d = 1 \;\;\; \text{(8)} $$
# 
# where $d$ is a positive integer. Eq. 8 has $d$ roots. For any complex number, we can transform it into the polar form:
# 
# $$ z = x + iy = \lvert z \rvert (cos \phi + i sin \phi) = re^{i\phi} $$
# 
# where $x = Re(z)$, the real part of the complex number $z$; $y = Im(z)$, the imaginary part of $z$; $r = \lvert z \rvert = \sqrt{x2 + y2}$, the magnitude of $z$; and $\phi = arg(z)$, the angle in radians between
# the x axis on a complex plane and the vector made by $z$. For instance, when $r = 1$, Figure 4
# shows the argument $\phi$.
# 
# ![](resources/E7_Lab8_4.jpg)
# *Figure 4: $z = x + iy = re^{i\phi}$ on a complex plane. Image from https://sites.google.com/site/greatmathmoments/identity.*
# 
# Rewriting Eq. 8 in the exponential form, we have:
# $$\begin{align} (re^{i\phi})^d &= e^{2\pi ni} \\
# r^d (e^{i(\phi d)}) &= (1)e^{2\pi ni} && (10) \end{align}$$
# 
# where $n$ equals $0, 1, 2, 3, \dots, d - 1$. Eq. 10 gives us $r^d = 1$ and $\phi d = 2\phi n$. Therefore, $r = 1$ and $\phi = \frac{2\pi}{d}n$. 
# 
# So the solutions to Eq. 8 are: $1, e^{i \frac{2\pi}{d}}, e^{2i \frac{2\pi}{d}}, e^{3i \frac{2\pi}{d}}, \dots, e^{i 2\pi \frac{d-1}{d}}$. 
# 
# To practice solving complex polynomial with the polar form, let's look at the polynomial $z_3 = -1$ again (Equation 7). To solve this equation using the polar form, we have:
# 
# $$\begin{align} z^3 &= -1 \\
# (re^{i\phi)})^3 &= e^{(2n+1)\pi i} && (11) \end{align}$$
# 
# where $n$ equals $0,1,2$. Therefore:
# 
# $$\begin{align} r^3 &= 1 \\
# 3\phi = (2n+1)\pi \end{align}$$
# 
# Solving for $r$ and $\phi$:
# 
# $$\begin{align} r &= 1 \\
# \phi &= \frac{2n+1}{3}\pi && (12) \\
# &= \frac{1}{3} \pi, \pi, \frac{5}{3}\pi \end{align}$$
# 
# Therefore, the solutions to $z^3 = -1$ are: $z_1 = e^{i \frac{1}{3} \pi} = -\frac{1}{2} + \frac{\sqrt{3}}{2}i$,  $z_2 = e^{\pi i} = -1$, and $z_3 = e^{i \frac{5}{3} \pi} = -\frac{1}{2} - \frac{\sqrt{3}}{2}i$

# For another example, let's look at the polynomial $z^5 = 1$. To solve this equation using the polar form, we have:
# 
# $$\begin{align} z^5 &= 1 \\
# (re^{i\phi})^5 &= e^{(2n)\pi i} && (13) \end{align}$$
# 
# where $n$ equals 0,1,2,3,4. Therefore:
# 
# $$\begin{align} z^5 &= 1 \\
# 5\phi &= (2n)\pi \end{align}$$
# 
# Solving for $r$ and $\phi$:
# 
# $$\begin{align} r &= 1 \\
# \phi &= \frac{2n}{5}\pi && (14) \\
# &= 0, \frac{2}{5} \pi, \frac{4}{5} \pi, \frac{6}{5} \pi, \frac{8}{5} \pi \end{align}$$
# 
# Therefore, the solutions to $z^5 = 1$ are:
# 
# $$\begin{align}
# z_1 &= e^{i0} = 1 + 0i \\
# z_1 &= e^{i\frac{2}{5}\pi} = 0.309 + 0.9511i \\
# z_1 &= e^{i\frac{4}{5}\pi} = -0.809 + 0.5878i \\
# z_1 &= e^{i\frac{6}{5}\pi} = -0.809 - 0.5878i \\
# z_1 &= e^{i\frac{7}{5}\pi} = 0.309 - 0.9511i 
# \end{align}$$

# Now that you know how to solve complex polynomial, write a function `PolynomialExactSolutions(d)`,
# where `d` is the order of the polynomial from Eq. 8. Your function should output an array of
# `d` elements that contain the complex solutions to Eq. 8.
# Note: You need to find $\phi$ for $n = 0,1,2,\dots$ using the pattern given above, then transform the
# polar form to rectangular form ($z = x + yi$). You are not allowed to use any root-finding
# Python functions in the function `PolynomialExactSolutions(d)`. Your function should output the roots in order, as seen in the test cases below.
# 
# ```Python
# >>PolynomialExactSolutions(9)
# ```
# 
# <img src="resources/E7_Lab8_5.jpg" style="width: 300px;"/>

# In[ ]:


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


# ### 4.2: Convergence using Newton's Method
# 
# Different starting points on a complex plane, when chosen as the initial guess to Newton's
# method, will converge to different roots. In this section, even though we know the roots to
# a complex polynomial, we are trying to see whether Newton's method can reach a root in a
# given number of iterations, and if yes, which roots these different initial guesses will converge
# to.
# 
# Now pick any point on a complex plane, $z$, use it as the initial guess to a root of Eq. 8,
# and apply Newton's method n times on the complex plane $z$. Write a function `NewtonConv(d, z, n, tol)`
# where `d` is the order of the polynomial from Eq. 8, `z` is a complex number as the initial guess,
# `n` is the number of iterations for which we apply Newton's method, and `tol` is the tolerance which determines if the output has converged after `n` iterations of Newton's method. 
# 
# Your function should return a tuple, `(ConvergeOrNot, ConvergeToRoot)`. If the iteration result is within tolerance of a certain root, `ConvergeOrNot` equals 1, and
# `ConvergeToRoot` is the root it's converging to; if the iteration result is not within tolerance
# of any roots, `ConvergeOrNot` should be 0, and `ConvergeToRoot` is `NaN`. All output should
# be of class double.
# 
# Hint: Call the function `PolynomialExactSolutions` you wrote to generate an array
# containing the true roots. Since `NewtonConv` relies on `PolynomialExactSolutions`, be extra careful to check that it works correctly before you start `NewtonConv`!

# In[ ]:


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


# ### 4.3: Newton Fractal
# 
# As you can see from the function `NewtonConv`, different starting points $z$ will converge to
# different roots. You can color the points on the complex plane according to which root of
# the polynomial each of them converge to. This will generate a Newton fractal. You can
# Google "Newton Fractals" and look at the pretty pictures. Here you will write a function
# to generate your own Newton's fractal for polynomials like Eq. 8. 
# 
# Write the function `NewtonFractal(d,n,tol,res,ULcorner,sqrL)` where `d`, `n`, and `tol` are as defined in the function `NewtonConv`, `res` is a scalar double indicating the total number of points in the $x$ and $y$ axis of your plot (resolution), `ULcorner` is a 1-by-2 double array containing the x and y coordinates of the upper-left corner of your
# plot's domain, and `sqrL` is the length of the square which makes up your domain (your
# domain will always be a square). (An example domain is illustrated in Figure 6.)
# 
# <img src="resources/E7_Lab8_6.jpg" style="width: 300px;"/>
# <center>*Figure 6: The example domain created by input ULcorner=(-1.5,1.5), sqrL=2.5, res=6.*</center>

# Your function will output two things: a res-by-res matrix containing values $1,2,3,\dots,d$
# that refer to which root a point in the plotting domain converges to, or 0 for a point which
# does not converge to any root. Your function will also output a square image of length sqrL
# of this matrix, with 0 colored white. You can define the colors of other values $(1,2,3,\dots,d)$
# to your own liking. Your *output* has to match the rule of assignment given in the guide
# below; your plot should have the same title structure, domain size, and axis labels, but it
# does not need to have the same color scheme.
# 
# Your plot will show the range of your $x$ and $y$ axes, and have a title indicating `d`, `n`, `tol`,
# and `res`. Refer to Figure 7 and 8 for plotting examples. You should suppress the call of the
# function at the command line, as output can be a very large matrix.
# 
# You can follow the guide below to start the problem:
# 1. Define your $x$ and $y$ axis arrays based on `res`, `ULcorner` and `sqrL`. Then use `meshgrid`
# to generate `X` and `Y`.
# 2. Define `Z` using `X` and `Y`. Every element in `Z` should be a complex number.
# 3. Perform Newton's method `n` times using each value of `Z` as a starting point.
# 4. Find the roots of the polynomial using `PolynomialExactSolutions(d)`. We need to know the exact roots. This is in addition to what we do using Newton's method next.
# 5. Define your output as a matrix of 0's and of same size as `Z`. Loop through every root
# in `solutions` using a for loop. For each root, check which elements in complex
# plane `Z` converge to this root, and assign an integer from 1 to $d$ to these elements
# by recording the integer in the appropriate position in output. For instance, if an
# element in `Z` converges to the first root output by `PolynomialExactSolutions`, you
# assign 1 to the same location in output; if it converges to the second root output by
# `PolynomialExactSolutions`, assign 2 to the same location in output; so on and so
# forth.
# 6. You end up with the matrix output that has $d$ different integers and may or may not
# have 0's. (The higher the iteration `n`, the less likely you will get 0's, because Newton's
# method will have more iterations to get within the tolerance tol of an exact root. But
# the higher the iteration, the more computing time it takes.)
# 7. Now plot your output. Define your own set of colors associated with the different integers.
# Zeros should be white.
# To define your own color scheme for a `Z` that contains 0's, you can generate a (d+1)-by-3
# array, such as:
# 
# ```MATLAB
# mycolormap=[1 1 1;
# 1 0 0; 0 1 0; 0 0 1;
# 1 1 0; 0 1 1; 1 0 1];
# % This gives a 7􀀀element array of white, red, green, blue,
# %yellow, cyan, purple.
# % OR
# R=linspace(1,0,d+1); % size of d+1
# G=R;
# B=G; % Define a GRAY scale from (1 1 1) to (0 0 0);
# mycolormap=[R;G;B]';
# % OR
# mycolormap=[1 1 1; hsv(d)]; % The first row is white color, and
# % then pick d number of colors from the built􀀀in palette hsv.
# % You can also look up other built􀀀in palettes,
# % such as 'spring','hot','jet', etc.
# ```
# 
# Then you can use `imagesc` to plot `Z` and apply your colors using `colormap(mycolormap)`.
# 
# Test case (Figure 7):
# 
# ```MATLAB
# >>d=7;
# >>n=200;
# >>tol=1e􀀀4;
# >>res=200;
# >>ULcorner=[􀀀1 1];
# >>sqrL=2;
# >>output=NewtonFractal(d,n,tol,res,ULcorner,sqrL);
# ```
# 
# <img src="resources/E7_Lab8_7.jpg" style="width: 300px;"/>
# <center>*Figure 7: Example plot with $n = 200$.*</center>
# 
# Test case (Figure 8):
# ```
# >>n=25; % Keep d,tol,res,ULcorner,sqrL the same, just change the iterations
# >>output=NewtonFractal(d,n,tol,res,ULcorner,sqrL);
# ```
# 
# <img src="resources/E7_Lab8_8.jpg" style="width: 300px;"/>
# <center>*Figure 8: Example plot with $n = 25$.*</center>
# 
# Test case (Figure 9):
# ```MATLAB
# >>d=3;
# >>n=200;
# >>tol=1e􀀀5;
# >>res=500;
# >>ULcorner=[􀀀1.5 1.5];
# >>sqrL=3;
# >>output=NewtonFractal(d,n,tol,res,ULcorner,sqrL);
# ```
# <img src="resources/E7_Lab8_9.jpg" style="width: 300px;"/>
# <center>*Figure 9: Example plot with $d = 3$.*</center>
# 
# Note how Figure 9 compares to Figure 5, both for $z_3 = 1$. It's along the mid-point edge of
# each pair of roots where fractals get generated.
# 
# Try varying the size of your domain and look at the intricate details of the fractal. You
# can zoom in and out by clicking the zoom icons on top of the plot window. As you zoom
# into particular regions, you will discover the self-similarity of the fractal.
# 
# 

# In[ ]:


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


# ### Optional: Add shading to Newton's fractal
# 
# You have plotted Newton fractal with discrete colors. Now, when you Google "Newton fractal", you may come across something like Figure 10.
# 
# <img src="resources/E7_Lab8_10.jpg" style="width: 300px;"/>
# <center>*Figure 10: A Newton fractal plotted with shading*</center>
# 
# Note that in Figure 10, there are different shades of red, yellow, green, etc. The colors are
# determined by which root a guess converges to, as we programmed in NewtonFractal, and
# the shades are determined by how many iterations are needed to reach the roots. To plot
# something similar to Figure 10, you count the number of iterations in the function, instead
# of having the number of iterations as an input variable. 
# 
# Your function may `ShadedNewtonFractal(d,tol,res,ULcorner,sqrL)`,
# where your output is no longer a matrix containing integer values, but a matrix containing
# numbers with decimal points that indicate *both* which root an initial guess converges to and
# how many iterations it takes. The integer part of the number indicates the root, and the
# decimal part of the number indicates the number of iterations. For instance, 1.005 means
# it takes 5 iterations to reach the first root; and 4.580 means it takes 580 iterations to reach
# the fourth root. Then you can play around with `mycolormap` to obtain the right color and
# shade for each number in output. Only try this part if you finish all the required problems
# above.
# 
