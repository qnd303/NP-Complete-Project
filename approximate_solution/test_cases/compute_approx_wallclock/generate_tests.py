import os
import random
import subprocess
import time
import csv

# --- CONFIG ---
GRAPH_DIR = "test_graphs"
OUTPUT_FILE = "runtime_results.csv"
os.makedirs(GRAPH_DIR, exist_ok=True)

APPROX_CMD = ["python3", "approx.py"]
EXACT_CMD  = ["python3", "exact.py"]

TESTS_PER_TYPE = 6
TIMEOUT_SEC = 15

# --------------------------------------
# Graph Generators
# --------------------------------------
def gen_sparse_graph(n, p):
    edges = []
    for u in range(n):
        for v in range(u+1, n):
            if random.random() < p:
                edges.append((u, v))
    return edges

def gen_star_graph(n):
    edges = [(0, v) for v in range(1, n)]  # star centered at 0
    return edges

def gen_hub_graph(n, extra_edges=3):
    edges = []

    # Pick a random hub
    hub = random.randint(0, n-1)

    # Base: star edges
    for v in range(n):
        if v != hub:
            edges.append((hub, v))

    # Add a few random edges to increase complexity
    for _ in range(extra_edges):
        u = random.randint(0, n-1)
        v = random.randint(0, n-1)
        if u != v:
            edges.append(tuple(sorted((u, v))))

    return list(set(edges))

def gen_preferential_attachment(n, m=2):
    edges = []
    degrees = [1] * n  # initial degree weight
    nodes = list(range(n))

    for v in range(m, n):
        targets = random.choices(nodes[:v], weights=degrees[:v], k=m)
        for u in targets:
            edges.append((u, v))
            degrees[u] += 1
            degrees[v] += 1

    return edges

def write_graph(path, edges):
    with open(path, "w") as f:
        for u, v in edges:
            f.write(f"{u} {v}\n")

# --------------------------------------
# Run solver + timing
# --------------------------------------
def run_solver(cmd, path):
    start = time.time()
    try:
        result = subprocess.run(
            cmd + [path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=TIMEOUT_SEC
        )
        output = result.stdout.strip()
    except subprocess.TimeoutExpired:
        return None, "TIMEOUT"
    return round(time.time() - start, 6), output

def extract_vertex_cover_size(output):
    if output in ["TIMEOUT", ""]:
        return None
    for token in output.split():
        try:
            return int(token)
        except:
            continue
    return None

# --------------------------------------
# MAIN
# --------------------------------------
def main():
    results = []
    idx = 1

    GRAPH_TYPES = [
        ("Sparse", lambda: gen_sparse_graph(random.randint(15, 22), random.uniform(0.07, 0.15))),
        ("Star", lambda: gen_star_graph(random.randint(15, 22))),
        ("Hub", lambda: gen_hub_graph(random.randint(15, 22), extra_edges=5)),
        ("PrefAttach", lambda: gen_preferential_attachment(random.randint(15, 22), m=2)),
    ]

    for label, generator in GRAPH_TYPES:
        for _ in range(TESTS_PER_TYPE):

            edges = generator()
            n = max(max(u,v) for u,v in edges) + 1

            file_path = os.path.join(GRAPH_DIR, f"graph_{idx}.txt")
            write_graph(file_path, edges)

            print(f"[{label}] graph {idx}: n={n}, edges={len(edges)}")

            # run exact
            exact_time, exact_out = run_solver(EXACT_CMD, file_path)
            exact_size = extract_vertex_cover_size(exact_out)
            if exact_out == "TIMEOUT":
                exact_size = "TIMEOUT"

            # run approx
            approx_time, approx_out = run_solver(APPROX_CMD, file_path)
            approx_size = extract_vertex_cover_size(approx_out)
            if approx_out == "TIMEOUT":
                approx_size = "TIMEOUT"

            results.append([
                f"graph_{idx}.txt",
                label,
                n,
                len(edges),
                exact_size,
                approx_size,
                exact_time,
                approx_time
            ])
            idx += 1

    # Write CSV
    with open(OUTPUT_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            "file", "type", "V", "E",
            "exact_size", "approx_size",
            "exact_time", "approx_time"
        ])
        writer.writerows(results)

    print("\nDone! Results saved to", OUTPUT_FILE)

if __name__ == "__main__":
    main()
