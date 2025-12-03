#!/bin/bash

# Run all test cases for the approximation algorithm

echo "Running small graph..."
python3 cs412_minvertexcover_approx.py test_cases/small_graph.txt

echo "Running medium graph..."
python3 cs412_minvertexcover_approx.py test_cases/medium_graph.txt

echo "Running large graph..."
python3 cs412_minvertexcover_approx.py test_cases/large_graph.txt

echo "Running non-optimal graph..."
python3 cs412_minvertexcover_approx.py test_cases/non_optimal.txt
