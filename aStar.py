import sys

graph1 = {'S': {'A': 3, 'B': 1, 'C': 8},
          'A': {'S': 3, 'D': 3, 'E': 7, 'G': 15},
          'B': {'S': 1, 'G': 20},
          'C': {'S': 8, 'G': 5},
          'D': {'A': 3},
          'E': {'A': 7},
          'G': {'A': 15, 'B': 20, 'C': 5}
          }

# Returns cost in (node,cost) pair.

def getCost(x):
    return x[1]

# Heurstic function of each node: (Actual shortest path to the goal.)
heurstic = {'S': 13, 'A': 15, 'B': 14, 'C': 5, 'D': 18, 'E': 22, 'G': 0}

# A* Search

def a_star(graph, src, goal):
    # Queue format: (node, heurstic cost + step cost)
    queue = [(src, heurstic[src] + 0)]
    visited = []
    cost = 0
    while queue:
        node = queue.pop(0)
        if node[0] not in visited:
            # Total step cost from the start to the current node.
            cost = node[1] - heurstic[node[0]]
            visited.append(node[0])
            if node[0] == goal:
                print("A* SEARCH")
                print('FOUND:', node[0])
                print(visited)
                print('Number of nodes expanded =', len(visited))
                print('Path cost =', node[1])
                sys.exit()
            for neighbour in graph[node[0]]:
                if neighbour not in visited:
                    # Add the step cost of the current node to all its neighbours.
                    graph[node[0]][neighbour] += cost
                    # Add (neighbour, heurstic cost + step cost) pair to the queue.
                    queue.append(
                        (neighbour, heurstic[neighbour] + graph[node[0]][neighbour]))
            # Sort the queue by heurstic cost + step cost.
            queue = sorted(queue, key=getCost)

a_star(graph1,'S','G')