
# coding: utf-8

# # E7: Introduction to Computer Programming for Scientists and Engineers

# ## Lab Assignment 11

# For each question, you will have to fill in one or more Python functions. We provide an autograder with a number of test cases that you can use to test your function. Note that the fact that your function works for all test cases thus provided does necessarily guarantee
# that it will work for all possible test cases relevant to the question. It is your responsibility
# to test your function thoroughly, to ensure that it will also work in situations not covered
# by the test cases provided

# In[1]:


# Please run this cell, and do not modify the contets
import math
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate
np.seterr(all='ignore');
# %run lab2_ag.py

# THE QUESTION TEXT HAS NOT BEEN CHANGED. TEXT EXAMPLES ARE GIVEN IN MATLAB STILL BUT SOLUTIONS ARE WRITTEN IN PYTHON


# ## Question 1: Numerical Differentiation
# 
# ### 1.1 Helicopter Speed Checks
# 
# A helicopter pilot is stationary above a road and timing cars as they pass by visible land-
# marks. The pilot can determine the speed and acceleration of these cars by recording the
# time at which they pass the various landmarks. The speed and acceleration can then be
# computed using finite difference formulas.
# 
# Write a function `speedFD(x, t, output_units)` returning the tuple `(speed, acceleration)`
# where `x` and `t` are $1 \times N$ double arrays representing the $x$ coordinates (in feet) of the
# landmarks and time $1 \times n$ seconds) when a car passes these landmarks, respectively. The
# outputs `speed` and `acceleration` should be double arrays with the same size as `x` and
# `t` giving the speed and acceleration of the car at each landmark. The input argument
# `output_units` is a char array with possible values `'mph'` or `'fps'`. If `output_units` is
# `'fps'` then the outputs should be given in the units $ft/s$ and $ft/s^2$. If output_units is
# `'mph'` then the outputs should be given in units $mi/hr$ and $mi/hr^2$. Note that the inputs
# will always be given in feet and seconds. Your function should compute the outputs using
# the central difference method. This will work for all but the edge points, where you should
# use a forward difference at the first point, and a backward difference at the last point. To
# compute acceleration, we could use the first derivative of the speed or the second derivative
# of position. For this assignment, use the first derivative of the speed.
# 
# - Forward Difference
# $$\frac{df}{dx}\rvert_{x_k} \approx \frac{f(x_{k+1})-f(x_k)}{x_{k-1}-x_k}$$
# 
# - Central Difference
# $$\frac{df}{dx}\rvert_{x_k} \approx \frac{f(x_{k+1})-f(x_{k-1})}{x_{k+1}-x_{k-1}}$$
# 
# - Backward Difference
# $$\frac{df}{dx}\rvert_{x_k} \approx \frac{f(x_{k})-f(x_{k-1})}{x_{k}-x_{k-1}}$$

# Alternative second derivative formula (optional)
# 
# In class, we derived the expressions for the forward, backward and central differences using
# Taylor series. We can similarly use this method to derive formulas for the second derivative,
# again using a linear combination of Taylor series. For a non-uniform grid (as in the example
# above), the second derivative can be expressed as
# 
# $$\frac{d^2f}{dx^2}\rvert_{x_k} = 2\Big[\frac{f(x_{k-1})}{h_k (h_k + h_{k+1})} - \frac{f(x_k)}{h_kh_{k+1}} + \frac{f(x_{k+1})}{h_{k+1}(h_k + h_{k+1})}\Big] + \mathcal{O}(h^2)$$
# 
# where $h_k = x_k - x_{k-1}$ and $h_{k+1} = x_{k+1} - x_k$. You can try out this formula for the second
# derivative and compare it to your answer above, where you applied a finite difference for the
# first derivative twice. Note that for a uniform grid where $h = x_{k+1} - x_k = x_k - x_{k-1}$ this
# reduces to the formula we found in lecture:
# 
# $$\frac{d^2f}{dx^2}\rvert_{x_k} = \frac{f(x_{k+1})-2f(x_k)+f(x_{k-1})}{h^2} + \mathcal{O}(h^2)$$
# 
# for uniform grids.
# 
# <img src="resources/E7_Lab11_1.jpg" style="width: 500px;"/>
# <center>*Figure 1: Velocity in mph and fps*</center>

# In[5]:


