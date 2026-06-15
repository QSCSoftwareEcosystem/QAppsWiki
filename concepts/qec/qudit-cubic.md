---
type: concept
name: Qudit cubic code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/analog-stabilizer
- concepts/qec/fracton
- concepts/qec/homological-rotor
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/qudit_cubic
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: qudit_cubic
---

# Qudit cubic code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/qudit_cubic) (`code_id: qudit_cubic`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Generalization of the Haah cubic code to modular qudits.

(source: raw/error-correction-zoo.md)

## Protection

Performance over the erasure and depolarizing channels was studied in Ref.  ([doi:10.23919/ISITA.2018.8664389](https://doi.org/10.23919/ISITA.2018.8664389)).

## Relations

- _parent_: [[concepts/qec/fracton]] — Haah cubic  ([arXiv:1101.1962](https://arxiv.org/abs/1101.1962)) codes 1-4, 7, 8, and 10 do not have string logical operators and are the first examples of Type-II fracton phases. The remaining cubic codes are fractal Type-I fracton codes  ([arXiv:1908.08049](https://arxiv.org/abs/1908.08049), [arXiv:2001.01722](https://arxiv.org/abs/2001.01722)). The qutrit models in  ([arXiv:1908.08049](https://arxiv.org/abs/1908.08049)) are likely Type-II, with no string operators found numerically up to width 20, while the $q=5$ qudit model in  ([arXiv:1908.08049](https://arxiv.org/abs/1908.08049)) satisfies a proven no-string condition and is Type-II.
- _cousin_: [[concepts/qec/homological-rotor]] — The qudit cubic code can be generalized to rotors ,arxiv:1709.04460}.
- _cousin_: [[concepts/qec/analog-stabilizer]] — The qudit cubic code can be generalized to oscillators  ([arXiv:1709.04460](https://arxiv.org/abs/1709.04460)).
