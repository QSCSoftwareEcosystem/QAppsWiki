---
type: concept
name: Long-range enhanced surface code (LRESC)
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/cyclic-hgp
- concepts/qec/lacross
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/lresc
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: lresc
---

# Long-range enhanced surface code (LRESC)

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/lresc) (`code_id: lresc`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Code constructed using a hypergraph product of two copies of a concatenated LDPC-repetition seed code.
This family interpolates between surface codes and hypergraph codes since the hypergraph product of two repetition codes yields the planar surface code.
The construction uses small $[3,2,2]$ and $[6,2,4]$ LDPC codes concatenated with $[4,1,4]$ and $[2,1,2]$ repetition codes, respectively.
An example using a $[5,2,3]$ code is also presented.

(source: raw/error-correction-zoo.md)

## General gates

- Patch-transversal gates for suitable seed codes  ([arXiv:2309.11719](https://arxiv.org/abs/2309.11719)).

## Realizations

- Preparation of GHZ state of four logical qubits with beyond break-even fidelity in a $⟦25,4,3⟧$ LRESC  ([arXiv:2406.02666](https://arxiv.org/abs/2406.02666)).

## Relations

- _parent_: [[concepts/qec/cyclic-hgp]] — LRESCs are constructed using a hypergraph product of a concatenated LDPC-repetition code with itself.
- _cousin_: [[concepts/qec/lacross]] — La-cross codes yield LRESCs for $k=2$. La-cross codes have a number of long-range stabilizers that scales linearly with code size, while the number of LRESC long-range stabilizers can be tuned to scale between the square-root of the size and linearly in the size.
- _cousin_: [`ldpc`](https://errorcorrectionzoo.org/c/ldpc) — LRESCs are constructed using a hypergraph product of two copies of a concatenated LDPC-repetition seed code.
- _cousin_: [`repetition`](https://errorcorrectionzoo.org/c/repetition) — LRESCs are constructed using a hypergraph product of two copies of a concatenated LDPC-repetition seed code.
- _cousin_: [`concatenated`](https://errorcorrectionzoo.org/c/concatenated) — LRESCs are constructed using a hypergraph product of two copies of a concatenated LDPC-repetition seed code.
