import sys

graph1 = {'S': {'A': 3, 'B': 1, 'C': 8},
          'A': {'S': 3, 'D': 3, 'E': 7, 'G': 15},
          'B': {'S': 1, 'G': 20},
          'C': {'S': 8, 'G': 5},
          'D': {'A': 3},
          'E': {'A': 7},
          'G': {'A': 15, 'B': 20, 'C': 5}
          }

# Heurstic function of each node: (Actual shortest path to the goal.)
heurstic = {'S': 13, 'A': 15, 'B': 14, 'C': 5, 'D': 18, 'E': 22, 'G': 0}

# Greedy Search
def greedy(graph,src,goal):
    path = [src]
    node = src
    while heurstic[node] != 0:
        firstNeighbour = list(graph['S'].keys())[0]
        min = heurstic[firstNeighbour]      # Initialize minimum with the first neighbour's heurstic.
        temp = firstNeighbour
        for neighbour in graph[node]:
            if heurstic[neighbour] < min:
                min = heurstic[neighbour]
                temp = neighbour
        node = temp               # Set the neighbour with the minimum heurstic as the next node to expand.
        path.append(node)
    print(path)
    print('Number of nodes expanded =',len(path))
    print('Path cost =',heurstic[src])

greedy(graph1,'S','G')