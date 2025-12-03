V = 34
graph = {u: [] for u in range(V)}

left = range(15)
right = range(15, 30)

for u in left:
    for v in right:
        graph[u].append(v)
        graph[v].append(u)
