---
type: concept
name: Variational Quantum Eigensolver
status: provisional
updated: '2026-09-29'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qem/cdr
- concepts/qem/measurement-error-mitigation
- concepts/qem/n-representability
- concepts/qem/symmetry-verification
- concepts/qem/zne
sources:
- raw/qem-zoo.md
- https://qemzoo.com/technique.html?id=vqe
provenance_status: needs-verification
imported_from: qem-zoo
imported_id: vqe
qem_catalog: applications
---

# Variational Quantum Eigensolver

> **Imported by `qappswiki import-zoo qemzoo`** from the [QEM Zoo](https://qemzoo.com/technique.html?id=vqe) (`id: vqe`, catalog: applications, category: chemistry). Public domain (The Unlicense); cited as the QEM Zoo (qemzoo.com), public domain (The Unlicense). This is a `needs-verification` page — confirm against the references below.

## Summary

VQE is a hybrid quantum-classical algorithm for finding ground state energies of molecular Hamiltonians. Error mitigation is critical for achieving chemical accuracy on NISQ devices. Techniques like symmetry verification, ZNE, and N-representability constraints help correct noisy energy estimates.

(source: raw/qem-zoo.md)

## Key results

- Chemical accuracy achieved for small molecules (H₂, LiH) on NISQ hardware
- Symmetry verification exploits particle number and spin conservation
- CDR leverages near-Clifford training circuits for regression-based correction

## Related techniques

- [[concepts/qem/zne]] — uses
- [[concepts/qem/symmetry-verification]] — uses
- [[concepts/qem/n-representability]] — uses
- [[concepts/qem/measurement-error-mitigation]] — uses
- [[concepts/qem/cdr]] — uses

## References

- A. Kandala, K. Temme, A. D. Córcoles, A. Mezzacapo, J. M. Chow, J. M. Gambetta. *Error Mitigation Extends the Computational Reach of a Noisy Quantum Processor*. Nature, 2019 [arXiv:1805.04492](https://arxiv.org/abs/1805.04492) [doi](https://doi.org/10.1038/s41586-019-1040-7)
- R. Sagastizabal, X. Bonet-Monroig, M. Singh, M. A. Rol, C. C. Bultink, X. Fu, C. H. Price, V. P. Ostroukh, N. Muthusubramanian, A. Bruno, M. Beekman, N. Haider, T. E. O'Brien, L. DiCarlo. *Experimental Error Mitigation via Symmetry Verification in a Variational Quantum Eigensolver*. Physical Review A, 2019 [arXiv:1902.11258](https://arxiv.org/abs/1902.11258) [doi](https://doi.org/10.1103/PhysRevA.100.010302)
- S. McArdle, X. Yuan, S. Benjamin. *Error-Mitigated Digital Quantum Simulation*. Physical Review Letters, 2019 [arXiv:1807.02467](https://arxiv.org/abs/1807.02467) [doi](https://doi.org/10.1103/PhysRevLett.122.180501)
- P. Czarnik, A. Arrasmith, P. J. Coles, L. Cincio. *Error Mitigation with Clifford Quantum-Circuit Data*. Quantum, 2021 [arXiv:2005.10189](https://arxiv.org/abs/2005.10189) [doi](https://doi.org/10.22331/q-2021-11-26-592)
- M. Urbanek, B. Nachman, W. A. de Jong. *Error Detection on Quantum Computers Improving the Accuracy of Chemical Calculations*. Physical Review A, 2020 [arXiv:1910.00129](https://arxiv.org/abs/1910.00129) [doi](https://doi.org/10.1103/PhysRevA.102.022427)
