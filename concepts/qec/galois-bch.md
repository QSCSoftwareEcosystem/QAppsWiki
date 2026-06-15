---
type: concept
name: Galois-qudit BCH code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/asymmetric-qecc
- concepts/qec/galois-css
- concepts/qec/galois-subsystem-stabilizer
- concepts/qec/galois-true-stabilizer
- concepts/qec/general-qldpc
- concepts/qec/quasi-cyclic-qldpc
- concepts/qec/stabilizer-over-gfqsq
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/galois_bch
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: galois_bch
---

# Galois-qudit BCH code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/galois_bch) (`code_id: galois_bch`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

True Galois-qudit stabilizer code constructed from BCH codes via either the Hermitian construction or the Galois-qudit CSS construction.
Parameters can be improved by applying \ref{topic:steane-enlargement}  ([doi:10.1016/j.disc.2010.06.043](https://doi.org/10.1016/j.disc.2010.06.043)), e.g., as in Ref.  ([doi:10.1103/PhysRevA.80.042331](https://doi.org/10.1103/PhysRevA.80.042331)).

(source: raw/error-correction-zoo.md)

## Relations

- _parent_: [[concepts/qec/galois-true-stabilizer]] — Galois-qudit BCH codes can be constructed via the CSS construction or the Hermitian construction.
- _cousin_: [`q-ary_bch`](https://errorcorrectionzoo.org/c/q-ary_bch) — Galois-qudit BCH codes are quantum analogues of q-ary BCH codes.
- _cousin_: [[concepts/qec/galois-css]] — Galois-qudit BCH codes can be constructed via the CSS construction or the Hermitian construction.
- _cousin_: [[concepts/qec/stabilizer-over-gfqsq]] — Galois-qudit BCH codes can be constructed via the CSS construction or the Hermitian construction.
- _cousin_: [[concepts/qec/asymmetric-qecc]] — Asymmetric quantum BCH codes have been constructed  ([doi:10.1098/rspa.2008.0439](https://doi.org/10.1098/rspa.2008.0439)) ([arXiv:quant-ph/0606107](https://arxiv.org/abs/quant-ph/0606107), [doi:10.1109/ICCES.2008.4772987](https://doi.org/10.1109/ICCES.2008.4772987)) ([arXiv:0812.5104](https://arxiv.org/abs/0812.5104)) ([doi:10.26421/QIC11.3-4-4](https://doi.org/10.26421/QIC11.3-4-4)), including subsystem BCH codes  ([arXiv:0803.0764](https://arxiv.org/abs/0803.0764)) ([arXiv:0812.5104](https://arxiv.org/abs/0812.5104)).
- _cousin_: [[concepts/qec/galois-subsystem-stabilizer]] — Asymmetric quantum BCH codes have been constructed  ([doi:10.1098/rspa.2008.0439](https://doi.org/10.1098/rspa.2008.0439)) ([arXiv:quant-ph/0606107](https://arxiv.org/abs/quant-ph/0606107), [doi:10.1109/ICCES.2008.4772987](https://doi.org/10.1109/ICCES.2008.4772987)) ([arXiv:0812.5104](https://arxiv.org/abs/0812.5104)) ([doi:10.26421/QIC11.3-4-4](https://doi.org/10.26421/QIC11.3-4-4)), including subsystem BCH codes  ([arXiv:0803.0764](https://arxiv.org/abs/0803.0764)) ([arXiv:0812.5104](https://arxiv.org/abs/0812.5104)).
- _cousin_: [[concepts/qec/general-qldpc]] — Some Galois-qudit BCH codes are QLDPC  ([arXiv:0802.4079](https://arxiv.org/abs/0802.4079)) ([arXiv:0812.5104](https://arxiv.org/abs/0812.5104)).
- _cousin_: [[concepts/qec/quasi-cyclic-qldpc]] — Some Galois-qudit BCH codes are QC-QLDPC  ([arXiv:0812.5104](https://arxiv.org/abs/0812.5104)).

## Notes

- See Ref.  ([doi:10.1017/CBO9781139034807.014](https://doi.org/10.1017/CBO9781139034807.014)) for an overview of quantum BCH codes.
