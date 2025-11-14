"""
name: Quan Do
Honor Code and Acknowledgments:
This work complies with the JMU Honor Code.
Comments here on your code and submission.

Citations: https://www.geeksforgeeks.org/dsa/introduction-and-approximate-solution-for-vertex-cover-problem/
"""

def exact_vertex_cover(graph, V):
    best = None
    
    def dfs(i, cover):
        nonlocal best

        # prune
        if best is not None and len(cover) >= len(best):
            return
        
        # if checked all vertices
        if i == V:
            # check if cover covers all edges
            for u in range(V):
                for v in graph[u]:
                    if u not in cover and v not in cover:
                        return
            best = cover.copy()
            return
        
        # Case 1: don't include i
        dfs(i + 1, cover)
        
        # Case 2: include i
        cover.add(i)
        dfs(i + 1, cover)
        cover.remove(i)

    dfs(0, set())
    return best
