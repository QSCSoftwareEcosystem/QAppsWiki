---
type: concept
name: Many-Body Quantum Chaos
status: provisional
updated: '2026-09-29'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qem/pauli-twirling
- concepts/qem/tem
- concepts/qem/trex
sources:
- raw/qem-zoo.md
- https://qemzoo.com/technique.html?id=many-body-chaos
provenance_status: needs-verification
imported_from: qem-zoo
imported_id: many-body-chaos
qem_catalog: applications
---

# Many-Body Quantum Chaos

> **Imported by `qappswiki import-zoo qemzoo`** from the [QEM Zoo](https://qemzoo.com/technique.html?id=many-body-chaos) (`id: many-body-chaos`, catalog: applications, category: simulation). Public domain (The Unlicense); cited as the QEM Zoo (qemzoo.com), public domain (The Unlicense). This is a `needs-verification` page — confirm against the references below.

## Summary

Simulating chaotic quantum many-body dynamics, such as dual-unitary circuits and kicked Ising models, tests quantum processors against exactly solvable models exhibiting maximal chaos. Error mitigation enables accurate computation of dynamical correlators and exploration of emergent quantum phases beyond the reach of classical tensor network methods.

(source: raw/qem-zoo.md)

## Key results

- 91-qubit simulation of dual-unitary circuits with 4,095 two-qubit ECR gates on IBM ibm_strasbourg
- Tensor network error mitigation (TEM) with learned sparse Pauli-Lindblad noise model
- Results verified against exact analytical solutions at the dual-unitary point
- Explored perturbed circuits beyond exact solvability, outperforming classical tensor network approximations
- 262,144 shots per data point with ~3.4 hour total execution time

## Related techniques

- [[concepts/qem/tem]] — uses
- [[concepts/qem/pauli-twirling]] — uses
- [[concepts/qem/trex]] — uses

## References

- L. E. Fischer, M. Leahy, A. Eddins, N. Keenan, D. Ferracin, M. A. C. Rossi, Y. Kim, A. He, F. Pietracaprina, B. Sokolov, S. Dooley, Z. Zimborás, F. Tacchino, S. Maniscalco, J. Goold, G. García-Pérez, I. Tavernelli, A. Kandala, S. N. Filippov. *Dynamical Simulations of Many-Body Quantum Chaos on a Quantum Computer*. Nature Physics, 2026 [arXiv:2411.00765](https://arxiv.org/abs/2411.00765) [doi](https://doi.org/10.1038/s41567-025-03144-9)
