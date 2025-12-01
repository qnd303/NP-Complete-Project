"""
name: Quan Do
Honor Code and Acknowledgments:
This work complies with the JMU Honor Code.
Comments here on your code and submission.

Citations: https://www.geeksforgeeks.org/dsa/introduction-and-approximate-solution-for-vertex-cover-problem/
"""

from itertools import combinations

from itertools import combinations

def brute_force_vertex_cover(graph):
    nodes = list(graph.keys())
    min_cover = None

    for k in range(len(nodes) + 1):
        for subset in combinations(nodes, k):
            cover = set(subset)
            valid = True
            for u in graph:
                for v in graph[u]:
                    if u not in cover and v not in cover:
                        valid = False
                        break
                if not valid:
                    break
            if valid:
                min_cover = cover
                return min_cover
    return None



def main():
    pass
if __name__ == "__main__":
    main()