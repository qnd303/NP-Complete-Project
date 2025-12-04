#!/bin/bash

set -e

mkdir -p results

for testfile in test/test_*.txt; do
    base=$(basename "$testfile" .txt)
    echo "=== Processing $testfile ==="

    echo "  [1] Greedy VC:"
    /usr/bin/time -p python3 approx_solution_augment.py < "$testfile" > "results/${base}_vc_greedy.txt"

    echo "  [2] VC → IS conversion:"
    /usr/bin/time -p python3 vc_to_is.py < "$testfile" > "results/${base}.isinput"

    echo "  [3] IS Approximation:"
    /usr/bin/time -p python3 indset_approx.py --t 2 < "results/${base}.isinput" > "results/${base}.is"

    echo "  [4] IS → VC conversion:"
    /usr/bin/time -p python3 is_to_vc.py "$testfile" "results/${base}.is" > "results/${base}_vc_from_is.txt"

    # Count VC sizes (unchanged)
    greedy_size=$(grep -o '[0-9]\+' "results/${base}_vc_greedy.txt" | wc -l)
    is_vc_size=$(grep -o '[0-9]\+' "results/${base}_vc_from_is.txt" | wc -l)

    echo "  Greedy VC size:   $greedy_size"
    echo "  IS-based VC size: $is_vc_size"
    echo
done

echo "All tests processed. Check the results/ directory."
