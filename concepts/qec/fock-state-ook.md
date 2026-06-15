---
type: concept
name: Fock-state OOK c-q modulation format
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Number-state OOK c-q modulation format
- Fock-state OOK c-q modulation code
- Fock-state OOK c-q modulation scheme
- Fock-state OOK c-q signaling format
- Single-photon OOK c-q modulation format
- Single-rail c-q code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/bosonic-classical-into-quantum
- concepts/qec/fock-state
- concepts/qec/quantum-ook
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/fock_state_ook
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: fock_state_ook
---

# Fock-state OOK c-q modulation format

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/fock_state_ook) (`code_id: fock_state_ook`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Bosonic c-q on-off keying (OOK) modulation format whose binary alphabet consists of the vacuum state $|0\rangle$ and the single-photon Fock state $|1\rangle$ of one mode.
More generally, the nonzero OOK symbol can be a number state or a mixture of adjacent number states.
Fock-state OOK with photon-number detection was analyzed as a nonclassical alternative to coherent-state OOK for photon-efficient communication  ([doi:10.1109/ITA.2012.6181832](https://doi.org/10.1109/ITA.2012.6181832)).

(source: raw/error-correction-zoo.md)

## Decoders

- Photon-number detection distinguishes the erasure/loss-degraded output alphabet by detecting whether photons are present in the received mode  ([doi:10.1109/ITA.2012.6181832](https://doi.org/10.1109/ITA.2012.6181832), [arXiv:1410.4575](https://arxiv.org/abs/1410.4575)).
- Number-state modulation with photon detection, including the numerical observation that the optimal prior distribution can be multimodal, was studied in Ref. }. Later work on incoherent OOK and PPM quantified improvements from sub-Poissonian nonclassical light and used Fock states as the nonclassical low-photon-number alphabet  ([arXiv:1410.4575](https://arxiv.org/abs/1410.4575)).

## Relations

- _parent_: [[concepts/qec/bosonic-classical-into-quantum]]
- _cousin_: [[concepts/qec/quantum-ook]] — Fock-state OOK and coherent-state OOK both use a vacuum off symbol, but their on symbols are respectively a single-photon number state and a coherent state.
- _cousin_: [[concepts/qec/fock-state]] — Fock-state OOK transmits classical information using Fock states, while Fock-state bosonic codes store quantum information in subspaces built from Fock states.
