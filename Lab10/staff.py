
# coding: utf-8

# # E7: Introduction to Computer Programming for Scientists and Engineers

# ## Lab Assignment 10

# For each question, you will have to fill in one or more Python functions. We provide an autograder with a number of test cases that you can use to test your function. Note that the fact that your function works for all test cases thus provided does necessarily guarantee
# that it will work for all possible test cases relevant to the question. It is your responsibility
# to test your function thoroughly, to ensure that it will also work in situations not covered
# by the test cases provided

# In[1]:


# Please run this cell, and do not modify the contets
import math
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize
from scipy.interpolate import interp1d
np.seterr(all='ignore');
# %run lab2_ag.py


# ## Question 1: Writing your own trigonometric function
# 
# There is no direct way to calculate trigonometric functions generically, even on a computer. In order to find the solution to a given trigonometric function, the computer uses a high
# accuracy estimate. For this problem, you will code your own trigonometric function using a
# Taylor series and an old school table look-up. Computers actually use the CORDIC method
# to implement trigonometric functions, which is pretty cool. You can look into this more
# [here](https://en.wikipedia.org/wiki/CORDIC), but you will not have to code it for this assignment. You can watch [this video](https://www.khanacademy.org/math/integral-calculus/sequences-series-approx-calc/maclaurin_taylor/v/maclauren-and-taylor-series-intuition) for more
# information on how Taylor series are derived.

# ### 1.1: Taylor series for sine
# 
# The Taylor series expansion about zero for sine (with input in radians) is:
# 
# $$\sin(x) \approx x - x^3/3! + x^5/5! - x^7/7! + \dots + (-1)^{(n-1)}\frac{x^{(2n-1)}}{(2n-1)!}$$
# 
# Or, in summation notation:
# 
# $$\sin(x) \approx \sum_{n=1}^N (-1)^{(n-1)}\frac{x^{(2n-1)}}{(2n-1)!}$$
# 
# For this problem, we will consider the $N^{th}$ Taylor expansion of sine to be the sum of the
# first $N$ terms of this series. The approximation above becomes exact as $N$ approaches infinity.
# 
# Write a function `mySin(X,N)`
# which computes sine at every radian value given in the 2D array `X` (class double) using the
# $N^{th}$ Taylor expansion for sine. The input `N` is a scalar double which is an integer greater
# than 0. The output sinSeries should be a double with the same size as `X`.

# In[62]:


def mySin(X, N):
    """
    Computes the Nth Taylor expansion of sine for a given 2D matrix of X Inputs
    X: 2D array (doubles), radians
    N: Nth degree of a sine Taylor Series expansion
    Output: Double same size as X
    """
    X = np.array(X)
    sinSeries = np.zeros(X.shape)
    
    for i in range(1, N+1):
        #print(sinSeries)
        sinSeries = sinSeries + ((-1)**(i-1) * (np.power(X,(2*i-1)))) / math.factorial(2*i-1)
    
    return sinSeries


# In[63]:


print(mySin(np.array([[2.4]]), 3))

mtx = np.matrix([[0, 1], [2, 3]])
#print(mtx.shape)
print(mySin(mtx, 8))

mtx = np.matrix([[-1, 4], [7, -9]])
print(mySin(mtx, 2))


# ### 1.2: Order of convergence for the Taylor series
# For a finite number of terms, the error of the Taylor series estimate for sine (expanded about
# the origin) increases the further you get from the origin. This error is often approximated
# based on the next term of the Taylor series, since that term is the largest that is being
# neglected. Thus, the $2^{nd}$ Taylor approximation for sine would have error that is of the order
# of $x^5/5!$ (the constant coefficient is often dropped and the expression written in shorthand
# as $O(x^5)$). For this problem, you will write a function that finds the error between your
# approximation for sine and the Python `math.sin` function. You will also compute the value of the
# next term in the Taylor series expansion for sine, so that we can compare the two to see if
# they actually do produce similar results.
# 
# Write a function with header: `CompareTaylorConvergence(N)`
# which finds the error in the $N^{th}$ Taylor approximation for sine, along with the absolute value
# of the $(N+1)^{th}$ term of the Taylor expansion. Your function should evaluate each of these
# for $x$ data ranging from $[-\frac{N\pi}{2}, \frac{N\pi}{2}]$ in increments of $\frac{\pi}{8}$. As an output, your function should
# return a $1 \times (8N + 1)$ row vector `[x, err, next_term]` for each variable, where `x` is the $x$ values where the errors
# were evaluated, err is the actual (absolute value) error between your Taylor approximation
# and the Python `math.sin` function, and `next_term` is the absolute value of the next term in the
# Taylor series.

