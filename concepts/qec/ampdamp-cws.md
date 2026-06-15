---
type: concept
name: Amplitude-damping CWS code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/cws
- concepts/qec/self-complementary
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/ampdamp_cws
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: ampdamp_cws
---

# Amplitude-damping CWS code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/ampdamp_cws) (`code_id: ampdamp_cws`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Self-complementary CWS code that is designed to detect and correct AD errors.

Ref.  ([arXiv:0907.5149](https://arxiv.org/abs/0907.5149)) constructs such codes by starting from classical self-complementary single-error-correcting codes for the binary asymmetric channel and lifting them to quantum codewords of the form $|u\rangle+|\overline{u}\rangle$.
In particular, the paper uses nonlinear Constantin-Rao and related Varshamov-Tenengol'ts codes, and also a binary-to-ternary mapping to obtain improved families for short block lengths.

(source: raw/error-correction-zoo.md)

## Encoders

- Because the resulting codes are of CWS type, encoding circuits can be obtained from the underlying CWS construction  ([arXiv:0907.5149](https://arxiv.org/abs/0907.5149)).

## Decoders

- Because the resulting codes are of CWS type, decoding circuits can be obtained from the underlying CWS construction  ([arXiv:0907.5149](https://arxiv.org/abs/0907.5149)).

## Relations

- _parent_: [[concepts/qec/cws]]
- _parent_: [[concepts/qec/self-complementary]]
- _cousin_: [`constantin_rao`](https://errorcorrectionzoo.org/c/constantin_rao) — Amplitude-damping CWS codes can be obtained from CR codes  ([arXiv:0907.5149](https://arxiv.org/abs/0907.5149)).
