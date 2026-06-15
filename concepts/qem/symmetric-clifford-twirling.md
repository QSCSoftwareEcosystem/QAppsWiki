---
type: concept
name: Symmetric Clifford Twirling
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- SCT
- symmetric twirling
- structure-preserving twirling
domains:
- quantum-error-correction
related_concepts:
- concepts/qem/pauli-twirling
- concepts/qem/pec
- concepts/qem/pseudo-twirling
sources:
- raw/qem-zoo.md
- https://qemzoo.com/technique.html?id=symmetric-clifford-twirling
provenance_status: needs-verification
imported_from: qem-zoo
imported_id: symmetric-clifford-twirling
---

# Symmetric Clifford Twirling

> **Imported by `qappswiki import-zoo qemzoo`** from the [QEM Zoo](https://qemzoo.com/technique.html?id=symmetric-clifford-twirling) (`id: symmetric-clifford-twirling`, category: suppression). Public domain (The Unlicense); cited as the QEM Zoo (qemzoo.com), public domain (The Unlicense). This is a `needs-verification` page — confirm against the references below.

## Summary

Applies Clifford twirling using only symmetric Clifford operators that commute with certain Pauli subgroups, preserving the structure of the target operation while scrambling noise to approximately global white noise with exponential precision. Hardware-efficient variants use only local symmetric Cliffords to accelerate noise scrambling. Particularly effective in the early fault-tolerant regime where non-Clifford operations must be error-mitigated with minimal overhead.

(source: raw/qem-zoo.md)

## Properties

| Property | Value |
|---|---|
| Bias | Exponentially small; noise approaches global white noise |
| Sampling overhead | Reduced compared to full Clifford twirling; hardware-efficient variants minimize gate count |
| Noise model required | None |
| Applicability | Early FTQC regime; Hamiltonian simulation; circuits with non-Clifford operations |

## Related techniques

- [[concepts/qem/pauli-twirling]] — symmetric Clifford twirling is a structured extension of Pauli twirling
- [[concepts/qem/pseudo-twirling]] — both extend twirling techniques beyond standard Pauli/Clifford gates
- [[concepts/qem/pec]] — can be used as preprocessing to simplify noise for PEC

## References

- K. Tsubouchi, Y. Mitsuhashi, K. Sharma, N. Yoshioka. *Symmetric Clifford Twirling for Cost-Optimal Quantum Error Mitigation in Early FTQC Regime*. npj Quantum Information, 2025 [arXiv:2405.07720](https://arxiv.org/abs/2405.07720) [doi](https://doi.org/10.1038/s41534-025-01050-9)
