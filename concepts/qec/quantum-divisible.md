---
type: concept
name: Quantum divisible code
status: provisional
updated: '2026-09-29'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/generalized-quantum-divisible
- concepts/qec/weakly-divisible-css
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/quantum_divisible
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: quantum_divisible
---

# Quantum divisible code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/quantum_divisible) (`code_id: quantum_divisible`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A level-$\nu$ quantum divisible code is a generalized quantum divisible code whose coefficient vector $t$ has entries in $\{\pm 1\}$  ([arXiv:1709.08658](https://arxiv.org/abs/1709.08658)).
Each qubit is rotated about $Z$ by $\pi/2^{\nu-1}$, in a direction set by the sign of the corresponding entry of $t$.
This transversal rotation implements a gate at the $\nu$th level of the \term{Clifford hierarchy} on every logical qubit  ([arXiv:1709.08658](https://arxiv.org/abs/1709.08658)).

The coefficient signs partition the qubits into sets $M^+$ and $M^-$ that witness weak $2^\nu$-divisibility of the $X$-type stabilizer space  ([arXiv:2408.12752](https://arxiv.org/abs/2408.12752)).
If all signs agree, this space is $2^\nu$-divisible in the ordinary sense.
It is therefore doubly even at level two and triply even at level three, while mixed-sign codes need not have either property.

(source: raw/error-correction-zoo.md)

## Transversal gates

- A level-$\nu$ quantum divisible code admits a transversal product of $Z$-axis rotations by $\pi/2^{\nu-1}$, with direction set by the coefficient vector. This product implements the same level-$\nu$ rotation on every logical qubit  ([arXiv:1709.08658](https://arxiv.org/abs/1709.08658)).

## Relations

- _parent_: [[concepts/qec/generalized-quantum-divisible]] — Quantum divisible codes are generalized quantum divisible codes whose coefficient vector has entries in $\{\pm1\}$  ([arXiv:1709.08658](https://arxiv.org/abs/1709.08658)).
- _parent_: [[concepts/qec/weakly-divisible-css]] — The signs of the coefficient vector witness weak $2^\nu$-divisibility of the $X$-type stabilizer space  ([arXiv:1709.08658](https://arxiv.org/abs/1709.08658)).
Quantum divisible codes additionally constrain the logical $X$ representatives and all their joint products with stabilizers.
- _cousin_: [`divisible`](https://errorcorrectionzoo.org/c/divisible) — When all coefficient signs agree, the $X$-type stabilizers of a level-$\nu$ quantum divisible code form a $\nu$-even linear binary code. Mixed signs instead give weak $2^\nu$-divisibility.
