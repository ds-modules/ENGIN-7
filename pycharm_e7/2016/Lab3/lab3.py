import numpy as np
import math
import scipy.io as sio

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

    mat_contents = sio.loadmat('EV_Comparison.mat')
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

    GHG_index, Cost_index, annual_cost, annual_emmisions = \
        {'CA': (min_GHG_index_ca, cost_index_ca, annual_cost_ca, annual_GHG_emisions_ca),
         'KS': (min_GHG_index_ks, cost_index_ks, annual_cost_ks, annual_GHG_emisions_ks),
         'FL': (min_GHG_index_fl, cost_index_fl, annual_cost_fl, annual_GHG_emisions_fl)}[state]

    GHG_vehicle = car_make[GHG_index][0][0]
    GHG_model = car_model[GHG_index][0][0]
    Cost_vehicle = car_make[Cost_index][0][0]
    Cost_model = car_model[Cost_index][0][0]

    GHG = {'Vehicle': GHG_vehicle+' '+GHG_model, 'Cost': annual_cost[GHG_index], 'GHG': annual_emmisions[GHG_index]}
    Cost = {'Vehicle': Cost_vehicle+' '+Cost_model, 'Cost': annual_cost[Cost_index], 'GHG': annual_emmisions[Cost_index]}

    return {'Name': consumerName, 'State': state, 'GHG_Recommendation': GHG, 'Cost_Recommendation': Cost}


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
        string = "The {} costs ${:.2f} per year less but emits {} g CO2e per year more than the {}."\
            .format(v1, cost, ghg, v2)
    else:
        string = "The {} is the best option for {} because it costs ${:.2f} per year less and emits {} g CO2e per year " \
             "less than the {}.".format(v1, name, cost, ghg, v2)

    return string