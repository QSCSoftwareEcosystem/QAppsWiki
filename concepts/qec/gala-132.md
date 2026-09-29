---
type: concept
name: $⟦132,30,12⟧$ self-dual GALA code
status: provisional
updated: '2026-09-29'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/gala
- concepts/qec/self-dual-css
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/gala_132
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: gala_132
---

# $⟦132,30,12⟧$ self-dual GALA code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/gala_132) (`code_id: gala_132`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A hyperbolic self-dual GALA code whose Hadamard-type and phase-type fold-transversal Clifford operations are implemented physically by depth-one layers of single-qubit gates.

The code is $\mathrm{GALA}_{12,5}(e\times C_{11})$: the row weight is $L=12$, the number of active block rows is $J=5$, the top factor is trivial, and the Abelian bottom is the cyclic group $C_{11}$, giving $n=12\times1\times11=132$ qubits at rate $0.227$  ([arXiv:2608.07431](https://arxiv.org/abs/2608.07431)).
Every entry of the $G$-lift is a single group element, so the code is monomial.
Its $ZX$ duality comes from a reflection-type sector involution, which is why the Tanner graph has girth four rather than the girth of at least six targeted elsewhere in the family.
The duality permutation is the identity, which is what reduces both fold-transversal operations to depth-one layers of single-qubit gates  ([arXiv:2608.07431](https://arxiv.org/abs/2608.07431)).

Since the duality permutation is the identity, the two fold-transversal operators are
\begin{align}
  H_{\tau}=H^{\otimes 132}~,\qquad S_{\tau}=(S^{\dagger})^{\otimes 132}~,
\end{align}
each a depth-one layer of single-qubit gates  ([arXiv:2608.07431](https://arxiv.org/abs/2608.07431)).
In an orthonormal logical basis, $H_{\tau}$ acts as fifteen copies of $(\bar H\otimes\bar H)\overline{\mathrm{SWAP}}$, while $S_{\tau}$ acts as fifteen disjoint logical controlled-$Z$ gates together with single-logical-qubit phases on thirteen of the thirty logical qubits  ([arXiv:2608.07431](https://arxiv.org/abs/2608.07431)).

(source: raw/error-correction-zoo.md)

## Protection

The rate is $0.227$ and the Tanner graph has girth four  ([arXiv:2608.07431](https://arxiv.org/abs/2608.07431)).
Since $J>L/4$, the parent matrices are fully orthogonal, and an independent latent row supplies a weight-$L$ logical operator. An exhaustive search certifies $d=L=12$, so the code attains that cap exactly  ([arXiv:2608.07431](https://arxiv.org/abs/2608.07431)).

Minimum-weight bases of $X$-type and of $Z$-type logical operators attain the code distance on every logical qubit, with all representatives of weight 12, but the two bases are not symplectic partners  ([arXiv:2608.07431](https://arxiv.org/abs/2608.07431)). Completing the minimum-weight $X$-type basis to a symplectic basis requires $Z$-type partners of weights 18 to 24.

## Transversal gates

- The physical depth-one layers $H^{\otimes 132}$ and $(S^{\dagger})^{\otimes 132}$ implement Hadamard-type and phase-type logical Clifford operations. In an orthonormal logical basis these are, respectively, fifteen $(\bar H\otimes\bar H)\overline{\mathrm{SWAP}}$ operations and fifteen disjoint logical controlled-$Z$ gates together with phases on thirteen logical qubits  ([arXiv:2608.07431](https://arxiv.org/abs/2608.07431)).
- A cyclic shift automorphism is implemented by a single rigid qubit permutation, shifting the bottom chains by one while fixing the top chain  ([arXiv:2608.07431](https://arxiv.org/abs/2608.07431)). The shift is termed dirty because each chain of eleven sites carries only ten logical qubits, so the eleven-cycle permutes an overcomplete labeling rather than a basis.

## Decoders

- At physical error rate $10^{-3}$, a two-stage Relay-BP cascade with a mixed-integer linear-programming fallback ran five million circuit-level shots without a recorded logical failure  ([arXiv:2608.07431](https://arxiv.org/abs/2608.07431)).

## Relations

- _parent_: [[concepts/qec/gala]] — The code is the GALA instance $\mathrm{GALA}_{12,5}(e\times C_{11})$, with trivial non-Abelian top and cyclic Abelian bottom  ([arXiv:2608.07431](https://arxiv.org/abs/2608.07431)).
- _parent_: [[concepts/qec/self-dual-css]] — The code is a hyperbolic self-dual CSS code: the column weight $J=5$ is odd, so the all-ones vector lies in each row space and every logical operator has even weight, forcing the pairing matrix to be alternating in every basis and hence admitting no normal magic basis  ([arXiv:1703.07847](https://arxiv.org/abs/1703.07847)) ([arXiv:2608.07431](https://arxiv.org/abs/2608.07431)). Consistently, transversal Hadamard acts pairwise rather than as thirty logical Hadamards, and $n$, $k$, and $d$ are all even.
