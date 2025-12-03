#!/bin/bash

# Adjust to your Python path
PYTHON="/c/Python314/python.exe"

echo "==== Running All Vertex Cover Tests ===="

TEST_CASES=("test_small.py" "test_medium.py" "test_hard.py" "test_extreme_23.py")
TEST_NAMES=("Small" "Medium" "Hard" "Extreme23")

for i in "${!TEST_CASES[@]}"; do
    name=${TEST_NAMES[$i]}
    file="test_cases/${TEST_CASES[$i]}"  # path to test file

    echo "Running $name ($file)..."

    # Use ./run_test.py explicitly to force the correct folder
    $PYTHON ./run_test.py "$file"

    echo "-------------------------------"
done

echo "All tests finished."

# NOTE: test_extreme_23.py may take more than 20 minutes
