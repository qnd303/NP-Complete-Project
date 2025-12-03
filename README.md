README.txt
===========

Author: Quan Do
Honor Code and Acknowledgments: This work complies with the JMU Honor Code.

Project: Exact Vertex Cover Solver (CS412 NP-Complete Project)

Overview:
---------
This project implements a brute-force exact solution for the Minimum Vertex Cover problem. 
The program reads an undirected graph from input, finds a minimal vertex cover, 
and prints the solution. 

Instructions to Run:
--------------------
1. Place your input graph in a text file. Format:
   Each line represents an edge: "u v"
   Example:
       0 1
       0 2
       1 2

2. Run the exact solver:
   - Using standard input:
       python cs412_minvertexcover_exact.py < input.txt
   - Using a file argument (optional):
       python cs412_minvertexcover_exact.py input.txt

3. Run all test cases (provided in test_cases/):
   - Make sure run_test_cases.sh is executable: (Use if on linux or mac)
       chmod +x run_test_cases.sh
   - Use git bash if on windows
   - Execute:
       ./run_test_cases.sh
   - This will run the solver on all test cases (small, medium, hard, extreme) and output:
       - Size of the vertex cover
       - Runtime for each test

Test Cases:
-----------
- test_small.py     : small graph, fast runtime
- test_medium.py    : medium graph
- test_hard.py      : harder graph
- test_extreme_23.py: extreme case for >20 minutes runtime

Notes:
------
- The extreme case uses a complete bipartite graph K15,15 to illustrate exponential runtime.
- The solver is guaranteed to find the minimal vertex cover but runtime grows exponentially with graph size.

Problem Importance:
-------------------
The Minimum Vertex Cover problem is a fundamental NP-complete problem with applications in:
- Network security: minimizing monitoring points in a network
- Bioinformatics: identifying critical nodes in protein interaction networks
- Resource allocation: optimizing placement of resources to cover connections
- Scheduling and computational geometry

Citations:
----------
- GeeksforGeeks: Introduction and Approximate Solution for Vertex Cover Problem
  https://www.geeksforgeeks.org/dsa/introduction-and-approximate-solution-for-vertex-cover-problem/