# Test Case (produces Figure 1):
#     
# ```MATLAB
# [ x , e r r , next term ] = CompareTaylorConvergence ( 2 ) ;
# f igure ;
# plot (x , [ e r r ; next term ] , ' Linewidth ' , 2 ) ;
# axis ([􀀀pi /2N pi /2N 0 2 ] ) ;
# t i t l e ( 'Order o f Convergence Plot ' , ' FontSize ' , 1 6 ) ;
# xlabel ( ' x ' ) ;
# ylabel ( ' Er ror s ' ) ;
# legend ( ' Actual Er ror ' , 'Next Term ' , ' Locat ion ' , ' Best ' ) ;
# ```
# 
# <img src="resources/E7_Lab10_1.jpg" style="width: 500px;"/>
# <center>*Figure 1*</center>

# In[64]:


def CompareTaylorConvergence(N):
    """
    Finds the error in the Nth Taylor approximation for sine, along with
    absolute value of the (N+1)th term of the Taylor expansion
    
    Input
    N: number of iterations of Taylor approximation

    Outputs
    x: x values that you evaluated the errors at
    error: actual error between your Taylor approximation and the Python sin() function
    next_term: absolute value of the next term in the Taylor series
    """
    eval_pts = np.arange(-N*math.pi/2., N*math.pi/2.+0.01, math.pi/8.)
    tot_err = []
    all_term = []
    for x in eval_pts:
        err = abs(mySin([[x]], N) - math.sin(x))
        next_term = abs((-1)**N * (x**(2*N+1)) / math.factorial(2*N+1))
        tot_err.append(err)
        all_term.append(next_term)
    
    return eval_pts, tot_err, all_term


# In[65]:


CompareTaylorConvergence(2)


# ### 1.3: Using the periodicity of sine
# 
# From the last problem, you can see that, far enough away from the origin, a finite Taylor
# expansion always diverges from the actual solution for sine. One way to improve our accuracy
# from inputs far from the origin is to use the periodicity of sine. i.e.
# 
# $$\sin(x \pm 2\pi) = \sin(x)$$
# 
# Write a function `mySinPeriodic(X,N)` which converts every radian value in the 2D matrix `X` to the range $[-\pi, \pi]$ using the periodicity of sine and then calculates sine at each point using the Nth Taylor expansion for sine.
# The output should be the same size as the input `X`.
# 
# Hint: You may wish to use the Python function mod, `%`, for this problem; you will have to be a bit clever about it.

# In[85]:


def mySinPeriodic(X, N):
    """
    function [approxs] = mySinPeriodic(X,N)
    converts every radian value in the 2D matrix X to the range [-pi,pi] using
    the periodicity of sine and then calculates sine at each point using the
    Nth Taylor expansion for sine
    """
    X = np.array(X)
    xr, xc = X.shape
    for i in range(xr*xc):
        while X[i] < -math.pi:
            X[i] += 2*math.pi
        while X[i] > math.pi:
            X[i] -= 2*math.pi
            
    approxs = mySin(X, N)
    return approxs


# In[86]:


mySinPeriodic([[6.], [-2.]], 3)


