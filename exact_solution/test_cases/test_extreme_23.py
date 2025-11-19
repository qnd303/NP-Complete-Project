V = 28
graph = {u: [] for u in range(V)}

# Left side: 0-13
# Right side: 14-27
left = range(14)
right = range(14, 28)

# Build complete bipartite graph K14,14
for u in left:
    for v in right:
        graph[u].append(v)
        graph[v].append(u)
