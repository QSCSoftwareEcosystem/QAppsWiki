---
type: concept
name: Monitored random-circuit code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/random-circuit
- concepts/qec/random-stabilizer
- concepts/qec/topological
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/monitored_random_circuits
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: monitored_random_circuits
---

# Monitored random-circuit code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/monitored_random_circuits) (`code_id: monitored_random_circuits`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Error-correcting code arising from a monitored random circuit. Such a circuit is described by a series of intermittent random local projective Pauli measurements with random unitary time-evolution operators.

An important sub-family consists of *Clifford monitored random circuits*, where unitaries are sampled from the Clifford group  ([arXiv:1901.08092](https://arxiv.org/abs/1901.08092)).
When the rate of projective measurements is independently controlled by a probability parameter $p$, there can exist two stable phases, one described by volume-law entanglement entropy and the other by area-law entanglement entropy.
The phases and their transition can be understood from the perspective of quantum error correction, information scrambling, and channel capacities  ([arXiv:1903.05124](https://arxiv.org/abs/1903.05124), [arXiv:1905.05195](https://arxiv.org/abs/1905.05195)).

In the volume-law or mixed phase ($ p < p_c $ for some critical probability $p_c$), the channel-capacity density remains nonzero on polynomial timescales and the purification time grows exponentially with system size  ([arXiv:1905.05195](https://arxiv.org/abs/1905.05195)).
The monitored dynamics projects the system into a random error-correcting code, and for strong purification transitions this code can be capacity-achieving for the future unraveled evolution of the channel  ([arXiv:1905.05195](https://arxiv.org/abs/1905.05195)).
In the area-law or pure phase ($ p > p_c $), the channel-capacity density vanishes and the system purifies rapidly  ([arXiv:1905.05195](https://arxiv.org/abs/1905.05195)).
With appropriately chosen evolution operators and measurements, the code is a stabilizer code whose parameters depend on time, $ ⟦n,k(t),d(t)⟧ $.
A similar notion applies to Haar random circuits with measurements  ([arXiv:1911.00008](https://arxiv.org/abs/1911.00008)).

(source: raw/error-correction-zoo.md)

## Protection

When $ p < p_c $, protects against monitored projective measurements by dynamically encoding information into a late-time code space. For one-dimensional stabilizer circuits, the average contiguous code length is efficiently computable and upper bounds the code distance; it is subextensive deep in the mixed phase and appears extensive near $ p_c $  ([arXiv:1905.05195](https://arxiv.org/abs/1905.05195)).

## Rate

Rate can be finite for $ p < p_c $ and vanishes for $ p > p_c $; in the 1+1-dimensional random Clifford model, the residual entropy density equals the channel-capacity density in the mixed phase  ([arXiv:1905.05195](https://arxiv.org/abs/1905.05195)).

## Encoders

- The dynamics of the monitored random circuit can be recast in the language of stabilizer codes  ([arXiv:1905.05195](https://arxiv.org/abs/1905.05195)). The stabilizer group of the error-correcting code resulting from a monitored Clifford circuit either grows or shrinks with each time step, depending on which projective measurements were performed during the time step.
- For strong purification transitions, the monitored dynamics itself implements a single-copy capacity-achieving encoding for the future unraveled evolution of the channel  ([arXiv:1905.05195](https://arxiv.org/abs/1905.05195)).

## Decoders

- With access to the measurement record, recovery operations can reverse the future unraveled evolution with high fidelity; on the code space, the induced dynamics becomes effectively unitary in the thermodynamic limit  ([arXiv:1905.05195](https://arxiv.org/abs/1905.05195)).

## Threshold

- At the purification threshold $ p_c $, the channel-capacity density changes from finite to zero; above $ p_c $, the natural error-correction properties of the circuit can no longer protect an extensive amount of information  ([arXiv:1905.05195](https://arxiv.org/abs/1905.05195)).
- These dynamically generated codes saturate the trade-off between the density of encoded information and the error-rate threshold  ([arXiv:1905.05195](https://arxiv.org/abs/1905.05195)).

## Realizations

- Measurement-induced quantum phases have been realized in a trapped-ion processor  ([arXiv:2106.05881](https://arxiv.org/abs/2106.05881)).

## Relations

- _parent_: [[concepts/qec/random-circuit]] — Monitored random circuits are random circuits where projective measurements are interspersed throughout the circuit and measurement results are recorded.
- _cousin_: [[concepts/qec/topological]] — Topological order can be generated in 2D monitored random circuits  ([arXiv:2011.06595](https://arxiv.org/abs/2011.06595)).
- _cousin_: [[concepts/qec/random-stabilizer]] — An important sub-family of monitored random-circuit codes is the Clifford monitored random-circuit family, where unitaries are sampled from the Clifford group  ([arXiv:1901.08092](https://arxiv.org/abs/1901.08092)).

## Notes

- Connections to information scrambling in black hole physics, as introduced in  ([arXiv:1903.05124](https://arxiv.org/abs/1903.05124)). In particular, monitored random circuits can be viewed as the Hayden-Preskill recovery problem  ([doi:10.1103/PhysRevD.100.086001](https://doi.org/10.1103/PhysRevD.100.086001)) running backwards in time. In this setting, the volume-law entanglement phase of the monitored circuit describes the phase when information can be recovered from an old black hole (i.e., a black hole that is maximally entangled with the early universe).
- Mapping monitored random circuits to statistical mechanics models can help estimate thresholds and code distances for these systems  ([arXiv:2007.03822](https://arxiv.org/abs/2007.03822)).
