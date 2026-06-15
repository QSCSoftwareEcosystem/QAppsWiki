---
type: concept
name: Oscillator-into-oscillator GKP code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- GKP-stabilizer code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/dfour-gkp
- concepts/qec/gkp-concatenated
- concepts/qec/hexagonal-gkp
- concepts/qec/oscillators-into-oscillators
- concepts/qec/quantum-lattice
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/gkp-stabilizer
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: gkp-stabilizer
---

# Oscillator-into-oscillator GKP code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/gkp-stabilizer) (`code_id: gkp-stabilizer`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Multimode GKP code with an infinite-dimensional logical space. Can be obtained by considering an $n$-mode GKP code with a finite-dimensional logical space, removing stabilizers such that the logical space becomes infinite dimensional, and applying a Gaussian circuit.

Simple oscillator-into-oscillator GKP codes include GKP-repetition codes and GKP two-mode-squeezing (TMS) codes  ([arXiv:1903.12615](https://arxiv.org/abs/1903.12615)).
Arbitrary oscillator-into-oscillator GKP codes can be reduced to a standard form consisting of a direct sum of GKP TMS codes, up to symplectic transformations  ([arXiv:2212.11970](https://arxiv.org/abs/2212.11970)).
The optimal code design problem of determining the squeezing parameters can be efficiently solved  ([arXiv:2212.11970](https://arxiv.org/abs/2212.11970)).

(source: raw/error-correction-zoo.md)

## Protection

Oscillator-into-oscillator GKP codes to protect one or more modes against displacement noise using GKP resource states.

## Encoders

- Gaussian circuit applied to $k$ modes storing logical information and $n-k$ modes initialized in a fixed GKP state.

## Threshold

- Thresholds against displacement noise cannot be obtained without ideal (i.e., non-normalizable) codewords  ([arXiv:2102.05545](https://arxiv.org/abs/2102.05545)).

## Decoders

- Syndromes can be read off using ancilla modes, yielding partial information about noise in the logical modes that can then be used in an efficient ML decoding procedure  ([arXiv:2209.04573](https://arxiv.org/abs/2209.04573)).

## Relations

- _parent_: [[concepts/qec/quantum-lattice]] — Oscillator-into-oscillator GKP codes are $n$-mode quantum lattice codes with less than $2n$ stabilizers, i.e., constructed using a degenerate lattice (see Appx. A of Ref.  ([arXiv:2109.14645](https://arxiv.org/abs/2109.14645))).
- _parent_: [[concepts/qec/oscillators-into-oscillators]]
- _cousin_: [[concepts/qec/gkp-concatenated]] — Oscillator-into-oscillator GKP codes concatenated with qubit-into-oscillator GKP codes can outperform more conventional concatenations of qubit-into-oscillator GKP codes with qubit stabilizer codes  ([arXiv:2209.04573](https://arxiv.org/abs/2209.04573)).
- _cousin_: [[concepts/qec/dfour-gkp]] — $D_4$ hyper-diamond GKP codes may be optimal for oscillator-into-oscillator GKP codes utilizing two ancilla modes  ([arXiv:2212.11970](https://arxiv.org/abs/2212.11970)).
- _cousin_: [[concepts/qec/hexagonal-gkp]] — Hexagonal GKP codes may be optimal for oscillator-into-oscillator GKP codes utilizing one ancilla mode  ([arXiv:2212.11970](https://arxiv.org/abs/2212.11970)).

## Notes

- Introduction to and examples of oscillator-into-oscillator GKP codes  ([arXiv:2211.05714](https://arxiv.org/abs/2211.05714)).
