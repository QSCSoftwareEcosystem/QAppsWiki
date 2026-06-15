---
type: concept
name: Bacon-Shor code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/surface
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/bacon_shor
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: bacon_shor
---

# Bacon-Shor code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/bacon_shor) (`code_id: bacon_shor`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Subsystem CSS code defined on an $m_1 \times m_2$ lattice of qubits that generalizes the $⟦9,1,3⟧$ (subspace) Shor code.
It is said to be *symmetric* when $m_1=m_2$, and *asymmetric* otherwise.

The $X$-type and $Z$-type stabilizers are defined as $X$ and $Z$ operators acting on all qubits on adjacent columns and rows, respectively. Let $O_{i,j}$ denote an operator acting on the qubit at a position $(i,j)$ on the lattice, with $i\in\{0,1,\ldots ,m_1-1\}$ and $j\in\{0,1,\ldots,m_2-1\}$. The code's stabilizer group is
\begin{align}
\mathsf{S}=\langle X_{i,*}X_{i+1,*},Z_{*,j}Z_{*,j+1}\rangle~,
\end{align}
with generators expressed as products of nearest-neighbor two-qubit gauge operators,
\begin{align}
\begin{split}
X_{i,*}X_{i+1,*}= \bigotimes_{k=0}^{m_2-1} X_{i,k}X_{i+1,k} \\
Z_{*,j}Z_{*,j+1}=\bigotimes_{k=0}^{m_1-1} Z_{k,j}Z_{k,j+1}~.
\end{split}
\end{align}
Syndrome extraction can be done by measuring these gauge operators, which act on fewer qubits and are local.

