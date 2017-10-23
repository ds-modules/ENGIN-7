
# coding: utf-8

# # E7: Introduction to Computer Programming for Scientists and Engineers

# ## Lab Assignment 1

# For each question, you will have to fill in one or more Python functions. We provide an autograder with a number of test cases that you can use to test your function. Note that the fact that your function works for all test cases thus provided does necessarily guarantee
# that it will work for all possible test cases relevant to the question. It is your responsibility
# to test your function thoroughly, to ensure that it will also work in situations not covered
# by the test cases provided

# In[1]:


# Please run this cell, and do not modify the contets
import math
import numpy as np
import cmath
import scipy.io as sio
import matplotlib.pyplot as plt
np.seterr(all='ignore');
# %run lab1_ag.py


# ## Question 1: Using Python as a calculator

# 1. Define variables $a = 3, b = -6, c = 4$, and $x = 2$
# 2. For each of the quantities $E_1$ through $E_10$, construct a one-line Python expression that computes the value and assigns it to a variable. Your assignments should give appropriate values for $E_1$ throught $E_10$ regardless of the values of $a, b, c$, and $x$ (i.e. you should use the variable names instead of their numerical values).
# 
# In Python, we will use variable names `E1` through `E10` to store the values $E_1$ through $E_10$. Definitions of the variables `E1` through `E10` have been started for you in the template.

# $$\text{i.} \quad E_1 = \sqrt{a^2+b^2+c^2}$$
# 
# $$\text{ii.} \quad E_2 = \frac{-b-\sqrt{b^2-4ac}}{2a}$$
# 
# $$\text{iii.} \quad E_3 = \ln(3x-a)$$
# 
# $$\text{iv.} \quad E_4 = \log_{10} (3 \left|x\right|+\frac{c}{5})$$
# 
# $$\text{v.} \quad E_5 = (ax+\frac{ab}{c})^{1/3}$$
# 
# $$\text{vi.} \quad E_6 = \frac{x^2+1}{(ax-1)\left|b-e^x\right|}$$
# 
# $$\text{vii.} \quad E_7 = (cos(\frac{\sqrt{a}}{3}\pi))^2+\cos(\frac{\sqrt{a}}{3}\pi)^2$$
# 
# $$\text{viii.} \quad E_8 = e^{\pi\sqrt{-1}}$$
# 
# $$\text{viv.} \quad E_9 = \arccos(\cos(x))$$
# 
# $$\text{x.} \quad E_{10} = \frac{a+2c}{\sin(\frac{b+2c}{\sqrt{a^2+b^2+c^2}})}$$
# 

# In[2]:


def q1():
    a, b, c, x = 3., -6., 4., 2.
    E1 = math.sqrt(a*a+b*b+c*c)
    E2 = (-b-cmath.sqrt(b*b-4*a*c))/(2*a)
    E3 = math.log(3*x-a)
    E4 = math.log(3*abs(b)+c/5,10)
    E5 = math.pow(a*x+a*b/c,1./3)
    E6 = (x*x+1)/((a*x-1)*abs(b-math.exp(x)))
    E7 = math.cos(math.sqrt(a)/3*math.pi)**2 +          math.cos((math.sqrt(a)/3*math.pi)**2)
    E8 = cmath.exp(cmath.pi*cmath.sqrt(-1))
    E9 = math.acos(math.cos(x))
    E10 = (a+2*c)/(math.sin((b+2*c)/math.sqrt(a**2+b**2+c**2)))

    return E1,E2,E3,E4,E5,E6,E7,E8,E9,E10


# In[3]:


q1()


# ## Question 2: Football
# 
# In this question you will be plotting the number of wins and losses by the Cal Football
# team from 1886-2015.

# a. The table shows the win-loss record for the Cal football team from 2007-2015. Create three variables in Python: Year, Wins, and Losses, containing data from the corresponding columns in the table.
# 
# [//]: # (You can save yourself some typing using the shortcut of 2007:2015 to dene Year. When you are done with thisstep, each variable should be a vector (1-D array) containing 9 data points.)
# 
# | Year | Wins | Losses |
# |------|------|--------|
# | 2007 | 7    | 6      |
# | 2008 | 9    | 4      |
# | 2009 | 8    | 2      |
# | 2010 | 5    | 7      |
# | 2011 | 7    | 6      |
# | 2012 | 3    | 9      |
# | 2013 | 1    | 11     |
# | 2014 | 5    | 7      |
# | 2015 | 8    | 5      |

