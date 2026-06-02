---
type: source
status: active
updated: 2026-06-02
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

For PDFs, use the MarkItDown plugin path with Marker-backed extraction when
equations, tables, layout, or figures matter. Preserve both raw source and
extracted markdown in derived pages.

```yaml
sources:
  - raw/pdf/<source>.pdf
source_markdown:
  - raw/md/<source>.md
extracted_with: markitdown
extraction_backend: marker
```
