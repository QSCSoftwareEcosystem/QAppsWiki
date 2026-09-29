---
type: concept
name: Phantom code
status: provisional
updated: '2026-09-29'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/hypergraph-product
- concepts/qec/quantum-reed-muller
- concepts/qec/qubit-concatenated
- concepts/qec/qubit-css
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/phantom
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: phantom
---

# Phantom code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/phantom) (`code_id: phantom`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Qubit CSS code for which, in some logical basis, every ordered-pair logical $\overline{\mathrm{CNOT}}_{ab}$ gate between logical qubits in the same code block can be implemented by a physical-qubit permutation  ([arXiv:2601.20927](https://arxiv.org/abs/2601.20927)).
Such a permutation maps the code onto itself and acts on the logical Pauli operators as the CNOT gate.
It can therefore be absorbed into circuit compilation as a relabeling of the physical qubits, at zero overhead and with perfect fidelity  ([arXiv:2601.20927](https://arxiv.org/abs/2601.20927)).
The definition has been extended to non-CSS and non-qubit codes  ([arXiv:2604.15111](https://arxiv.org/abs/2604.15111)).

The smallest phantom code is the $⟦4,2,2⟧$ code with logical operators $\overline{X}_1=XXII$, $\overline{X}_2=XIXI$, $\overline{Z}_1=ZIZI$, and $\overline{Z}_2=ZZII$, for which swapping qubits 1 and 3 implements $\overline{\mathrm{CNOT}}_{12}$ and swapping qubits 1 and 2 implements $\overline{\mathrm{CNOT}}_{21}$  ([arXiv:2601.20927](https://arxiv.org/abs/2601.20927)).
Gluing $m$ copies of the $⟦4,2,2⟧$ code into a tube, with $X$-type stabilizers on the faces joining consecutive copies, yields CSS phantom codes with parameters $⟦4m,2,(d_X=2,d_Z=2m)⟧$.
Each logical CNOT of the glued code is one transposition applied in every copy.
Puncturing one qubit gives $⟦4m-1,2,(d_X=2,d_Z=2m-1)⟧$, for $m\geq1$  ([arXiv:2601.20927](https://arxiv.org/abs/2601.20927)).

(source: raw/error-correction-zoo.md)

## Protection

CSS phantom codes obey a Hamming-type constraint  ([arXiv:2601.20927](https://arxiv.org/abs/2601.20927)).
If $d=d_{\mu}$ for $\mu\in\{X,Z\}$, then $\eta(2^k-1)\leq B(n,d)$.
Here $\eta$ counts weight-$d$ logical operators in a fixed $\mu$-type logical equivalence class.
The quantity $B(n,d)\leq {n \choose d}$ is the maximum size of a binary length-$n$ code whose pairwise sums have weight at least $d$  ([arXiv:2601.20927](https://arxiv.org/abs/2601.20927)).
Any qubit phantom code of distance $d\geq 2$ encoding $k\geq 2$ logical qubits with $k\neq 4$ obeys $n\geq 2^k-1$, equivalently $k\leq \log_2(n+1)$  ([arXiv:2604.15111](https://arxiv.org/abs/2604.15111)).
This parameter bound also holds for non-CSS phantom codes and for qubit subspace or subsystem phantom-LU codes  ([arXiv:2604.15111](https://arxiv.org/abs/2604.15111)).
For qubit stabilizer codes supporting every logical CX gate by single-qubit Clifford gates and qubit permutations, the bound holds for all $k$ and distances except the $⟦2,2,1⟧$ code  ([arXiv:2609.19250](https://arxiv.org/abs/2609.19250)).
A nonstabilizer $((8,2^4,2))$ phantom code shows why the $k=4$ exception remains necessary for general quantum codes  ([arXiv:2604.15111](https://arxiv.org/abs/2604.15111)).

## Transversal gates

- For CSS phantom codes, interblock $\overline{\mathrm{CNOT}}$ gates are transversal.
Combining transversal interblock CNOTs with in-block permutation CNOTs implements any logical CNOT circuit on $2^a$ phantom-code blocks.
The physical depth is at most $4(2^a-1)$, up to a residual logical-qubit permutation.
For unidirectional CNOT circuits, the depth bound is $2(2^a-1)$ and the logical-qubit order is preserved  ([arXiv:2601.20927](https://arxiv.org/abs/2601.20927)).
- A stabilizer code supporting a logical gate by qubit permutations cannot admit any strictly transversal logical gate that does not commute with that permutation-implemented gate  ([arXiv:2601.20927](https://arxiv.org/abs/2601.20927)). This rules out strictly transversal implementations of several gates on phantom codes  ([arXiv:2601.20927](https://arxiv.org/abs/2601.20927)).
- Additional logical Clifford and non-Clifford gates can arise from code automorphisms combining local Cliffords and qubit permutations. Such gates can also arise from fold-diagonal gates using patterned one- and two-qubit diagonal interactions, and from non-uniform diagonal single-qubit rotations  ([arXiv:2601.20927](https://arxiv.org/abs/2601.20927)).

## General gates

- Certain phantom quantum RM codes admit the full logical Clifford group via fold-$\overline{S}_i\overline{S}_j$ gates and teleported Hadamards  ([arXiv:2601.20927](https://arxiv.org/abs/2601.20927)). The same codes admit a distance-two magic-gate scheme by temporarily projecting into hypercube-code subspaces  ([arXiv:2601.20927](https://arxiv.org/abs/2601.20927)).

## Decoders

- Spatiotemporal sliding-window correlated list and most-likely-error decoders for Steane-style error correction  ([arXiv:2601.20927](https://arxiv.org/abs/2601.20927)).

## Fault tolerance

- Preselection-based fault-tolerant state preparation and Steane-style error correction for non-LDPC phantom quantum RM codes  ([arXiv:2601.20927](https://arxiv.org/abs/2601.20927)).

## Relations

- _parent_: [[concepts/qec/qubit-css]]
- _cousin_: [[concepts/qec/quantum-reed-muller]] — Some quantum RM codes are phantom after selected logical qubits of a parent quantum RM code are fixed to $\ket{\overline{0}}$ or $\ket{\overline{+}}$, promoting the corresponding logical operators to stabilizers  ([arXiv:2601.20927](https://arxiv.org/abs/2601.20927)).
- _cousin_: [[concepts/qec/qubit-concatenated]] — Concatenating a phantom inner code with a one-logical-qubit outer quantum code preserves phantomness.
- _cousin_: [[concepts/qec/hypergraph-product]] — Some hypergraph-product constructions, such as products of a classical simplex code and a repetition code, yield phantom codes  ([arXiv:2601.20927](https://arxiv.org/abs/2601.20927)). The smallest such examples have lower rates than the phantom quantum RM constructions  ([arXiv:2601.20927](https://arxiv.org/abs/2601.20927)).

## Notes

- Among the $2.71\times10^{10}$ inequivalent CSS codes with $n\leq14$, $1.39\times10^5$ are CSS phantom codes  ([arXiv:2601.20927](https://arxiv.org/abs/2601.20927)). Further examples are known up to $n=21$  ([arXiv:2601.20927](https://arxiv.org/abs/2601.20927)).
