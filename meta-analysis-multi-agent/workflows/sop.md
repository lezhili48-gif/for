# Multi-Agent SOP for Meta-Analysis Writing

## Phase 0 — Project kickoff

**Owner:** Orchestrator

Deliverables:
- `templates/project_charter.md`
- Initial `templates/status_board.csv`

Exit criteria:
- Primary endpoint, effect size type, and target population are fixed.

## Phase 1 — Protocol and criteria

**Owner:** Orchestrator + Search Agent

Deliverables:
- `templates/protocol.md`
- `templates/eligibility_criteria.yaml`

Exit criteria:
- Inclusion/exclusion criteria and analysis plan are pre-specified.

## Phase 2 — Search and screening

**Owner:** Search Agent

Deliverables:
- Search strings per database under `logs/`
- Raw exports in `data/raw/`
- Deduplicated set in `data/processed/`

Exit criteria:
- Search is reproducible (date, DB, syntax, hit count).
- Title/abstract and full-text screening decisions are logged.

## Phase 3 — Extraction and risk of bias

**Owner:** Stats Agent (for structure) + Orchestrator (adjudication)

Deliverables:
- `data/processed/extraction_sheet.csv`
- `data/processed/risk_of_bias.csv`

Exit criteria:
- Double extraction completed and conflicts resolved.

## Phase 4 — Statistical synthesis

**Owner:** Stats Agent

Deliverables:
- Scripts in `analysis_scripts/`
- Outputs in `data/processed/` and `figures/`

Minimum analyses:
- Main model (usually random-effects)
- Heterogeneity: I², τ², Q
- Sensitivity analysis
- Publication bias checks when appropriate

Exit criteria:
- All numbers in summary tables are script-generated.

## Phase 5 — Writing and QA

**Owner:** Writing Agent + Orchestrator

Deliverables:
- Manuscript draft in `docs/manuscript.md`
- PRISMA checklist in `docs/prisma_checklist.md`

Exit criteria:
- PRISMA mapping complete.
- Numerical consistency check passed.

---

## Quality gates

- **Gate A (Method):** question and protocol are pre-registered/frozen.
- **Gate B (Evidence):** search/screening logs are complete.
- **Gate C (Analysis):** model rationale and sensitivity checks present.
- **Gate D (Writing):** all key PRISMA items addressed.
- **Gate E (Reproducibility):** scripts regenerate results and figures.

