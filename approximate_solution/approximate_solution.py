#Approximate solution with greedy approach:
#Strategy A:
#Greedy approximation algorithm

# Initialize an empty set C to be the vertex cover.
# While there is an edge remaining in the graph:
# Choose an arbitrary edge 
#  from the graph.
# Add both vertices 
#  and 
#  to the set C.
# Remove 
# , 
# , and all edges connected to either of them from the graph.
# Return the set C. 

#have 4-6 slides for the presentations

# Python3 program to print Vertex Cover
# of a given undirected graph 

# This class represents a directed graph 
# using adjacency list representation 
import sys

def vertex_cover_approx(graph):
    """
    graph: dict mapping vertex -> set of neighbors
           Example: {1: {2,3}, 2:{1}, 3:{1}}

    Returns: a set C that is a 2-approximate vertex cover.
    """
    
    G = {u: set(vs) for u, vs in graph.items()}
    
    C = set()  # vertex cover
    
    # While edges remain
    while True:
        u = None
        v = None
        
        for x in G:
            if G[x]:     
                u = x
                v = next(iter(G[x]))  # arbitrary neighbor
                break
        
        if u is None:  # no edges left
            break
        
        # Add both endpoints to vertex cover
        C.add(u)
        C.add(v)
        
        for neighbor in list(G[u]):
            G[neighbor].discard(u)
        for neighbor in list(G[v]):
            G[neighbor].discard(v)
        
        G[u].clear()
        G[v].clear()

    return C

def parse_graph_from_lines(lines):
    """
    Expects lines like:
        u v
    meaning an undirected edge.
    """
    graph = {}

    for line in lines:
        parts = line.split()
        if len(parts) != 2:
            continue

        u, v = parts

        # convert to int if they are numbers
        try:
            u = int(u)
            v = int(v)
        except:
            pass

        graph.setdefault(u, set()).add(v)
        graph.setdefault(v, set()).add(u)

    return graph


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("no filename provided")

    filename = sys.argv[1]

    with open(filename, "r") as f:
        file_contents = f.read()

    # Clean lines
    lines = [line.strip() for line in file_contents.splitlines() if line.strip()]

    # Parse graph
    graph = parse_graph_from_lines(lines)

    # Compute vertex cover
    C = vertex_cover_approx(graph)

    # Print result
    print("Vertex Cover:", C)
