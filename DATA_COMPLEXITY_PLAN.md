# A substantive complexity upgrade for Aq_Econ

The expanded AQ_Econ2 dataset has now been merged into this workspace: 500,000 workload rows, 550,000 attempts, 5,000 accounts, 100 route groups and 147.37 MiB of inputs. Routing and quotation histories are implemented. The additions below remain a proposed next-stage redesign, not data already added or a difficulty claim. Generated scenario data is permitted, as confirmed by the user.

## What currently limits the challenge

The current workload has substantial row counts and more accounts/routes, but replay evaluation still reduces to six model/use-case groups. The replay factors are simple cell averages. Most commercial terms are short and centralized. The planning policy gives an almost executable recipe for demand, token billing and peak capacity. The attempt log mainly supports a count distinction rather than a necessary reconciliation. Once those conventions are read, adding more identically structured rows would mostly increase runtime.

The goal should be six interacting sources of economic evidence, with multiple independent ways for a plausible analysis to choose the wrong plan. Keep all three options commercially plausible until the detailed comparison is done. Do not manufacture difficulty by hiding an amendment, leaving an essential definition unresolved, or setting penalties that suppress scores.

## Recommended additions, in priority order

| Priority and dataset | Proposed content and scale | Required cross-reference | Economically consequential mistake |
|---|---|---|---|
| 1. Event-level operations database | 5-8 million logical requests across 90 days, 150-300 accounts, 8-12 use cases and at least two regions. SQLite tables for request revisions, status changes, alias history, routing assignments and ingestion batches. Include event time and ingestion time. | Join effective-dated account identities, service entitlements, retry chains and business cut-off rules. | Counting replays or superseded revisions as fresh demand, or assigning a merged account to the wrong commercial terms changes billable volume. |
| 2. Attempt, cache and performance traces | 12-25 million attempt events in partitioned Parquet/JSONL, linked to requests. Include retry cause, partial output, cache-key lineage, model/version, region, start/end time, queue delay, concurrency and actual billed tokens. Include unequal cohort sizes and version rollout periods. | Reconcile the request database to observed attempts, model-version benchmarks and billed usage. | Treating retries as independent customer requests, applying cache benefits to an ineligible region, or using unrepresentative aggregate benchmark means changes model cost or feasibility. |
| 3. Contract and amendment evidence | A relational XLSX register with about 1,000-3,000 account/product/term rows, plus substantive contract PDFs covering 20-40 pages in total. Include signed amendments, effective dates, account migrations, minimum commitments, tier boundaries, credit eligibility and region restrictions. | Register entries point to document IDs, clauses, products and effective dates; usage and billing map through account histories. | Applying a superseded tariff, pooling commitments across ineligible products, or missing a valid credit reverses contribution ranking. |
| 4. Shared-capacity evidence | GPU telemetry at five-minute intervals for 30-60 devices over 90 days, reservation/maintenance calendars and benchmark experiments across model versions, concurrency and context-length bands. Include shared-pool membership and region limits. | Align demand peaks to time zones, actual pool membership, scheduled outages and valid benchmark conditions. | Summing isolated route peaks instead of simultaneous pool load overstates capacity; using quarter averages understates it. Both should affect the plan decision. |
| 5. Billing and finance ledger | 100,000-300,000 invoice lines, corrections, credits and cost allocations, with service month, posting date, currency and original-document references. Add an authoritative monthly FX table only if multi-currency economics is in scope. | Reconcile invoices to contract terms and usage; distinguish recurring prospective costs from historical true-ups and migration cash spending. | Treating all postings as current operating cost, double counting reversals or missing floors changes the financially preferred plan. |
| 6. Commercial forecast and service evidence | Forecast vintages and signed commercial status for each account/product/month; quality evaluations and incident records linked to affected accounts, model versions and service periods. Include contracted versus contingent demand and overlapping service incidents. | Connect customer commitments to valid forecast vintages and SLA exposure, with documented treatment of contingent volumes and overlapping incidents. | Counting unsigned pipeline as guaranteed revenue, double counting credits, or extrapolating clean benchmark results to an ineligible production cohort creates a different preferred option. |

