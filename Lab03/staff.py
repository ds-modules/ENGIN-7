
# coding: utf-8

# # E7: Introduction to Computer Programming for Scientists and Engineers

# ## Lab Assignment 3

# For each question, you will have to fill in one or more Python functions. We provide an autograder with a number of test cases that you can use to test your function. Note that the fact that your function works for all test cases thus provided does necessarily guarantee
# that it will work for all possible test cases relevant to the question. It is your responsibility
# to test your function thoroughly, to ensure that it will also work in situations not covered
# by the test cases provided

# In[1]:


# Please run this cell, and do not modify the contets
import numpy as np
import math
import scipy.io as sio
np.seterr(all='ignore');
# %run lab3_ag.py


# ## Question 1: Array vs. Matrix Multiplication
# 
# Write a "smart" function that multiplies two arrays together in the manner that makes
# the most sense for their given dimensions.
# 
# This function should return the result of multiplying the two arrays together using
# matrix multiplication if their inner dimensions are the same (i.e. `m1` is an $M$ x $N$ matrix
# and `m2` is a $N$ x $P$ matrix). Alternatively, it should return the result of multiplying
# the two arrays together using element-wise multiplication if the arrays have the same
# dimensions in both directions (i.e. `m1` is an $M$ x $N$ matrix and `m2` is a $M$ x $N$ matrix).
# In the situation that either multiplication can be used, it should return the string
# multiplication ambiguous, and if neither multiplication can be used, it should return
# the string no valid multiplication. The function should consider multiplying `m1`
# by `m2`, and not consider the possibility of multiplying `m2` by `m1`. The function should
# also be able to handle the case when one or both inputs are scalar, and return the
# appropriate product.

# In[2]:


def mySmartMultiply(m1, m2):
    """
    >>> mySmartMultiply(1,2)
    2
    >>> mySmartMultiply(np.array([[2,3,3],[4,5,5]]),np.array([[1,2],[3,4],[5,5]]))
    array([[26, 31],
           [44, 53]])
    >>> mySmartMultiply(np.array([[2,3],[3,4],[5,5]]),np.array([[1,2],[3,4],[5,5]]))
    array([[ 2,  6],
           [ 9, 16],
           [25, 25]])
    >>> mySmartMultiply(np.array([[2,5],[8,3]]),np.array([[5,1],[3,2]]))
    'multiplication ambiguous'
    >>> mySmartMultiply(np.array([[2],[8]]),np.array([[5,1],[3,2]]))
    'no valid multiplication'
    """
    if np.isscalar(m1) or np.isscalar(m2):
        return m1*m2

    size_m1 = m1.shape
    size_m2 = m2.shape
    # print(size_m1,size_m2)
    if size_m1[1] == size_m2[0]:
        if np.array_equal(size_m1, size_m2):
            result = 'multiplication ambiguous'
        else:
            result = np.dot(m1, m2)
    else:
        if np.array_equal(size_m1, size_m2):
            result = m1*m2
        else:
            result = 'no valid multiplication'

    return result


# ## Question 2: Subcritical vs. Supercritical Open Channel Flow
# 
# In the field of open channel hydraulics, 
# ow in a channel or a river can be classified using
# a dimensionless number called the Froude number. The Froude number represents the
# speed of the flow relative to the speed that a wave travels across the water's surface,
# and can be calculated as:
# 
# $$ Fr = \frac{u}{\sqrt{gh}} $$
# 
# where $u$ is the 
# fluid velocity, $g$ is the gravitational constant, and $h$ is the depth of
# the flow. The Froude number then determines when a 
# flow is supercritical, critical, or
# subcritical using the following criteria:
# 
# $$\begin{align} 
# Fr &> 1, && \text{supercritical} \\
# Fr &= 1, && \text{crtical} \\
# Fr &< 1, && \text{subcritical}
# \end{align}$$

# Write a function that classifies a given 
# flow as supercritical, critical, or subcritical.
# 
# `unitsys` is an input that describes the unit system that is being used for the calculation,
# either metric or imperial. Note that you should use a gravitational constant of
# 
# $g = 9.81  \text{m}/s^2$ for metric units
# 
# $g = 32.2 \text{ft}/s^2$ for imperial units
# 
# Computer calculations often generate small errors when making calculations, called
# floating point errors. These errors occur because many fractions cannot be exactly
# represented in the computer's native binary format. We will discuss this more later in the
# course. To account for this, your function should only consider the first 3 decimal
# places when comparing the Froude number values.

