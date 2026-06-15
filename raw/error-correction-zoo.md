---
type: source
status: active
updated: '2026-06-15'
title: Error Correction Zoo
source_type: documentation
location: https://errorcorrectionzoo.org/
preferred_ingest_path: external
provenance_status: source-backed
domains: [quantum-error-correction, quantum-information]
---

# Error Correction Zoo

> **Curated external reference catalog.** Registered as a high-value ingest
> candidate for the quantum-error-correction domain. This page tracks the
> source; it is not itself a distilled content page.

## Summary

The [Error Correction Zoo](https://errorcorrectionzoo.org/) is a comprehensive,
community-maintained reference catalog of error-correcting codes — classical,
quantum, and classical-quantum — maintained by Victor V. Albert and Philippe
Faist with many contributors. At the time of registration it catalogs on the
order of 1,100 code entries organized hierarchically into *domains* (classical /
quantum / classical-quantum), *kingdoms*, and curated *code lists*, alongside a
code graph and a glossary of concepts. Each code entry carries bibliographic
references back to the primary literature, which makes the Zoo a natural index
into source papers for QAppsWiki's quantum-error-correction coverage.

## Why it matters here

- Authoritative, structured taxonomy of QEC codes (stabilizer, topological,
  bosonic, qLDPC, …) that maps cleanly onto the `quantum-error-correction`
  domain and the `qec` `concept_kind` / `qec-artifact` page type.
- Per-code references provide a vetted on-ramp to primary sources for
  promotion into concept pages via the discover→promote loop.
- Open data: the catalog is licensed **CC-BY-SA** with source data on GitHub,
  so entries can be cited and (with attribution) ingested.

## Ingest notes

- **Imported.** `qappswiki import-zoo eczoo` pulls the catalog's structured YAML
  (`errorcorrectionzoo/eczoo_data`, one file per code) into schema-valid
  `concepts/qec/` pages. A bounded flagship set is already imported
  (stabilizer, CSS, surface, toric, color, qLDPC, hypergraph-product,
  Bacon-Shor, Steane, Shor-9, 5-qubit); `--all` imports the full ~1100-code
  catalog (needs a `GITHUB_TOKEN` for the API rate limit).
- Imported pages are `provenance_status: needs-verification` — verify against
  the cited primary sources before relying on them.
- Attribute as **CC-BY-SA, Error Correction Zoo (errorcorrectionzoo.org)** when
  reusing entry text; cite the underlying primary source for technical claims.

## Related

- [[raw/qem-zoo]] — sibling catalog for quantum error *mitigation*.
- [[raw/source-inventory]] — master source inventory.
