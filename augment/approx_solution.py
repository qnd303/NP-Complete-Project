"""
Approximate Vertex Cover using:
- Randomized maximal matching
- Reduction pass (removes unnecessary vertices)

"""

import sys
import random
import os
from collections import defaultdict

def parse_graph_lines(lines):
    G = defaultdict(set)
    edges = []
    for line in lines:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        parts = line.split()
        if len(parts) != 2:
            continue
        u, v = parts
        G[u].add(v)
        G[v].add(u)
        edges.append((u, v))
    return G, edges

def randomized_maximal_matching(edges, seed=None):
    if seed is not None:
        random.seed(seed)
    else:
        random.seed()

    edges_shuffled = edges[:]
    random.shuffle(edges_shuffled)

    matched = set()
    matching = []

    for (u, v) in edges_shuffled:
        if u not in matched and v not in matched:
            matching.append((u, v))
            matched.add(u)
            matched.add(v)

    return matching

def build_cover_from_matching(matching):
    C = set()
    for (u, v) in matching:
        C.add(u)
        C.add(v)
    return C

def reduction_pass(G, C):
    removed_any = True
    while removed_any:
        removed_any = False
        for v in list(C):
            all_neighbors_in_C = True
            for u in G.get(v, []):
                if u not in C:
                    all_neighbors_in_C = False
                    break
            if all_neighbors_in_C:
                C.remove(v)
                removed_any = True
    return C

def cover_valid(G, C):
    for u, neighs in G.items():
        for v in neighs:
            if u not in C and v not in C:
                return False
    return True

# 🔥 THIS FUNCTION IS NEW — used for comparison script
def approx_vertex_cover_from_edge_lines(lines, seed=None):
    G, edges = parse_graph_lines(lines)
    if not edges:
        return set()

    matching = randomized_maximal_matching(edges, seed=seed)
    C = build_cover_from_matching(matching)
    C = reduction_pass(G, C)

    if not cover_valid(G, C):
        for (u, v) in edges:
            if u not in C and v not in C:
                C.add(u)
                C.add(v)
        C = reduction_pass(G, C)

    return C

def main():
    data = None
    if not sys.stdin.isatty():
        data = sys.stdin.read()
    if (data is None or data.strip() == "") and os.path.exists("input.txt"):
        with open("input.txt", "r") as f:
            data = f.read()
    if data is None:
        data = ""

    lines = data.splitlines()
    G, edges = parse_graph_lines(lines)

    if not edges:
        print()
        return

    seed_env = os.getenv("SEED")
    seed = None
    if seed_env is not None:
        try:
            seed = int(seed_env)
        except:
            seed = None

    matching = randomized_maximal_matching(edges, seed=seed)
    C = build_cover_from_matching(matching)
    C = reduction_pass(G, C)

    if not cover_valid(G, C):
        for (u, v) in edges:
            if u not in C and v not in C:
                C.add(u)
                C.add(v)
        C = reduction_pass(G, C)

    try:
        ordered = sorted(C, key=lambda x: (0, int(x)) if x.isdigit() else (1, x))
    except Exception:
        ordered = sorted(C)

    print(" ".join(map(str, ordered)))

if __name__ == "__main__":
    main()