# In[3]:


def classifyFlow(u, h, unitsys):
    """
    >>> classifyFlow(5, .5, 'metric')
    'supercritical'
    >>> classifyFlow(1, 10, 'imperial')
    'subcritical'
    >>> classifyFlow(15.01, 7, 'imperial')
    'critical'
    """

    if unitsys == 'metric':
        g = 9.81
    else:
        g = 32.2

    froude = u/math.sqrt(g*h)
    froude = round(froude, 3)
    # print(froude)
    if math.isclose(froude, 1.0):
        return 'critical'
    elif froude < 1.0:
        return 'subcritical'
    else:
        return 'supercritical'


# ## Question 3: Sprite Collisions
# 
# You have seen how Snap! can be used to make animations and computer games. Here
# you will consider the programming decisions made for collisions between sprites using
# Matlab. Pretend you are programming an arcade style video game and have already
# written code that checks for collisions between sprites during every step of the game.
# Now, all that remains is for you to program a function that tells your script how to
# handle collisions between different types of sprite during the game.
# 
# The function will take in two inputs, `sprite1` and `sprite2`
# where both `sprite1` and `sprite2` could be any of 'laser', 'rocket', 'player',
# 'fighter', or 'mothership'. The function should return a triple with elements
# that represent the points tallied, whether sprite1 should be destroyed, and whether
# sprite2 should be destroyed, in that order. Note that the points tallied are a result of
# the type of collision, and not assigned to either sprite. Whether or not a sprite should
# be destroyed should be represented as a double with one representing that the sprite
# should be destroyed and zero representing that a sprite should not be destroyed.
# 
# Your function should represent the following behavior:
# 1. Lasers destroy rockets, players, and ghters but are destroyed when colliding with
# the mothership.
# 2. Rockets destroy both sprites when colliding with other rockets, players, fighters,
# or the mothership.
# 3. The player destroys both sprites when colliding with fighters or the mothership.
# 4. No other collisions have any eect.
# 5. Each fighter destroyed is worth 1 point.
# 6. Destroying the mothership is worth 20 points.
# 
# Note that your function should be able to handle collisions no matter what order the
# sprites are entered. i.e. Both collision('player','fighter') and
# collision('fighter','player') are valid functions calls that should be handled
# appropriately.

# In[4]:


def collisions(sprite1, sprite2):
    """
    >>> collisions('rocket', 'player')
    [0, 1, 1]
    >>> collisions('fighter', 'laser')
    [1, 1, 0]
    >>> collisions('mothership', 'fighter')
    [0, 0, 0]
    >>> collisions('rocket', 'mothership')
    [20, 1, 1]
    >>> collisions('laser', 'rocket')
    [0, 0, 1]
    >>> collisions('player', 'fighter')
    [1, 1, 1]
    """
    result = [0,0,0]
    laser = 0
    rocket = 0
    player = 0
    fighter = 0
    mothership = 0
    if sprite1 == 'laser':
        laser += 1
    elif sprite1 == 'rocket':
        rocket += 1
    elif sprite1 == 'player':
        player += 1
    elif sprite1 == 'fighter':
        fighter += 1
    else:
        mothership += 1

    if sprite2 == 'laser':
        laser += 1
    elif sprite2 == 'rocket':
        rocket += 1
    elif sprite2 == 'player':
        player += 1
    elif sprite2 == 'fighter':
        fighter += 1
    else:
        mothership += 1

    if (laser == 1) and (rocket == 1 or player == 1 or fighter == 1):
        if sprite1 == 'laser':
            result[2] = 1
        else:
            result[1] = 1

        if fighter == 1:
            result[0] = 1

    if (laser == 1) and (mothership == 1):
        if sprite1 == 'laser':
            result[1] = 1
        else:
            result[2] = 1

    if (rocket == 2) or (rocket == 1 and (player == 1 or fighter == 1 or mothership == 1)):
        result[1] = 1
        result[2] = 1

        if fighter == 1:
            result[0] = 1
        elif mothership == 1:
            result[0] = 20

    if player == 1 and (fighter == 1 or mothership == 1):
        result[1] = 1
        result[2] = 1

        if fighter == 1:
            result[0] = 1
        elif mothership == 1:
            result[0] = 20

    return result