# ### 1.4: Accurate range of the Taylor series
# Now, we will examine how well our new and improved approximation for sine works by finding the range of values for which its accuracy is acceptable.
# 
# Write a function `TaylorAccRange(N, tol)` that finds the range of angles for which the error in the $N^{th}$ Taylor expansion is less than
# the given tolerance, `tol`. The range should be returned as a $1 \times 2$ array containing the
# minimum and maximum angle in radians for which every angle in between can be found to
# within the given tolerance. You should consider the periodicity of sine in the function, such
# that angles outside of the range $[-\pi, pi]$ are taken as their corresponding angle within that
# range. (i.e. What does this imply if your tolerance range is greater than or equal to $[-\pi, pi]$
# without considering periodicity?). If your Taylor approximation is within the tolerance for
# all angles, your function should return the vector $[-\inf, \inf]$.
# 
# **Hint**: You may wish to rewrite this problem as a root solving problem; you are free to use
# Python predefined functions (or your own functions from a previous problem set!) to solve
# for the root.

# In[140]:


def TaylorAccRange(N, tol):
    """
    function [range] = TaylorAccRange(N, tol)
    finds the range of angles for which the error in the Nth taylor expansion is less than the given tolerance, tol
    
    Output
    range: 1x2 array containing minimum and maximum angle in radians for which 
    every angle in between can be found within the given tolerance
    """
    f = lambda x: tol - abs(((-1)**(N) * x**(2*N+1)) / math.factorial(2*N+1))
    
    angle = scipy.optimize.fsolve(f, 0.)
    print(angle)
    
    range = [-abs(angle), abs(angle)]
    
    if abs(angle) >= math.pi:
        range = [-np.inf, np.inf]
        
    return range


# In[141]:


print(TaylorAccRange(1., 0.001))
print(TaylorAccRange(5., 0.1))


# ### 1.5 Table Lookup
# 
# Before the widespread use of handheld calculators, it was common practice to look up the
# values of trigonometric functions from tables (many older math textbooks have such tables).
# Even today, engineers use such lookup tables for more complex functions. Engineers will typically use linear interpolation to find values between entries in such tables. In this problem,
# we will apply this same methodology to make a new version of the trigonometric function
# we have been developing.
# 
# Write a function `sinLookup (X, table)`
# which finds sine at each angle (given in radians) in the 2D matrix `X` using linear interpolation
# of a table of sine values, given in the input argument table. This table can be loaded from
# the file `SineLookup.csv` (see test case below), which includes two columns of data. The first
# column contains the angle in degrees and the second column contains the value of sine at
# that angle (calculated out to 5 decimal places). This data table only goes from -180 to 180
# degrees, so you will have to take the periodicity of sine into account in order to calculate
# values outside of that range. The output should be the same size as the input `X`.
# Note: Your function should not make use of any predefined Python interpolation functions.
# 

# In[142]:


def sinLookup(X, table):
    tab_ang = table[:,1]*math.pi/180
    tab_val = table[:,2]
    X = (X + math.pi) % (2 * math.pi) - math.pi
    out = []
    
    for i in range(len(X[0])):
        for j in range(len(X[1])):
            low_ang, loc = max(tab_ang[tab_ang <= X[i][j]])
            low_val = tab_val(loc)
            high_ang = tab_ang(loc+1)
            high_val = tab_val(loc+1)
            
            out[i][j] = low_val + (high_val - low_val) / (high_ang-low_ang) * (X[i][j] - low_ang)
            
    return out


# In[143]:


sinLookup([-5.4, 2.3, 8.4])


# ## Question 2: Interpolation: Biomechanics
# 
# In the field of biomechanics, data interpolation is often used to define anatomical joint angles
# as a function of the walking cycle (clinically, this is known as the gait cycle). For example, engineers designing a prosthetic leg may be interested in analyzing the hip angle of an
# able-bodied individual in order to design a prosthetic leg that mimics natural leg motions.
# 
# For clarity, illustrations defining hip angle (Figure 2) as well as the gait cycle (Figure 3) are
# provided. As shown in Figure 3, the gait cycle goes from 0 to 100% for each foot and is
# periodic in nature. For a given leg, an entire period of the gait cycle begins with the heel
# striking the 
# oor and ends when the same heel strikes the 
# oor again. Additionally, when
# the thigh and torso are completely vertical (i.e. standing perfectly vertical), the hip angle
# is zero degrees. Assuming a perfectly vertical torso, moving the thigh forward signifies hip flexion (positive angle) whereas moving the thigh backward signifies hip extension (negative angle).

