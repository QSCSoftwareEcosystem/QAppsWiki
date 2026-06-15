---
type: concept
name: GNU PI code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/bacon-shor
- concepts/qec/binomial
- concepts/qec/combinatorial-permutation-invariant
- concepts/qec/frustration-free
- concepts/qec/metopt
- concepts/qec/qudit-gnu-permutation-invariant
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/gnu_permutation_invariant
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: gnu_permutation_invariant
---

# GNU PI code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/gnu_permutation_invariant) (`code_id: gnu_permutation_invariant`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

PI code whose codewords can be expressed as superpositions of Dicke states with coefficients are square-roots of the binomial distribution.

In terms of Dicke states, logical codewords for codes encoding a single qubit  ([arXiv:1302.3247](https://arxiv.org/abs/1302.3247)) are
\begin{align}
|\overline{\pm}\rangle = \sum_{\ell=0}^{m} \frac{(\pm 1)^\ell}{\sqrt{2^m}} \sqrt{m \choose \ell} |D^n_{g \ell}\rangle~.
\end{align}
Here, $n$ is the number of particles used for encoding $1$ qubit, and $g, m \leq n$ are arbitrary positive integers.
Codes with higher logical dimension are developed in Ref.  ([arXiv:1512.02469](https://arxiv.org/abs/1512.02469)).
Each Dicke state in the code can be *shifted* by adding a shift $s$ to both $n$ and $g$.

(source: raw/error-correction-zoo.md)

## Protection

Depends on the family. One family which is completely symmetrized versions of Bacon-Shor codes (parameterized by $t$) protects against arbitrary weight-$t$ spin errors. Additionally, codes with large enough length $(t+1)(3t+1)+t$ can approximately correct $t$ spontaneous decay errors.

## Decoders

- For a family of shifted gnu codes, decoding can be done using projection, probability amplitude rebalancing, and gate teleportation in time $O(n^2)$  ([arXiv:2102.02494](https://arxiv.org/abs/2102.02494)).
- Syndrome extraction protocol for insertion errors  ([arXiv:2509.03413](https://arxiv.org/abs/2509.03413)).

## Relations

- _parent_: [[concepts/qec/qudit-gnu-permutation-invariant]] — Qudit GNU codes encoding logical qubits reduce to GNU codes.
- _cousin_: [[concepts/qec/combinatorial-permutation-invariant]] — Combinatorial PI codes $Q_{g,(m-1)/2,g-1,+}$ are GNU codes for odd $m$  ([arXiv:2310.05358](https://arxiv.org/abs/2310.05358)).
- _cousin_: [[concepts/qec/bacon-shor]] — GNU codes of length $(2t+1)^2$ result from projecting Bacon-Shor codes into the PI qubit subspace  ([arXiv:1302.3247](https://arxiv.org/abs/1302.3247)).
- _cousin_: [[concepts/qec/frustration-free]] — GNU codes lie within the ground state of ferromagnetic Heisenberg models without an external magnetic field  ([arXiv:1904.01458](https://arxiv.org/abs/1904.01458)).
- _cousin_: [[concepts/qec/binomial]] — Binomial codes and GNU codes related via the Holstein-Primakoff mapping  ([doi:10.1103/PhysRev.58.1098](https://doi.org/10.1103/PhysRev.58.1098), [doi:10.2307/3212170](https://doi.org/10.2307/3212170), [doi:10.1103/RevModPhys.63.375](https://doi.org/10.1103/RevModPhys.63.375)). A qudit generalization of GNU codes can be obtained from qudit binomial codes  ([arXiv:1708.05010](https://arxiv.org/abs/1708.05010)).
- _cousin_: [[concepts/qec/metopt]] — GNU codes can be used to sense signals within the PI subspace  ([arXiv:2212.06285](https://arxiv.org/abs/2212.06285)).

## Notes

- The degree of entanglement in (non-concatenated) GNU codes scales at most logarithmically in their distance  ([arXiv:2405.01332](https://arxiv.org/abs/2405.01332)).
