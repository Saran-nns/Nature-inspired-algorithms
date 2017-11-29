# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 12:33:10 2017
@author: JoJo, yj, tn
"""
import numpy as np
import random
from numpy.random import choice
import heapq

# Global constants
num_cities = 150  # Should be based on row /column length of .tsp contents. For sake of time, just hard coded!
alpha = 1
beta = 1
rho = 0.5


class Ant:
    def __init__(self):
        """

        initialize an ant, to traverse the map
        possible_locations -> a list of possible locations the ant can travel to
        path -> [1,2,5,3,4,6,1] a list of integers, where each integer represents a city, and the path[i] to the path[i+1] entrance is an edge the ant has traveled
        pathCost -> cost, in this case the sum of the edgecosts the ant has traveled
        """
        self.possible_locations = list(range(0, 150))  # num_cities in PheromonesUpdate class
        self.path = [0]
        self.ants_path = list(range(0, 10))  # Number of ants
        self.pathCost = 0
        # print("30 SELF.PATHCOST", self.pathCost)
        self.pheromone_map = []

    # ----------------------------------Solution Construction-------------------------------


    def findSolution(self, pheromone_map):
        """
        As long as the List of possible next location self.possible_locations is not empty
        we chosse the next City and update the path
        """
        paths = [[0]]
        while self.possible_locations:

            # first chose the next city
            next_city = self.choseCity(pheromone_map)

            # update the path with the new city
            next_city = self.update_path(next_city)
            paths.append(next_city)
            # update the path cost of the ant
            self.update_pathcost()
        return paths

    # @property
    def choseCity(self, pheromone_map):

        """
        choses the next city based on the pheromone level
        calculate the attractiveness of each possible transition from the current location
        then randomly choose a next path, based on its attractiveness
        """

        # self.pheromone_map.copy()
        current_location = self.get_location()
        possible_locations = self.possible_locations

        # probabilitys to visit the node, mapped over the possible_locations list
        pathProbabilities = []

        # List with all numerator values for each possible next_location
        numeratorList = []

        # Compute the numerator for every possible node and save in the numeratorList

        for city in self.possible_locations:

            # get the pheromone_amount for the possible nect location and the distance between those cities

            pheromone_amount = pheromone_map[current_location][city]
            if tspmat[current_location][city] == 0:
                distance = 0
            else:
                distance = np.divide(1, tspmat[current_location][city])

            # fill the numerator list
            numeratorList.append(np.multiply(np.power(pheromone_amount, alpha), np.power(distance, beta)))  # pow(1/distance,beta) changed
        # compute the denominator
        denominator = sum(numeratorList)

        # compute the path probabilities by deviding the numerator with the deonominator
        for i in range(len(self.possible_locations)):
            if denominator != 0:
                pathProbabilities.append(numeratorList[i] / denominator)
            elif denominator == 0:
                pathProbabilities.append(0)
        next_node = np.asscalar(choice(possible_locations, 1, pathProbabilities))  # pathProbabilities REMOVED

        return next_node

        # return possible_locations[pathProbabilities.index(max(pathProbabilities))]

    # ----------------------------------Solution Construction Ends-------------------------------

    def update_pathcost(self):
        """
        This function updates the Cost (length) of the path the ant has traveled
        """

        # print("115 TSPMAT",tspmat[self.path[0]])
        new_path_costs = [0]
        # print("108 slef.path",len(self.path))
        for i in range(len(self.path)-1):

            new_path_costs_temp = new_path_costs[-1] + (tspmat[self.path[i]][self.path[i + 1]])
            new_path_costs.append(int(new_path_costs_temp))

        return new_path_costs[-1]

    def update_path(self, city):
        """
        Adds a new node to self.path and
        removes the pass from self.possible_locations so we can't visit nods twice
        """
        paths = []
        self.path.append(city)
        paths.append(city)
        self.possible_locations.remove(city)
        return paths


    def get_pathCost(self):
        """
        get the past cost
        """
        if len(self.possible_locations) == 0:
            return self.pathCost
        return None

    def get_path(self):
        """
        get the path, if it's created completely
        """
        path = self.path
        return path

    def get_location(self):
        """
        return the current location of the ant
        """
        # print("Path, get_location", self.path)
        return self.path[-1]


# ----------------------------------Class Ant ends---------------------------------


# ----------------------------------Pheromone_update-------------------------------

class PheromonesUpdate(Ant):
    """
    Properties:
    1. Initialize pheromones (Zeros/Random)
    2. Measure the fitness of ants, given pathCost from Parent Class(Ant)
    3. Get the path of the best ant
    4. Evaporation
    5. Intensification
    6. Further work: Update pheromones applies to all pheromones with respect to the quality of solutions produced by the ants
    """

    def __init__(self):
        super().__init__()  # Ants, number of cities and path
        self.rho = rho

        self.path = Ant().path
        self.pathCost = Ant().pathCost

    def init_pheromones(self, _random=False):

        """
        :param num_cities:
        :param _random: Type of initialization. Zeros or Random
        :return: array of pheromones
        """

        if _random:
            pheromones = np.random.random((num_cities, num_cities))
            np.fill_diagonal(pheromones, 0)
        else:
            pheromones = np.zeros((num_cities, num_cities))

        return pheromones

    def fitness_measure(self, ants, ants_paths, pathcost):

        """
        :param ants: list of antIDs
        :param ants_paths = list of arrays of paths of ants
        :param pathcost: Path cost of each ant
        :return: fittest_ant, list of their fitness
        """

        ants_paths_temp = ants_paths.copy()
        print("202", len(ants_paths_temp))
        print("203 pathcosts", pathcost)
        _paths = []
        for path in ants_paths_temp:
            _path = []
            for x in path:
                _path.append(x[0])
            _paths.append(_path)
        print("210",_paths)

        fitness_ants = np.subtract(max(pathcost), pathcost)
        fittest_ant = ants[np.argmax(fitness_ants)]
        fittest_ant_path = ants_paths[fittest_ant]

        return fitness_ants, fittest_ant, fittest_ant_path

    def get_path_of_fittest_ant(self, fittest_ant):

        pass

    def evaporation(self, pheromones):
        """
        :param pheromones: Array of pheromones
        :return: Array vaporized pheromones
        """

        return np.multiply((1 - self.rho), pheromones)

    def intensification(self, pheromones, fitness_ants, fittest_ant, fittest_ant_path):

        """

        :param pheromones: Array of pheromones
        :param fittest_ant_path : List of fittest ant's path in an iteration
        :param fitness_ants: Fitnesses of all ants in the iteration
        :param fittest_ant: Fittest ant index (AntID)
        :return: intensified_pheromones : Of the best ant's path
        """
        path = fittest_ant_path.copy()

        intensified_pheromones = pheromones.copy()
        for cities in path:
            i, j = cities
            intensification_factor = np.multiply(self.rho, (fitness_ants[fittest_ant] / np.sum(fitness_ants, axis=0)))
            intensified_pheromones[i][j] = pheromones[i][j] + intensification_factor

        return intensified_pheromones

    def update_pheromones(self, pheromones, ants, fitness_ants, fittest_ant, paths):

        """
        :param pheromones:  Array of pheromones
        :param ants: list of antIDs
        :param fittest_ant: int (index of the fittest ant in the population)
        :param fitness_ants: list of fitness of each ant
        :param paths : tuple of paths of  ants
        :return: array updated_pheromones
        """

        updated_pheromones = np.zeros((num_cities, num_cities))
        for ant in range(len(ants)):
            for path in paths[ant]:
                i, j = path
                evaporation_factor = np.multiply((1 - self.rho), pheromones[i][j])
                intensification_factor = np.multiply(self.rho, (fitness_ants[ant] / np.sum(fitness_ants, axis=0)))
                updated_pheromones[i][j] = evaporation_factor + intensification_factor
                # np.fill_diagonal(pheromones, 0)  # Hardcoded, just to make sure intensification
                #                                    is not performed between same city

        return updated_pheromones


# ------------------------PheromoneUpdate Class Ends---------------------------


# ------------------------Helper functions for mainloop-------------------------


def BestWay(ants):
    """
    Evaluates the best way in this iteration, considering all path_lengths of all ants
    input: list of all ants
    output: bestWay: Integer value for the shortest way found
    """
    bestWay = ants[0].path_length()
    for ant in ants:
        if ants[ant].path_length() < bestWay:
            bestWay = ants[ant].path_length()

    return bestWay


def read_file(filename):
    """
    This function reads in the tsp files and converts them into int matrices. The matrix can be accessed globably with the variable name tspmat
    """
    tspmat = None

    if filename == 1:
        tspmat = np.loadtxt("1.tsp")

    if filename == 2:
        tspmat = np.loadtxt("2.tsp")

    if filename == 3:
        tspmat = np.loadtxt("3.tsp")

    valuematrix = tspmat.astype(int)
    return valuematrix


# ----------------------------------Main loop Ends-------------------------------


# --------------Helper functions for the classes Ants and PheromonesUpdate-----------------------

def createAnts(antnmbr):

    """
    :param number_of_ants: Number of ants as requested by user
    :return: a list (from 0 to number_of_ants -1 )
    """

    return list(range(0, antnmbr))


def initalize(benchmark, antnmbr):
    """

    :param benchmark: Requested by the user
    :param antnmbr: Number of ants requested by the user
    :return: list of ants using createAnts function call

    """
    global tspmat
    tspmat = read_file(benchmark)

    return createAnts(antnmbr)


def user_input():
    benchmark = int(input("Please specify TSP benchmark to use [1],[2],[3]: "))
    number_of_ants = int(input("Please specify number of ants to be used: "))
    global stoppingcriterion
    stoppingcriterion = int(input("Please specify after how many iterations without an improved solution you want to stop: "))
    return initalize(benchmark, number_of_ants), stoppingcriterion


# ***********We do not need this function, since "CreateAnts()" function call in "initialize()" already did it****

# def createAntColony(antnmbr):
#     """
#     creates an array 'ant' with as many ant-objects in it as user input wanted
#     """
#     AntColony = []
#     for i in range(0,antnmbr):
#         AntColony.append(ant)

