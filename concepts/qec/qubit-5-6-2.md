---
type: concept
name: $((5,6,2))$ qubit code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/arvind
- concepts/qec/quantum-cyclic
- concepts/qec/rains
- concepts/qec/stab-4-2-2
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/qubit_5_6_2
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: qubit_5_6_2
---

# $((5,6,2))$ qubit code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/qubit_5_6_2) (`code_id: qubit_5_6_2`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Five-qubit cyclic CWS code detecting a single-qubit error.
This code has a logical subspace whose dimension is larger than that of the $⟦5,2,2⟧$ code, the best five-qubit stabilizer code with the same distance  ([arXiv:0709.1780](https://arxiv.org/abs/0709.1780)).

Its codeword stabilizer consists of all cyclic shifts of $ZXZII$.
A standard-form CWS presentation uses the five-cycle graph together with the classical codewords $00000$, $11010$, $01101$, $10110$, $01011$, and $10101$  ([arXiv:0708.1021](https://arxiv.org/abs/0708.1021), [arXiv:0709.1780](https://arxiv.org/abs/0709.1780)).
Its automorphism group is of size 3840 and given in Ref.  ([arXiv:quant-ph/9703002](https://arxiv.org/abs/quant-ph/9703002)) (see also  ([arXiv:quant-ph/9704043](https://arxiv.org/abs/quant-ph/9704043))).

(source: raw/error-correction-zoo.md)

## Relations

- _parent_: [[concepts/qec/rains]] — The $((5,6,2))$ code is the smallest nontrivial Rains code  ([arXiv:quant-ph/9704043](https://arxiv.org/abs/quant-ph/9704043)) (see also  ([arXiv:cs/0610159](https://arxiv.org/abs/cs/0610159)) ([arXiv:0801.0831](https://arxiv.org/abs/0801.0831))).
- _parent_: [[concepts/qec/arvind]] — The $((5,6,2))$ code is the $((n,1+n(q-1),2))_q$ union stabilizer code for $n=5$ and $q=2$  ([arXiv:quant-ph/0210097](https://arxiv.org/abs/quant-ph/0210097)).
- _parent_: [[concepts/qec/quantum-cyclic]]
- _cousin_: [[concepts/qec/stab-4-2-2]] — Tracing out any one qubit of the $((5,6,2))$ code projector yields a $((4,4,2))$ code; for this code, all five such partial traces are additive and therefore locally equivalent to the $⟦4,2,2⟧$ code  ([arXiv:quant-ph/9704043](https://arxiv.org/abs/quant-ph/9704043)).
