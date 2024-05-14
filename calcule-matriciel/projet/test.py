import numpy as np
import networkx as nx

def convert_to_dag(matrice):
    # Convert an undirected graph into a directed acyclic graph (DAG)
    n = matrice.shape[0]
    dag_matrix = np.zeros((n, n), dtype=int)

    for i in range(n):
        for j in range(i + 1, n):
            if matrice[i, j] == 1 or matrice[j, i] == 1:
                dag_matrix[i, j] = 1
            elif matrice[j, i] == 1:
                dag_matrix[j, i] = 1

    return dag_matrix

def longest_path_in_dag(matrice):
    n = matrice.shape[0]
    ordre = []

    in_degree = np.sum(matrice, axis=1)
    queue = [node for node in range(n) if in_degree[node] == 0]

    while queue:
        node = queue.pop(0)
        ordre.append(node)
        for neighbor in range(n):
            if matrice[node, neighbor] == 1:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

    max_chemin = np.zeros(n)

    for node in ordre:
        for neighbor in range(n):
            if matrice[node, neighbor] == 1:
                max_chemin[neighbor] = max(max_chemin[neighbor], max_chemin[node] + 1)

    max_length = int(np.max(max_chemin))
    path = [ordre[np.argmax(max_chemin)]]

    for i in range(max_length - 1, -1, -1):
        for neighbor in range(n):
            if matrice[path[-1], neighbor] == 1 and max_chemin[neighbor] == i:
                path.append(neighbor)
                break

    return max_length, list(reversed(path))

# Example usage for an undirected graph:
graph = np.array([
    [0, 1, 1, 0, 0],
    [1, 0, 0, 1, 0],
    [1, 0, 0, 1, 0],
    [0, 1, 1, 0, 1],
    [0, 0, 0, 1, 0]
])

dag_graph = convert_to_dag(graph)
length, path = longest_path_in_dag(dag_graph)
print("Longest Path Length:", length)
print("Longest Path:", path)