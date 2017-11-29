import networkx as nx
import matplotlib.pyplot as plt


def draw_route(tour):

    """
    Args:
        tour(tuple) - List contains pairs(currentcity,nextcity)

    Returns:

        image(graph) - Route of ant
        """

    G = nx.DiGraph()
    black_edges = [edge for edge in G.edges()]
    pos = nx.spring_layout(G)
    G.add_edges_from(tour)

    nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), node_size=500)
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos, edgelist=black_edges, arrows=True)
    nx.draw_networkx(G, pos, arrows=True)
    return plt.show()


# Test draw function
tour = [(1,2),(2,3),(3,1), (3,4)]
draw_route(tour)

"""

class Ant:

    # Properties of Ant

def cities(num_cities):
    # This function is just to test. Should be changed
    # Generates distance between cities as an array

    _cities = np.random.randint(num_cities, size=(num_cities, num_cities))
    np.fill_diagonal(_cities, 0.0)

    return _cities



# Check
distance_matrix = cities(5)
print(distance_matrix)


def next_possible_city(alpha, beta,  ):

    # Compute probability of choosing the next edge/city in each step
    #
    pass

"""