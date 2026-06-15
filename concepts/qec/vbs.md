---
type: concept
name: Valence-bond-solid (VBS) code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/approximate-qecc
- concepts/qec/covariant
- concepts/qec/frustration-free
- concepts/qec/spins-into-spins
- concepts/qec/spt
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/vbs
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: vbs
---

# Valence-bond-solid (VBS) code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/vbs) (`code_id: vbs`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A member of an approximate $q$-dimensional spin-code family whose codespace is described in terms of $SU(q)$ valence-bond-solid (VBS)  ([doi:10.1007/978-3-662-06390-3_18](https://doi.org/10.1007/978-3-662-06390-3_18)) matrix product states with various boundary conditions.
The codes become exact when either $n$ or $q$ go to infinity.
The original work on these codes studied the $q=2$ case  ([arXiv:quant-ph/0006092](https://arxiv.org/abs/quant-ph/0006092)).

(source: raw/error-correction-zoo.md)

## Protection

VBS codes approximately protect against erasures, with the approximation becoming exact in the thermodynamic limit  ([arXiv:1910.00038](https://arxiv.org/abs/1910.00038), [arXiv:2105.14777](https://arxiv.org/abs/2105.14777)).

## Transversal gates

- Two classes of (approximate) VBS codes have $SU(q)$ transversal gates  ([arXiv:2105.14777](https://arxiv.org/abs/2105.14777)).

## Relations

- _parent_: [[concepts/qec/spins-into-spins]] — VBS codewords are eigenstates of the frustration-free VBS Hamiltonian  ([arXiv:1910.00038](https://arxiv.org/abs/1910.00038), [arXiv:2105.14777](https://arxiv.org/abs/2105.14777)).
- _parent_: [[concepts/qec/frustration-free]] — VBS codewords are eigenstates of the frustration-free VBS Hamiltonian  ([arXiv:1910.00038](https://arxiv.org/abs/1910.00038), [arXiv:2105.14777](https://arxiv.org/abs/2105.14777)).
- _parent_: [[concepts/qec/approximate-qecc]] — VBS codes approximately protect against erasures in the thermodynamic limit.
- _cousin_: [[concepts/qec/covariant]] — Two classes of (approximate) VBS codes have $SU(q)$ transversal gates, i.e., are $SU(q)$-covariant  ([arXiv:2105.14777](https://arxiv.org/abs/2105.14777)).
- _cousin_: [[concepts/qec/spt]] — VBS codewords  ([arXiv:1910.00038](https://arxiv.org/abs/1910.00038)) are associated with 1D SPT orders  ([arXiv:1008.3745](https://arxiv.org/abs/1008.3745), [arXiv:1010.3732](https://arxiv.org/abs/1010.3732), [arXiv:1103.3323](https://arxiv.org/abs/1103.3323), [arXiv:1106.4772](https://arxiv.org/abs/1106.4772)).
