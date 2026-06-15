---
type: concept
name: Locally compact Abelian (LCA) stabilizer code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Mixed GKP code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/group-gkp
- concepts/qec/hybrid-qudit-oscillator
- concepts/qec/stabilizer
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/lca_stabilizer
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: lca_stabilizer
---

# Locally compact Abelian (LCA) stabilizer code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/lca_stabilizer) (`code_id: lca_stabilizer`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A mixed oscillator stabilizer code whose codewords are quantum lattice states defined on any number of qudits and a nonzero number of oscillators.
Its stabilizers are countably infinite subgroups of the qudit Pauli and oscillator displacement groups.
Codewords are entangled across the qudit-oscillator bipartition.

The simplest LCA state is a Bell state of a single physical qubit and a GKP-encoded qubit,
\begin{align}
  |\text{LCA}\rangle&=\sum_{\ell\in\mathbb{Z}}|x=\ell\sqrt{\pi}\rangle\left|\ell\text{ mod }2\right\rangle \\&=\sum_{s\in\mathbb{Z}}{|{x=(2s)\sqrt{\pi}}\rangle}\left|0\right\rangle +{|{x=(2s+1)\sqrt{\pi}}\rangle}\left|1\right\rangle ~.
\end{align}
LCA stabilizers with such codewords are called simple.

*Simple* single-mode single-qudit LCA codewords can be viewed as $Kc$-dimensional GKP codewords whose logical subsystem decomposition $\mathbb{Z}_{Kc}\cong\mathbb{Z}_{K}\times\mathbb{Z}_{c}$ entangles the $\mathbb{Z}_{c}$ factor with the physical qudit  ([arXiv:2508.04819](https://arxiv.org/abs/2508.04819)).

(source: raw/error-correction-zoo.md)

## Protection

Simple LCA stabilizers can protect against either a larger set of displacements than GKP codes or a smaller set along with all single-qudit Pauli errors  ([arXiv:2508.04819](https://arxiv.org/abs/2508.04819)).

The syndrome space of a simple LCA stabilizer can be characterized entirely by a unit cell of displacements. For a single $c$-dimensional qudit and single-oscillator code, the area of this cell is $2\pi c$. Displacement values that keep the codewords inside this unit cell can be measured simultaneously, meaning that one can simultaneously measure an arbitrary range of values of two non-commuting displacements given sufficient qudit dimension  ([arXiv:2508.04819](https://arxiv.org/abs/2508.04819)).

## Rate

Single-mode single-qudit LCA codes have logical dimension $K=c\theta+d$ for integers $\theta\geq 0$ and $d\in\mathbb{Z}_{c}^{\times}$, the multiplicative group of integers modulo $c$  ([arXiv:2508.04819](https://arxiv.org/abs/2508.04819)).

## Encoders

- Codewords of a simple single-qudit single-oscillator code can be initialized by applying a conditional oscillator-qudit displacement to a GKP state and a qudit $|+\rangle$ state  ([arXiv:2508.04819](https://arxiv.org/abs/2508.04819)). Alternatively, one can prepare a two-qudit Bell state and encode one subsystem into a GKP qudit code  ([arXiv:2508.04819](https://arxiv.org/abs/2508.04819)).
- General LCA stabilizers can be created by using a general embedding of their stabilizer algebra, a non-commutative torus  ([doi:10.4153/CJM-1988-012-9](https://doi.org/10.4153/CJM-1988-012-9), [arXiv:hep-th/9805034](https://arxiv.org/abs/hep-th/9805034), [arXiv:hep-th/9711162](https://arxiv.org/abs/hep-th/9711162), [arXiv:math/9803057](https://arxiv.org/abs/math/9803057)), into LCA groups  ([arXiv:2508.04819](https://arxiv.org/abs/2508.04819)). Logical operators can be obtained via Morita equivalence  ([arXiv:2508.04819](https://arxiv.org/abs/2508.04819)).

## General gates

- Several LCA code families admit logical Clifford gates via Gaussian transformations on the oscillators together with Clifford gates on the qudits; for single-mode $(c,d)$-LCA codes, this includes a logical Hadamard implemented by an oscillator Fourier transform and a corresponding qudit Clifford operation  ([arXiv:2508.04819](https://arxiv.org/abs/2508.04819)).
- Adding a conditional oscillator-qudit displacement makes the gate set universal  ([arXiv:2509.18854](https://arxiv.org/abs/2509.18854)).

## Decoders

- Simple LCA codes admit a decoder for pure displacement noise, a decoder for all single-qudit Pauli errors together with a smaller displacement range, and for physical qubits a balanced decoder that trades oscillator against qudit error tolerance by moving syndrome-region boundaries  ([arXiv:2508.04819](https://arxiv.org/abs/2508.04819)).
- Under Petz (transpose) recovery against photon loss and qubit amplitude damping, $c=2$ LCA codes can match or outperform comparable GKP codes at low energy for sufficiently large logical dimension  ([arXiv:2508.04819](https://arxiv.org/abs/2508.04819)).

## Relations

- _parent_: [[concepts/qec/hybrid-qudit-oscillator]]
- _parent_: [[concepts/qec/stabilizer]]
- _cousin_: [`binary_linear`](https://errorcorrectionzoo.org/c/binary_linear) — Linear binary codes can be used to construct LCA stabilizer codes  ([arXiv:2508.04819](https://arxiv.org/abs/2508.04819)).
- _cousin_: [`eeight`](https://errorcorrectionzoo.org/c/eeight) — Integer symplectic matrices like the symplectic $E_8$ generator matrix can be used to construct LCA stabilizer codes  ([arXiv:2508.04819](https://arxiv.org/abs/2508.04819)).
- _cousin_: [[concepts/qec/group-gkp]] — Simple single-mode single-qudit LCA codes are Abelian group-GKP codes with $Kc \mathbb{Z} \subset \mathbb{Z} \subset \mathbb{R} \times \mathbb{Z}_c$, where the logical dimension $K$ is coprime to the physical qudit dimension $c$  ([arXiv:2508.04819](https://arxiv.org/abs/2508.04819)).
