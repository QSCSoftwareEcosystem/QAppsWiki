---
type: concept
name: Twisted quantum double (TQD) code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- 2D Dijkgraaf-Witten gauge theory code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/dijkgraaf-witten
- concepts/qec/spt
- concepts/qec/string-net
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/tqd
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: tqd
---

# Twisted quantum double (TQD) code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/tqd) (`code_id: tqd`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Code whose codewords realize a 2D topological order rendered by a Chern-Simons topological field theory.
The corresponding anyon theory is defined by a finite group $G$ and a 3-cocycle $\omega\in H^3( G, U(1) )$  ([arXiv:0705.0665](https://arxiv.org/abs/0705.0665), [arXiv:1211.3695](https://arxiv.org/abs/1211.3695), [arXiv:2112.11394](https://arxiv.org/abs/2112.11394)).
Canonical TQD models  ([arXiv:1211.3695](https://arxiv.org/abs/1211.3695)) are defined on group-valued qudits.

Logical dimension is determined by the genus of the underlying surface (for closed surfaces), types of boundaries (for open surfaces), and any twist defects present.
Excitations are described by the twisted quantum double (a.k.a. twisted Drinfeld double) $D^{\omega}(G)$.
Gapped boundaries of the models are classified by a subgroup $K \subseteq G$ and a particular two-cochain  ([arXiv:1706.03611](https://arxiv.org/abs/1706.03611)).

(source: raw/error-correction-zoo.md)

## Protection

These models realize local topological order (LTO)  ([arXiv:2411.08675](https://arxiv.org/abs/2411.08675)).

## Encoders

- For any solvable group $G$, ground-state preparation can be done with an adaptive constant-depth circuit with geometrically local gates and measurements throughout  ([arXiv:2209.06202](https://arxiv.org/abs/2209.06202)).

## Relations

- _parent_: [[concepts/qec/dijkgraaf-witten]] — Restricting Dijkgraaf-Witten gauge theory to a 2D manifold reproduces the phase of the TQD model  ([arXiv:0705.0665](https://arxiv.org/abs/0705.0665)).
The Drinfeld center of the category $\text{Vec}^{\omega}(G)$ is used to describe bulk excitations of 3D Dijkgraaf-Witten models, and this center is equivalent to the twisted quantum double $D^{\omega}(G)$  ([arXiv:1905.08673](https://arxiv.org/abs/1905.08673)).
TQD codewords are gauge-invariant boundary states of a 3D Dijkgraaf-Witten theory  ([arXiv:1211.3695](https://arxiv.org/abs/1211.3695)).
- _parent_: [[concepts/qec/string-net]] — String-net models realize TQDs for categories $\text{Vec}^{\omega}G$, where $G$ is a finite group and $\omega$ is a 3-cocycle on $G$. There is a duality between a large class of string-net models and certain TQD models  ([arXiv:1211.3695](https://arxiv.org/abs/1211.3695)).
- _cousin_: [[concepts/qec/spt]] — A TQD code Hamiltonian can be obtained by gauging  ([arXiv:1202.3120](https://arxiv.org/abs/1202.3120), [arXiv:1407.1025](https://arxiv.org/abs/1407.1025), [arXiv:1603.04442](https://arxiv.org/abs/1603.04442), [arXiv:1603.05182](https://arxiv.org/abs/1603.05182), [arXiv:1605.01640](https://arxiv.org/abs/1605.01640), [arXiv:1805.01836](https://arxiv.org/abs/1805.01836), [arXiv:1806.08679](https://arxiv.org/abs/1806.08679), [arXiv:2108.11402](https://arxiv.org/abs/2108.11402), [arXiv:2310.16032](https://arxiv.org/abs/2310.16032), [arXiv:2410.02213](https://arxiv.org/abs/2410.02213)) the symmetry of a particular 2D SPT model. The same group and cocycle data classifies both 2D SPTs and TQDs  ([arXiv:1202.3120](https://arxiv.org/abs/1202.3120), [arXiv:1301.0861](https://arxiv.org/abs/1301.0861)).
