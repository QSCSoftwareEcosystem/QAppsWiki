---
type: concept
name: Squeezed-coherent BPSK c-q modulation format
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Displaced-squeezed BPSK c-q modulation format
- Squeezed-state BPSK c-q modulation code
- Squeezed-state BPSK c-q modulation scheme
- Squeezed-state BPSK c-q signaling format
- Two-photon coherent-state BPSK c-q modulation format
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/bosonic-classical-into-quantum
- concepts/qec/squeezed-cat
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/squeezed_coherent_bpsk
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: squeezed_coherent_bpsk
---

# Squeezed-coherent BPSK c-q modulation format

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/squeezed_coherent_bpsk) (`code_id: squeezed_coherent_bpsk`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Bosonic c-q binary modulation format whose codewords are antipodal displaced-squeezed states, i.e., states of the form $D(\pm\alpha)S(\zeta)|0\rangle$ for a common squeezing parameter $\zeta$.
The format was originally formulated using the term *two-photon coherent states* (TCS), an early name for squeezed states.

(source: raw/error-correction-zoo.md)

## Protection

Optimizing the displacement and squeezing for fixed mean photon number $N$ changes the coherent-state BPSK overlap exponent from $4N$ to $4N(N+1)$  ([doi:10.1109/TIT.1979.1056033](https://doi.org/10.1109/TIT.1979.1056033)).
Thus, in the ideal binary pure-state discrimination expression, the coherent-state BPSK factor $\exp[-4N]$ is replaced by $\exp[-4N(N+1)]$.

## Rate

The c-q capacity of squeezed-state modulation over a pure-loss bosonic channel with coherent homodyne or heterodyne receivers, including closed-form optima for homodyne detection, was studied in Ref. }.

## Decoders

- Homodyne detection realizes the field-quadrature measurement advantage of antipodal TCS signals in the ideal model  ([doi:10.1109/TIT.1979.1056033](https://doi.org/10.1109/TIT.1979.1056033)).
- Homodyne and heterodyne receivers for squeezed-state modulation are treated in Ref. }.

## Relations

- _parent_: [[concepts/qec/bosonic-classical-into-quantum]]
- _cousin_: [[concepts/qec/squeezed-cat]] — Squeezed-coherent BPSK c-q modulation transmits classical information using displaced-squeezed states, while squeezed cat codes store quantum information in superpositions of squeezed coherent states.
