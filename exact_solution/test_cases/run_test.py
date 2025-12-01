import time
from cs412_minvertexcover_exact import brute_force_vertex_cover

test_files = [
    ("Small", "test_small.py"),
    ("Medium", "test_medium.py"),
    ("Hard", "test_hard.py"),
    ("Extreme23", "test_extreme_23.py"),
]

def run_test(test_file):
    ns = {}
    exec(open(test_file).read(), ns)  # loads V and graph
    V = ns["V"]
    graph = ns["graph"]

    print(f"Running {test_file}  (V={V})...")

    start = time.time()
    result = brute_force_vertex_cover(graph, V)
    end = time.time()

    size = len(result) if result is not None else None

    print(f"  → Size: {size}")
    print(f"  → Runtime: {end - start:.4f} sec\n")

    return (test_file, V, size, end - start)


def run_all():
    print("==== Running All Vertex Cover Tests ====")
    results = []

    for name, file in test_files:
        results.append(run_test(file))

    print("==== Summary ====")
    for (file, V, size, t) in results:
        print(f"{file}: V={V}, size={size}, time={t:.4f} sec")

    # Write summary to CSV
    with open("runtime_summary.csv", "w") as f:
        f.write("test_file,V,size,time_sec\n")
        for (file, V, size, t) in results:
            f.write(f"{file},{V},{size},{t}\n")

    print("\nRuntime summary saved to runtime_summary.csv")


if __name__ == "__main__":
    run_all()
