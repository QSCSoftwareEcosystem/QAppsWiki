---
type: concept
name: EA MDS code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/ea-galois-into-galois
- concepts/qec/quantum-mds
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/ea_mds
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: ea_mds
---

# EA MDS code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/ea_mds) (`code_id: ea_mds`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

EA Galois-qudit code whose parameters make the EAQECC Singleton bound  ([arXiv:2010.07902](https://arxiv.org/abs/2010.07902)) become an equality.

The original EAQECC Singleton bound  ([arXiv:quant-ph/0608027](https://arxiv.org/abs/quant-ph/0608027), [arXiv:quant-ph/0610092](https://arxiv.org/abs/quant-ph/0610092)) was shown to be erroneous  ([arXiv:2007.01249](https://arxiv.org/abs/2007.01249)) and corrected in Ref.  ([arXiv:2010.07902](https://arxiv.org/abs/2010.07902)).

(source: raw/error-correction-zoo.md)

## Relations

- _parent_: [[concepts/qec/ea-galois-into-galois]]
- _cousin_: [[concepts/qec/quantum-mds]] — EA MDS codes are entanglement-assisted versions of quantum MDS codes.
- _cousin_: [`mds`](https://errorcorrectionzoo.org/c/mds) — MDS codes give rise to families of EA Galois-qudit codes that saturate the original (erroneous) EAQECC Singleton bound  ([arXiv:1602.02235](https://arxiv.org/abs/1602.02235)).
