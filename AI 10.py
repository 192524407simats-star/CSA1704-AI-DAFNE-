graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'D': 1, 'E': 5},
    'C': {'F': 2},
    'D': {'G': 3},
    'E': {'G': 2},
    'F': {'G': 1},
    'G': {}
}

h = {'A': 5, 'B': 4, 'C': 3, 'D': 2, 'E': 1, 'F': 1, 'G': 0}

def astar(start, goal):
    open_list = [(h[start], 0, start, [start])]
    while open_list:
        open_list.sort()
        f, cost, node, path = open_list.pop(0)

        if node == goal:
            print("Path:", path)
            print("Cost:", cost)
            return

        for neighbour, weight in graph[node].items():
            new_cost = cost + weight
            open_list.append((new_cost + h[neighbour], new_cost,
                              neighbour, path + [neighbour]))

astar('A', 'G')