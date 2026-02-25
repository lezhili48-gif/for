# Meta-Analysis Multi-Agent Kit

A practical, auditable workflow template for running a full meta-analysis paper pipeline with multi-agent collaboration.

## What this kit solves

- Role-based collaboration for Orchestrator / Search / Stats / Writing agents.
- Reproducible handoffs via explicit artifact contracts.
- Phase-based execution with quality gates before manuscript finalization.

## Common gaps from earlier drafts (and fixes here)

- Gap: templates existed but startup actions were unclear.
  - Fix: added Chinese startup playbook at `docs/startup_playbook_zh.md`.
- Gap: manuscript skeleton was too thin for direct drafting.
  - Fix: expanded `docs/manuscript.md` into section-by-section drafting blueprint.

## Quick start (recommended order)

1. Fill protocol and eligibility criteria:
   - `templates/protocol.md`
   - `templates/eligibility_criteria.yaml`
2. Configure project control files:
   - `templates/project_charter.md`
   - `templates/decision_log.md`
   - `templates/status_board.csv`
3. Run the 4-agent workflow:
   - `prompts/orchestrator.md`
   - `prompts/search_agent.md`
   - `prompts/stats_agent.md`
   - `prompts/writing_agent.md`
4. Follow staged execution in `workflows/sop.md`.
5. If your team works in Chinese, use `docs/startup_playbook_zh.md` as the day-1 runbook.

## Repository layout

- `templates/`: fill-in documents and machine-readable schemas.
- `prompts/`: production-ready prompts for 4 core agents.
- `workflows/`: SOP and quality gates.
- `docs/`: manuscript and PRISMA writing assets.
- `analysis_scripts/`: analysis code (R/Python).
- `data/raw/`: raw records and exports.
- `data/processed/`: deduplicated, screened, and extracted data.
- `figures/`: generated plots (forest/funnel/sensitivity).
- `logs/`: run logs and audit trails.

## Suggested execution contract

Every agent output should include:

- `task_id`
- `input_artifacts`
- `output_artifacts`
- `assumptions`
- `open_risks`
- `done_definition` checklist result

Numerical claims in manuscript must be traceable to analysis outputs.

## Recommended stack

- Screening: Rayyan/Covidence + Zotero
- Analysis: R (`metafor`, `meta`) preferred
- Writing: Markdown + Git
- Reproducibility: `renv` (R) or `conda` (Python)

## Input intake for your 3 core files

Place these files in `meta-analysis-multi-agent/inputs/` (recommended) or any repo subfolder:

- `PRISMA_Protocol_Biochar_DNRA_Denitrification.pdf` (or same-name `.md`)
- `Data_Extraction_Template.xlsx`
- `Meta_Analysis_R_Code.R`

Then run:

```bash
python meta-analysis-multi-agent/scripts/ingest_and_assess.py
```

Generated outputs:
- `docs/input_assessment_report_zh.md`
- `docs/pipeline_progress_zh.md`
- `logs/input_assessment_summary.json`

