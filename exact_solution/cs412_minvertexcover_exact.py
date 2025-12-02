"""
name: Quan Do
Honor Code and Acknowledgments:
This work complies with the JMU Honor Code.
Comments here on your code and submission.

Citations: https://www.geeksforgeeks.org/dsa/introduction-and-approximate-solution-for-vertex-cover-problem/
"""
import sys
from itertools import combinations
from collections import defaultdict
import os

def parse_graph_lines(lines):
    G = defaultdict(set)
    edges = set()
    for line in lines:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        parts = line.split()
        if len(parts) < 2:
            continue
        u = int(parts[0])
        neighbors = [int(v) for v in parts[1:]]
        for v in neighbors:
            G[u].add(v)
            G[v].add(u)
            edges.add(tuple(sorted((u, v))))
    return G, edges

def brute_force_vertex_cover(graph, edges):
    nodes = list(graph.keys())
    current_best = None

    for k in range(len(nodes) + 1):
        found_this_size = []
        for subset in combinations(nodes, k):
            cover = set(subset)
            valid = True
            for u, v in edges:
                if u not in cover and v not in cover:
                    valid = False
                    break
            if valid:
                found_this_size.append(cover)

        if found_this_size:
            return found_this_size[0]

    return None

def cover_valid(G, C):
    for u, neighs in G.items():
        for v in neighs:
            if u not in C and v not in C:
                return False
    return True

def main():
    data = None
    if not sys.stdin.isatty():
        data = sys.stdin.read()
    if (data is None or data.strip() == "") and os.path.exists("input.txt"):
        with open("input.txt", "r") as f:
            data = f.read()
    if data is None:
        data = ""

    lines = [line.strip() for line in data.splitlines() if line.strip()]
    G, edges = parse_graph_lines(lines)

    if not edges:
        print()
        return

    cover = brute_force_vertex_cover(G, edges)

    if cover is None or not cover_valid(G, cover):
        cover = set()
        for u, v in edges:
            cover.add(u)
            cover.add(v)

    ordered = sorted(cover)
    print(" ".join(map(str, ordered)))

if __name__ == "__main__":
    main()