# ## Question 4: To EV or not to EV.
# 
# Part I: Consumer Vehicle Recommendations
# 
# The transportation industry accounts for nearly one third of greenhouse gas (GHG)
# emissions in the United States. As the United States aims to curb its emissions, it will
# be crucial to wean the transportation industry off of oil. Electric vehicles will play an
# ever important role in the electrification of transportation. Consumers now need to
# make smart economic decisions on whether or not investing in the higher capital costs
# of an electric vehicle (EV) is financially viable as compared to fuel efficient hybrids or
# standard internal combustion engine (ICE) cars.
# 
# Your task is to develop a function that will recommend both a low-emitting and
# a cost-conscious vehicle to a consumer given their location (state), annual kilome-
# ters traveled, and annual budget (USD 2015). 
# 
# The function will take in the inputs: `consumerName, state, annualkmTraveled, annualBudget`
# 
# Note that `consumerName` and `state` are of type char, while `annualkmTraveled` and
# `annualBudget` are of type double.
# 
# This function will return a dictionary of the following form:
# 
# `EDU >> consumer =
# Name: 'Janet'
# State: 'CA'
# GHG Recommendation: [dictionary]
# Cost Recommendation: [dictionary]`
# 
# `consumer.GHGRecommendation
# ans = Vehicle: 'BMW i3'
# Cost: 2560
# GHG: 1370000`
# 
# `consumer.CostRecommendation
# ans = Vehicle: 'Chevrolet Spark'
# Cost: 1410
# GHG: 2661000`

# The function should be able to:
# 
# (a) Manipulate the vehicle data (in the file EV_Comparison.mat) and perform calcula-
# tions using the given inputs. Values for California (CA), Kansas (KS), and Florida
# (FL) are provided for each vehicle. Notice that due to the different gas prices,
# electricity prices, and electricity generation emissions in each state, the carbon
# footprint and normalized cost values vary signicantly. For example, Kansas has
# more coal generation than the other states, which means that the electricity used
# to power the EVs generates more GHG emissions. For this reason, GHG emissions for EVs are significantly higher in Kansas than the other states. Emissions attributed to the manufacturing of the vehicle (life-cycle carbon footprint) are
# captured in the carbon footprint values. Also note that the normalized cost rep-
# resents the net present value of purchasing, maintaining, running, and salvaging
# the vehicle spread over a lifetime of 12 years. The societal cost of carbon, an ex-
# ternality in economic terms, is also captured in the normalized cost. For a given
# consumer, use the following equations to calculate the annual GHG emissions and
# annual Cost of each vehicle based on the consumer's state.
# 
# - Annual GHG Emissions ($\frac{gC0_{2,e})}{year}$) = Total Life-Cycle Carbon Footprint ($\frac{gCO_{2,e}}{km}$) x Annual km Traveled ($\frac{km}{year}$)
# - Annual Cost ($\frac{\$}{year}$) = Normalized Cost ($\frac{\$}{km}$) x Annual km Traveled ($\frac{km}{year}$)
# 
# (b) Use branching statements (if-statements) to determine the GHG recommendation
# and the Cost recommendation for the consumer.
# 
# - The GHG recommendation should be the vehicle with the lowest annual GHG emissions for the consumer based on the consumer's state and annual km
# traveled.
# - The Cost recommendation should be the vehicle whose annual cost is closest to the consumer's budget. NOTE: this is not necessarily the cheapest car for the consumer, but rather the car that is closest to the consumer's budget without exceeding it. For example, consider a consumer with an annual budget of \$5,000 per year wanting to purchase a higher-end car within his or her budget. If two cars have an annual cost of \$3,000 and \$4,500 respectively, your function should recommend the \$4,500 car since it is closest to the consumer's budget without exceeding it.
# 
# (c) Output a dictionary including the consumer's name, the GHG recommendation
# (including the vehicles make and model, the annual cost of the
# vehicle, and the annual GHG emissions), and the Cost recommendation (including
# the vehicle's make and model, the annual cost of the vehicle, and the annual GHG
# emissions). Make sure your dictionary key names match exactly the format of the
# example given above.

# NOTE: This function needs the information in the file EV_Comparison.mat in order to
# work properly. You can use the load command inside the function to access this data.
# When your function is being graded, this file will be available in the same directory
# that your function is in, so do not include a path in the call to load. In other words,
# load('resources/EV_Comparison.mat') is okay, but load('C:/Users/Aditya/E7/Lab03/resources/EV_Comparison.mat') is NOT okay.

# In[5]:


