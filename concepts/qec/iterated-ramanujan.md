---
type: concept
name: Tensor-product HDX code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/multisector-hypergraph
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/iterated_ramanujan
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: iterated_ramanujan
---

# Tensor-product HDX code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/iterated_ramanujan) (`code_id: iterated_ramanujan`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A code constructed in a similar way as the HDX code, but utilizing iterated homological products of *multiple* Ramanujan complexes and then applying distance balancing. For any fixed tensor-power parameter $c$, these yield explicit QLDPC codes with distance scaling as $\sqrt{n}\log^{c} n$, improving on the original HDX construction by replacing a single logarithmic enhancement with arbitrarily high fixed polylogarithmic enhancement. The utility of such tensor products comes from the fact that one of the Ramanujan complexes is a *collective cosystolic expander* as opposed to just a cosystolic expander.

(source: raw/error-correction-zoo.md)

## Protection

Construction yields explicit QLDPC codes with distance $\sqrt{n}\log^c n$ for any fixed $c$, using the $c$-fold tensor product of Ramanujan complexes followed by distance balancing  ([arXiv:2008.09495](https://arxiv.org/abs/2008.09495)).

## Relations

- _parent_: [[concepts/qec/multisector-hypergraph]] — Tensor-product HDX codes result from iterated homological products of length-two chain complexes (i.e., quantum codes) based on Ramanujan complexes  ([arXiv:2103.06309](https://arxiv.org/abs/2103.06309)).
