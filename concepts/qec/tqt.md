---
type: concept
name: Twisted quantum triple (TQT) code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- 3D Dijkgraaf-Witten gauge theory code
- 3D twisted quantum-double code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/dijkgraaf-witten
- concepts/qec/tqd
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/tqt
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: tqt
---

# Twisted quantum triple (TQT) code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/tqt) (`code_id: tqt`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Group-based code realizing a 3D topological order rendered by a Dijkgraaf-Witten gauge theory.
The corresponding anyon theory is defined by a finite group $G$ and a Type-IV four-cocycle $\omega$.
Canonical TQT models  ([arXiv:1212.0835](https://arxiv.org/abs/1212.0835), [arXiv:1404.1062](https://arxiv.org/abs/1404.1062)) and other formulations whose ground states are in the same phase are all defined on group-valued qudits.

Boundaries and excitations have been studied in Refs.  ([arXiv:1807.11083](https://arxiv.org/abs/1807.11083), [arXiv:2006.06536](https://arxiv.org/abs/2006.06536), [arXiv:2401.13042](https://arxiv.org/abs/2401.13042)).
Gapped boundaries are classified by a subgroup $K \subseteq G$ and a particular three-cochain  ([arXiv:1807.11083](https://arxiv.org/abs/1807.11083)).
Generalizations of Ocneanu's tube algebras  ([doi:10.2969/aspm/03110235](https://doi.org/10.2969/aspm/03110235)) can be used to characterize excitations, which are described by the tube algebra of the category $\text{Vec}^{\omega}(G)$  ([arXiv:1905.08673](https://arxiv.org/abs/1905.08673), [arXiv:2305.17165](https://arxiv.org/abs/2305.17165)).

(source: raw/error-correction-zoo.md)

## Relations

- _parent_: [[concepts/qec/dijkgraaf-witten]] — Restricting Dijkgraaf-Witten gauge theory to a 3D manifold reproduces the phase of the TQT model.
- _cousin_: [[concepts/qec/tqd]] — The TQT model can be thought of as a 3D version of the TQD model.
