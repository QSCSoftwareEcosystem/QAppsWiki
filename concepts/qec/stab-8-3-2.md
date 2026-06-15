---
type: concept
name: $⟦8,3,2⟧$ Smallest interesting color code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/3d-color
- concepts/qec/3d-surface
- concepts/qec/campbell-howard
- concepts/qec/hypercube-quantum
- concepts/qec/qubit-concatenated
- concepts/qec/stab-15-1-3
- concepts/qec/xp-stabilizer
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/stab_8_3_2
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: stab_8_3_2
---

# $⟦8,3,2⟧$ Smallest interesting color code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/stab_8_3_2) (`code_id: stab_8_3_2`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Smallest 3D color code whose physical qubits lie on vertices of a cube and which admits a (weakly) transversal $CCZ$ gate.

A stabilizer tableau for the code is given by 
\begin{align}
\begin{array}{cccccccc}
  Z & Z & I & I & I & I & Z & Z \\
  Z & I & Z & Z & I & I & Z & I \\
  I & I & Z & I & Z & I & Z & Z \\
  Z & I & Z & I & I & Z & I & Z \\
  X & X & X & X & X & X & X & X
\end{array}~.
\end{align}

In encoded IQP sampling, the final measurement outcomes determine both the logical sample and stabilizer checks, enabling end-of-circuit error detection or postselected decoding directly from the classical samples  ([arXiv:2404.19005](https://arxiv.org/abs/2404.19005)).

(source: raw/error-correction-zoo.md)

## Transversal gates

- $CZ$ gates between any two logical qubits  ([arXiv:1912.10063](https://arxiv.org/abs/1912.10063)) and (weakly) transversal $CCZ$ gate  ([arXiv:1503.02065](https://arxiv.org/abs/1503.02065), [arXiv:1912.10063](https://arxiv.org/abs/1912.10063)).

## General gates

- $CCZ$ gate can be distilled in a fault-tolerant manner  ([arXiv:2007.07929](https://arxiv.org/abs/2007.07929)).
- Fault-tolerant and teleportation-free logical Hadamard  ([arXiv:2505.20261](https://arxiv.org/abs/2505.20261)).

## Fault tolerance

- $CCZ$ gate can be distilled in a fault-tolerant manner  ([arXiv:2007.07929](https://arxiv.org/abs/2007.07929)).
- Fault-tolerant and teleportation-free logical Hadamard  ([arXiv:2505.20261](https://arxiv.org/abs/2505.20261)).
- Universal weakly fault-tolerant computation via code switching between this and another $⟦8,3,2⟧$ CSS code in a postselected error-detecting regime  ([arXiv:2603.15610](https://arxiv.org/abs/2603.15610)).
- Fault-tolerant architecture  ([arXiv:2507.20387](https://arxiv.org/abs/2507.20387)).
- For hIQP sampling with decoding only in the final measurement round, error-detected $⟦8,3,2⟧$ circuits outperform the $⟦16,3,4⟧$ and $⟦15,1,3⟧$ comparison circuits studied in Ref.  ([arXiv:2404.19005](https://arxiv.org/abs/2404.19005)) under its two-qubit-gate-noise model.

## Realizations

- Trapped ions: one-qubit addition algorithm implemented fault-tolerantly on the Quantinuum H1-1 device  ([arXiv:2309.09893](https://arxiv.org/abs/2309.09893)). Trapped-ion processor by AQT: measurement-free universal fault-tolerant logical operations and a Grover-search demonstration  ([arXiv:2506.22600](https://arxiv.org/abs/2506.22600)).
- Superconducting circuits: fault-tolerant $CCZ$ gate performed on IBM and IonQ devices  ([arXiv:2309.08663](https://arxiv.org/abs/2309.08663)).
- Neutral atom arrays: Lukin group  ([arXiv:2312.03982](https://arxiv.org/abs/2312.03982)). 48 logical qubits, 228 logical two-qubit gates, 48 logical $CCZ$ gates, and error detection performed in 16 blocks. Circuit outcomes were sampled and cross-entropy (XEB) was calculated to verify quantumness. Logical entanglement entropy was measured  ([arXiv:2312.03982](https://arxiv.org/abs/2312.03982)).

## Relations

- _parent_: [[concepts/qec/3d-color]] — The $⟦8,3,2⟧$ code is the smallest non-trivial 3D color code.
- _parent_: [[concepts/qec/hypercube-quantum]] — The $⟦8,3,2⟧$ code is a hypercube code for $D=3$.
- _parent_: [[concepts/qec/campbell-howard]] — The $⟦8,3,2⟧$ code is the $k=1$ member of the $⟦6k+2,3k,2⟧$ Campbell-Howard family with a quasi-transversal logical $CCZ$ gate  ([arXiv:1606.01904](https://arxiv.org/abs/1606.01904)).
- _cousin_: [`hamming844`](https://errorcorrectionzoo.org/c/hamming844) — The $⟦8,3,2⟧$ hypercube code $H_X$ check matrix is the parity-check matrix of the $[8,4,4]$ extended Hamming code, while its $H_Z$ matrix is that of the SPC code.
- _cousin_: [`parity_check`](https://errorcorrectionzoo.org/c/parity_check) — The $⟦8,3,2⟧$ hypercube code $H_X$ check matrix is the parity-check matrix of the $[8,4,4]$ extended Hamming code, while its $H_Z$ matrix is that of the SPC code.
- _cousin_: [[concepts/qec/xp-stabilizer]] — As the $D=3$ member of the hypercube-code family, the $⟦8,3,2⟧$ code can be viewed as an XP stabilizer code with precision $N=8$  ([arXiv:2203.00103](https://arxiv.org/abs/2203.00103)).
- _cousin_: [[concepts/qec/stab-15-1-3]] — The $⟦8,3,2⟧$ code can be obtained from a subset of physical qubits of the $⟦15,1,3⟧$ code  ([arXiv:2112.01446](https://arxiv.org/abs/2112.01446)).
- _cousin_: [[concepts/qec/3d-surface]] — Three cyclically rotated copies of the 3D surface/toric code admit a logical $CCZ$ gate via transversal physical $CCZ$ gates, and concatenating each such qubit triple with an $⟦8,3,2⟧$ block yields a 3D toric/color family with parameters $⟦8n,3,2d⟧$; its smallest member has parameters $⟦72,3,4⟧$  ([arXiv:2404.19005](https://arxiv.org/abs/2404.19005)).
- _cousin_: [[concepts/qec/qubit-concatenated]] — Concatenating $⟦8,3,2⟧$ blocks with triples of qubits drawn from three cyclically rotated 3D surface/toric codes yields a 3D toric/color family with parameters $⟦8n,3,2d⟧$ and transversal logical $CCZ$ implemented by physical $T$ gates on the inner $⟦8,3,2⟧$ blocks  ([arXiv:2404.19005](https://arxiv.org/abs/2404.19005)).