def speedFD(x, t, output_units):
    x = np.array(x)
    t = np.array(t)
    if output_units.lower() == 'mph':
        x = x/5280.
        t = t/3600.
    
    last = len(x) - 1
    
    speed = [(x[1] - x[0]) / (t[1] - t[0])]
    for i in range(1, len(x)-1):
        speed.append((x[i+1] - x[i-1]) / (t[i+1] - t[i-1]))
    speed.append((x[last] - x[last-1])/(t[last]-t[last-1]))
        
    acceleration = [(speed[1] - speed[0]) / (t[1] - t[0])]
    for i in range(1, len(x)-1):
        acceleration.append((speed[i+1] - speed[i-1]) / (t[i+1] - t[i-1]))
    acceleration.append((speed[last] - speed[last-1])/(t[last]-t[last-1]))
    
    return speed, acceleration


# In[6]:


t = [0, 13, 20, 24.5, 28, 31, 33.5, 35.5, 37]
x = [0, 200, 400, 600, 800, 1000, 1200, 1400, 1600]

#t = [0., 1., 2.1, 3.6, 5., 6.5, 8., 9.2, 10.]
#x = [1., 4., 8., 5., 6., 7.8, 9., 8., 4.5]
print(speedFD(x, t, 'fps'))
print()
print(speedFD(x, t, 'mph'))


# ### 1.2: 2D Numerical Differentiation and Gradient
# 
# Functions often have more than one variable. For example, think of the area of a rectangle
# that is a function of its length and width. If we call $x$ the length and $y$ the width, we can
# write the area as a function $f$ of $x$ and $y$ such as:
# 
# $$f(x, y) = xy$$
# 
# To determine how the area changes if we change the width, we need to take a derivative of $f$
# while holding other variables (the length) constant. This is called a partial derivative of
# $f$ with respect to $y$, all other terms being held constant. The partial derivative with respect
# to $x$ is denoted $\frac{\partial f}{\partial x}$ and in this example where $f = xy$:
# 
# $$\frac{\partial f}{\partial x}(x,y) = y$$
# 
# The gradient of $f(x, y)$ is denoted $\text{grad}_f(x, y)$ and is defined as the vector of partial derivatives:
# 
# $\text{grad}_f(x, y) = [\frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}]$
# 
# The gradient can be evaluated at a specific point $(x,y) = (a,b)$ by evaluating the partial
# derivatives at those points. For the area function above:
# 
# $$\text{grad}_f(a,b) = [b,a]$$
# 
# Another example: if $g(x, y) = e^x \sin(y)$, then
# 
# $$\text{grad}_g(x,y) = [e^x \sin(y), e^x \cos(y)]$$
# 
# In terms of numerical differentiation, you can use the central difference formula such that
# you have:
# 
# $$\text{grad}_f(x_j,y_k) = \Big[\frac{f(x_{j+1},y_k)-f(x_{j-1},y_k)}{x_{j+1}-x_{j-1}}, \frac{f(x_{j},y_{k+1})-f(x_{j},y_{k+1})}{y_{k+1}-y_{k-1}} \Big]$$
# 
# Since the gradient of $f$ is a vector which is spatially variable, we refer to it as a vector field
# that we can plot in two dimensions (recall Lab 6 when you plotted groundwater velocity
# vectors). 

# Write a function `myGradient(f,bbox,N)` where `f` is a function handle, `bbox` is a bounding box (a $1 \times 4$ double of the form `[xmin, xmax, ymin, ymax]`, and `N` is the total number of grid points in each of the intervals `[xmin, xmax]` and `[ymin, ymax]` (including the end points). The output `grad` should be a $(N-2) \times (N-2) \times 2$ double array representing the gradient of `f`. Note that `grad(:,:,1)` represents $\frac{\partial f}{\partial x}$ and `grad(:,:,2)` represents $\frac{\partial f}{\partial y}$. If you wish, you can define $x$ and $y$ using `meshgrid` in
# the same way as the code in the test case below.
# 
# When computing $\frac{\partial f}{\partial x}$ with a central difference, you will create a $N \times (N - 2)$ matrix, and
# when computing $\frac{\partial f}{\partial y}$ , you will create a $(N - 2) \times N$ matrix. Then when combining to create
# the output grad, you will take the $(N - 2) \times (N - 2)$ subset of each where both derivatives
# are defined. (Note that in many applications there are boundary conditions applied to the
# edge values but we are leaving the edge points alone here.)
# You can now plot a contour plot of $f$ over the bounding box (using Python `contourf`) and
# superimpose on this the vector field of the function gradient: at each point $(x, y)$ there should
# be an arrow equal to the gradient of $f$ at $(x, y)$, using the Python `quiver` command (see the
# test case below).

