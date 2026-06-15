---
type: concept
name: RM Majorana code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/majorana-stab
- concepts/qec/quantum-reed-muller
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/majorana_reed_muller
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: majorana_reed_muller
---

# RM Majorana code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/majorana_reed_muller) (`code_id: majorana_reed_muller`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A Majorana stabilizer code constructed from a self-orthogonal RM code.
These codes have the additional property that the global fermion parity is fixed in the codespace. 
Logical measurements are reduced to parity measurements of some subset of Majorana fermions in the code.

(source: raw/error-correction-zoo.md)

## Protection

Code parameters are $⟦2^{m-1},2^{m-1} - \sum_{j=0}^{r} {m \choose j},2^{r+1}⟧_{f}$, which are optimal per Majorana LP bounds for $r = 0$ and $m \geq 1$, and $r=1$ and $m=4,5$  ([arXiv:2502.14165](https://arxiv.org/abs/2502.14165)).

## Relations

- _parent_: [[concepts/qec/majorana-stab]]
- _cousin_: [`reed_muller`](https://errorcorrectionzoo.org/c/reed_muller) — RM Majorana codes are constructed from self-orthogonal RM codes.
- _cousin_: [[concepts/qec/quantum-reed-muller]] — RM Majorana (quantum RM) codes are designed for fermionic (qubit) noise.
