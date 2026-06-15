---
type: concept
name: Coherent FSK (CFSK) c-q modulation format
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Coherent FSK (CFSK) c-q modulation code
- Coherent FSK (CFSK) c-q modulation scheme
- Coherent FSK (CFSK) c-q signaling format
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/coherent-state-c-q
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/quantum_fsk
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: quantum_fsk
---

# Coherent FSK (CFSK) c-q modulation format

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/quantum_fsk) (`code_id: quantum_fsk`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Coherent-state c-q code encoding into coherent states that are frequency-shifted with certain initial relative phase.

Codewords are coherent states $|\alpha_m\rangle$, where \begin{align} \alpha_m
= \alpha e^{i(\omega_0+[m-1]\Delta\omega)t+i(m-1)\Delta\theta} \end{align} for common
frequency $\omega_0$, frequency shift $\Delta\omega < 2\pi/T$, total time $T$,
and phase shift $\Delta\theta$.

(source: raw/error-correction-zoo.md)

## Protection

The square-root measurement is not optimal for CFSK c-q codes, unlike for PSK c-q codes  ([arXiv:2203.09822](https://arxiv.org/abs/2203.09822)).

## Decoders

- Bondurant receiver  ([doi:10.1364/OL.18.001896](https://doi.org/10.1364/OL.18.001896)).
- Cyclic receiver  ([doi:10.1364/OSAC.409200](https://doi.org/10.1364/OSAC.409200)).
- Time-resolving receiver  ([arXiv:1802.08287](https://arxiv.org/abs/1802.08287), [doi:10.1103/PRXQuantum.1.010308](https://doi.org/10.1103/PRXQuantum.1.010308), [doi:10.1038/s41534-022-00573-9](https://doi.org/10.1038/s41534-022-00573-9)).
- Bayesian inference  ([arXiv:1802.08287](https://arxiv.org/abs/1802.08287)).

## Realizations

- Time-resolving quantum receiver  ([doi:10.1038/s41534-022-00573-9](https://doi.org/10.1038/s41534-022-00573-9)).
- Bondurant receiver  ([doi:10.1364/OSAC.409200](https://doi.org/10.1364/OSAC.409200)).
- Bayesian inference  ([doi:10.1103/PRXQuantum.1.010308](https://doi.org/10.1103/PRXQuantum.1.010308)).

## Relations

- _parent_: [[concepts/qec/coherent-state-c-q]]
- _cousin_: [`fsk`](https://errorcorrectionzoo.org/c/fsk) — Coherent FSK c-q codes are classical-quantum analogues of FSK codes.
