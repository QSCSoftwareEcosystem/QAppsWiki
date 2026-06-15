---
type: concept
name: Double-semion stabilizer code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Doubled semion model code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/qudit-surface
- concepts/qec/tqd-abelian-stabilizer
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/double_semion
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: double_semion
---

# Double-semion stabilizer code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/double_semion) (`code_id: double_semion`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A 2D lattice modular-qudit stabilizer code with qudit dimension $q=4$ that realizes the 2D double semion topological phase.
The code can be obtained from a $\mathbb{Z}_4$ toric-code ground state by condensing the emergent boson $e^2 m^2$; in the stabilizer construction this condensation is implemented by two-body measurements  ([arXiv:2112.11394](https://arxiv.org/abs/2112.11394), [arXiv:2211.03798](https://arxiv.org/abs/2211.03798)).
Its ground-state subspace can be mapped to that of the double-semion string-net model by a finite-depth quantum circuit with ancillas  ([arXiv:2112.11394](https://arxiv.org/abs/2112.11394)).

This stabilizer code family is inequivalent to a CSS code via a constant-depth Clifford circuit  ([arXiv:1506.08883](https://arxiv.org/abs/1506.08883)).
Similarly, the double semion model has a sign problem  ([arXiv:1506.08883](https://arxiv.org/abs/1506.08883), [arXiv:2005.05343](https://arxiv.org/abs/2005.05343)) that cannot be eliminated via such a circuit.
However, the sign problem can be eliminated via a non-local circuit  ([arXiv:2509.03708](https://arxiv.org/abs/2509.03708)).

(source: raw/error-correction-zoo.md)

## Relations

- _parent_: [[concepts/qec/tqd-abelian-stabilizer]] — When treated as ground states of the code Hamiltonian, the double-semion stabilizer code states realize 2D double-semion topological order, i.e., the Abelian TQD for $G=\mathbb{Z}_2$ with nontrivial Type-I cocycle, a topological phase that also exists as the deconfined phase of the 2D twisted $\mathbb{Z}_2$ gauge theory  ([doi:10.1007/BF02096988](https://doi.org/10.1007/BF02096988), [arXiv:2112.11394](https://arxiv.org/abs/2112.11394)).
- _cousin_: [[concepts/qec/qudit-surface]] — The exchange statistics of the anyon for the double-semion code coincides with a subset of anyons in the $\mathbb{Z}_4$ surface code, but the fusion rules are different. The double-semion code can be obtained from the $\mathbb{Z}_4$ surface code by condensing the anyon $e^2 m^2$  ([arXiv:2211.03798](https://arxiv.org/abs/2211.03798)) or by gauging  ([arXiv:1202.3120](https://arxiv.org/abs/1202.3120), [arXiv:1407.1025](https://arxiv.org/abs/1407.1025), [arXiv:1603.04442](https://arxiv.org/abs/1603.04442), [arXiv:1603.05182](https://arxiv.org/abs/1603.05182), [arXiv:1605.01640](https://arxiv.org/abs/1605.01640), [arXiv:1805.01836](https://arxiv.org/abs/1805.01836), [arXiv:1806.08679](https://arxiv.org/abs/1806.08679), [arXiv:2108.11402](https://arxiv.org/abs/2108.11402), [arXiv:2310.16032](https://arxiv.org/abs/2310.16032), [arXiv:2410.02213](https://arxiv.org/abs/2410.02213)) the one-form symmetry associated with said anyon  ([arXiv:2211.03798](https://arxiv.org/abs/2211.03798)).
