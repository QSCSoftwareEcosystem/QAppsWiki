---
type: concept
name: Twisted $1$-group code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/fock-state
- concepts/qec/group-representation
- concepts/qec/permutation-invariant
- concepts/qec/small-distance-quantum
- concepts/qec/spins-into-spins
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/t_group
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: t_group
---

# Twisted $1$-group code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/t_group) (`code_id: t_group`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Block group-representation code realizing particular irreps of particular groups such that a distance of two is automatically guaranteed.
Groups which admit irreps with this property are called *twisted (unitary) $1$-groups* and include the binary icosahedral group $2I$, the $\Sigma(360\phi)$ subgroup of $SU(3)$, the family $\{PSp(2b, 3), b \geq 1\}$, and the alternating groups $A_{5,6}$.
Groups whose irreps are images of the appropriate irreps of twisted $1$-groups also yield such properties, e.g., the binary tetrahedral group $2T$ or qutrit Pauli group $\Sigma(72\phi)$.

A $((3,2,2))_3$ code can implement the qutrit Pauli group $\Sigma(72\phi)$ transversally, a $((6,3,2))$ code can implement $A_5$ transversally, a $((6,2,2))_3$ implements $2T$ transversally, and a $((6,5,2))_3$ code implements $A_6$ transversally.

(source: raw/error-correction-zoo.md)

## Transversal gates

- All gates in the underlying twisted $1$-group. See  ([arXiv:2403.08999](https://arxiv.org/abs/2403.08999)) for other notable groups including the sporadic groups.

## Relations

- _parent_: [[concepts/qec/spins-into-spins]]
- _parent_: [[concepts/qec/permutation-invariant]]
- _parent_: [[concepts/qec/group-representation]] — Twisted $1$-group codes are group-representation codes with $G$ being a twisted $1$-group.
- _parent_: [[concepts/qec/small-distance-quantum]] — All twisted $1$-group codes have a distance $d \geq 2$.
- _cousin_: [`unitary_design`](https://errorcorrectionzoo.org/c/unitary_design) — Twisted unitary $t$-groups  ([arXiv:2402.01638](https://arxiv.org/abs/2402.01638)) generalize the idea of unitary $t$-groups  ([arXiv:math/0502080](https://arxiv.org/abs/math/0502080), [arXiv:0809.3813](https://arxiv.org/abs/0809.3813), [arXiv:1810.02507](https://arxiv.org/abs/1810.02507)), which are subgroups of the unitary group that form unitary $t$-designs.
- _cousin_: [[concepts/qec/fock-state]] — Twisted $1$-group codes can be converted to constant-excitation Fock-state codes via the simplex mapping  ([arXiv:2509.20545](https://arxiv.org/abs/2509.20545)). Any transversal gates are mapped to Gaussian gates on the Fock-state codes  ([arXiv:2509.20545](https://arxiv.org/abs/2509.20545)).
