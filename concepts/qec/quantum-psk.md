---
type: concept
name: PSK c-q modulation format
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- PSK c-q modulation code
- PSK c-q modulation scheme
- PSK c-q signaling format
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/cat
- concepts/qec/quantum-fsk
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/quantum_psk
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: quantum_psk
---

# PSK c-q modulation format

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/quantum_psk) (`code_id: quantum_psk`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Coherent-state c-q $q$-ary code whose $j$th codeword corresponds to a coherent state whose phase is the $j$th multiple of $2\pi/q$. These states are also called geometrically uniform states (GUS)  ([doi:10.1109/18.915636](https://doi.org/10.1109/18.915636)).

(source: raw/error-correction-zoo.md)

## Protection

The error probability for $q=4$ under an optimal quantum detector is worked out in ; see also  ([doi:10.1109/18.915636](https://doi.org/10.1109/18.915636), [doi:10.1109/26.752130](https://doi.org/10.1109/26.752130), [arXiv:1410.5282](https://arxiv.org/abs/1410.5282)).

## Decoders

- Multi-stage quantum receivers  ([arXiv:quant-ph/0410133](https://arxiv.org/abs/quant-ph/0410133), [doi:10.1103/PhysRevA.84.062324](https://doi.org/10.1103/PhysRevA.84.062324), [arXiv:0905.2496](https://arxiv.org/abs/0905.2496), [arXiv:1208.1815](https://arxiv.org/abs/1208.1815), [arXiv:1302.2691](https://arxiv.org/abs/1302.2691), [arXiv:1304.7316](https://arxiv.org/abs/1304.7316)).
- Bayesian inference  ([arXiv:1802.08287](https://arxiv.org/abs/1802.08287)).

## Realizations

- Unambiguous state discrimination using displacement-based receiver for 4-PSK  ([doi:10.1038/ncomms3028](https://doi.org/10.1038/ncomms3028)).
- Multi-stage quantum receivers  ([doi:10.1038/nphoton.2012.316](https://doi.org/10.1038/nphoton.2012.316), [arXiv:2001.05902](https://arxiv.org/abs/2001.05902), [doi:10.1038/nphoton.2014.280](https://doi.org/10.1038/nphoton.2014.280), [arXiv:1711.00074](https://arxiv.org/abs/1711.00074)).
- Bayesian inference  ([doi:10.1364/CLEO_QELS.2020.FF1D.1](https://doi.org/10.1364/CLEO_QELS.2020.FF1D.1)).
- Time resolving quantum receiver operating in the telecom C band  ([doi:10.1116/5.0123880](https://doi.org/10.1116/5.0123880)).
- Displacements and photon detection  ([arXiv:2009.02558](https://arxiv.org/abs/2009.02558)).
- Adaptive decoder using linear-optical elements and photon detection  ([arXiv:2207.12234](https://arxiv.org/abs/2207.12234)).

## Relations

- _parent_: [[concepts/qec/quantum-fsk]] — The CFSK c-q code reduces to the $q$-ary PSK c-q code when $\Delta\omega = 0$ and $\Delta\theta = 2\pi/q$.
- _cousin_: [`psk`](https://errorcorrectionzoo.org/c/psk) — PSK (PSK c-q) codes are used to transmit classical information using single-mode coherent states distributed on a circle over classical (quantum) channels.
- _cousin_: [[concepts/qec/cat]] — PSK c-q (cat) codes are used to transmit classical (quantum) information using (superpositions of) single-mode coherent states distributed on a circle over quantum channels.
