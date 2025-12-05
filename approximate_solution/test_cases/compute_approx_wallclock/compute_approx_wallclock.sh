#!/bin/bash
# run_tests.sh

GRAPH_DIR="test_graphs"
mkdir -p "$GRAPH_DIR"

echo "Generating graphs and running benchmarks..."
python3 generate_tests.py
echo "All graphs generated and results saved to runtime_results.csv!"
