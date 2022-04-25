import sys

graph1 = {'S': {'A': 3, 'B': 1, 'C': 8},
          'A': {'S': 3, 'D': 3, 'E': 7, 'G': 15},
          'B': {'S': 1, 'G': 20},
          'C': {'S': 8, 'G': 5},
          'D': {'A': 3},
          'E': {'A': 7},
          'G': {'A': 15, 'B': 20, 'C': 5}
          }

# Breadth-First Search

def bfs(graph, src, goal):
    # Queue format: (node, cost). Cost is relevant to the path taken.
    queue = [(src, 0)]
    visited = []
    cost = 0
    while queue:
        node = queue.pop(0)
        if node not in visited:
            # Total cost from the start to the current node.
            cost = node[1]
            visited.append(node[0])
            if node[0] == goal:
                print('FOUND:', node[0])
                print(visited)
                print('Number of nodes expanded =', len(visited))
                print('Path cost =', cost)
                sys.exit()
            for neighbour in graph[node[0]]:
                if neighbour not in visited:
                    # Add the cost of the current node to all its neighbours.
                    graph[node[0]][neighbour] += cost
                    # Add (neighbour, cost of neighbour) pair to the queue.
                    queue.append((neighbour, graph[node[0]][neighbour]))
bfs(graph1,'S','G')
