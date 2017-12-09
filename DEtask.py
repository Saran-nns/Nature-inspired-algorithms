# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 14:27:24 2017

@author: Johannes
"""

import numpy as np
import random
import math

# - - - - - - - - - - - - - - - I N D I V I D U A L   D E F I N I T I O N - - - - - - - - - - - - - - - - - - 
class individual():
    def __init__(self, genome, revenue):
        self.genome = genome
        self.revenue = revenue
    def update_revenue():
        return None


#----------------------------------GENERATE POPULATION--------------------------------------


def initialise(agentnmbr):
    """
    input: agentnmbr = number of agents defined by the user (for our problem 20 should be more than sufficient)
    output: either none, or if needed the array of agents. I would suggest however to make the array global.

    creates as many agents as user defines. randomly assigns values to the number of powerplants.
    randomly divides the overall energy created over all the markets
    takes the price of the market (m1,m2,m3) as given as a global variable
    """
    m1 = 0.45
    m2 = 0.25
    m3 = 0.20
    kwh1 = 5
    kwh2 = 10
    kwh3 = 20
    population = []
    for i in range(0, agentnmbr):
        p1 = random.randint(0, 100)
        p2 = random.randint(0, 50)
        p3 = random.randint(0, 3)
        # randomly choosing how many powerplants we have for each agent

        sum = p1 * kwh1 + p2 * kwh2 + p3 * kwh3
        # print(sum)
        s1 = random.randint(0, sum)
        sum = sum - s1
        # print(sum)
        s2 = random.randint(0, sum)
        sum = sum - s2
        # print(sum)
        s3 = sum
        # assigning random values for each market, depending on the overall produced energy
        new_agent = (p1, p2, p3, s1, s2, s3, m1, m2, m3)
        # print(new_agent)
        population.append(new_agent)

    # print(population)
    return population
"""# - - - - - - - - - - - - - - - P R O B L E M  &  P A R A M E T E R   D E S C R I P T I O N - - - - - - - - - -
class problem():
    class powerplant():
        def __init__(self, planttype):
            if planttype == 1:
                self.power = 50000
                self.cost = 10000
                self.amount = 100
                
            if planttype == 2:
                self.power = 600000
                self.cost = 80000
                self.amount = 50
                
            if planttype == 3:
                self.power = 4000000
                self.cost = 400000
                self.amount = 3
        None
    def market_model():
        None
    def plant_cost_model():
        None
    def 
"""

# - - - - - - - - - - - - - - - P O P U L A T I O N   I N I T I A L I Z A T I O N - - - - - - - - - - - - - - -

# - - - - - - - - - - - - - - - M A I N - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def __MAIN__():
    """
    1. Handle user input
    2. Mainloop:
        a initialize population
        b donor selection
            c trial generation
            d Selection
            e update Population
        f Update termination condition value
    3. return best after termination
    """
# - - - - - - - - - - - - - - - D O N O R   S E L E C T I O N - - - - - - - - - - - - - - - - - - - - - - - - 


def generate_newgenome():
    """
    Create energy list within max range
    Planned amount of energy sold
    Price for market of type 1

    newgenome = []

    # Energy produced with plants of type i
    newgenome.append(np.random.randint(1, 50000))  # e1
    newgenome.append(np.random.randint(1, 6000000))  # e2
    newgenome.append(np.random.randint(1, 4000000))  # e3


    # Energy planned to be sold to market
    newgenome.append(np.random.randint(1, 50000))  # s1
    newgenome.append(np.random.randint(1, 6000000))  # s2
    newgenome.append(np.random.randint(1, 4000000))  # s3

    # Price for market of type
    newgenome.append(np.random.uniform(0, 0.5))  # p1
    newgenome.append(np.random.uniform(0, 0.3))  # p2
    newgenome.append(np.random.uniform(0, 25))  # p3

    # newgenome = np.random.randint(0,5,5).tolist()
    # newgenome = [float(gene) for gene in newgenome]

    # return newgenome

