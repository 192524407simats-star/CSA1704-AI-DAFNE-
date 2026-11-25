def minimax(depth, node, maximizing):
    if depth == 2:
        return node

    if maximizing:
        return max(minimax(depth + 1, x, False) for x in tree[node])
    else:
        return min(minimax(depth + 1, x, True) for x in tree[node])

tree = {
    'A': ['B', 'C'],
    'B': [3, 5],
    'C': [2, 9]
}

print("Best Value:", minimax(0, 'A', True))