# <img src="resources/E7_Lab10_2.jpg" style="width: 200px;"/>
# <center>*Figure 2: Definition of Hip Angle*</center>
# 
# <img src="resources/E7_Lab10_3.jpg" style="width: 500px;"/>
# <center>*Figure 3: Definition of Gait Cycle*</center>

# To plot the hip angle as a function of the gait cycle, some researchers make use of state-of-the-art gait laboratories equipped with infrared cameras to get very accurate estimates
# of the hip angle at all instances of the gait cycle. However, most researchers do not have
# access to these gait labs (they cost hundreds of thousands of dollars) and instead resort to
# less costly methods of calculating hip angles. For instance, a graduate student researcher may simply take pictures of a human subject at specific instances of the gait cycle and use
# a protractor on each image to estimate the hip angle at each specific moment. Once the
# researcher has obtained a few data points, they may then use software such as Python to
# interpolate between these points. That way, the hip angle is now known across the entire
# gait cycle and not just at a few discrete points.
# 
# In this problem, you are asked to write a function that performs the interpolation men-
# tioned in the previous paragraph. You are provided with a data file `GaitLabData.mat` which
# contains four double arrays: `crude_gait_cycle`, `crude_hip_angles`, `ideal_gait_cycle`,
# and `gait_lab_hip_angles`. The arrays `crude_gait_cycle` and `crude_hip_angles` correspond to the gait cycle instances and hip angles calculated using a protractor and a traditional camera. The array `ideal_gait_cycle` corresponds to the values of the gait cycle
# in which it is desired to have interpolated hip angle values. Thus, the number of elements
# in `ideal_gait_cycle` is much larger than the number of elements in `crude_gait_cycle`.
# The array `gait_lab_hip_angles` contains data from an actual gait laboratory, which we
# can use to evaluate the effectiveness of different interpolation methods (the more closely the
# interpolation matches the gait lab data, the better it is).
# 
# Write a function `gait_data_interp(crude_gait_cycle, crude_angles, ideal_gait_cycle, interp_method)`. Your function will take inputs of the crude gait cycle points, the crude hip angles, the
# ideal gait cycle points, and finally a character array specifying the interpolation method.
# Your function should be able to perform linear, cubic, or spline interpolations, which will
# correspond to values of `interp_method`: `linear`, `cubic`, and `spline`. Using the Python function `interp1`, the output of interpolated hip angles should be produced. If an interpolation method is called that is not linear, cubic, or spline, the function should output an empty
# array `[]` and display `"Please input either linear, cubic, or spline"`. Note that the spline
# option for the Python `interp1` function performs a traditional cubic spline, as discussed
# in lecture and the textbook, while the cubic option performs a more sophisticated method
# that never locally overshoots its target. You do not need to worry about the details of this
# method for this class, but you are free to look into it more if you are interested.

