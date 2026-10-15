# Meridian AI deployment investment decision

## Recommendation

Approve P3 for 1 October to 31 December 2026. It produces the highest feasible Q4 operating contribution after transition spending: USD 2,921,547.55. P3 exceeds P1 by USD 17,377.14. P3 exceeds P2 by USD 1,911.30.

## Evidence

The decision basis is Q4 operating contribution after transition spending, not headline model price or gross margin percentage. All three plans satisfy the minimum quality pass rate of 0.94, replay p95 ceiling of 3000 ms, restricted-account residency rule and monthly physical pool limits of 10 GPUs. Restricted accounts remain on Local-L. Source: planning_policy.pdf, Decision mandate and Capacity eligibility and planning limits; commercial_terms.pdf, Service and quality requirements.

| Plan | Revenue (USD) | Managed invoice (USD) | GPU cost (USD) | Overhead (USD) | Transition (USD) | Q4 contribution (USD) | GPUs Oct/Nov/Dec | Feasible |
|---|---:|---:|---:|---:|---:|---:|---|---|
| P1 | 3,317,096.25 | 89,141.83 | 50,784.00 | 255,000.00 | 18,000.00 | 2,904,170.42 | 2/2/2 | true |
| P2 | 3,317,096.25 | 7,500.00 | 126,960.00 | 255,000.00 | 8,000.00 | 2,919,636.25 | 5/5/5 | true |
| P3 | 3,317,096.25 | 28,980.70 | 101,568.00 | 255,000.00 | 10,000.00 | 2,921,547.55 | 4/4/4 | true |


The source workload contains 500,000 version rows representing 450,000 logical requests before filtering. It has 442,622 completed logical requests after discarding 50,000 older request revisions and excluding 7,378 cancelled latest requests. The troubleshooting file has 550,000 observed inference attempts. Attempts are not additional logical demand. There are 40,239 completed records in ktokens; these quantities require conversion to individual tokens. Account normalization resolves 49,180 completed records with case or surrounding whitespace differences. Source: workload.sqlite, request_versions; attempt_events.jsonl; data_dictionary.pdf, Scope and identifiers.

The customer forecast contains 5,000 contracted accounts. Its factors change volume rather than subscription revenue. The highest revision replaces earlier versions of each logical request and mapping identifier; these are corrections rather than additional demand or routes. Cancelled latest requests are excluded from prospective completed demand. The plan register contains 500 rows but only 300 current routing rules after resolving 200 older versions by mapping identifier. The infrastructure register contains 360 quote rows; 36 current offers remain across 12 pools and three months, and only resident-a is award eligible. Superseded or award-ineligible infrastructure quotations cannot price the approved resident workload. The benchmark has 5,000 independent batches, not routing revisions. Source: customer_forecast.csv; deployment_options.csv; infrastructure_offer.csv; replay_benchmark.csv; data_dictionary.pdf.

For P3, reserve 4 GPUs in October, 4 GPUs in November and 4 GPUs in December. Use the eligible latest monthly quotes: USD 11.50 per GPU-hour, throughput 310 output-equivalent tokens per second, and 80% permitted utilisation. The minimum reservation is two GPUs, and the physical limit is ten GPUs. Hourly peak load establishes the reservation; idle hours do not offset a busy-hour shortage. Calendar-day scaling affects monthly inference activity, not representative hourly peak demand. Source: infrastructure_offer.csv, current resident-a rows; planning_policy.pdf, Resident capacity convention.

The selected plan's October contribution, including its entire transition charge, is USD 967,057.16. Revenue is fixed contracted monthly revenue. The shared platform overhead is USD 85,000 per month, or USD 255,000 over Q4. Source: customer_forecast.csv, monthly_revenue_usd; planning_policy.pdf, Decision mandate and Comparability and timing.

## Alternatives

The cheaper-model hypothesis favours local processing on price intuition, but it must include the reserved peak pool, the surviving managed commitment and transition spending. P2 still owes USD 2,500 each month even with no managed traffic. Cached eligible first-pass input is discounted, while retry input remains billable and retry outputs use the partial-output factor. Adding another retry-waste surcharge would double-count this processing. The table compares every plan on the same cost boundary. Source: commercial_terms.pdf, Executed amendment and Invoice boundary and cost ownership.

The headline-price hypothesis must use the executed September rates of USD 6 per million input tokens and USD 24 per million output tokens. The July USD 4/14 schedule is superseded. Monthly managed commitments are floors, not additive fees. Transition quotes of USD 18,000 for P1, USD 8,000 for P2 and USD 10,000 for P3 apply once per plan, rather than once per routing row. Ineligible pool quotations and superseded mapping revisions do not describe executable alternatives. Source: commercial_terms.pdf, Transition quotes and Superseded commercial schedule; deployment_options.csv; infrastructure_offer.csv.

## Risks

Replay drift could invalidate a route that currently meets its service requirements. Reconsider if production validation shows a deployed model/use-case quality pass rate below 0.94 or p95 latency above 3000 ms. Replay evidence is a planning assumption rather than a measured causal effect of migration. Source: commercial_terms.pdf, Service and quality requirements.

Concentrated account growth could increase the hourly peak and reservation cost. Reconsider if updated demand requires more than 10 GPUs in any month, or if revised total costs erase the selected plan's smallest contribution advantage of USD 1,911.30. The financial and operational owners should refresh demand and benchmark evidence before implementation. No unsupported revenue uplift or negotiated future rebate enters this comparison. Source: planning_policy.pdf, Capacity eligibility and planning limits and Reconciliation and limitations.
