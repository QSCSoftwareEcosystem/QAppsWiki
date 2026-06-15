---
type: concept
name: Metrological code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/covariant
- concepts/qec/metopt
- concepts/qec/quantum-into-quantum
- concepts/qec/qubit-stabilizer
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/metrological
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: metrological
---

# Metrological code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/metrological) (`code_id: metrological`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Two-dimensional subspace of a Hilbert space whose basis states satisfy only a part of the \term{Knill-Laflamme conditions}. The satisfied part of the conditions ensures that the code can be used for local parameter estimation.

Letting $\Pi = U U^\dagger$ be the codespace projector for encoding isometry $U$ and projecting a pair of errors $E_i,E_j$ from an error set $\cal E$ into the two-dimensional codespace yields
\begin{align}
  \Pi E_{i}^{^{\dagger}}E_{j}\Pi=c_{ij}\,\Pi+x_{ij}\overline{X}+y_{ij}\overline{Y}+z_{ij}\overline{Z}
\end{align}
with error-matrix element $c_{ij}$ and logical-error coefficients
\begin{align}
  \left\{ x,y,z\right\} _{ij}={\textstyle \frac{1}{2}}\text{Tr}\left(\{ \overline{X},\overline{Y},\overline{Z}\} E_{i}^{^{\dagger}}E_{j}\right)~.
\end{align}
If all three logical-error coefficients are zero, then the \term{Knill-Laflamme conditions} are satisfied, and the code is a QECC. If only one of the three coefficients is zero, then the code is the more general metrological code.

(source: raw/error-correction-zoo.md)

## Protection

Physical noise can cause logical errors along one of the three axes, i.e., either logical-$X$, $Y$, or $Z$, depending on what basis is used. Codes protect against logical errors along the remaining two axes.

A metrological block quantum code has distance $d$ if the above conditions are satisfied for an error set $\cal E$ consisting of errors supported on $d-1$ subsystems or fewer.

## Relations

- _parent_: [[concepts/qec/quantum-into-quantum]]
- _cousin_: [[concepts/qec/metopt]] — Error-corrected sensing codes are required to satisfy the \term{Knill-Laflamme conditions}, while metrological codes need only satisfy the conditions partially.
- _cousin_: [[concepts/qec/covariant]] — Any time-covariant QECC, i.e., a code admitting a continuous-parameter $U(1)$ family of gates, is automatically a metrological code.
- _cousin_: [[concepts/qec/qubit-stabilizer]] — A joint $+1$ and $-1$ eigenstate of a set of stabilizers can form a metrological stabilizer code  ([arXiv:2207.13707](https://arxiv.org/abs/2207.13707)).
