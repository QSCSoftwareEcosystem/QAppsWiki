---
type: concept
name: Concatenated Steane code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/cluster-state
- concepts/qec/holographic-steane
- concepts/qec/qldpc
- concepts/qec/qubit-concatenated
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/concatenated_steane
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: concatenated_steane
---

# Concatenated Steane code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/concatenated_steane) (`code_id: concatenated_steane`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A member of the family of $⟦7^m,1,3^m⟧$ CSS codes, each of which is a recursive level-$m$ concatenation of the Steane code.
This family is one of the first to admit a concatenated threshold  ([arXiv:quant-ph/9702058](https://arxiv.org/abs/quant-ph/9702058), [arXiv:quant-ph/9809054](https://arxiv.org/abs/quant-ph/9809054), [arXiv:quant-ph/0207119](https://arxiv.org/abs/quant-ph/0207119), [arXiv:quant-ph/0410047](https://arxiv.org/abs/quant-ph/0410047), [arXiv:quant-ph/0604090](https://arxiv.org/abs/quant-ph/0604090)).

(source: raw/error-correction-zoo.md)

## Protection

Code performance against general Pauli channels has been worked out  ([arXiv:quant-ph/0111003](https://arxiv.org/abs/quant-ph/0111003), [arXiv:quant-ph/0206061](https://arxiv.org/abs/quant-ph/0206061)).

## Decoders

- A simple message-passing decoder from level 1 to level 2 corrects all weight-four errors for the $⟦49,1,9⟧$ code and was used in the comparative threshold study of Ref.  ([arXiv:0711.1556](https://arxiv.org/abs/0711.1556)).
- There exist fault-tolerant syndrome extraction protocols for the concatenated Steane code  ([arXiv:2403.09978](https://arxiv.org/abs/2403.09978)).
- Randomized compiling helps reduce logical error rate for some noise models  ([arXiv:2303.06846](https://arxiv.org/abs/2303.06846)).

## Fault tolerance

- Fault-tolerant computation can be done on nearest-neighbor arrays  ([arXiv:quant-ph/0702201](https://arxiv.org/abs/quant-ph/0702201)).
- There exist fault-tolerant syndrome extraction protocols for the concatenated Steane code  ([arXiv:2403.09978](https://arxiv.org/abs/2403.09978)).
- The combination of the concatenated Steane code and QLDPC codes with non-vanishing rate yields fault-tolerant quantum computation with constant space and polylogarithmic time overheads, even when classical computation time is taken into account  ([arXiv:2411.03683](https://arxiv.org/abs/2411.03683)).

## Code capacity threshold

- This family is one of the first to admit a concatenated threshold  ([arXiv:quant-ph/9702058](https://arxiv.org/abs/quant-ph/9702058), [arXiv:quant-ph/9809054](https://arxiv.org/abs/quant-ph/9809054), [arXiv:quant-ph/0207119](https://arxiv.org/abs/quant-ph/0207119), [arXiv:quant-ph/0410047](https://arxiv.org/abs/quant-ph/0410047), [arXiv:quant-ph/0504218](https://arxiv.org/abs/quant-ph/0504218), [arXiv:quant-ph/0703230](https://arxiv.org/abs/quant-ph/0703230), [arXiv:quant-ph/0604090](https://arxiv.org/abs/quant-ph/0604090)); see the book .

## Threshold

- Between $1.78\%$ and $11.5\%$ with faulty photon detectors when combined with the dual-rail code at the first concatenation step in a variant of the KLM protocol  ([arXiv:quant-ph/0405112](https://arxiv.org/abs/quant-ph/0405112), [arXiv:quant-ph/0502101](https://arxiv.org/abs/quant-ph/0502101)).
- For the adversarial-stochastic exRec analysis of the concatenated 7-qubit protocol, a crude bound gives $p_T > 3.6\times 10^{-6}$, while circuit optimization together with careful counting of malignant sets improves this to $p_T \geq 2.7\times 10^{-5}$ .
- When used as the underlying code of a Steane/Hamming concatenation in a unified logical-CNOT comparison under circuit-level depolarizing noise, the threshold is $0.030\%$; at physical error rate $0.1\%$, this underlying code cannot suppress the logical error rate to $10^{-24}$, while at $0.01\%$ it requires space overhead $6.1\times 10^3$  ([arXiv:2402.09606](https://arxiv.org/abs/2402.09606)).
- The recursively concatenated Steane code has a measurement threshold of one  ([arXiv:2402.00145](https://arxiv.org/abs/2402.00145)).

## Relations

- _parent_: [[concepts/qec/holographic-steane]] — A recursively concatenated Steane code is a heptagon holographic code on a tree tensor network.
- _parent_: [[concepts/qec/qubit-concatenated]] — The combination of the concatenated Steane code and QLDPC codes with non-vanishing rate yields fault-tolerant quantum computation with constant space and polylogarithmic time overheads, even when classical computation time is taken into account  ([arXiv:2411.03683](https://arxiv.org/abs/2411.03683)).
- _cousin_: [[concepts/qec/qldpc]] — The combination of the concatenated Steane code and QLDPC codes with non-vanishing rate yields fault-tolerant quantum computation with constant space and polylogarithmic time overheads, even when classical computation time is taken into account  ([arXiv:2411.03683](https://arxiv.org/abs/2411.03683)).
- _cousin_: [[concepts/qec/cluster-state]] — The cluster state corresponding to the concatenated Steane code has been worked out  ([arXiv:quant-ph/0307130](https://arxiv.org/abs/quant-ph/0307130)).
