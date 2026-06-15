---
type: concept
name: Chen-Hsin invertible-order code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/clifford-hierarchy
- concepts/qec/spt
- concepts/qec/topological-abelian
- concepts/qec/yetter-gauge-theory
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/invertible
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: invertible
---

# Chen-Hsin invertible-order code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/invertible) (`code_id: invertible`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A geometrically local commuting-projector code that realizes beyond-group-cohomology invertible topological phases in arbitrary dimensions.
Its code Hamiltonian terms include Pauli-$Z$ operators and products of Pauli-$X$ operators and $CZ$ gates  ([arXiv:2110.14644](https://arxiv.org/abs/2110.14644)).
Instances of the code in 4D realize the 3D $\mathbb{Z}_2$ gauge theory with fermionic charge and either bosonic (FcBl) or fermionic (FcFl) loop excitations at their boundaries  ([arXiv:2011.11165](https://arxiv.org/abs/2011.11165), [arXiv:2110.14654](https://arxiv.org/abs/2110.14654)); see Ref.  ([arXiv:1912.05565](https://arxiv.org/abs/1912.05565)) for a different lattice-model formulation of the FcBl boundary code.

(source: raw/error-correction-zoo.md)

## Encoders

- QCA encoder  ([arXiv:2110.14644](https://arxiv.org/abs/2110.14644), [arXiv:2407.07951](https://arxiv.org/abs/2407.07951)).

## Relations

- _parent_: [[concepts/qec/clifford-hierarchy]] — Chen-Hsin invertible-order code Hamiltonian terms include Pauli and $CZ$ operators, making them Clifford stabilizer codes.
- _parent_: [[concepts/qec/yetter-gauge-theory]] — Chen-Hsin invertible-order codes realize beyond-group-cohomology invertible topological phases of order two and four in arbitrary dimensions. These phases are described by invertible two-gauge theories  ([arXiv:2110.14644](https://arxiv.org/abs/2110.14644)).
- _cousin_: [[concepts/qec/topological-abelian]] — Instances of the code in 4D realize the 3D $\mathbb{Z}_2$ gauge theory with fermionic charge and either bosonic (FcBl) or fermionic (FcFl) loop excitations at their boundaries  ([arXiv:2011.11165](https://arxiv.org/abs/2011.11165), [arXiv:2110.14654](https://arxiv.org/abs/2110.14654)); see Ref.  ([arXiv:1912.05565](https://arxiv.org/abs/1912.05565)) for a different lattice-model formulation of the FcBl boundary code.
- _cousin_: [[concepts/qec/spt]] — Instances of the Chen-Hsin invertible-order code realize beyond-group-cohomology SPTs  ([arXiv:2110.14644](https://arxiv.org/abs/2110.14644)).
