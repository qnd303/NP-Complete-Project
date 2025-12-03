#!/usr/bin/env bash
# Run all Part E/F stuff:
# - VC -> IS reduction (for each test graph)
# - exact vs approx comparison
# Results go to augment/results/augment_results.txt

set -e

AUGMENT_DIR="augment"
TEST_DIR="$AUGMENT_DIR/test"
RESULTS_DIR="$AUGMENT_DIR/results"

mkdir -p "$RESULTS_DIR"

OUT_FILE="$RESULTS_DIR/augment_results.txt"
# Truncate previous results
: > "$OUT_FILE"

# Use YOUR filenames here:
GRAPHS=(
  "$TEST_DIR/vc_small_triangle.txt"
  "$TEST_DIR/vc_square.txt"
  "$TEST_DIR/vc_star.txt"
)

echo "=== NP Project: Part E/F Augment & Compare Run ===" | tee -a "$OUT_FILE"
date | tee -a "$OUT_FILE"
echo "" | tee -a "$OUT_FILE"

for G in "${GRAPHS[@]}"; do
  if [ ! -f "$G" ]; then
    echo "WARNING: $G not found, skipping." | tee -a "$OUT_FILE"
    continue
  fi

  BASENAME=$(basename "$G" .txt)
  IS_FILE="$RESULTS_DIR/${BASENAME}.is"

  echo "==========================================" | tee -a "$OUT_FILE"
  echo "Graph: $G" | tee -a "$OUT_FILE"
  echo "" | tee -a "$OUT_FILE"

  # ---- VC -> IS reduction (Part E) ----
  echo "--- VC -> IS reduction (saved to $IS_FILE) ---" | tee -a "$OUT_FILE"
  python3 "$AUGMENT_DIR/vc_to_is.py" < "$G" | tee "$IS_FILE" | tee -a "$OUT_FILE"
  echo "" | tee -a "$OUT_FILE"

  # ---- Exact vs Approx comparison (Part F data) ----
  echo "--- Exact vs Approx comparison ---" | tee -a "$OUT_FILE"
  python3 "$AUGMENT_DIR/compare_vc_methods.py" "$G" | tee -a "$OUT_FILE"
  echo "" | tee -a "$OUT_FILE"
done

echo "==========================================" | tee -a "$OUT_FILE"
echo "Done. See:" | tee -a "$OUT_FILE"
echo "  - $OUT_FILE for full text results" | tee -a "$OUT_FILE"
echo "  - $RESULTS_DIR/*.is for IS instances from the reduction" | tee -a "$OUT_FILE"
