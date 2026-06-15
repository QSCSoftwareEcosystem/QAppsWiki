---
type: concept
name: Brickwork $XS$ stabilizer code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/3d-color
- concepts/qec/hexagonal-cz
- concepts/qec/quantum-double-dihedral
- concepts/qec/tqd-abelian
- concepts/qec/xs-stabilizer
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/brickwork
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: brickwork
---

# Brickwork $XS$ stabilizer code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/brickwork) (`code_id: brickwork`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

An $XS$ stabilizer code that realizes the topological order of the Type-III $G=\mathbb{Z}^3_2$ TQD model  ([arXiv:1508.03468](https://arxiv.org/abs/1508.03468), [arXiv:2405.11719](https://arxiv.org/abs/2405.11719)), which is the same topological order as the $G=D_4$ quantum double  ([arXiv:hep-th/9511195](https://arxiv.org/abs/hep-th/9511195)).
Its qubits are placed on a 2D square lattice, and the stabilizers are defined using two overlapping rectangular tilings.

(source: raw/error-correction-zoo.md)

## Decoders

- Just-in-time decoder  ([arXiv:2503.15751](https://arxiv.org/abs/2503.15751)).

## Relations

- _parent_: [[concepts/qec/xs-stabilizer]] — The brickwork $XS$ stabilizer code is an $XS$ stabilizer code  ([arXiv:2503.15751](https://arxiv.org/abs/2503.15751)).
- _parent_: [[concepts/qec/tqd-abelian]] — The ground-state subspace of the brickwork $XS$ stabilizer code realizes the topological order of the Type-III $G=\mathbb{Z}^3_2$ TQD model  ([arXiv:1508.03468](https://arxiv.org/abs/1508.03468), [arXiv:2405.11719](https://arxiv.org/abs/2405.11719)), which is the same topological order as the $G=D_4$ quantum double  ([arXiv:hep-th/9511195](https://arxiv.org/abs/hep-th/9511195)).
- _cousin_: [[concepts/qec/quantum-double-dihedral]] — The ground-state subspace of the brickwork $XS$ stabilizer code realizes the topological order of the non-Abelian Type-III $G=\mathbb{Z}^3_2$ TQD model  ([arXiv:1508.03468](https://arxiv.org/abs/1508.03468), [arXiv:2405.11719](https://arxiv.org/abs/2405.11719)), which is the same topological order as the ordinary $G=D_4$ quantum double  ([arXiv:hep-th/9511195](https://arxiv.org/abs/hep-th/9511195)).
- _cousin_: [[concepts/qec/3d-color]] — The brickwork $XS$ stabilizer code can be obtained from a 3D color code  ([arXiv:2503.15751](https://arxiv.org/abs/2503.15751)).
- _cousin_: [[concepts/qec/hexagonal-cz]] — The brickwork $XS$ stabilizer code and the hexagonal $CZ$ code realize the same topological phase and are equivalent via a local unitary  ([arXiv:2503.15751](https://arxiv.org/abs/2503.15751)).