# print(generate_newgenome())

def generate_new_pop(num_pop):

    pop = []
    for _ in range(num_pop):
        pop.append(generate_newgenome())

    return pop
"""

pop = initialise(5)

print("POPULATION",pop)

# - - - - - - - - - - - - - - - M A I N - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def __MAIN__():
    """
    1. Handle user input
    2. Mainloop:
        a initialize population
        b donor selection
            c trial generation
            d Selection
            e update Population
        f Update termination condition value
    3. return best after termination
    """
    pass
# - - - - - - - - - - - - - - - D O N O R   S E L E C T I O N - - - - - - - - - - - - - - - - - - - - - - - -

# GENERATE TARGET AND DONOR PAIRS FROM THE POPULATION AND
def donor_selection(population, scaling_factor):
    """
    INPUT: Population, a list of objects containing vectors as a representation for genome projecting into the search-space
    OUTPUT: A list of tuples. Each tuple contains the target at position 0  donor objects at position 1
    """
    target_position = 0
    target_and_donors_list = []
    #this is the output list, which contains tuples with the target at position 1 and all donor individuals at 2
    while target_position != len(population):
        target_donors = population.copy()
        target = population[target_position]
        del target_donors[target_position]

        # Randomly select the base for each target
        base_idx = np.random.randint(0,len(target_donors))
        base = target_donors[base_idx]
        del target_donors[base_idx]

        #Select two vectors randomly
        x1_idx = np.random.randint(0,len(target_donors))
        x1 = target_donors[x1_idx]
        del target_donors[x1_idx]

        x2_idx = np.random.randint(0,len(target_donors))
        x2  = target_donors[x2_idx]
        del target_donors[x2_idx]

        # COMPUTE DIFFERENCE DONOR
        # Subtract two vectors x1 and x2
        sub_dummy = [x - y for x,y in zip(x1,x2)]
        mul_dummy = np.dot(scaling_factor,sub_dummy)
        donor = [b + x for b, x in (zip(base, mul_dummy))]

        target_and_donors = (target, donor)
        target_and_donors_list.append(target_and_donors)
        target_position += 1
    return target_and_donors_list

targets_and_donors = donor_selection(pop,0.5)
print(targets_and_donors)


# - - - - - - - - - - - - - - - TRIAL   S E L E C T I O N - - - - - - - - - - - - - - - - - - - - - - - -

# TRIAL GENERATION FOR SINGLE TARGET,DONOR PAIR
# LOOP OVER this function in targets_and_donors list to get the list of trials for entire population

def trial_generation(target_and_donor,CR = 0.5):

    """

    :param target_and_donor: Tuple of (target,donor) pairs
    :param CR: Crossover ratio
    :return: trial
    """

    target,donor = target_and_donor[0],target_and_donor[1]
    z = []

    for i in range(len(target)):
        r = np.random.uniform(0,1)
        if r<= CR:
            z.append(donor[i])
        else:
            z.append(target[i])
    return z


z = trial_generation(targets_and_donors[0])
print(z)
# - - - - - - - - - - - - - - - PLANT COST MODEL - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

def cost(x, kwhPerPlant, costPerPlant, maxPlants):
    """ 
    calculates the cost we will have to build the amount of plants that is needed.
    
    INPUT
    - x (desired amount of energy)
    - kwhPerPlant (how much energy one plant provides)
    - maxPlants (maximum amount of plants we can have)

    """
    
    # if x non-positive, return 0
    if(x <= 0):
        return 0
    
    #if x larger than possible generation, return infinite
    if(x > kwhPerPlants * maxPlants):
        return float.("inf")
    
    #otherwise find amount of plants needed to generate x
    plantsNeeded = math.ceil(x / kwhPerPlant)
    
    #return cost (amount of plants * cost per plant)
    return plantsNeeded * costPerPlant



# - - - - - - - - - - - - - - - U S E R   I N P U T - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def user_input():
    return None
---