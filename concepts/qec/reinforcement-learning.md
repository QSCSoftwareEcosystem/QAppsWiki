---
type: concept
name: Reinforcement-learning quantum code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/approximate-qecc
- concepts/qec/numopt
- concepts/qec/qubits-into-qubits
- concepts/qec/small-distance-qubit-stabilizer
- concepts/qec/stab-5-1-3
- concepts/qec/surface
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/reinforcement_learning
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: reinforcement_learning
---

# Reinforcement-learning quantum code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/reinforcement_learning) (`code_id: reinforcement_learning`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

An approximate qubit code obtained from a numerical optimization involving a reinforcement learning agent.

(source: raw/error-correction-zoo.md)

## Protection

Depends on the parameter being optimized.

## Rate

Neural network codes can be obtained by optimizing the coherent information  ([arXiv:1806.08781](https://arxiv.org/abs/1806.08781)).

## Encoders

- Both codes and encoding circuits can be obtained via a reinforcement learning agent  ([arXiv:2311.04750](https://arxiv.org/abs/2311.04750)).

## Relations

- _parent_: [[concepts/qec/qubits-into-qubits]]
- _parent_: [[concepts/qec/approximate-qecc]]
- _cousin_: [[concepts/qec/surface]] — Reinforcement learners can be used to optimize the geometry of the surface code to be more suited to a noise channel  ([arXiv:1812.08451](https://arxiv.org/abs/1812.08451)).
- _cousin_: [[concepts/qec/numopt]] — Numerically optimized bosonic codes can be obtained via reinforcement learning  ([arXiv:2108.02766](https://arxiv.org/abs/2108.02766), [arXiv:2212.11651](https://arxiv.org/abs/2212.11651)).
- _cousin_: [[concepts/qec/small-distance-qubit-stabilizer]] — 13 inequivalent $⟦9,3,3⟧$ codes, along with others, have been found via reinforcement learning  ([arXiv:2311.04750](https://arxiv.org/abs/2311.04750)).
- _cousin_: [[concepts/qec/stab-5-1-3]] — Various five-qubit codes, numerically obtained through variational techniques, can outperform the five-qubit perfect code against depolarizing noise  ([arXiv:2506.11552](https://arxiv.org/abs/2506.11552)).

## Notes

- See a review on the use of artificial intelligence in quantum error correction  ([arXiv:2412.20380](https://arxiv.org/abs/2412.20380)).
