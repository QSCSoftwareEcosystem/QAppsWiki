---
type: concept
name: Self-dual CSS code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Weakly self-dual CSS code
- Symmetric CSS code
- Self-orthogonal CSS code
- Homogeneous CSS code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/generalized-quantum-divisible
- concepts/qec/majorana-stab
- concepts/qec/quantum-divisible
- concepts/qec/quantum-reed-muller
- concepts/qec/quantum-triorthogonal
- concepts/qec/qubit-css
- concepts/qec/qubit-stabilizer
- concepts/qec/stab-4-2-2
- concepts/qec/tetron
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/self_dual_css
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: self_dual_css
---

# Self-dual CSS code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/self_dual_css) (`code_id: self_dual_css`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A qubit CSS code for which transversal Hadamard is a logical operation.
Equivalently, the stabilizer group is preserved by exchanging $X$-type and $Z$-type Pauli operators.

Specializing the CSS construction to the case when $C_Z=[n,k]$ is dual-containing and $C_X=C_Z$ yields an $⟦n,2k-n⟧$ self-dual qubit CSS code (a.k.a. weakly self-dual, symmetric  ([arXiv:2510.05708](https://arxiv.org/abs/2510.05708)), self-orthogonal, or homogeneous  ([doi:10.1109/TCOMM.2022.3231879](https://doi.org/10.1109/TCOMM.2022.3231879)) qubit CSS code).
Its $X$-type and $Z$-type stabilizers are identically supported, and transversal Hadamard preserves the stabilizer group.

Self-dual CSS codes split into *normal* and *hyperbolic* classes depending on whether transversal Hadamard acts as logical Hadamards or as pairwise logical swaps in a suitable logical basis  ([arXiv:1703.07847](https://arxiv.org/abs/1703.07847)).
Hyperbolic codes necessarily encode an even number of logical qubits and have even blocklength and distance  ([arXiv:1703.07847](https://arxiv.org/abs/1703.07847)).

(source: raw/error-correction-zoo.md)

## Magic scaling exponent

Normal and hyperbolic self-dual CSS codes yield magic-state distillation protocols with asymptotically constant space overhead and yield parameter $\gamma \to 1^{+}$  ([arXiv:1703.07847](https://arxiv.org/abs/1703.07847)) ([arXiv:1709.02789](https://arxiv.org/abs/1709.02789)).

## Transversal gates

- Self-dual CSS codes admit a transversal Hadamard gate. There are criteria for when such codes realize logical gates from tensor products of $S$ and $S^{\dagger}$ gates  ([arXiv:2503.19790](https://arxiv.org/abs/2503.19790)).
- Diagonal transversal Clifford gates on $\ell$ codeblocks of a CSS code form $Sp(2\ell,\mathbb{F}_2)$ for self-dual CSS codes  ([arXiv:2507.10519](https://arxiv.org/abs/2507.10519)).
- A self-dual weakly doubly even $⟦n,1,d⟧$ CSS code admits a partitioned transversal physical $S$ gate that realizes $\overline{S}^m$, where $m=|M^+|-|M^-| \pmod 4$; for odd $m$, together with transversal Hadamard and CNOT, this yields the full logical Clifford group transversally  ([arXiv:1509.03239](https://arxiv.org/abs/1509.03239)) ([arXiv:2408.12752](https://arxiv.org/abs/2408.12752)).

## Fault tolerance

- Any self-dual CSS code with bounded-weight stabilizer generators admits flag fault-tolerant syndrome extraction  ([arXiv:1708.02246](https://arxiv.org/abs/1708.02246)).
- Triorthogonal codes realizing logical $T$ gates using only physical $T$ gates can be paired up with self-dual CSS codes to yield a transversal CNOT gate and universal fault-tolerant gates using Steane error correction  ([arXiv:2510.05708](https://arxiv.org/abs/2510.05708)).

## Relations

- _parent_: [[concepts/qec/qubit-css]] — Self-dual CSS codes are qubit CSS codes whose stabilizer group is preserved by transversal Hadamard.
- _cousin_: [`dual`](https://errorcorrectionzoo.org/c/dual) — Self-dual CSS codes arise from dual-containing (equivalently, self-orthogonal a.k.a. weakly self-dual) binary linear codes.
- _cousin_: [[concepts/qec/qubit-stabilizer]] — Any $⟦n,k,d⟧$ qubit stabilizer code maps to a $⟦4n,2k,2d⟧$ self-dual CSS code by applying the BLT mapping and concatenating each qubit pair with the $⟦4,2,2⟧$ code  ([arXiv:2605.15344](https://arxiv.org/abs/2605.15344)) ([arXiv:1004.3791](https://arxiv.org/abs/1004.3791)). The BLT mapping proceeds by first concatenating each qubit with the tetron code to obtain an intermediate $⟦2n,k,2d⟧_{f}$ Majorana stabilizer code.
- _cousin_: [[concepts/qec/tetron]] — Any $⟦n,k,d⟧$ qubit stabilizer code maps to a $⟦4n,2k,2d⟧$ self-dual CSS code by applying the BLT mapping and concatenating each qubit pair with the $⟦4,2,2⟧$ code  ([arXiv:2605.15344](https://arxiv.org/abs/2605.15344)) ([arXiv:1004.3791](https://arxiv.org/abs/1004.3791)). The BLT mapping proceeds by first concatenating each qubit with the tetron code to obtain an intermediate $⟦2n,k,2d⟧_{f}$ Majorana stabilizer code.
- _cousin_: [[concepts/qec/stab-4-2-2]] — Any $⟦n,k,d⟧$ qubit stabilizer code maps to a $⟦4n,2k,2d⟧$ self-dual CSS code by applying the BLT mapping and concatenating each qubit pair with the $⟦4,2,2⟧$ code  ([arXiv:2605.15344](https://arxiv.org/abs/2605.15344)) ([arXiv:1004.3791](https://arxiv.org/abs/1004.3791)). The BLT mapping proceeds by first concatenating each qubit with the tetron code to obtain an intermediate $⟦2n,k,2d⟧_{f}$ Majorana stabilizer code.
- _cousin_: [[concepts/qec/quantum-reed-muller]] — The $⟦2^m,{m \choose r}, 2^{\min(r,m-r)}⟧$ quantum RM family contains a self-dual sub-family for $m=2r$, which admits logical Clifford group gates via permutations, transversal gates, and fold-transversal gates  ([arXiv:2410.23263](https://arxiv.org/abs/2410.23263), [arXiv:2602.09788](https://arxiv.org/abs/2602.09788)).
- _cousin_: [[concepts/qec/quantum-divisible]] — A self-dual weakly doubly even $⟦n,1,d⟧$ CSS code admits a partitioned transversal physical $S$ gate that realizes $\overline{S}^m$, where $m=|M^+|-|M^-| \pmod 4$; for odd $m$, together with transversal Hadamard and CNOT, this yields the full logical Clifford group transversally  ([arXiv:1509.03239](https://arxiv.org/abs/1509.03239)) ([arXiv:2408.12752](https://arxiv.org/abs/2408.12752)).
- _cousin_: [[concepts/qec/generalized-quantum-divisible]] — Any self-dual CSS code yields a level-three generalized quantum divisible code when level-lifted  ([arXiv:1709.08658](https://arxiv.org/abs/1709.08658)).
- _cousin_: [[concepts/qec/quantum-triorthogonal]] — Triorthogonal codes realizing logical $T$ gates using only physical $T$ gates can be paired up with self-dual CSS codes to yield a transversal CNOT gate and universal fault-tolerant gates using Steane error correction  ([arXiv:2510.05708](https://arxiv.org/abs/2510.05708)).
- _cousin_: [[concepts/qec/majorana-stab]] — An odd-length self-dual CSS code can be converted into a complex-fermion code by replacing qubit $Z$-type and $X$-type operators with $\gamma$-type and $\tilde{\gamma}$-type Majorana operators, respectively  ([arXiv:2411.08955](https://arxiv.org/abs/2411.08955)).
