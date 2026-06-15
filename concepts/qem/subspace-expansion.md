---
type: concept
name: Quantum Subspace Expansion
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- QSE
- quantum subspace expansion
domains:
- quantum-error-correction
related_concepts:
- concepts/qem/gse
- concepts/qem/logical-shadow-tomography
- concepts/qem/n-representability
- concepts/qem/purification
- concepts/qem/qed
- concepts/qem/sqd
- concepts/qem/symmetry-verification
sources:
- raw/qem-zoo.md
- https://qemzoo.com/technique.html?id=subspace-expansion
provenance_status: needs-verification
imported_from: qem-zoo
imported_id: subspace-expansion
---

# Quantum Subspace Expansion

> **Imported by `qappswiki import-zoo qemzoo`** from the [QEM Zoo](https://qemzoo.com/technique.html?id=subspace-expansion) (`id: subspace-expansion`, category: mitigation). Public domain (The Unlicense); cited as the QEM Zoo (qemzoo.com), public domain (The Unlicense). This is a `needs-verification` page — confirm against the references below.

## Summary

Constructs an expanded subspace by applying a set of operators (e.g., excitation operators) to a reference state obtained from a quantum device. A generalized eigenvalue problem is then solved classically within this subspace. By including directions that span the noise-induced leakage, the method can project back onto the physical subspace and recover improved estimates.

(source: raw/qem-zoo.md)

## Properties

| Property | Value |
|---|---|
| Bias | Reduced; depends on quality of subspace basis |
| Sampling overhead | Additional measurements for subspace matrix elements |
| Noise model required | None |
| Applicability | Primarily variational algorithms (VQE) |

## Related techniques

- [[concepts/qem/n-representability]] — both are post-processing methods for variational algorithms
- [[concepts/qem/purification]] — both use multiple quantum states to improve estimates
- [[concepts/qem/symmetry-verification]] — subspace expansion can incorporate symmetry constraints
- [[concepts/qem/qed]] — QSE can decode errors similarly to quantum error detection codes
- [[concepts/qem/logical-shadow-tomography]] — QSE is a special case of the LST framework
- [[concepts/qem/sqd]] — SQD uses Krylov subspaces instead of excitation operators
- [[concepts/qem/gse]] — GSE generalizes QSE to handle stochastic, coherent, and algorithmic errors

## References

- J. R. McClean, M. E. Kimchi-Schwartz, J. Carter, W. A. de Jong. *Hybrid Quantum-Classical Hierarchy for Mitigation of Decoherence and Determination of Excited States*. Physical Review A, 2017 [arXiv:1603.05681](https://arxiv.org/abs/1603.05681) [doi](https://doi.org/10.1103/PhysRevA.95.042308)
- J. R. McClean, Z. Jiang, N. C. Rubin, R. Babbush, H. Neven. *Decoding Quantum Errors with Subspace Expansions*. Nature Communications, 2020 [arXiv:1903.05786](https://arxiv.org/abs/1903.05786) [doi](https://doi.org/10.1038/s41467-020-14341-w)
- W. J. Huggins, J. R. McClean, N. C. Rubin, Z. Jiang, N. Wiebe, K. B. Whaley, R. Babbush. *Efficient and Noise Resilient Measurements for Quantum Chemistry on Near-Term Quantum Computers*. npj Quantum Information, 2019 [arXiv:1907.13117](https://arxiv.org/abs/1907.13117) [doi](https://doi.org/10.1038/s41534-020-00341-7)
- N. Yoshioka, H. Hakoshima, Y. Matsuzaki, Y. Tokunaga, Y. Suzuki, S. Endo. *Generalized Quantum Subspace Expansion*. Physical Review Letters, 2022 [arXiv:2107.02611](https://arxiv.org/abs/2107.02611) [doi](https://doi.org/10.1103/PhysRevLett.129.020502)