# The following test case should produce the plot shown in Figure 2:
# 
# ```MATLAB    
# %% Test case 3
# f=@(x,y) x.ˆ2􀀀y.ˆ2;
# bbox=[􀀀2 2 􀀀2 2];
# N=21;
# grad=myGradient(f,bbox, N);
# x=linspace(bbox(1),bbox(2),N);
# y=linspace(bbox(4),bbox(3),N); %note the ordering here
# [xx,yy]=meshgrid(x,y);
# zz=f(xx,yy);
# figure
# contourf(x,y,zz);
# hold on
# quiver(x(2:end􀀀1),y(2:end􀀀1),grad(:,:,1),grad(:,:,2));
# axis('equal')
# title('Gradient Plot of f(x)=xˆ2􀀀yˆ2')
# xlabel('x');ylabel('y');
# legend('Contour of f','Gradient of f')
# colorbar
# hold off
# ```
# 
# <img src="resources/E7_Lab11_2.jpg" style="width: 600px;"/>
# <center>*Figure 2: Result from the 3rd test case*</center>

# In[58]:


def myGradient(f, bbox, n):
    x_data = np.linspace(bbox[0], bbox[1], n)
    y_data = np.linspace(bbox[2], bbox[3], n)
    x_partial = np.zeros((n, n-2))
    y_partial = np.zeros((n-2, n))
    
    for i in range(len(x_data)):
        for j in range(1, len(x_data) - 1):
            end_y = len(y_data)-1
            end_x = len(x_data)-1
            x_partial[i][j-1] = (f(x_data[j+1],y_data[end_y-i]) - f(x_data[j-1], y_data[end_y-i]))/(x_data[j+1]-x_data[j-1])
            
    for i in range(1, len(y_data) - 1):
        for j in range(len(y_data)):
            end_y = len(y_data)-1
            end_x = len(x_data)-1
            y_partial[i-1][j] = (f(x_data[j], y_data[end_y-i+1]) - f(x_data[j], y_data[end_y-i-1]))/(y_data[end_y-i+1]-y_data[end_y-i-1])
            
    grad = np.zeros((n-2,n-2,2))
    grad[:,:,0] = x_partial[1:-1,:]
    grad[:,:,1] = y_partial[:,1:-1]
    return grad


# In[60]:


f = lambda x, y: x**2 - y**2 + 1
grad = myGradient(f, [-1, 1, -1, 1], 5)
print(grad[:,:,0])
print(grad[:,:,1])
print()

g = lambda x, y: math.exp(x)*math.sin(y)
grad = myGradient(g, [-1, 1, -1, 1], 6)
print(grad[:,:,0])
print(grad[:,:,1])
print()

h = lambda x, y: (x**2 + x**3)*(1+y) - y**2
grad = myGradient(h, [-10, 10, -10, 10], 5)
print(grad[:,:,0])
print(grad[:,:,1])


# ## Question 2: Numerical Integration
# 
# ### Gauss Integral
# 
# In probability theory, the Gaussian distribution is of crucial importance and plays a role in a
# large number of problems. The density $f$ of the zero-mean, one-standard deviation Gaussian
# distribution (shown in Figure 3) is given by:
# 
# $$f(x) = \frac{1}{\sqrt{2\pi}}e^{-\frac{-x^2}{2}}$$
# 
# In many applications, this function must be integrated to compute the area between $-\text{A}$ and
# $\text{A}$, given by $I = \int^A_{-A} \frac{1}{\sqrt{2\pi}}e^{-\frac{x^2}{2}} dx$ (see Figure 4).
# 
# <img src="resources/E7_Lab11_3.jpg" style="width: 350px;"/>
# <center>*Figure 3: Gaussian Distribution*</center>
# 
# <img src="resources/E7_Lab11_4.jpg" style="width: 350px;"/>
# <center>*Figure 4: Area $[-\text{A},\text{A}]$ of Gaussian Distribution*</center>

# Write a function `GaussIntegral(A,n)` returning `I`,
# which calculates the area shown in Figure 4 by numerically integrating $f(x)$ between $-\text{A}$ and
# $\text{A}$ and dividing the interval $[-\text{A},\text{A}]$ into $n$ equal parts. In other words, interval endpoints are
# $x_1, x_2, \dots; x_{n+1}$ and the $k^{th}$ interval is between $x_k$ and $x_{k+1}$ where $x_1 = -\text{A}$ and $x_{n+1} = \text{A}$.
# 
# `A`, `n`, and `I` are scalars of class double. To estimate the function value for each interval
# $[x_k, x_{k+1}]$, take the left endpoint value, i.e. $f(x_k)$, which is a form of a Riemann integral.
# 
# As you notice, as $\text{A}$ get bigger and bigger, the integral is closer and closer to 1 (as long as $n$
# is sufficiently large). Indeed, it is a characteristic of a probability density function to have
# its integral between $-\infty$ and $+\infty$ equal to 1.

