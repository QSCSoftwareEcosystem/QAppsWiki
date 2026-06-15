---
type: concept
name: $⟦2^D,D,2⟧$ hypercube quantum code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Hyperoctahedron code
- Hyperoctahedron color code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/ball-color
- concepts/qec/higher-dimensional-surface
- concepts/qec/phantom
- concepts/qec/quantum-reed-muller
- concepts/qec/quantum-repetition
- concepts/qec/qubit-concatenated
- concepts/qec/self-complementary
- concepts/qec/xp-stabilizer
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/hypercube_quantum
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: hypercube_quantum
---

# $⟦2^D,D,2⟧$ hypercube quantum code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/hypercube_quantum) (`code_id: hypercube_quantum`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Member of a family of codes defined by placing qubits on a $D$-dimensional hypercube, $Z$-stabilizers on all two-dimensional faces, and an $X$-stabilizer on all vertices.
These codes realize gates at the $(D-1)$-st level of the Clifford hierarchy.
The measured physical bit string can be post-processed into both a logical output string and stabilizer checks, enabling end-of-circuit error detection directly from classical samples  ([arXiv:2404.19005](https://arxiv.org/abs/2404.19005)).
Puncturing the $⟦2^D,D,2⟧$ hypercube quantum code yields the $⟦2^D-1,D,2⟧$ punctured-hypercube family.

Higher-distance generalizations include a $⟦2^{2D},D,4⟧$ hyperoctahedron family and a $⟦2^D(2^D+1),D,4⟧$ family built from distance-two $D$-dimensional toric/surface-code blocks  ([arXiv:2404.19005](https://arxiv.org/abs/2404.19005)).
Various other concatenations give families with increasing distance (see cousins).

In the color-code picture, they arise from hypercube-like lattices with no bulk qubits and opposite boundaries carrying the same color; after local Clifford disentangling, the transversal $\widetilde{R_D}$ operator acts as a logical $C^{D-1}Z$ gate on $D$ decoupled distance-two toric/surface-code factors  ([arXiv:1503.02065](https://arxiv.org/abs/1503.02065)).

(source: raw/error-correction-zoo.md)

## Protection

The code detects a single general error but has an $X$-distance $d_X = 4$.
In encoded IQP sampling, this allows error detection without intermediate measurements by postselecting on the final stabilizer data extracted from measurement samples  ([arXiv:2404.19005](https://arxiv.org/abs/2404.19005)).

## Transversal gates

- $CZ$, $CCZ$, and generalized $CZ$ gates at the $(D-1)$-st level of the Clifford hierarchy  ([arXiv:2203.00103](https://arxiv.org/abs/2203.00103)). CNOT and SWAP gates can be realized by qubit permutations  ([arXiv:2404.19005](https://arxiv.org/abs/2404.19005)).

## Relations

- _parent_: [[concepts/qec/ball-color]] — $⟦2^D,D,2⟧$ hypercube quantum codes can be thought of as small ball codes constructed from hyperoctahedra  ([arXiv:2112.01446](https://arxiv.org/abs/2112.01446)), or on lattices with no bulk qubits and cubic boundaries   ([arXiv:1503.02065](https://arxiv.org/abs/1503.02065)).
- _parent_: [[concepts/qec/quantum-reed-muller]] — $⟦2^D,D,2⟧$ hypercube quantum codes are special cases of the $⟦2^m,{m \choose r}, 2^r⟧$ quantum RM codes for $m=D$ and $r=1$  ([arXiv:1910.09333](https://arxiv.org/abs/1910.09333)) ([arXiv:1606.01904](https://arxiv.org/abs/1606.01904), [arXiv:1606.01906](https://arxiv.org/abs/1606.01906), [arXiv:1709.02832](https://arxiv.org/abs/1709.02832), [arXiv:2410.23263](https://arxiv.org/abs/2410.23263)).
- _parent_: [[concepts/qec/phantom]] — The $⟦2^D,D,2⟧$ hypercube quantum codes are phantom codes: all ordered-pair in-block logical CNOT gates can be implemented by physical-qubit permutations  ([arXiv:2601.20927](https://arxiv.org/abs/2601.20927)). The punctured hypercube family is unique among binary CSS phantom codes saturating $n\geq 2^k-1$ for $k=3$ and $k\geq 5$  ([arXiv:2604.15111](https://arxiv.org/abs/2604.15111)).
- _parent_: [[concepts/qec/self-complementary]] — A basis of hypercube quantum codewords of the form $|c\rangle+|\overline{c}\rangle$ can be obtained via the qubit CSS codeword construction since their sole $X$-type stabilizer generator acts on all qubits.
- _cousin_: [[concepts/qec/xp-stabilizer]] — The $D$th hypercube quantum code can be viewed as an XP stabilizer code with precision $N = 2^D$  ([arXiv:2203.00103](https://arxiv.org/abs/2203.00103)).
- _cousin_: [`hypercube`](https://errorcorrectionzoo.org/c/hypercube) — $⟦2^D,D,2⟧$ hypercube quantum code qubits are placed on vertices of a $D$-cube.
- _cousin_: [[concepts/qec/quantum-repetition]] — The hypercube quantum code can be concatenated with a two-qubit quantum repetition code to yield a $⟦2^{D+1},D,4⟧$ error-detecting code family  ([arXiv:2404.19005](https://arxiv.org/abs/2404.19005)).
- _cousin_: [[concepts/qec/higher-dimensional-surface]] — The hypercube quantum code can be concatenated with $D$ distance-two $D$-dimensional toric/surface-code blocks to yield a $⟦2^D(2^D+1),D,4⟧$ error-correcting family that admits a transversal implementation of the logical $C^{D-1}Z$ gate  ([arXiv:2404.19005](https://arxiv.org/abs/2404.19005)).
- _cousin_: [[concepts/qec/qubit-concatenated]] — The hypercube quantum code can be concatenated with a two-qubit quantum repetition code to yield a $⟦2^{D+1},D,4⟧$ error-detecting code family  ([arXiv:2404.19005](https://arxiv.org/abs/2404.19005)).
It can also be concatenated with $D$ distance-two $D$-dimensional toric/surface-code blocks to yield a $⟦2^D(2^D+1),D,4⟧$ error-correcting code family that admits a transversal implementation of the logical $C^{D-1}Z$ gate  ([arXiv:2404.19005](https://arxiv.org/abs/2404.19005)).

## Notes

- Degree-$D$ instantaneous quantum polynomial (IQP) circuits  ([arXiv:1504.07999](https://arxiv.org/abs/1504.07999)) can be realized on hypercube quantum codes in a hardware-efficient way; Ref.  ([arXiv:2404.19005](https://arxiv.org/abs/2404.19005)) proposes hypercube IQP (hIQP) circuits on a hypercube connectivity graph.
- For $D=4$, Bell sampling on two copies of degree-$4$ IQP circuits encoded in the $⟦16,4,2⟧$ member is proposed as an efficiently classically verifiable quantum-advantage experiment  ([arXiv:2404.19005](https://arxiv.org/abs/2404.19005)).
