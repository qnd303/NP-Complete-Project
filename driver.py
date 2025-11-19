""" Test casees for exact solution of vertex cover problem."""


from exact_solution import exact_vertex_cover as evc

def is_vertex_cover(graph, V, cover):
    """
    Returns True if 'cover' is a vertex cover of 'graph' with V vertices.
    """
    for u in range(V):
        for v in graph[u]:
            if u not in cover and v not in cover:
                return False
    return True


# 1. Empty graph (no vertices)
g_empty = []  # V = 0
# Expected: cover = set(), size 0


# 2. Three isolated vertices (no edges)
g_isolated = [
    [],  # 0
    [],  # 1
    [],  # 2
]  # V = 3
# Expected: cover = set(), size 0


# 3. Single edge: 0 -- 1
g_single_edge = [
    [1],  # 0
    [0],  # 1
]  # V = 2
# Expected: min size = 1 (either {0} or {1})


# 4. Path of length 2: 0 -- 1 -- 2
g_path3 = [
    [1],     # 0
    [0, 2],  # 1
    [1],     # 2
]  # V = 3
# Expected: min size = 1 (e.g., {1})


# 5. Triangle K3: 0 -- 1 -- 2 -- 0
g_triangle = [
    [1, 2],  # 0
    [0, 2],  # 1
    [0, 1],  # 2
]  # V = 3
# Expected: min size = 2 (any 2 vertices, e.g., {1, 2})


# 6. Square cycle C4: 0 -- 1 -- 2 -- 3 -- 0
g_square = [
    [1, 3],  # 0
    [0, 2],  # 1
    [1, 3],  # 2
    [0, 2],  # 3
]  # V = 4
# Expected: min size = 2 (e.g., {0, 2} or {1, 3})


# 7. Star with center 0 and leaves 1..4
g_star5 = [
    [1, 2, 3, 4],  # 0
    [0],           # 1
    [0],           # 2
    [0],           # 3
    [0],           # 4
]  # V = 5
# Expected: min size = 1 (just {0})


# 8. Square with a diagonal: 0-1-2-3-0 plus 0-2
g_square_diag = [
    [1, 3, 2],  # 0
    [0, 2],     # 1
    [1, 3, 0],  # 2
    [0, 2],     # 3
]  # V = 4
# Expected: min size = 2 (e.g., {0, 2})

# 0-1-2-0 is a triangle, 3 is isolated
g_triangle_plus_isolated = [
    [1, 2],  # 0
    [0, 2],  # 1
    [0, 1],  # 2
    [],      # 3 (isolated)
]  # V = 4

# Expected: min size = 2, e.g. {0,1} or {1,2} or {0,2}
# Vertex 3 should NOT be in an optimal cover.


# Two disconnected K3 components: {0,1,2} and {3,4,5}
g_two_triangles = [
    [1, 2],  # 0
    [0, 2],  # 1
    [0, 1],  # 2
    [4, 5],  # 3
    [3, 5],  # 4
    [3, 4],  # 5
]  # V = 6

# Expected: min size = 4 (2 per triangle).
# Example min cover: {0,1,3,4}


# Path: 0-1-2-3-4
g_path5 = [
    [1],      # 0
    [0, 2],   # 1
    [1, 3],   # 2
    [2, 4],   # 3
    [3],      # 4
]  # V = 5

# For a path on 5 vertices, min vertex cover size = 2 (e.g. {1,3}).


# Star on 0 with leaves 1..4, plus an extra edge 1-2
g_star_extra = [
    [1, 2, 3, 4],  # 0
    [0, 2],        # 1
    [0, 1],        # 2
    [0],           # 3
    [0],           # 4
]  # V = 5

# Expected min size = 2 (e.g. {0,1} or {0,2}).
# If it picks too many leaves, you’ll see a larger cover size.


# Vertex 0 has a self-loop, plus edge 0-1
g_self_loop = [
    [0, 1],  # 0, note the 0 -> 0 self-loop
    [0],     # 1
]  # V = 2

# To cover the self-loop on 0, you MUST include 0.
# Expected min cover = {0}, size = 1.


# Edge 0 -> 1, but not 1 -> 0
g_asymmetric = [
    [1],  # 0
    [],   # 1
]  # V = 2

# Expected: As a directed cover, either {0} or {1} is fine:
# edge (0,1) is covered if 0 in cover or 1 in cover.
# This test is more about reminding you what your representation means.



def run_tests():
    tests = [
        ("Empty graph",        g_empty,       0),
        ("3 isolated vertices",g_isolated,    0),
        ("Single edge",        g_single_edge, 1),
        ("Path 0-1-2",         g_path3,       1),
        ("Triangle K3",        g_triangle,    2),
        ("Square C4",          g_square,      2),
        ("Star (center 0)",    g_star5,       1),
        ("Square + diagonal",  g_square_diag, 2),
        ("Triangle + isolated",g_triangle_plus_isolated, 2),
        ("Two triangles",      g_two_triangles, 4),
        ("Path 0-1-2-3-4",     g_path5,       2),
        ("Star + extra edge",  g_star_extra,  2),
        ("Self-loop on 0",     g_self_loop,   1),
        ("Asymmetric edge",    g_asymmetric,  1),
    ]

    for name, graph, expected_size in tests:
        V = len(graph)
        cover = evc(graph, V)
        print(f"{name}: cover = {cover}, size = {len(cover)}")

        # basic checks
        assert is_vertex_cover(graph, V, cover), f"{name}: result is not a vertex cover!"
        assert len(cover) == expected_size, f"{name}: expected size {expected_size}, got {len(cover)}"

    print("All tests passed!")

# Call this at the bottom of your file (or in a separate test file):
if __name__ == "__main__":
    run_tests()
