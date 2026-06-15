---
type: concept
name: Double-semion string-net code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/commuting-projector
- concepts/qec/double-semion
- concepts/qec/string-net
- concepts/qec/surface
- concepts/qec/topological-abelian
- concepts/qec/tqd-abelian
- concepts/qec/xs-stabilizer
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/double_semion_string_net
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: double_semion_string_net
---

# Double-semion string-net code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/double_semion_string_net) (`code_id: double_semion_string_net`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

An $XS$ stabilizer code that realizes the 2D double semion topological phase.
The model can be extended to other spatial dimensions  ([arXiv:1507.05676](https://arxiv.org/abs/1507.05676)).

(source: raw/error-correction-zoo.md)

## Relations

- _parent_: [[concepts/qec/xs-stabilizer]] — The double-semion string-net code is an $XS$ stabilizer code  ([arXiv:1404.5327](https://arxiv.org/abs/1404.5327)).
- _parent_: [[concepts/qec/tqd-abelian]] — When treated as ground states of the code Hamiltonian, the double-semion string-net code states realize 2D double-semion topological order, a topological phase of matter that exists as the deconfined phase of the 2D twisted $\mathbb{Z}_2$ gauge theory  ([doi:10.1007/BF02096988](https://doi.org/10.1007/BF02096988)).
- _parent_: [[concepts/qec/topological-abelian]] — When treated as ground states of the code Hamiltonian, the double-semion string-net code states realize 2D double-semion topological order, a topological phase of matter that exists as the deconfined phase of the 2D twisted $\mathbb{Z}_2$ gauge theory  ([doi:10.1007/BF02096988](https://doi.org/10.1007/BF02096988)).
- _cousin_: [[concepts/qec/string-net]] — The string-net model code for the category $\text{Vec}^{\omega}\mathbb{Z}_2$ for a nontrivial cocycle is the double semion string-net code.
- _cousin_: [[concepts/qec/double-semion]] — The double-semion stabilizer code and the double-semion string-net code both realize the double semion topological phase, but the former is a modular-qudit Pauli stabilizer code while the latter is an $XS$ stabilizer code. Their ground-state subspaces are connected by a finite-depth circuit with ancillas  ([arXiv:2112.11394](https://arxiv.org/abs/2112.11394)). A commuting-projector version of the double-semion string-net code can also be derived  ([arXiv:1810.08204](https://arxiv.org/abs/1810.08204), [arXiv:2001.11516](https://arxiv.org/abs/2001.11516)).
- _cousin_: [[concepts/qec/surface]] — There is a logical basis for both the toric and double-semion string-net codes where each codeword is a superposition of states corresponding to all noncontractible loops of a particular homotopy type. The superposition is equal for the toric code, whereas an odd number of loops appear with a $-1$ coefficient for the double semion.
- _cousin_: [[concepts/qec/commuting-projector]] — A commuting-projector version of the double-semion string-net code can also be derived  ([arXiv:1810.08204](https://arxiv.org/abs/1810.08204), [arXiv:2001.11516](https://arxiv.org/abs/2001.11516)).
