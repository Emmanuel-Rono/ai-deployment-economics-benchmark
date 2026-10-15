# Task description
Act as a commercial analyst selecting one of three Q4 AI deployment plans. Deliver recommendation.md. Ten input files span CSV, SQLite, JSONL and PDF. The inputs contain exactly 500,000 workload rows (450,000 logical requests and 50,000 retained earlier revisions), 550,000 observed attempts, 5,000 customer accounts, 5,000 benchmark batches, 500 routing rows (300 current mappings plus 200 older revisions), and 360 infrastructure quotations. Commercial terms and planning policy are each exactly 1,200 words. All formatted input documents use 10-point Times. product_research.pdf is the only distractor (10%).

# Complexity justification
1. Workload identity: revised records, cancelled outcomes, case/whitespace variations and mixed quantity units require reconciliation. Correct completed demand is 442,622; counting raw rows or attempt events gives a different population.
2. Two independent commercial histories: mapping revisions determine the executable routes, while offer revisions determine eligible pool pricing. Choosing stale quotes can reverse the recommendation. A careless analyst may also sum repeated transition quotations as separate purchases.
3. Capacity and financial boundaries: hourly peak, replay cache/retry factors, headroom, whole-month reservations and a surviving managed minimum interact. A cheap model is not equivalent to the cheapest feasible complete plan.
4. Scope and timing: fixed monthly customer revenue differs from volume growth, and the full one-time transition is charged in October. Applying volume multipliers to revenue invents income and obscures the actual comparison.

# Taxonomy tags
Domain: Technology / AI infrastructure economics (closest platform category).
Primary: Opportunity Sizing & Decision Support.
Additional: Comparative Analysis & Explanation; Data Quality, Monitoring & Alerting.
Phases: Explore / Discover; Hypothesize; Analyze & Validate; Synthesize; Recommend.

# Expected difficulty range
Target, not measured: strong-model mean below 0.5 with no trial above 0.7, and weak models at least 0.25 below strong models, subject to current project rules. No model sweeps have been run. Difficulty must be established experimentally and must not be manufactured through penalties.

# Ground truth recommendation and rationale
Approve P3, contribution USD 2,921,547.55. All three plans are feasible. P1 contribution is USD 2,904,170.42. P2 contribution is USD 2,919,636.25. P3's advantages are USD 17,377.14 and USD 1,911.30. The reference solver reconstructs these values from shipped inputs. Gold deliverables stay outside environment.

# Expected reasoning trajectory
Establish controlling terms; resolve latest record, mapping and offer revisions; reconcile units and customer joins; aggregate replay evidence; forecast route usage; calculate invoices and peak reservations; apply transition spending once; check feasibility; compare contributions and explain risks. Other methods yielding the same correct results are acceptable.

# Provenance and validation status
Records and scenario documents are generated evaluation material for a fictional business, not historical operations of an actual company. No original user workbook is redistributed. See LICENSE. The user explicitly confirmed on 15 October 2026 that generated fictional inputs are permitted for this project. Direct and extracted-copy checks are in BUILD_REPORT.md. Official Harbor results for the merged ZIP are recorded separately in HARBOR_RUN_RESULTS.md; previous runs on smaller packages do not certify it. Platform rubric/model evaluations remain unrun. The merged prompt deliberately does not require diagnostic counts or October contribution, although the reference memo includes these as optional supporting evidence.

# Exact prompt alignment
The prompt is the exact memo-only text supplied by the user. No CSV, financial table, decimal precision, diagnostic-count checklist or October contribution is compulsory. A 35-item, 100-point memo rubric replaces the former 66-item rubric. Numerical criteria respect displayed precision. Programmatic tests check only the memo and its four headings; substantive grading is rubric-based. Previous 40-check run reports describe older archives.