# b. The correct number of losses in 2009 should be 5, not 2. Correct the 3rd entryof the losses data array to 5. You can manually reassign Losses(3) = 5 without retyping any of the other data.

# c. The file CalFB_HistoricalData.mat, which is available on bCourses, contains
# wins and losses data (as well as other data) for the years 1886-2006. Load this
# data (use the command load) and create variables which contain all data from
# 1886-2015. The file contains variables `Y` for year, `W` for wins, and `L` for losses. You
# need to create new variables `Y_all`, `W_all`, and `L_all` using both the variables
# loaded from the file and the variables you already defined.
# The commands size and who might be helpful. Pay attention to the number of
# rows and columns when you're concatenating. 
# 
# [//]: # 
# 
# (The source of this data is [here](http://www.calbears.com/fls/30100/old_site/pdf/m-footbl/pdf-07FB151to190-072007.pdf?DB_OEM_ID=30100). -> ERROR THE LINK IS OUTDATED? )

# d. Plot wins and losses for the years 1886-2015 using the variables `Y_all`, `W_all`, and
# `L_all`. 
# 
# Use the MATLAB command help to learn about the commands plot,
# xlabel, ylabel, title, legend, and axis. -> Python commands??
# 
# Construct and modify a plot in steps
# as you read about each command. Choose a different color and line style (solid,
# dashed, dot-dashed, etc.) for showing `Wins` and `Losses` data. Add a legend box,
# and adjust it as necessary so it does not cover up the data. The vertical axis on
# your plot should be set to range from 0 to 15.

# e. Add text to your figure with your name, SID, lab section number, and name of
# your GSI. 
# 
# For information about how to do this, type help text into MATLAB.
# 
# Copy and paste your figure to a separate file which can be converted to a pdf (e.g.
# a Word document). You will add more figures to your file in the next question.

# In[6]:


def q2():
    # Q2A
    year = list(range(2007,2016))
    wins, losses = [7,9,8,5,7,3,1,5,8], [6,4,2,7,6,9,11,7,5]
    # print(year, wins, losses)

    # Q2B
    losses[2] = 5

    # Q2C
    mat_contents = sio.loadmat('resources/CALFB_HistoricalData.mat')
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


# In[7]:


q2()


# ## Question 3. Using Scratch
# 
# Here, you will get your first taste of writing a full computer program using a high-
# level block-based computer language called Scratch. (See http://scratch.mit.edu
# for more info if you're curious.) You will follow a tutorial which will teach you what
# to do, and at the end you'll be able to create something on your own. (Technically,
# this tutorial uses a language called Blockly, which is very similar to Scratch. We will
# actually use Scratch next week.)

# a. First, watch this video with Mark Zuckerberg explaining how loops work:
# https://www.youtube.com/watch?v=mgooqyWMTxk
# 
# b. Now watch this video with Bill Gates explaining how if statements work:
# https://www.youtube.com/watch?v=m2Ux2PnJe6E
# 
# c. Complete the Hour of Code Artist activity found here (you will need to sign up):
# http://studio.code.org/join/TXLHDX
# 
# Follow the steps (in sequence) to complete parts 1-8 of the Artist activity. If you
# need to see the instructions for an exercise again, click in the lower left part of
# your browser window. If you feel stuck, test out your code by hitting Run (in the
# lower left) and look at the tips or hints provided.

# (d) In part 9, modify the code to create a grid of triangles instead of hexagons. The
# triangles should all be touching but not overlapping, so you will need to figure
# out the distances you need to move, etc. (There are several possibilities - just
# make sure your final result is a grid of triangles that are all touching but not
# overlapping.) Take a screenshot of your final image. Add this screenshot to the
# file with the figure from the previous question. The screenshot shold show
# the entire browser window, including the work area, the picture, and
# the block code.
# 
# (e) Click on the purple button that says ''Show Code'' to see the source code written
# in JavaScript (note what it says at the top of the pop up window!). This is all
# code that you wrote!! JavaScript uses different syntax from Matlab (which we are
# in the process of learning) but you should still be able to get the general idea.
# 
# (f) In Part 10, use what you learned to create your own unique design. You should
# use one function and at least one repeat block. Take a screenshot of your final
# browser window (showing the final result and the block code) and add it to the
# file with the other two images.
#     
# (g) When you're done, feel free to explore other Hour of Code modules!

# ## Submission Instructions
# 
# TBD