A Floquet version of the Bacon-Shor code admits a period-four measurement sequence that utilizes its gauge degrees of freedom as defects evolving across measurement rounds. This *Floquet-Bacon-Shor* code saturates the subsystem BT bound.
Applying a period-four measurement schedule to the original Bacon-Shor code yields a numerical threshold under circuit-level noise  ([arXiv:2504.02749](https://arxiv.org/abs/2504.02749)).

(source: raw/error-correction-zoo.md)

## Protection

The $⟦m_1 m_2,1,min(m_1,m_2)⟧$ variant has distance $d=min(m_1,m_2)$.
In a symmetric 3-dimensional case (defined on a cubic lattice) with $L^3$ qubits, the code has the parameters $⟦L^3,1,L⟧$.
Bacon-Shor code parameters can be optimized by changing the block geometry, yielding good performance against biased noise  ([arXiv:1209.0794](https://arxiv.org/abs/1209.0794)).

## Rate

A non-LDPC family of Bacon-Shor codes achieves a distance of order $\Omega(n^{1-\epsilon})$ with sparse gauge operators.

## Transversal gates

- Logical Hadamard is transversal in symmetric Bacon-Shor codes up to a qubit permutation  ([arXiv:quant-ph/0610063](https://arxiv.org/abs/quant-ph/0610063)) and can be implemented with teleportation  ([arXiv:quant-ph/0002039](https://arxiv.org/abs/quant-ph/0002039)).
- Bacon-Shor codes on an $m \times m^k$ lattice admit transversal $k$-qubit-controlled $Z$ gates  ([arXiv:1705.01686](https://arxiv.org/abs/1705.01686)).

## General gates

- Pieceably fault-tolerant circuits can be employed to construct non-transversal gates effectively .
- Subsystem lattice surgery  ([arXiv:1609.08062](https://arxiv.org/abs/1609.08062)).
- Measurement-free deformation protocol realizing the $CCZ$ gate  ([arXiv:2412.15187](https://arxiv.org/abs/2412.15187)).

## Fault tolerance

- Fault-tolerant teleportation-based computation scheme for asymmetric Bacon-Shor codes that is effective against highly biased noise  ([arXiv:1211.1400](https://arxiv.org/abs/1211.1400)).
- Pieceably fault-tolerant circuits can be employed to construct non-transversal gates effectively .

## Code capacity threshold

- The number of check operators scales sublinearly with system size, so the Bacon-Shor codes alone do not exhibit a topological threshold in the $m_1,m_2 \to \infty$ limit  ([arXiv:1903.03937](https://arxiv.org/abs/1903.03937)). However, a threshold can be obtained from concatenated Bacon-Shor codes that are further restricted to planar geometries, whose recovery circuit is a subset of a circuit used by a larger bona-fide Bacon-Shor code  ([arXiv:2305.12046](https://arxiv.org/abs/2305.12046)). This threshold differs from a concatenated threshold in that there are no long-range connectivity requirements.
- Lower bounds for the concatenated threshold of various small Bacon-Shor codes are tabulated in  ([arXiv:quant-ph/0610063](https://arxiv.org/abs/quant-ph/0610063)).

## Threshold

- The Bacon-Shor code has a measurement threshold of zero  ([arXiv:2402.00145](https://arxiv.org/abs/2402.00145)).
- Applying a period-four measurement schedule to the original Bacon-Shor code yields a numerical threshold under circuit-level noise  ([arXiv:2504.02749](https://arxiv.org/abs/2504.02749)).

## Decoders

- Majority-voting decoder  ([arXiv:0711.1556](https://arxiv.org/abs/0711.1556)).
- Steane error correction can outperform Shor error correction for this code  ([arXiv:2403.01659](https://arxiv.org/abs/2403.01659)).
- Utilizing the mapping of the effect of the noise to a statistical mechanical model  ([arXiv:quant-ph/0110143](https://arxiv.org/abs/quant-ph/0110143), [arXiv:2002.11733](https://arxiv.org/abs/2002.11733)) yields several copies of the 1D Ising model  ([arXiv:0908.4246](https://arxiv.org/abs/0908.4246)).
- While check operators are few-body, stabilizer weights scale with the number of qubits, and stabilizer expectation values are obtained by taking products of gauge-operator expectation values. It is thus not clear how to extract stabilizer values in a fault-tolerant manner  ([arXiv:2009.03921](https://arxiv.org/abs/2009.03921), [arXiv:2107.02194](https://arxiv.org/abs/2107.02194)).
- Autonomous QEC  ([arXiv:1212.3564](https://arxiv.org/abs/1212.3564)).
- Applying a period-four measurement schedule to the original Bacon-Shor code yields a numerical threshold under circuit-level noise  ([arXiv:2504.02749](https://arxiv.org/abs/2504.02749)).

## Realizations

- Superconducting qubits: The Floquet-Bacon-Shor code has been realized on a 3-by-3 lattice  ([arXiv:2503.03867](https://arxiv.org/abs/2503.03867)).

## Relations

- _parent_: [`bravyi_bacon_shor`](https://errorcorrectionzoo.org/c/bravyi_bacon_shor)
- _parent_: [`subsystem_quantum_parity`](https://errorcorrectionzoo.org/c/subsystem_quantum_parity)
- _parent_: [`compass_model`](https://errorcorrectionzoo.org/c/compass_model) — A compass code on a fully non-colored lattice reduces to the Bacon-Shor code.
- _cousin_: [`hamiltonian`](https://errorcorrectionzoo.org/c/hamiltonian) — The 2D Bacon-Shor gauge-group Hamiltonian is the compass model  ([doi:10.1070/PU1982v025n04ABEH004537](https://doi.org/10.1070/PU1982v025n04ABEH004537), [arXiv:cond-mat/0501708](https://arxiv.org/abs/cond-mat/0501708), [arXiv:1303.5922](https://arxiv.org/abs/1303.5922)).
- _cousin_: [`floquet`](https://errorcorrectionzoo.org/c/floquet) — A Floquet version of the Bacon-Shor code admits a period-four measurement sequence that utilizes its gauge degrees of freedom as defects evolving across measurement rounds. This *Floquet-Bacon-Shor* code saturates the subsystem BT bound. Applying a period-four measurement schedule to the original Bacon-Shor code yields a numerical threshold under circuit-level noise  ([arXiv:2504.02749](https://arxiv.org/abs/2504.02749)).
- _cousin_: [`quantum_lego`](https://errorcorrectionzoo.org/c/quantum_lego) — The 2D Bacon-Shor code can also be obtained from a surface-code tensor network by reassigning every other row of dangling physical legs to logical legs; in this quantum-Lego picture, the gauge generators remain weight-two $XX$ and $ZZ$ operators and the construction makes explicit a connection to the quantum compass model  ([arXiv:2109.08158](https://arxiv.org/abs/2109.08158)).
- _cousin_: [[concepts/qec/surface]] — The 2D Bacon-Shor code can also be obtained from a surface-code tensor network by reassigning every other row of dangling physical legs to logical legs; in this quantum-Lego picture, the gauge generators remain weight-two $XX$ and $ZZ$ operators and the construction makes explicit a connection to the quantum compass model  ([arXiv:2109.08158](https://arxiv.org/abs/2109.08158)).

## Notes

- See  ([arXiv:1302.3428](https://arxiv.org/abs/1302.3428)) for an exposition.
