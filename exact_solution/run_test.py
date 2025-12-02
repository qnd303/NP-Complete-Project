# run_test.py
import sys
import time
from cs412_minvertexcover_exact import brute_force_vertex_cover

if len(sys.argv) < 2:
    print("Usage: python run_test.py <test_case_file>")
    sys.exit(1)

test_file = sys.argv[1]

# Load test case
ns = {}
with open(test_file) as f:
    exec(f.read(), ns)

graph = ns["graph"]

# Build edges list for the solver
edges = set()
for u in graph:
    for v in graph[u]:
        edges.add(tuple(sorted((u, v))))

print(f"Running {test_file}...")

start = time.time()
result = brute_force_vertex_cover(graph, edges)
end = time.time()

size = len(result) if result is not None else None

print(f"  → Size: {size}")
print(f"  → Runtime: {end - start:.4f} sec\n")