# Once you have created your function, the following test case should result in a figure that is identical to Figure 4:
# 
# Test Case:
# ```MATLAB
# load ( 'resources/GaitLabData .mat ' )
# a n g l e l i n e a r = g a i t d a t a i n t e r p ( c r u d e g a i t c y c l e , c rude hip ang l e s , . . .
# i d e a l g a i t c y c l e , ' l i n e a r ' ) ;
# a n g l e c u b i c = g a i t d a t a i n t e r p ( c r u d e g a i t c y c l e , c rude hip ang l e s , . . .
# i d e a l g a i t c y c l e , ' cubi c ' ) ;
# a n g l e s p l i n e = g a i t d a t a i n t e r p ( c r u d e g a i t c y c l e , c rude hip ang l e s , . . .
# i d e a l g a i t c y c l e , ' s p l i n e ' ) ;
# f igure
# %Plot crude data p o int s
# plot ( c r u d e g a i t c y c l e , c rude hip ang l e s , ' k . ' , 'MarkerSize ' , 3 0 ) ;
# hold on ;
# grid on ;
# %Plot l i n e a r i n t e r p o l a t i o n
# plot ( i d e a l g a i t c y c l e , a n g l e l i n e a r , ' g ' , ' LineWidth ' , 2 ) ;
# %Plot cub i c i n t e r p o l a t i o n
# plot ( i d e a l g a i t c y c l e , ang l e cubi c , ' r ' , ' LineWidth ' , 2 ) ;
# %Plot s p l i n e i n t e r p o l a t i o n
# plot ( i d e a l g a i t c y c l e , a n g l e s p l i n e , 'b ' , ' LineWidth ' , 2 ) ;
# %Plot the a c t u a l g a i t l a b data
# plot ( i d e a l g a i t c y c l e , g a i t l a b h i p a n g l e s , ' k ' , ' LineWidth ' , 2 ) ;
# xlabel ( ' Percent Gait Cycle ' , ' FontSize ' , 1 6 ) ;
# ylabel ( 'Hip Angle ( Degrees ) ' , ' FontSize ' , 1 6 ) ;
# t i t l e ( ' I n t e r p o l a t i o n Methods f o r Hip Angle Analys i s ' , ' FontSize ' , 2 0 ) ;
# legend ( 'Crude Data ' , ' Linear I n t e r p o l a t i o n ' , ' Cubic I n t e r p o l a t i o n ' , . . .
# ' Spl ine I n t e r p o l a t i o n ' , ' Gait Lab Data ' , ' Locat ion ' , ' SouthEast ' ) ;
# ```
# 
# You should be able to see the ability of each interpolation method and how it compares to
# the extremely accurate data that can be obtained from a gait laboratory. Can you make
# sense of the data based on the definition of the gait cycle and the definition of hip 
# exion
# and hip extension?
# 
# <img src="resources/E7_Lab10_4.jpg" style="width: 1000px;"/>
# <center>*Figure 4: Problem 2 Interpolation Results*</center>

# In[ ]:


def gait_data_interp(crude_gait_cycle, crude_angles, ideal_gait_cycle, interp_method):
    if interp_method not in ('linear', 'cubic', 'spline'):
        print('Please input either "linear", "cubic", or "spline"')
        return
    
    return interp(crude_gait_cycle, crude_angles, ideal_gait_cycle, interp_method)
    
def interp(crude_gait_cycle, crude_angles, ideal_gait_cycle, interp_method):
    return


# In[ ]:


gait_data_interp()


# ## Question 3: Interpolation: Soil Layers
# Civil engineers often collect and analyze soil samples to better understand the properties of
# the soil and groundwater at a site before beginning a construction project. This data is often
# collected by drilling vertical boreholes. This allows engineers to bring soil samples back to
# the lab for testing of various properties and also to distinguish layers of different soil types
# as well as the depth to the water table. One of the key challenges remaining is that soil and
# groundwater properties can only be collected at a limited number of points on the site, while
# the properties across the entire site are extremely relevant to the design process. For this
# problem, you will implement a cubic spline that will interpolate the soil layering geometry
# across a cross-section of the site. In other words, you will be interpolating the vertical ($y$)
# coordinate of the top and bottom of each layer at horizontal ($x$) coordinates where there is
# no data (the top of a given layer is also the bottom of the layer above it).
# 
# Your function should take a matrix of data that matches the format in the file `Borings.csv`.
# Before you attempt to write this function, open up the file and look at how the data is
# formatted. Note that the water table and soil layers are measured in terms of depth from
# the surface. This means that you will have to subtract these values from the surface eleva-
# tion to convert them to elevations within a consistent reference frame. Once you've done
# this, you should perform 1D cubic spline interpolation to get new values for the surface,
# water table, and soil layer elevations. Lastly, you should convert these new values for the
# water table and soil layers back into depths and format them in a matrix similar to the input.
# 
# You should also notice that the depth to the clay layer is missing in the data for two of the
# boreholes. This means that the clay layer is absent in the locations of those boreholes. If a
# layer is present in one borehole and absent in the next, your function should use extrapolation
# to map that layer until it ceases to exist. When two layer interfaces intersect (i.e. the
# thickness of a layer becomes zero), this indicates that the layer no longer exists (see Figure
# 5). In other words, your function should find the horizontal end point(s) of a layer which
# does not span the entire cross-section. Past this point, your function should return NaN for
# that layer. Your function should be able to handle missing data in any layer, not just the
# clay layer in the given example. However, you may assume that the data will only be missing
# at the beginning and/or end of the data series (to program a function that would accomplish
# this generically, you would have to parse out the data, which is beyond the scope of this
# problem). You may also assume that any soil layer with missing data is sandwiched between
# two soil layers with no missing data.
# 

