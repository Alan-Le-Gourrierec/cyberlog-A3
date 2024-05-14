import numpy as np
from itertools import permutations
import networkx as nx

def find_longest_cycle(adj_matrix):
    num_nodes = len(adj_matrix)
    longest_cycle = []
    
    for cycle_length in range(num_nodes, 2, -1):
        for perm in permutations(range(num_nodes), cycle_length):
            cycle = list(perm)
            cycle += [cycle[0]]  # Add the first vertex to close the cycle
            
            is_cycle = True
            for i in range(cycle_length):
                if adj_matrix[cycle[i]][cycle[i+1]] != 1:
                    is_cycle = False
                    break
            
            if is_cycle:
                return cycle
            
    return []

# Example usage for an undirected graph:
graph = np.array([
    [0, 1, 0, 0, 1],
    [1, 0, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0]
])

G = nx.from_numpy_array(graph)
nx.draw(G)

longest_cycle = find_longest_cycle(graph)

if longest_cycle:
    print("Longest Cycle:", longest_cycle)
else:
    print("No cycle found in the graph.")