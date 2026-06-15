---
type: concept
name: Bosonic c-q code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Bosonic c-q modulation format
- Bosonic c-q modulation scheme
- Bosonic c-q modulation code
- Bosonic c-q signaling format
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/classical-into-quantum
- concepts/qec/oscillators
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/bosonic_classical_into_quantum
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: bosonic_classical_into_quantum
---

# Bosonic c-q code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/bosonic_classical_into_quantum) (`code_id: bosonic_classical_into_quantum`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Bosonic code designed for transmission of classical information through non-classical channels.
Encodes classical symbols into bosonic quantum states for transmission over a quantum channel and decoding with a quantum-enhanced *receiver*.
This entry includes bosonic c-q modulation formats and is distinct from a classical modulation scheme, which maps classical symbols into classical electromagnetic signals for transmission over classical channels.
A bosonic c-q modulation format instead treats the transmitted signals as quantum states and allows the receiver to use quantum measurements.

(source: raw/error-correction-zoo.md)

## Rate

The Holevo capacity has been calculated for various bosonic quantum channels  ([doi:10.1109/JSTQE.2009.2024959](https://doi.org/10.1109/JSTQE.2009.2024959), [arXiv:2002.05766](https://arxiv.org/abs/2002.05766), [doi:10.1515/9783110642490](https://doi.org/10.1515/9783110642490)) such as the pure-loss bosonic channel  ([arXiv:quant-ph/0308012](https://arxiv.org/abs/quant-ph/0308012)) or quantum AWGN  ([arXiv:1312.6225](https://arxiv.org/abs/1312.6225)). The energy-constrained capacity of the noiseless bosonic c-q channel is finite due to quantum effects  ([doi:10.1103/PhysRevLett.70.363](https://doi.org/10.1103/PhysRevLett.70.363), [doi:10.1103/RevModPhys.66.481](https://doi.org/10.1103/RevModPhys.66.481)), while the Shannon capacity can be infinite. Gordon was the first to calculate such capacities (in a published work) for a specific case  ([doi:10.1109/JRPROC.1962.288169](https://doi.org/10.1109/JRPROC.1962.288169)), and a related discussion is given by Forney . The most information-efficient format of a transmitted message is indistinguishable from black-body radiation  ([arXiv:cond-mat/9907500](https://arxiv.org/abs/cond-mat/9907500)).

## Relations

- _parent_: [[concepts/qec/classical-into-quantum]]
- _cousin_: [[concepts/qec/oscillators]] — Bosonic c-q codes are bosonic codes designed to transmit classical information.
- _cousin_: [`modulation`](https://errorcorrectionzoo.org/c/modulation) — Classical modulation schemes transmit classical signals over classical channels, while bosonic c-q modulation formats transmit quantum states over quantum channels and can use quantum-enhanced receivers.
