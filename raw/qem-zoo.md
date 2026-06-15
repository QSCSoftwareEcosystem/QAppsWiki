---
type: source
status: active
updated: '2026-06-15'
title: QEM Zoo
source_type: documentation
location: https://qemzoo.com/
preferred_ingest_path: external
provenance_status: source-backed
domains: [quantum-error-correction, quantum-software]
---

# QEM Zoo

> **Curated external reference catalog.** Registered as a high-value ingest
> candidate for the quantum-error-mitigation side of the
> quantum-error-correction domain. This page tracks the source; it is not
> itself a distilled content page.

## Summary

The [QEM Zoo](https://qemzoo.com/) is a reference catalog of quantum error
*mitigation* (QEM) and quantum error *suppression* (QES) techniques, created and
maintained by Vincent Russo. It distinguishes mitigation (classical
post-processing to reduce the effect of noise — e.g. zero-noise extrapolation)
from suppression (preventing errors beforehand), and is organized into four
sections: **Protocols**, **Techniques**, **Noise**, and **Applications**, plus
an FAQ and a References section. It is explicitly modeled on the Complexity Zoo
and the [[raw/error-correction-zoo]], and addresses an open call for such a
resource raised in the QEM survey literature (Cai et al. 2023).

## Why it matters here

- Complements the Error Correction Zoo: where that catalogs codes, the QEM Zoo
  catalogs the *near-term* noise-handling techniques (ZNE, probabilistic error
  cancellation, dynamical decoupling, …) that QAppsWiki software pages
  implement. These map onto the new error-mitigation extraction priors (e.g.
  zero-noise extrapolation) and the `validates-against` / `encodes-qec` typed
  edges.
- Its Protocols/Techniques/Noise/Applications structure is a ready-made
  scaffold for QEM concept pages and for tagging package capabilities.

## Ingest notes

- `preferred_ingest_path: external` — living web catalog. No documented API or
  bulk data export was found at registration time, so ingest per-technique
  pages or their cited papers into `raw/md/` on demand.
- No explicit license or how-to-cite statement was found on the site at
  registration; **confirm licensing before reusing entry text**, and cite the
  underlying primary sources for technical claims.

## Related

- [[raw/error-correction-zoo]] — sibling catalog for error-correcting codes.
- [[raw/source-inventory]] — master source inventory.