Do not add every feature independently. Design one coherent scenario: for example, an account migration changes its commitment pool, its region restriction changes routing, routing changes simultaneous resident load, and an outage exposes a service-credit clause. The analyst must connect the evidence to resolve a financial difference.

## Packaging and volume targets

Aim initially for roughly **1.2-2.5 GiB unpacked**, subject to measured runtime and compression. This is a design budget, not an acceptance threshold or a promise that size creates difficulty. Keep each physical file comfortably below the 1 GiB limit, for example 150-400 MiB per trace shard. Target a ZIP comfortably below 1 GiB and stay below 4 GiB unpacked. Measure actual archive sizes: Parquet may not compress much further inside ZIP.

An operational SQLite database supplies depth in the database category. The effective-dated contract workbook plus the commercial documents supply separate spreadsheet/text complexity: the workbook must require relational interpretation, not merely contain a long flat price list. Trace shards add scale and temporal evidence. Preserve at least one plausible distractor and keep distractors at no more than 20% of all data files, counting shards as individual files where the platform does.

Use representative small files to validate the design before expanding to millions of rows. Benchmark the final reference solution against the task's 4-CPU, 8-GiB-memory limits. Require streaming or indexed queries where appropriate; do not force the analyst to load every raw event into RAM. Set timeouts from measured runs, within the project's runner limits.

## Preserve one defensible answer

1. Define the business objective, decision cut-off, governing contract precedence, pool membership, forecast eligibility and acceptable service levels in normal business documents. Make the rules available without prescribing SQL, joins or analysis steps.
2. Build a private scenario specification outside `environment/`. Give every important business event consistent references across source systems. Model discrepancies through recognizable collection and accounting mechanisms, not random corrupted values.
3. Independently reconcile request, attempt and billing totals. Check that each emitted reference number can be traced to shipped evidence. Generate the answer from source data rather than copying a desired P3 label into outputs.
4. Compute the full ranking and feasibility after all mechanisms interact. Allow the winning plan to change from today's P3 if the redesigned evidence supports that result.
5. Measure counterfactual shortcuts independently: old terms, wrong demand population, wrong peak aggregation, missed credit/reversal, wrong forecast vintage. Record which number each mistake changes and whether it changes the winner or a meaningful feasibility finding. A shortcut with no decision consequence is secondary detail, not the central challenge.
6. Require a positive decision margin under numerical rounding and all permitted interpretations. If two defensible treatments produce different winners, clarify the business evidence. Do not resolve it through a hidden grading convention.
7. Grade independent conclusions rather than charging repeatedly for descendants of one incorrect aggregate. Retain partial credit and a method-independent rubric.
8. Run the reference solver, nop/oracle checks and platform difficulty sweeps. Treat difficulty as unmeasured until actual trials demonstrate it.

## How to simplify the planning policy without creating ambiguity

Retain authoritative business definitions such as which contract governs, how a reservation is charged, the service deadline, and the reporting period. Replace analysis recipes like “group these fields, compute these means, divide by these factors” with source-system semantics and commercial rules. Let the analyst discover the necessary grain, valid cohorts, temporal joins and simultaneous capacity calculation. Do not delete an essential rule merely to make interpretation harder.

## Recommended first implementation

Start with priorities **1-4 together**, not an isolated giant event export. They create the core interaction between logical demand, economic terms and physically feasible capacity. Add the finance ledger next to validate charges and adjustments. Add forecast/service-credit complexity only after it has documented decision relevance and a reliable reference implementation.

The redesign will require changes to `environment/data`, `solution/solve.py`, `tests/expected.json`, `rubrics.json`, the gold deliverables and task card. Revisit the output schema if several GPU pools or a revised revenue definition need separate reporting. Do not upload new raw files while retaining the old expected values and recommendation.
