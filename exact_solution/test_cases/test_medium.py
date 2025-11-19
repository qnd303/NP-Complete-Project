# Medium test case (V = 14)
V = 14
graph = {u: [] for u in range(V)}


# Build a dense graph where each vertex connects to the next 5
for u in range(V):
    for v in range(u+1, min(V, u+6)):
        graph[u].append(v)
        graph[v].append(u)