---
type: concept
name: Binarized-and-concatenated (B\&C) phantom code
status: provisional
updated: '2026-09-29'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/galois-3-1-2
- concepts/qec/galois-quad-residue
- concepts/qec/perm-self-dual-css
- concepts/qec/phantom
- concepts/qec/qubit-concatenated
- concepts/qec/stab-4-2-2
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/bc_phantom
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: bc_phantom
---

# Binarized-and-concatenated (B\&C) phantom code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/bc_phantom) (`code_id: bc_phantom`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Member of a family of $k=2$ CSS phantom codes obtained from a $q=4$ Galois-qudit CSS code by binarizing each $\mathbb{F}_4$ qudit into two qubits and then concatenating each qubit pair with the $⟦4,2,2⟧$ code  ([arXiv:2601.20927](https://arxiv.org/abs/2601.20927)).

The construction starts from a $⟦n,1,d⟧_4$ CSS code satisfying a condition that realizes the Frobenius transform $\gamma\mapsto\gamma^2$ by a coordinate permutation; together with field multiplication $\gamma\mapsto\alpha\gamma$, this supplies all $\mathrm{GL}(2,2)$ transformations on the two binary components of the logical $\mathbb{F}_4$ qudit after concatenation.
Binarization uses the self-dual normal basis $\{\omega,\omega^2\}$ of $\mathbb{F}_4$.
The subsequent $⟦4,2,2⟧$ layer maps a single $\mathbb{F}_4$-qudit Pauli to four-qubit Paulis, e.g.,
$X^\omega\mapsto XXII$, $X^{\omega^2}\mapsto XIXI$, $X^1\mapsto IXXI$, and similarly $Z^{\omega^2}\mapsto IIZZ$, $Z^\omega\mapsto IZIZ$, $Z^1\mapsto IZZI$  ([arXiv:2601.20927](https://arxiv.org/abs/2601.20927)).

This binarization-and-concatenation step is the second stage of concatenated symplectic doubling, which concatenates each binarized qubit pair with the $⟦4,2,2⟧$ code along a $ZX$ duality  ([arXiv:1004.3791](https://arxiv.org/abs/1004.3791)) ([arXiv:2605.15344](https://arxiv.org/abs/2605.15344)).
The starting Galois-qudit CSS code is a symplectic double of a qubit stabilizer code if and only if it is Hermitian self-dual.
In that case the resulting code is the concatenated symplectic double of that qubit stabilizer code and is a self-dual CSS code, while codes built from Euclidean self-dual starting codes are not obtained this way  ([arXiv:2601.20927](https://arxiv.org/abs/2601.20927), [arXiv:2605.15344](https://arxiv.org/abs/2605.15344)).

(source: raw/error-correction-zoo.md)

## Protection

A starting $⟦n,1,d⟧_4$ CSS code yields a qubit CSS code with parameters $⟦4n,2,\geq 2d⟧$ after binarization and concatenation with the $⟦4,2,2⟧$ code  ([arXiv:2601.20927](https://arxiv.org/abs/2601.20927)).
The outer $⟦4,2,2⟧$ blocks contribute many weight-four stabilizers, while completing the stabilizer group may require generators whose weight is at least the code distance.

## Transversal gates

- Ordinary CSS self-duality of the starting $q=4$ Galois-qudit CSS code yields a permutation-assisted logical Hadamard on the resulting qubit code. Hermitian self-duality, meaning that the $Z$-type check space is the Frobenius conjugate of the $X$-type check space, additionally yields a logical $CZ$ gate  ([arXiv:2601.20927](https://arxiv.org/abs/2601.20927)).

## Relations

- _parent_: [[concepts/qec/phantom]]
- _parent_: [[concepts/qec/qubit-concatenated]] — Each qubit pair obtained by binarizing one $\mathbb{F}_4$ qudit is concatenated with the $⟦4,2,2⟧$ code  ([arXiv:2601.20927](https://arxiv.org/abs/2601.20927)).
- _cousin_: [[concepts/qec/perm-self-dual-css]] — B\&C phantom codes built from the CSS quantum QR codes over $\mathbb{F}_4$ of prime length $p\equiv 3 \bmod 8$, which have $H_X=H_Z$, are permutationally self-dual. Transversal Hadamard composed with the block permutation induced by the coordinate map $i\mapsto 2i \bmod p$ preserves the stabilizer group  ([arXiv:2601.20927](https://arxiv.org/abs/2601.20927)). B\&C phantom codes built from Hermitian self-dual starting codes are self-dual CSS codes, and hence are also permutationally self-dual  ([arXiv:2601.20927](https://arxiv.org/abs/2601.20927)).
- _cousin_: [[concepts/qec/galois-quad-residue]] — A concrete B\&C phantom family starts from CSS quantum QR codes over $\mathbb{F}_4$  ([arXiv:2601.20927](https://arxiv.org/abs/2601.20927)).
- _cousin_: [[concepts/qec/galois-3-1-2]] — Binarizing the $⟦3,1,2⟧_4$ Galois-qudit CSS code and concatenating each qubit pair with the $⟦4,2,2⟧$ code yields the $⟦12,2,4⟧$ carbon code  ([arXiv:2601.20927](https://arxiv.org/abs/2601.20927)).
- _cousin_: [[concepts/qec/stab-4-2-2]] — The $⟦4,2,2⟧$ code is used as the outer code for each binarized $\mathbb{F}_4$-qudit pair  ([arXiv:2601.20927](https://arxiv.org/abs/2601.20927)).