# *********************************************************************************************************************

# ----------------------------------Main loop-------------------------------

def mainloop():

    """
    ACO scheme:

    repeat
        for ant k ∈ {1,...,m}
             construct a solution {solution finding}
        endfor
        forall pheromone values do
            decrease the value by a certain percentage {evaporation}
        endfor
        forall pheromone values corresponding to good solutions
        do
            increase the value {intensification}
        endfor
    until stopping criterion is met
    """

    ant = Ant()
    pheromones_update = PheromonesUpdate()
    number_of_ants, stoppingcriterion = user_input()
    pheromones_master_list = list(range(stoppingcriterion))  # iteration i and i+1
    pheromones_master_list[0] = pheromones_update.init_pheromones(_random=False)
    ant.pheromone_map = pheromones_master_list[0]   # Pass the pheromone value inside Ant class

    pathCosts = []      # pathCosts[i] = pathCosts of ant i in number_of_ants list
    list_fittest_ant = []
    list_fitness_ants = []
    list_fittest_ant_path = []
    for i in range(0, stoppingcriterion):
        # create pathes for every ant in the ANt AntColony
        paths_of_all_ants = []
        for antID in number_of_ants:
            # print("373 Pheromones masterlist 0", pheromones_master_list[i])
            paths_of_an_ant = ant.findSolution(pheromones_master_list[i])
            paths_of_all_ants.append(paths_of_an_ant)
            # ant.ants_path[antID] = paths_of_an_ant.copy()

        pathCosts = []
        for antID in number_of_ants:
            pass

        pathCosts.append(Ant().update_pathcost())
        print("392 Paths of all ants ", len(paths_of_all_ants))

        # Paths of all ants length = number of ants and their paths length 151 including the return to 0 and
        # they paths of ant 1 can be accessed by paths_of_all_ants[0]
        # and the first city in paths_of_all_ants[0] is  paths_of_all_ants[0][0]
        # which is an array so convert it to scalar using np.asscalar(paths_of_all_ants[ant][city])

        fittest_ant, fitness_ants, fittest_ant_path = pheromones_update.fitness_measure(number_of_ants,paths_of_all_ants,pathCosts)
        list_fitness_ants.append(fitness_ants)
        list_fittest_ant.append(fittest_ant)
        list_fittest_ant_path.append(fittest_ant_path)

        # evaporate_pheromones
        pheromones_master_list[i+1] = pheromones_update.evaporation(pheromones_master_list[i])

        # intensify_pheromones
        pheromones_master_list[i+1] = pheromones_update.intensification(pheromones_master_list[i+1],
                                                                        fitness_ants=fitness_ants,
                                                                        fittest_ant=fittest_ant,
                                                                        fittest_ant_path=fittest_ant_path)

        ant.pheromone_map = pheromones_master_list[i+1]  # Pass the pheromones iteratively to Ant class

    print("Fittest ant %s and it path %s " % (list_fittest_ant[-1], list_fittest_ant_path[-1]))


if __name__ == "__main__":
    mainloop()
