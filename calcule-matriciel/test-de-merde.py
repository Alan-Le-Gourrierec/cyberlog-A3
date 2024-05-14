import numpy as np
import networkx as nx

G = nx.Graph([(1, 2), (1, 3), (1, 4), (3, 4), (3, 5), (4, 5)])

dict(nx.eccentricity(G))
{1: 2, 2: 3, 3: 2, 4: 2, 5: 3}