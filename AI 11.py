colors = ['Red', 'Green', 'Blue']

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C'],
    'C': ['A', 'B']
}

color = {}

for region in graph:
    for c in colors:
        if all(color.get(n) != c for n in graph[region]):
            color[region] = c
            break

print(color)