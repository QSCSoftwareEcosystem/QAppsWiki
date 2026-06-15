---
type: concept
name: Icosahedral Fock-state code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/constant-excitation
- concepts/qec/fock-state
- concepts/qec/group-representation
- concepts/qec/icosahedral-spin
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/icosahedral_fock
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: icosahedral_fock
---

# Icosahedral Fock-state code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/icosahedral_fock) (`code_id: icosahedral_fock`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A constant-excitation Fock-state code designed to realize the $2I$ group of gates using Gaussian rotations.
It is obtained from the corresponding icosahedral spin code via the simplex mapping between spin and constant-excitation Fock spaces  ([arXiv:2509.20545](https://arxiv.org/abs/2509.20545)).

The code has unnormalized logical states
\begin{align}
  \begin{split}
    |0_{L}\rangle&\propto\sqrt{3}|07\rangle+\sqrt{7}|52\rangle\\
    |1_{L}\rangle&\propto\sqrt{7}|25\rangle-\sqrt{3}|70\rangle\,.
  \end{split}
\end{align}

(source: raw/error-correction-zoo.md)

## Relations

- _parent_: [[concepts/qec/fock-state]]
- _parent_: [[concepts/qec/constant-excitation]]
- _parent_: [[concepts/qec/group-representation]] — Icosahedral Fock-state codes are group-representation codes with the $G = 2I$ subgroup of Gaussian rotations  ([arXiv:2005.10910](https://arxiv.org/abs/2005.10910)).
- _cousin_: [[concepts/qec/icosahedral-spin]] — The icosahedral spin code maps to the icosahedral Fock-state code via the simplex mapping  ([arXiv:2509.20545](https://arxiv.org/abs/2509.20545)).
