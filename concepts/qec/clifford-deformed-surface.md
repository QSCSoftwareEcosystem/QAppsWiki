---
type: concept
name: Clifford-deformed surface code (CDSC)
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/dynamic-gen
- concepts/qec/qldpc
- concepts/qec/quantum-double-abelian
- concepts/qec/random-stabilizer
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/clifford-deformed_surface
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: clifford-deformed_surface
---

# Clifford-deformed surface code (CDSC)

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/clifford-deformed_surface) (`code_id: clifford-deformed_surface`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A generally non-CSS derivative of the surface code defined by applying a translationally invariant constant-depth Clifford circuit to the original (CSS) surface code.
Unlike the surface code, CDSCs include codes whose thresholds and subthreshold performance are enhanced under noise biased towards dephasing.
Examples of CDSCs include the XY code, XZZX code, and random CDSCs.

(source: raw/error-correction-zoo.md)

## Protection

As a stabilizer code, $⟦n=O(d^2), k=O(1), d⟧$.

## Fault tolerance

- In order to leverage the benefits of CDSCs into practical universal computation, we have to implement syndrome measurement circuits and fault-tolerant logical gates in a bias-preserving way.

## Code capacity threshold

- Depolarizing noise: the threshold under ML decoding corresponds to the value of a critical point of the weight-two (two-body) two-dimensional random-bond Ising model (RBIM) on the Nishimori line  ([doi:10.1143/JPSJ.55.3305](https://doi.org/10.1143/JPSJ.55.3305), [arXiv:quant-ph/0110143](https://arxiv.org/abs/quant-ph/0110143), [arXiv:2201.07802](https://arxiv.org/abs/2201.07802)). Utilizing this statistical mechanical mapping yields a phase diagram for a CDSC.
- A class of random CDSCs, parametrized by the probabilities $\Pi_{XZ},~ \Pi_{YZ}$ of $X\leftrightarrow Z$ and $Y\leftrightarrow Z$ Pauli permutations, respectively, has $50\%$ code capacity threshold at infinite $Z$ bias. Certain translation-invariant CDSCs such as the XY code and the XZZX code also have $50\%$ code capacity threshold at infinite $Z$ bias.
- XZZX code and the $(0.5,\Pi_{YZ})$ random CDSCs have a $50\%$ code capacity threshold for noise infinitely biased towards either Pauli-$X$, $Y$, or $Z$ errors.

## Relations

- _parent_: [[concepts/qec/qldpc]]
- _parent_: [[concepts/qec/quantum-double-abelian]] — When treated as ground states of the code Hamiltonian, surface codewords realize $\mathbb{Z}_2$ topological order, a topological phase of matter that also exists in $\mathbb{Z}_2$ lattice gauge theory  ([doi:10.1063/1.1665530](https://doi.org/10.1063/1.1665530)). Local Clifford deformation preserves this topological order.
- _cousin_: [[concepts/qec/dynamic-gen]] — To create CDSCs, a dynamical process is applied on top of the surface code  ([arXiv:2201.07802](https://arxiv.org/abs/2201.07802)).
- _cousin_: [[concepts/qec/random-stabilizer]] — Many useful CDSCs are constructed using random Clifford circuits.
