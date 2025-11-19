# Hard test case (V = 18)
V = 18
graph = {u: [] for u in range(V)}


# Build near-clique but leave out a few edges to avoid trivial cover
for u in range(V):
    for v in range(u+1, V):
        if (u + v) % 4 != 0: # remove some edges
            graph[u].append(v)
            graph[v].append(u)