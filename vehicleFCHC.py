# Import required libraires
import numpy as np
import random
import time
import itertools

def CurrentSolution(CurrentState):
    
    """ Estimate the customer_demand and value of current solution.
        
        Args:
            CurrentState(list) - List of count of vehicle types used
            Capacity(list) - List of available vehicles types (capacity) 
            
        Returns:
            CurrentState(list) - List of counts that corresponds to count of vehicle types used
            DemandMet(int) - Sum(VehiclesCapacity) which should be >= Total CustomerDemand
                  
    """     
    VehiclesCapacity = [VehicleCount*Capacity for VehicleCount,Capacity in zip(CurrentState,Capacity)]
    
    DemandMet = sum(VehiclesCapacity)   
       
    return CurrentState,DemandMet 


def GenerateNeighbor(CurrentState):
    """ Generate neighbors for current solution.
    
        Args:
            CurrentState(list) - List of counts that corresponds to count of an item in the Sack
    
        Returns:
            Neighbor(list) - Neighbour(list)   
    """
    NewState = CurrentState.copy() 
    NewState[random.randint(0,len(CurrentState)-1)] += StepSize  # Generate the neighbor randomly
    
    return NewState

def EvaluateNeighbor(Neighbor):
    
    """ Evauate the Neighbor of CurrentSolution 
        
        Args:
            Neighbor(list) - List of count of vehicle types used
            Capacity(list) - List of available vehicles types (capacity) 
            
        Returns:
            CurrentState(list) - List of counts that corresponds to count of vehicle types used
            DemandMet(int) - Sum(VehiclesCapacity) which should be >= Total CustomerDemand     
    """    
    NeighborVehiclesCapacity = [VehicleCount*Capacity for VehicleCount,Capacity in zip(Neighbor,Capacity)]
    
    NeighborDemandMet = sum(NeighborVehiclesCapacity)  
       
    return Neighbor, NeighborDemandMet

#if __name__ == "__main__":
def getVehicle():

    # Read txt files
    ReadCapacityFile = np.loadtxt("capacity.txt")
    ReadCustomerDemandFile = np.loadtxt("demand.txt")

    #Initialize global variables of the problem.

    global Capacity
    global CustomerDemand

    Capacity = np.unique(ReadCapacityFile.astype(int))
    # Capacity = [10,100,200,600]
    NumberOfVehicles = len(Capacity)
    CustomerDemand = np.sum(ReadCustomerDemandFile.astype(int))
    print(CustomerDemand,Capacity)
    

    # FCHC Hyperparameter
    global StepSize
    StepSize = 1        

    #Ground /Initial state of Hill Climber
    CurrentState = [0]* NumberOfVehicles    

    # CurrentState initialized with random values
    #CurrentState = [random.randint(0,NumberOfItems) for item in range(NumberOfItems)]
    print("Initial Current State",CurrentState)
    CurrentState, CurrentDemandMet = CurrentSolution(CurrentState) 

    #Loop until optimal solution is met

    iterations = 0
    StartTime = time.time()
    while True:

        NewNeighbor = GenerateNeighbor(CurrentState)
    
        Neighbor,NeighborDemandMet = EvaluateNeighbor(NewNeighbor)

        
        if NeighborDemandMet < CustomerDemand+Capacity[0] :
        
            CurrentState = Neighbor.copy()
            CurrentDemandMet = NeighborDemandMet
            iterations+=1
            print(CurrentState,CurrentDemandMet)   
            print("--- %s seconds ---" % (time.time() - StartTime))
            print("Best Solution is %s with Demand Met %s " %(CurrentState, CurrentDemandMet))
            print("Number of Iterations", iterations)

            if NeighborDemandMet >= CustomerDemand:
                break

    VehicleTypeList = []
    for vehicletype,count in enumerate(CurrentState):
        VehicleTypeList.append(np.ndarray.tolist((np.repeat(vehicletype,count)))) 

    VehicleList = list(itertools.chain.from_iterable(VehicleTypeList))
    return CurrentState, VehicleList