# ### 3.1: Interpolating the data
# 
# Write the function `mySoilSpline (borehole_data, site_locations)`
# where site_locations is a $1 \times N$ matrix of horizontal ($x$) locations along the cross section
# (in meters) where you will interpolate the borehole data, `borehole_data` is an $M \times B$ matrix of soil data at the boreholes, and `site_data` is an $M \times N$ matrix of the soil data at
# the interpolated locations, where $M$ is the number of rows of data within `Borings.csv`, $N$
# is the number of site locations, and $B$ is the number of boreholes drilled (i.e. columns in
# `Borings.csv`). Each row of site_data should refer to the same type of information as the
# corresponding row of the data in `Borings.csv`.
# 
# **Hint**: You are free to use Python predefined functions to do the cubic spline interpolation.
# 
# Note that in reality, it is very difficult to accurately predict the soil layering geometry in
# between data points (boreholes). Without any further information, straight lines are usually
# drawn, along with "question marks" indicating high levels of uncertainty. In cases where
# additional accuracy is necessary, the judgment of a geologist or geotechnical engineer with
# experience mapping the local geology is utilized. Sometimes more sophisticated geostatistical
# interpolation techniques are used. For this problem, we use cubic spline interpolation due
# to its simplicity and to arrive at smooth pictures like the one shown in Figure 5.
# 
# <img src="resources/E7_Lab10_5.jpg" style="width: 600px;"/>
# <center>*Figure 5: Example output from the soil viewer*</center>

# In[281]:


def mySoilSpline(bd, site_locations):
    result = [site_locations, bd]
    for row in bd[2:]:
        for i in range(len(row)):
            if row[i] == np.NaN:
                row[i] = 0
        adjustment = row
        row = [x - y for x, y in zip(bd[1], adjustment)]
        spline = interp1d(bd[0], row, kind='cubic')
        result += [spline(site_locations)]
        for n in result[-1]:
            if n==0:
                n = np.NaN
        result[-1] = [x+y for x, y in zip(result[-1], adjustment)]
    return result


# In[282]:


test = [[1300, 1420, 1550, 1600, 1780],
                  [350,  356, 354, 355, 359],
                  [8, 13, 9, 10, 14],
                  [2, 5, 3, 4, 1],
                  [np.NaN, np.NaN, 15, 14, 20],
                  [20, 23, 23, 29, 27],
                  [45, 47, 43, 49, 55]]
x = mySoilSpline(test, [1350, 1450, 1500, 1700])
print(x)


# ### 3.2: Visualizing the interpolated data
# 
# A function has been provided on bCourses that uses a working soil spline function to generate
# a soil profile. These profiles are commonly made to visualize the soil layer geometry along
# an entire cross section. To run successfully, both your spline function and the `Borings.csv`
# data file must be in the same folder. It may be helpful to look at (or modify) this code, but
# it is only there to help you develop your function and will not be used for grading.
