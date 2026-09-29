---
type: concept
name: Mirror code
status: provisional
updated: '2026-09-29'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/2bga
- concepts/qec/qldpc
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/mirror
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: mirror
---

# Mirror code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/mirror) (`code_id: mirror`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Stabilizer code defined by a finite group $G$ and two subsets $A,B\subseteq G$, with one qubit per group element  ([arXiv:2603.05496](https://arxiv.org/abs/2603.05496)).
Each stabilizer generator acts as $Z$ on a translate of $A$ and as $X$ on a translate of $B$, so the check weight is at most $|A|+|B|$.
Mirror codes contain all qubit Abelian 2BGA codes up to qubit permutations and Hadamard gates, and are not CSS in general.

The *symmetric* mirror code has stabilizer generators
\begin{align}
  S(g) = Z(Ag)\,X(Bg^{-1})~,\qquad g\in G~,
\end{align}
where $Ag=\{ag \mid a\in A\}$ and $Z(T)$, $X(T)$ denote products of $Z$, $X$ over the qubits in $T$.
The *asymmetric* mirror code uses $X(g^{-1}B)$ instead, and neither family contains the other  ([arXiv:2603.05496](https://arxiv.org/abs/2603.05496)).
For Abelian $G$, the two constructions coincide and any $A,B$ yield commuting generators.
An Abelian mirror code is equivalent to a CSS code via Hadamard gates iff $A$ and $B$ lie in different cosets of an index-two subgroup of $G$  ([arXiv:2603.05496](https://arxiv.org/abs/2603.05496)).

(source: raw/error-correction-zoo.md)

## Protection

Weight-six mirror codes include $⟦60,4,10⟧$, $⟦36,6,6⟧$, $⟦48,8,6⟧$, and $⟦85,8,9⟧$ codes, none of which is equivalent to a CSS code via Hadamard gates  ([arXiv:2603.05496](https://arxiv.org/abs/2603.05496)).
Weight-seven mirror codes with $kd>n$ exist, e.g., a $⟦48,10,6⟧$ code  ([arXiv:2603.05496](https://arxiv.org/abs/2603.05496)).

## Fault tolerance

- *Superdense* syndrome extraction with one ancilla per check, adapted from the color-code circuit of Ref.  ([arXiv:2312.08813](https://arxiv.org/abs/2312.08813)), pairs generators so that each flags faults on the other  ([arXiv:2603.05496](https://arxiv.org/abs/2603.05496)).
- The CSS-FT6 circuit uses three ancillas per check and is fault tolerant for all CSS codes with check weight at most six  ([arXiv:2603.05496](https://arxiv.org/abs/2603.05496)).
- The FT6 circuit uses six ancillas per check and is fault tolerant for all stabilizer codes with check weight at most six  ([arXiv:2603.05496](https://arxiv.org/abs/2603.05496)).

## Threshold

- SI1000 circuit-level noise: pseudo-threshold of order $0.2\%$  ([arXiv:2603.05496](https://arxiv.org/abs/2603.05496)).

## Relations

- _parent_: [[concepts/qec/qldpc]] — Every qubit of a mirror code lies in the support of at most $|A|+|B|$ stabilizer generators  ([arXiv:2603.05496](https://arxiv.org/abs/2603.05496)).
- _cousin_: [[concepts/qec/2bga]] — Any qubit 2BGA code with normal subsets $A,B$ is equivalent to a mirror code on $\mathbb{Z}_2\times G$ via Hadamard gates on one block and a qubit permutation  ([arXiv:2603.05496](https://arxiv.org/abs/2603.05496)). Neither family contains the other  ([arXiv:2603.05496](https://arxiv.org/abs/2603.05496)) ([arXiv:2603.05496](https://arxiv.org/abs/2603.05496)).

## Notes

- See Ref.  ([arXiv:2603.05496](https://arxiv.org/abs/2603.05496)) for a table of Abelian mirror codes.
