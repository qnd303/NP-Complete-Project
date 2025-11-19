"""
name: Quan Do
Honor Code and Acknowledgments:
This work complies with the JMU Honor Code.
Comments here on your code and submission.

Citations: https://www.geeksforgeeks.org/dsa/introduction-and-approximate-solution-for-vertex-cover-problem/
"""

from itertools import combinations

def brute_force_vertex_cover(graph, V):
    for k in range(V + 1):
        for subset in combinations(range(V), k):
            cover = set(subset)

            valid = True
            for u in range(V):
                for v in graph[u]:
                    if u not in cover and v not in cover:
                        valid = False
                        break
                if not valid:
                    break

            if valid:
                return cover

    return None
