---
type: concept
name: Prime-qudit RM code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/galois-reed-muller
- concepts/qec/qudit-css
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/qudit_reed_muller
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: qudit_reed_muller
---

# Prime-qudit RM code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/qudit_reed_muller) (`code_id: qudit_reed_muller`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Modular-qudit stabilizer code constructed from GRM codes or their duals via the modular-qudit CSS construction.

For prime local dimension $q$, CSS constructions from $\mathrm{GRM}_q(\nu_1,m) \subseteq \mathrm{GRM}_q(\nu_2,m)$ yield pure $⟦q^m,k(\nu_2)-k(\nu_1),\min\{d(\nu_1^\perp),d(\nu_2)\}⟧_q$ codes  ([arXiv:quant-ph/0502001](https://arxiv.org/abs/quant-ph/0502001)).
The special case $m=1$ gives quantum MDS codes $⟦q,q-2\nu-2,\nu+2⟧_q$ for $0 \leq \nu \leq (q-2)/2$  ([arXiv:quant-ph/0502001](https://arxiv.org/abs/quant-ph/0502001)).
An odd-prime-qudit CSS code family constructed from first-order punctured GRM codes transversally implements a diagonal gate at any level of the qudit Clifford hierarchy  ([arXiv:1205.3104](https://arxiv.org/abs/1205.3104), [arXiv:1406.3055](https://arxiv.org/abs/1406.3055)).

(source: raw/error-correction-zoo.md)

## Rate

For the CSS family from $\mathrm{GRM}_q(\nu_1,m) \subseteq \mathrm{GRM}_q(\nu_2,m)$, the rate is $( k(\nu_2)-k(\nu_1) )/q^m$  ([arXiv:quant-ph/0502001](https://arxiv.org/abs/quant-ph/0502001)).

## Magic scaling exponent

An odd-prime-qudit CSS code family constructed from first-order punctured GRM codes can be used for qudit magic-state distillation; see  ([arXiv:1205.3104](https://arxiv.org/abs/1205.3104)) for yields.

## Transversal gates

- An odd-prime-qudit CSS code family constructed from first-order punctured GRM codes transversally implements a diagonal gate at any level of the qudit Clifford hierarchy  ([arXiv:1205.3104](https://arxiv.org/abs/1205.3104), [arXiv:1406.3055](https://arxiv.org/abs/1406.3055)).

## Relations

- _parent_: [[concepts/qec/qudit-css]]
- _parent_: [[concepts/qec/galois-reed-muller]] — Galois-qudit RM codes reduce to prime-qudit RM codes when $q$ is prime.