def vehicleRecommendation(consumerName, state, annualkmTraveled, annualBudget):
    """
    >>> vehicleRecommendation('Brad', 'CA', 10000, 2000)
    {'Name': 'Brad', 'State': 'CA', 'GHG_Recommendation': {'Vehicle': 'BMW i3', 'Cost': 2560.0, 'GHG': 1370000.0}, 'Cost_Recommendation': {'Vehicle': 'Toyota Tacoma', 'Cost': 1990.0, 'GHG': 3765000.0}}
    >>> vehicleRecommendation('Janet', 'KS', 15000, 6090)
    {'Name': 'Janet', 'State': 'KS', 'GHG_Recommendation': {'Vehicle': 'BMW i3', 'Cost': 3870.0, 'GHG': 3105000.0}, 'Cost_Recommendation': {'Vehicle': 'Tesla Model S', 'Cost': 6090.0, 'GHG': 3490500.0}}
    >>> vehicleRecommendation('Stacy', 'FL', 18000, 7500)
    {'Name': 'Stacy', 'State': 'FL', 'GHG_Recommendation': {'Vehicle': 'BMW i3', 'Cost': 4626.0, 'GHG': 3087000.0}, 'Cost_Recommendation': {'Vehicle': 'Tesla Model S', 'Cost': 7290.0000000000009, 'GHG': 3394800.0}}
    >>> vehicleRecommendation('Tina', 'CA', 20000, 5000)
    {'Name': 'Tina', 'State': 'CA', 'GHG_Recommendation': {'Vehicle': 'BMW i3', 'Cost': 5120.0, 'GHG': 2740000.0}, 'Cost_Recommendation': {'Vehicle': 'Honda Accord Hybrid', 'Cost': 4340.0, 'GHG': 4328000.0}}
    """

    mat_contents = sio.loadmat('resources/EV_Comparison.mat')
    # print(mat_contents)

    annual_GHG_emisions_ca = annualkmTraveled * np.ndarray.flatten(mat_contents['total_life_cycle_carbon_footprint_ca'])
    annual_GHG_emisions_ks = annualkmTraveled * np.ndarray.flatten(mat_contents['total_life_cycle_carbon_footprint_ks'])
    annual_GHG_emisions_fl = annualkmTraveled * np.ndarray.flatten(mat_contents['total_life_cycle_carbon_footprint_fl'])

    annual_cost_ca = annualkmTraveled * np.ndarray.flatten(mat_contents['normalized_cost_ca'])
    annual_cost_ks = annualkmTraveled * np.ndarray.flatten(mat_contents['normalized_cost_ks'])
    annual_cost_fl = annualkmTraveled * np.ndarray.flatten(mat_contents['normalized_cost_fl'])

    min_GHG_index_ca = np.argmin(annual_GHG_emisions_ca)
    min_GHG_index_ks = np.argmin(annual_GHG_emisions_ks)
    min_GHG_index_fl = np.argmin(annual_GHG_emisions_fl)

    cost_difference_ca = annualBudget - annual_cost_ca
    current_winner_ca = 1e6
    cost_index_ca = -1

    for i in range(0, len(cost_difference_ca)):
        if cost_difference_ca[i] >= 0 and cost_difference_ca[i] < current_winner_ca:
            current_winner_ca, cost_index_ca = cost_difference_ca[i], i

    cost_difference_ks = annualBudget - annual_cost_ks
    current_winner_ks = 1e6
    cost_index_ks = -1

    for i in range(0, len(cost_difference_ks)):
        if cost_difference_ks[i] >= 0 and cost_difference_ks[i] < current_winner_ks:
            current_winner_ks, cost_index_ks = cost_difference_ks[i], i


    cost_difference_fl = annualBudget - annual_cost_fl
    current_winner_fl = 1e6
    cost_index_fl = -1

    for i in range(0, len(cost_difference_fl)):
        if cost_difference_fl[i] >= 0 and cost_difference_fl[i] < current_winner_fl:
            current_winner_fl, cost_index_fl = cost_difference_fl[i], i

    car_make = mat_contents['car_make']
    car_model = mat_contents['car_model']

    GHG_index, Cost_index, annual_cost, annual_emmisions =         {'CA': (min_GHG_index_ca, cost_index_ca, annual_cost_ca, annual_GHG_emisions_ca),
         'KS': (min_GHG_index_ks, cost_index_ks, annual_cost_ks, annual_GHG_emisions_ks),
         'FL': (min_GHG_index_fl, cost_index_fl, annual_cost_fl, annual_GHG_emisions_fl)}[state]

    GHG_vehicle = car_make[GHG_index][0][0]
    GHG_model = car_model[GHG_index][0][0]
    Cost_vehicle = car_make[Cost_index][0][0]
    Cost_model = car_model[Cost_index][0][0]

    GHG = {'Vehicle': GHG_vehicle+' '+GHG_model, 'Cost': annual_cost[GHG_index], 'GHG': annual_emmisions[GHG_index]}
    Cost = {'Vehicle': Cost_vehicle+' '+Cost_model, 'Cost': annual_cost[Cost_index], 'GHG': annual_emmisions[Cost_index]}

    return {'Name': consumerName, 'State': state, 'GHG_Recommendation': GHG, 'Cost_Recommendation': Cost}


