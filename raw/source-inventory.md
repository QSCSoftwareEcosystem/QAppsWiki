---
type: source
status: active
updated: 2026-06-03
title: QAppsWiki seed source inventory
source_type: documentation
location: raw/source-inventory.md
preferred_ingest_path: raw/md
provenance_status: source-backed
---

# Source Inventory

This page records the first source selected for each seed package. It does not
replace full source ingest; it defines the initial target for source collection
and conversion.

## Seed Package Sources

| Package | First source | Preferred ingest path | Notes |
|---------|--------------|-----------------------|-------|
| OpenQEvo | `../OpenQEvo/README.md` plus `../OpenQEvo/docs/architecture.md` | local markdown source | First internal package and current MVP slice. |
| Qiskit | Official Qiskit documentation | `raw/md/qiskit-official-docs.md` | Use official docs for installation, circuit model, and versioned adapter assumptions. |
| PennyLane | Official PennyLane documentation | `raw/md/pennylane-official-docs.md` | Use official docs for differentiable programming and adapter assumptions. |
| TNQVM | Official TNQVM / XACC documentation or repository docs | `raw/md/tnqvm-official-docs.md` | Confirm current project status before writing capability claims. |
| Stim | Official Stim documentation or repository docs | `raw/md/stim-official-docs.md` | Use for stabilizer-simulation package page and capability tags. |

## PDF Conversion Policy

For PDFs, use `markitdown-lightpdf` (no-OCR; math/table heuristics for
born-digital papers). Keep extracted markdown in `raw/md/` and record the
original download location here. Do not track raw PDF binaries in Git unless a
source is unavailable elsewhere or explicit archival approval is given.

```yaml
source_url: https://example.org/source.pdf
source_markdown:
  - raw/md/<source>.md
extracted_with: markitdown-lightpdf
```

## OpenQEvo Paper Source URLs

| Local markdown | Source URL |
|----------------|------------|
| `raw/md/2606.00239.md` | https://arxiv.org/pdf/2606.00239 |
| `raw/md/openqevo-annealing-albash-lidar-2016-1611.04471.md` | https://arxiv.org/pdf/1611.04471 |
| `raw/md/openqevo-annealing-das-chakrabarti-2008-0801.2193.md` | https://arxiv.org/pdf/0801.2193 |
| `raw/md/openqevo-annealing-farhi-2000-quant-ph-0001106.md` | https://arxiv.org/pdf/quant-ph/0001106 |
| `raw/md/openqevo-interaction-low-wiebe-2018-1805.00675.md` | https://arxiv.org/pdf/1805.00675 |
| `raw/md/openqevo-randomized-qdrift-campbell-2019-1811.08017.md` | https://arxiv.org/pdf/1811.08017 |
| `raw/md/openqevo-randomized-qswift-2023-2302.14811.md` | https://arxiv.org/pdf/2302.14811 |
| `raw/md/openqevo-randomized-random-trotter-childs-2019-1805.08385.md` | https://arxiv.org/pdf/1805.08385 |
| `raw/md/openqevo-randomized-sparsification-campbell-2019-1910.06255.md` | https://arxiv.org/pdf/1910.06255 |
| `raw/md/openqevo-trotter-gonzalez-garcia-2025-2502.05658.md` | https://arxiv.org/pdf/2502.05658 |
| `raw/md/openqevo-trotter-grimsley-2020-1910.10329.md` | https://arxiv.org/pdf/1910.10329 |
| `raw/md/openqevo-trotter-mehendale-2025-2312.13282.md` | https://arxiv.org/pdf/2312.13282 |
| `raw/md/openqevo-trotter-rajput-2022-q-2022-08-17-780.md` | https://quantum-journal.org/papers/q-2022-08-17-780/pdf/ |
| `raw/md/openqevo-trotter-sugisaki-fmo-2024-2402.17993.md` | https://arxiv.org/pdf/2402.17993 |
| `raw/md/openqevo-trotter-sugisaki-qpe-2024-2406.09830.md` | https://arxiv.org/pdf/2406.09830 |
| `raw/md/openqevo-trotter-suzuki-1976-10.1007-BF01609348.md` | https://doi.org/10.1007/BF01609348 |
| `raw/md/openqevo-trotter-tranter-2019-1912.07555.md` | https://arxiv.org/pdf/1912.07555 |
| `raw/md/openqevo-trotter-yang-2025-2505.04552.md` | https://arxiv.org/pdf/2505.04552 |