# In[66]:


def GaussIntegral(A, n):
    interval = np.linspace(-A, A, n+1)
    step_size = interval[1]-interval[0]
    f = lambda x: (1/np.sqrt(2*np.pi))*np.exp(-(x**2)/2)
    I = sum(f(interval[0:-1])*step_size)
    return I


# In[143]:


I1 = GaussIntegral(1,25)
print(I1)
I2 = GaussIntegral(2,40)
print(I2)
I3 = GaussIntegral(3,50)
print(I3)
I4 = GaussIntegral(1,5)
print(I4)


# ### 2.2 Corrugated Sheets
# 
# In constructing a roof, many types of materials may be used. One example is corrugated
# roofing, which is produced by pressing a 
# at sheet of aluminum into a sheet whose cross
# section resembles the shape of a sine wave (see Figure 5).
# 
# <img src="resources/E7_Lab11_5.jpg" style="width: 350px;"/>
# <center>*Figure 5: Corrugated Sheet*</center>
# 
# Consider a corrugated sheet that is $L_C$ inches long, with a wave height of $H$ inches from
# the center line, and a wavelength of $P$ inches. To manufacture such a sheet, we need to
# determine the required length $L_F$ of the initial 
# at sheet. To compute $L_F$ , we determine
# the arc length of the wave, where the wave is given by $f(x) = H \sin(\frac{2\pi}{P} x)$. Thus, we can
# compute the arc length $L_F$ using the equation
# 
# $$L_F = \int_0^{L_C}\sqrt{1+(f'(x))^2}dx$$
# 
# Where $f'(x)$ is given by:
# 
# $$f'(x) = \frac{2\pi H}{P}\cos(\frac{2\pi}{P}x)$$

# In this problem, you will write a function which computes this arc length ($L_F$) using:
# 
# 1. Trapezoidal Rule
# 2. Simpson's Rule
# 3. Riemann Integral (using left endpoints, as in the previous problem)
# 
# Write a function `roofSheetLength(L_C, H, P, N)` returning `(L_Trap, L_Simp, L_Riem)` where `N` is the number of equal intervals (like with `GaussIntegral`), and `L_C`, `H`, and `P` are the corrugated length, wave height, and wavelength, respectively (as given in the above equations). `L_Trap`, `L_Simp`, and `L_Riem` are the approximations of $L_F$ given by the Trapezodial Rule, Simpson's Rule, and the Riemann Integral, respectively. All inputs and outputs are
# scalars of class double. 
# 
# Do not use the built-in Python function `trapz` (though you can
# use it to check your answer). 
# 
# **Hint**: Make sure you check out the "Try it!" examples in
# Chapter 18 of the book before you do this problem!

# In[85]:


def roofSheetLength(L_C, H, P, N):
    x = np.linspace(0,L_C, N+1)
    step_size = x[1]-x[0]
    
    f = lambda x: np.sqrt(1+(((2*np.pi*H)/P)*np.cos((2*np.pi*x)/P))**2)
    L_Trap = sum(step_size*((1/2)*(f(x[0:-1]) + f(x[1:]))))
    L_Simp = sum((step_size/3)*(f(x[:-2:2]) + 4*f(x[1:-1:2]) + f(x[2::2])))
    L_Riem = sum(f(x[0:-1])*step_size)
    return L_Trap, L_Simp, L_Riem


# In[142]:


L_T1, L_S1, L_R1 = roofSheetLength(72, 1.5, 2*np.pi, 50)
print(L_T1)
print(L_S1)
print(L_R1)
print()
L_T2,L_S2,L_R2 = roofSheetLength(108,2,5,20)
print(L_T2)
print(L_S2)
print(L_R2)
print()
L_T3,L_S3,L_R3 = roofSheetLength(90,2,8,30)
print(L_T3)
print(L_S3)
print(L_R3)
print()


# ## Question 3: Lagrange polynomial
# 
# Read §18.4 in your textbook to get some background on how Simpson's rule is formulated.
# As you've read, to perform Simpson's Rule, we need to calculate the Lagrange interpolation
# polynomial of three given points. (With 3 points, this just means you are fitting a quadratic
# polynomial to the 3 points - the Lagrange polynomial is a convenient way to find this unique
# quadratic polynomial that passes through these points.) Given a set of points $(x_i, y_i)$, where
# $i = 1, 2, \dots; n$, the Lagrange interpolation polynomial $P$ of degree $n-1$ is such that $P(x_i) = y_i$.
# Note that there is only one unique Lagrange polynomial passing through a set of points. We
# also note that $P = a_0 + a_1X + \dots + a_{n-1}X_{n-1}$. See §14.4 for background on Lagrange
# polynomials.

