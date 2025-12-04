#!/usr/bin/env python3
"""
is_to_vc.py
Independent Set -> Vertex Cover (complement)
"""

import sys
import re

def load_vertices_from_adj_file(graph_file):
    """
    Read the original graph file (edge-list style: one 'u v' per line)
    and return the set of all vertex IDs that appear.
    """
    vertices = set()
    with open(graph_file) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split()
            if len(parts) != 2:
                continue
            u, v = parts
            # your test files use numeric labels
            vertices.add(int(u))
            vertices.add(int(v))
    return vertices

def load_independent_set(is_file):
    """
    Read the IS output from indset_approx.py.

    It can look like:
      {'0', '2', '4'}
    or just:
      0 2 4

    We just grab all integers.
    """
    with open(is_file) as f:
        text = f.read()
    if not text.strip():
        return set()
    nums = re.findall(r'-?\d+', text)
    return {int(x) for x in nums}

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 is_to_vc.py <graph.txt> <is.txt>")
        sys.exit(1)

    graph_file = sys.argv[1]
    is_file = sys.argv[2]

    V = load_vertices_from_adj_file(graph_file)
    I = load_independent_set(is_file)

    C = sorted(V - I)
    print(" ".join(map(str, C)))

if __name__ == "__main__":
    main()
