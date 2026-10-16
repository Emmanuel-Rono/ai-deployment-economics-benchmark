# Reference solution

`solve.py` computes Q4 plan economics from the supplied workload, forecast, routing, benchmark, quotation and contract data. `reporting.py` writes `recommendation.md`.

Oracle entry point: `solve.sh`.

```powershell
python solution/solve.py --data environment/data --output .local-checks/reference-output
```

Container dependencies: Python 3.12 and pypdf 6.1.1. The reference memo is stored in `gold/recommendation.md`.
