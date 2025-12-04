"""
compare_vc_methods.py

Compare:
- Exact VC (brute-force)
- Your Approx VC (randomized maximal matching)

Input: adjacency-list graph file (like vc_small_triangle.txt, etc).
"""

import sys
import time
import os
from collections import defaultdict

# ----- Make sure Python can find the modules in your repo -----

HERE = os.path.dirname(__file__)
ROOT = os.path.abspath(os.path.join(HERE, ".."))

# exact solution lives in: exact_solution/cs412_minvertexcover_exact.py
sys.path.insert(0, os.path.join(ROOT, "exact_solution"))
# your Part E approx copy lives in: augment/approx_solution.py
sys.path.insert(0, HERE)

from cs412_minvertexcover_exact import brute_force_vertex_cover as exact_vc
from augment.approx_solution_augment import approx_vertex_cover_from_edge_lines


def read_adj_graph(path):
    """
    Read adjacency-list graph from 'path'.

    Format:
        line i: neighbors of vertex i, space-separated (0-based indices).
    """
    G = defaultdict(set)
    with open(path) as f:
        for u, line in enumerate(f):
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            neighbors = [int(v) for v in line.split()]
            for v in neighbors:
                G[u].add(v)
                G[v].add(u)

    edges = set()
    for u, neighs in G.items():
        for v in neighs:
            if u < v:
                edges.add((u, v))

    return G, edges


def build_edge_list_lines(edges):
    """Convert set of (u, v) edges into 'u v' strings for the approx parser."""
    lines = []
    for u, v in sorted(edges):
        lines.append(f"{u} {v}")
    return lines


def compare_one(graph_file, out_stream=sys.stdout):
    G, edges = read_adj_graph(graph_file)
    print(f"Graph file: {graph_file}", file=out_stream)
    print(f"|V| = {len(G)}, |E| = {len(edges)}", file=out_stream)

    if not edges:
        print("No edges → trivial cover = empty set.\n", file=out_stream)
        return

    # ----- EXACT -----
    start = time.time()
    exact_cover = exact_vc(G, edges)
    exact_t = time.time() - start

    print("\n=== EXACT VERTEX COVER ===", file=out_stream)
    print("Cover:", sorted(exact_cover), file=out_stream)
    print("Size: ", len(exact_cover), file=out_stream)
    print(f"Time:  {exact_t:.5f} sec", file=out_stream)

    # ----- APPROX -----
    approx_input_lines = build_edge_list_lines(edges)
    start = time.time()
    approx_cover = approx_vertex_cover_from_edge_lines(approx_input_lines, seed=0)
    approx_t = time.time() - start

    print("\n=== APPROX VERTEX COVER ===", file=out_stream)
    print("Cover:", sorted(approx_cover), file=out_stream)
    print("Size: ", len(approx_cover), file=out_stream)
    print(f"Time:  {approx_t:.5f} sec", file=out_stream)

    # ----- Ratio -----
    if len(exact_cover) > 0:
        ratio = len(approx_cover) / len(exact_cover)
    else:
        ratio = float("inf")

    print(f"\nApproximation ratio = |C_approx| / |C_exact| = {ratio:.3f}", file=out_stream)
    print("\n", file=out_stream)


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 compare_vc_methods.py <graph.adj>")
        sys.exit(1)

    graph_file = sys.argv[1]
    compare_one(graph_file)

if __name__ == "__main__":
    main()
