# Part E – Augment the Study

For this part of the project, we added a second way to approximate the Minimum Vertex Cover.  
Instead of only using our greedy VC algorithm, we also converted the problem into an  
Independent Set (IS) problem, ran an IS approximation, and then converted the result back  
into a vertex cover. This gave us another solution to compare against our greedy method.

## What the scripts do
- `vc_to_is.py`  
  Takes a VC adjacency-list graph and converts it into the edge-list format required by the IS solver.

- `indset_approx.py`  
  Instructor-provided Independent Set approximation algorithm.

- `is_to_vc.py`  
  Converts the IS output back into a vertex cover using the complement: VC = V − IS.

- `approx_solution_augment.py`  
  Our greedy Vertex Cover approximation.

- `run_augment.sh`  
  Runs the entire pipeline automatically on every test graph.

## How to run everything
From inside the `augment/` directory:

chmod +x run_augment.sh
./run_augment.sh

This script will:
1. Run our greedy VC approximation  
2. Convert the graph to IS format  
3. Run the IS approximation  
4. Convert the IS solution back into a vertex cover  
5. Print both VC sizes and write all outputs to `results/`

That's all that’s needed to reproduce our augmented results.