# ### 3.1: Lagrange polynomial
# 
# Write a function`LagrangePolynomial(x,y)`
# where `x` and `y` are two vectors (class double) of length $n$ containing the coordinates of the
# points $(x_i, y_i)$. Your function should return the Lagrange interpolation polynomial in the
# form of a column vector (class double) of its coefficients, that is $[a_0, a_1, \dots, a_{n-1}]^T$.

# ```MATLAB
# % The following codes plots the points and function
# % and checks that it passes through the points
# >> plot(x,y,'o')
# >> hold on
# >> X=0:0.1:10;
# >> Y=P'*[X.ˆ0; X.ˆ1; X.ˆ2; X.ˆ3; X.ˆ4];
# >> plot(X,Y)
# ```

# In[118]:


def LagrangePolynomial(x, y):
    n = len(x)
    A = np.zeros((n,n))
    exponent = np.arange(0,n)
    for i in range(n):
        A[i,:] = x[i]**exponent
    b = y
    P = np.linalg.solve(A, b)
    return P


# In[141]:


x1 = [1,2]
y1 = [2,0]
P1 = LagrangePolynomial(x1, y1)
print(P1)
x2 = [1,2,5,7,8]
y2 = [2,0,3,-4,5]
P2 = LagrangePolynomial(x2,y2)
print(P2)
x3 = np.arange(1,11)
y3 = np.sin(x3)
P3 = LagrangePolynomial(x3,y3)
print(P3)


# ## Trinomial integration
# 
# On paper, show that
# 
# $$\int_a^b (a_0 + a_1x + a_2x^2) dx = a_0(b-a) + a_1\frac{b^2-a^2}{2} + a_2\frac{b^3-a^3}{3}$$
# 
# Write a function `TrinomialIntegral(a,b,P)` which returns the **exact** value of
# $\int_a^b P(x)dx$ where $P$ is a polynomial of degree 2 represented
# by the column vector of its coefficients: $P = [a_0, a_1, a_2]^T$. `I`, `a`, and `b` are scalars of class
# double. Here $P$ is a $3 \times 1$ array of class double.

# In[120]:


def TrinomialIntegral(a,b,P):
    I = (P[0]*(b-a)) + ((P[1]/2)*((b**2 - a**2))) + ((P[2]/3)*((b**3-a**3)))
    return I


# In[140]:


J1 = TrinomialIntegral(0,3,[1,2,1])
print(J1)
J2 = TrinomialIntegral(1,5,[3,0,3])
print(J2)
J3 = TrinomialIntegral(-5,8,[1,2,-3])
print(J3)


# ### 3.3 Simpson's Rule
# 
# Now that you can access the interpolation polynomial given a set of points and compute the
# exact integral of a polynomial of degree 2, you can implement Simpson's Rule where you
# only need to interpolate on sets of three points. 
# 
# Write a function `SimpsonIntegral(f,a,b,n)` returning the tuple `(I,e)`
# which calculates the integral `I` (scalar double) of the function handle `f` using Simpson's Rule
# and subdividing the interval $[a, b]$ in $2n$ equal parts. (You can use the functions you wrote
# above to do this.) Your function should also return the scalar double `e`, which represents
# the absolute value of the error between your estimate of the integral and Matlab's estimate
# which you can obtain using the function `integral`.

# In[137]:


def SimpsonIntegral(f,a,b,n):
    x = np.linspace(a,b,2*n+1)
    I = 0
    for i in np.arange(0,len(x)-1,2):
        current_polynomials = LagrangePolynomial(x[i:i+3], f(x[i:i+3]))
        I = I + TrinomialIntegral(x[i],x[i+2],current_polynomials)
    
    true = scipy.integrate.quad(f,a,b)[0]
    e = np.absolute(true - I)
    return I, e


# In[139]:


f = lambda x: np.sin(x)
I1, e1 = SimpsonIntegral(f,0,np.pi/2,10)
print(I1)
print(e1)
print()
g = lambda x: (x**2)*np.cos(x)
I2, e2 = SimpsonIntegral(g, 0,5,15)
print(I2)
print(e2)
print()
h = lambda x: np.sin(np.sin(x))
I3, e3 = SimpsonIntegral(h,0,0.5,30)
print(I3)
print(e3)
print()

