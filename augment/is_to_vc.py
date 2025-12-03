#!/usr/bin/env python3
"""
is_to_vc.py
Independent Set -> Vertex Cover (complement)
"""

import sys

def load_vertices_from_adj_file(graph_file):
    vertices = set()
    with open(graph_file) as f:
        for i, line in enumerate(f):
            if line.strip() and not line.startswith("#"):
                vertices.add(i)
    return vertices

def load_independent_set(is_file):
    with open(is_file) as f:
        text = f.read().strip()
    if not text:
        return set()
    return {int(x) for x in text.split()}

def main():
    if len(sys.argv) != 2 and len(sys.argv) != 3:
        print("Usage: python3 is_to_vc.py <graph.adj> <is.txt>")
        sys.exit(1)

    graph_file = sys.argv[1]
    is_file = sys.argv[2]

    V = load_vertices_from_adj_file(graph_file)
    I = load_independent_set(is_file)

    C = sorted(V - I)
    print(" ".join(map(str, C)))

if __name__ == "__main__":
    main()