# Part II: Consumer Vehicle Comparisons
# 
# You've written a function that can make both low-emitting and cost-conscious vehicle
# recommendations; however, consumers may want to have a single recommendation
# made for them.
# 
# Write a function that takes as input consumerStruct (same structure format as in Part I) and
# return a string that states the cheaper of the two recommendations and the diverence in
# GHG emissions. The output string has the following format
# where italics indicate words or values that change depending on the recommendation:
# 
# - The $Vehicle1$ costs \$xx.xx per year less but emits $xx$ g CO2e per year more than the $Vehicle2$.
# 
# 
# If a vehicle is cheaper and has lower GHG emissions, return the string:
# - The $Vehicle1$ is the best option for $consumerName$ because it costs $\$xx.xx$ per year less and emits $xx$ g CO2e per year less than the $Vehicle2$.
# 
# For example:
# - 'The Toyota Sienna costs \$1000.00 per year less but emits 100 g CO2e per year more than the Toyota Sequoia.'
# - 'The Toyota Prius is the best option for Joe Schmoe because it costs $100.00 per year less and emits 100 g CO2e per year less than the Toyota Sienna.'

# In[6]:


def vehicleComparison(rec):
    """
    >>> vehicleComparison(vehicleRecommendation('Brad', 'CA', 10000, 2000))
    'The Toyota Tacoma costs $570.00 per year less but emits 2395000 g CO2e per year more than the BMW i3.'
    >>> vehicleComparison(vehicleRecommendation('Janet', 'KS', 15000, 6090))
    'The BMW i3 is the best option for Janet because it costs $2220.00 per year less and emits 385500 g CO2e per year less than the Tesla Model S.'
    >>> vehicleComparison(vehicleRecommendation('Stacy', 'FL', 18000, 7500))
    'The BMW i3 is the best option for Stacy because it costs $2664.00 per year less and emits 307800 g CO2e per year less than the Tesla Model S.'
    >>> vehicleComparison(vehicleRecommendation('Tina', 'CA', 20000, 5000))
    'The Honda Accord Hybrid costs $780.00 per year less but emits 1588000 g CO2e per year more than the BMW i3.'
    """
    name = rec['Name']
    GHG_cost = rec['GHG_Recommendation']['Cost']
    GHG_GHG = rec['GHG_Recommendation']['GHG']
    GHG_vehicle = rec['GHG_Recommendation']['Vehicle']

    cost_cost = rec['Cost_Recommendation']['Cost']
    cost_GHG = rec['Cost_Recommendation']['GHG']
    cost_vehicle = rec['Cost_Recommendation']['Vehicle']

    v1, cost, ghg, v2 = '', '', '', ''
    switch = False

    if GHG_cost < cost_cost and GHG_GHG < cost_GHG:
        v1, cost, ghg, v2 = GHG_vehicle, cost_cost-GHG_cost, cost_GHG-GHG_GHG, cost_vehicle
        switch = True
    elif GHG_cost > cost_cost and GHG_GHG > cost_GHG:
        v1, cost, ghg, v2 = cost_vehicle, -cost_cost + GHG_cost, -cost_GHG + GHG_GHG, GHG_vehicle
        switch = True
    elif GHG_cost < cost_cost:
        v1, cost, ghg, v2 = GHG_vehicle, cost_cost - GHG_cost, -cost_GHG + GHG_GHG, cost_vehicle
    else:
        v1, cost, ghg, v2 = cost_vehicle, -cost_cost + GHG_cost, cost_GHG - GHG_GHG, GHG_vehicle

    ghg = int(ghg)

    if not switch:
        string = "The {} costs ${:.2f} per year less but emits {} g CO2e per year more than the {}."            .format(v1, cost, ghg, v2)
    else:
        string = "The {} is the best option for {} because it costs ${:.2f} per year less and emits {} g CO2e per year "              "less than the {}.".format(v1, name, cost, ghg, v2)

    return string

