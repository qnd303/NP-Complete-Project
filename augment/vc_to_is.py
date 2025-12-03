#!/usr/bin/env python3
"""
vc_to_is.py
Convert VC adjacency list -> IS edge list
"""

import sys
from collections import defaultdict

def parse_vc_adjacency(lines):
    G = defaultdict(set)
    for u, line in enumerate(lines):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        neighbors = [int(v) for v in line.split()]
        for v in neighbors:
            G[u].add(v)
            G[v].add(u)
    return G

def main():
    lines = sys.stdin.read().splitlines()
    G = parse_vc_adjacency(lines)

    edges = set()
    for u, neighs in G.items():
        for v in neighs:
            if u < v:
                edges.add((u, v))

    for (u, v) in sorted(edges):
        print(f"{u} {v}")

if __name__ == "__main__":
    main()
