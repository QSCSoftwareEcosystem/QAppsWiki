---
type: concept
name: Squeezed cat code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/ampdamp
- concepts/qec/single-mode
- concepts/qec/squeezed-fock-state
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/squeezed_cat
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: squeezed_cat
---

# Squeezed cat code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/squeezed_cat) (`code_id: squeezed_cat`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Two-component cat code whose two coherent states have been squeezed in a direction perpendicular to the segment formed by the two coherent state values $\pm\alpha$.

(source: raw/error-correction-zoo.md)

## Protection

Squeezing of coherent states allows for approximate protection against a single photon loss.

## Encoders

- Lindbladian-based dissipative encoding and autonomous QEC  ([arXiv:2201.02570](https://arxiv.org/abs/2201.02570), [arXiv:2210.13406](https://arxiv.org/abs/2210.13406), [arXiv:2210.13359](https://arxiv.org/abs/2210.13359), [arXiv:2407.18087](https://arxiv.org/abs/2407.18087)).

## Realizations

- Quantum optics: the Laurat group  ([arXiv:1707.06244](https://arxiv.org/abs/1707.06244)).
- Approximately squeezed cat states ("compressed cats") have been realized in a superconducting circuit device by the Gao group  ([arXiv:2212.01271](https://arxiv.org/abs/2212.01271)) (see also  ([arXiv:1707.06244](https://arxiv.org/abs/1707.06244))). Dissipative stabilization has been demonstrated by Alice and Bob  ([arXiv:2502.07892](https://arxiv.org/abs/2502.07892)).

## Relations

- _parent_: [[concepts/qec/single-mode]]
- _parent_: [[concepts/qec/ampdamp]] — Squeezing of coherent states allows for approximate protection against a single photon loss.
- _cousin_: [[concepts/qec/squeezed-fock-state]] — Squeezed Fock-state codes and squeezed cat codes both utilize squeezing to approximately protect against loss errors.
