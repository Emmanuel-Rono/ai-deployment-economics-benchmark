# Task description

Select one of three Q4 2026 deployment plans for Meridian AI's investment committee. Submit `recommendation.md`, comparing the alternatives using financial evidence, source citations, reconciled records and operating requirements.

Ten input files contain 500,000 workload versions, 550,000 attempts, 5,000 accounts, 5,000 replay batches, 500 routing records and 360 infrastructure quotations. Formats: SQLite, JSONL, CSV and PDF. `product_research.pdf` is the single distractor.

# Complexity justification

1. Workload identity: revisions, cancelled requests, identifier variants and mixed token units are present. Correct reconciliation retains 442,622 completed latest requests. Summing revisions or treating attempts as logical requests overstates demand.
2. Commercial history: routing and infrastructure registers retain prior revisions. Correct analysis uses approved current mappings and eligible monthly offers. Stale records misstate executable routes and capacity costs.
3. Capacity economics: demand peaks, cache/retry factors, throughput, headroom and whole-month reservations determine GPU costs. Average-load estimates understate required reservations.
4. Commitment and timing: managed commitments survive local routing; transition quotes apply once at quarter start. Dropping commitments or multiplying transition quotes by mapping rows misstates plan contribution.
5. Revenue scope: subscription revenue is fixed by account while forecast factors apply to usage. Scaling revenue with request growth invents income.

# Taxonomy

Domain: Technology / AI infrastructure economics.
Primary objective: Opportunity Sizing & Decision Support.
Additional objectives: Comparative Analysis & Explanation; Data Quality, Monitoring & Alerting.
Reasoning phases: Explore / Discover; Hypothesize; Analyze & Validate; Synthesize; Recommend.

# Expected difficulty

Hard. The task requires record reconciliation, versioned commercial interpretation, peak-capacity calculation and contribution comparison across connected sources.

# Ground truth

P3 maximizes feasible Q4 contribution at USD 2,921,547.55. P1 contributes USD 2,904,170.42; P2 contributes USD 2,919,636.25. P3's advantages are USD 17,377.14 and USD 1,911.30, calculated before rounding. All three plans satisfy operating requirements.

# Reference analysis

Resolve controlling terms and record revisions; normalize demand and account joins; apply replay evidence and monthly forecasts; calculate managed charges, peak reservations and transition spending; check feasibility; compare contributions and decision risks.

# Provenance

The dataset contains synthetic records and commercial documents for a fictional business. Licence: CC-BY-4.0; see LICENSE.
