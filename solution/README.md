# Reference solution
solve.py reads only the shipped data and reconstructs the quarter comparison. It extracts controlling price terms from the PDFs and computes costs from the latest request records. solve.sh is the oracle entry point. gold/ contains examples for reviewer inspection; neither it nor the solution is copied into the agent image.

Local non-container execution:
python solution/solve.py --data environment/data --output /tmp/meridian-output

Python 3.12 and pypdf 6.1.1 are the intended image dependencies. The supplied base-image digest previously resolved successfully on this machine. The merged image and reference execution are checked again through Harbor. `reporting.py` renders the memo from the recomputed results.

The agreed prompt now requests only recommendation.md. The reference solution emits that memo; its financial table and extra reconciliation counts are optional examples, not compulsory output structure.
