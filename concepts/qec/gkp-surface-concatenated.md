---
type: concept
name: GKP-surface code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/2d-stabilizer
- concepts/qec/analog-surface
- concepts/qec/gkp-concatenated
- concepts/qec/rotated-surface
- concepts/qec/toric
- concepts/qec/xzzx
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/gkp_surface_concatenated
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: gkp_surface_concatenated
---

# GKP-surface code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/gkp_surface_concatenated) (`code_id: gkp_surface_concatenated`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A concatenated code whose outer code is a GKP code and whose inner code is a surface code, including toric surface-code variants  ([arXiv:1712.00294](https://arxiv.org/abs/1712.00294), [arXiv:1810.00047](https://arxiv.org/abs/1810.00047)), rotated surface codes  ([arXiv:1908.03579](https://arxiv.org/abs/1908.03579), [arXiv:2101.03014](https://arxiv.org/abs/2101.03014), [arXiv:2103.06994](https://arxiv.org/abs/2103.06994), [arXiv:2303.04702](https://arxiv.org/abs/2303.04702)), and XZZX surface codes  ([arXiv:2207.04383](https://arxiv.org/abs/2207.04383)).

(source: raw/error-correction-zoo.md)

## Rate

The error threshold under ML decoding of GKP-rotated-surface codes comes close to $\sigma\approx 0.6065$, at which the best-known lower bound  ([arXiv:quant-ph/9912067](https://arxiv.org/abs/quant-ph/9912067)) on the capacity vanishes  ([arXiv:2411.04277](https://arxiv.org/abs/2411.04277)).

## Decoders

- Minimum-energy and random-plaquette-gauge-model decoders for the toric-GKP code  ([arXiv:1810.00047](https://arxiv.org/abs/1810.00047)).
- MWPM closest point decoder  ([arXiv:2303.04702](https://arxiv.org/abs/2303.04702)).

## Code capacity threshold

- $0.55$ ($0.54$) threshold displacement standard deviation for GKP-toric (GKP-surface) codes without using GKP analog information  ([arXiv:1810.00047](https://arxiv.org/abs/1810.00047)) ([arXiv:1712.00294](https://arxiv.org/abs/1712.00294)). Using the continuous GKP syndrome information raises the GKP-toric threshold to $\sigma_0\approx 0.6$, corresponding to a qubit error rate of about $14\%$  ([arXiv:1810.00047](https://arxiv.org/abs/1810.00047)).
- Analog QEC on GKP-surface codes with ideal syndrome measurements yields a threshold displacement standard deviation of about $0.607$, close to the hashing bound for the Gaussian quantum channel  ([arXiv:1712.00294](https://arxiv.org/abs/1712.00294)).
- $0.67$ threshold displacement standard deviation for GKP-XZZX-surface code  ([arXiv:2207.04383](https://arxiv.org/abs/2207.04383)).
- $0.602$ threshold displacement standard deviation for GKP-surface codes with analog side information using MWPM closest point decoder  ([arXiv:2303.04702](https://arxiv.org/abs/2303.04702)).

## Threshold

- The ML decoding problem for the toric-GKP code maps to a 3D compact QED model in the presence of a quenched random gauge field  ([arXiv:1810.00047](https://arxiv.org/abs/1810.00047)). A decoder based on this mapping yields a threshold displacement standard deviation of $\sigma_0\approx 0.243$ when toric-code measurements, data errors, and GKP ancilla errors are all noisy  ([arXiv:1810.00047](https://arxiv.org/abs/1810.00047)), but this noise model did not properly take into account error propagation  ([arXiv:1908.03579](https://arxiv.org/abs/1908.03579)).
- $11.2$dB of squeezing under displacement noise using MWPM decoding for GKP-rotated-surface codes  ([arXiv:1908.03579](https://arxiv.org/abs/1908.03579), [arXiv:2103.06994](https://arxiv.org/abs/2103.06994)). The error threshold under ML decoding of GKP-rotated-surface codes comes close to $\sigma\approx 0.6065$, at which the best-known lower bound  ([arXiv:quant-ph/9912067](https://arxiv.org/abs/quant-ph/9912067)) on the capacity vanishes  ([arXiv:2411.04277](https://arxiv.org/abs/2411.04277)).

## Relations

- _parent_: [[concepts/qec/gkp-concatenated]]
- _parent_: [[concepts/qec/2d-stabilizer]]
- _cousin_: [[concepts/qec/toric]] — GKP codes have been concatenated with toric codes  ([arXiv:1810.00047](https://arxiv.org/abs/1810.00047)).
- _cousin_: [[concepts/qec/rotated-surface]] — GKP codes have been concatenated with rotated surface codes  ([arXiv:1908.03579](https://arxiv.org/abs/1908.03579), [arXiv:2101.03014](https://arxiv.org/abs/2101.03014), [arXiv:2103.06994](https://arxiv.org/abs/2103.06994), [arXiv:2303.04702](https://arxiv.org/abs/2303.04702)).
- _cousin_: [[concepts/qec/xzzx]] — GKP codes have been concatenated with XZZX surface codes  ([arXiv:2207.04383](https://arxiv.org/abs/2207.04383)).
- _cousin_: [[concepts/qec/analog-surface]] — Condensing pure fluxes and charges in the analog surface code yields toric-GKP codes  ([arXiv:2411.04993](https://arxiv.org/abs/2411.04993)).
