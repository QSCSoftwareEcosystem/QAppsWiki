---
type: concept
name: Niset-Andersen-Cerf code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/bosonic-classical-into-quantum
- concepts/qec/coherent-state-c-q
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/niset_andersen_cerf
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: niset_andersen_cerf
---

# Niset-Andersen-Cerf code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/niset_andersen_cerf) (`code_id: niset_andersen_cerf`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Coherent-state c-q code encoding two-mode coherent states $\{|\alpha\rangle, |\beta\rangle\}$ into four modes such that the complex values $(\alpha,\beta)$ are recoverable after a single-mode erasure. There are two variations of the storage procedure: a deterministic protocol that offers recovery against a single-mode erasure, and a probabilistic one that can protect against multiple errors with post-selection. This code effectively protects classical information stored in $(\alpha,\beta)$ using quantum operations.

(source: raw/error-correction-zoo.md)

## Protection

The deterministic protocol protects against a single erasure error on a known mode. This recovers one state perfectly and the other state with fidelity $F = \frac{1}{1 + e^{-2 r}}$ for an initial EPR pair squeezed with variance $e^{-2r}$. The probabilistic protocol utilizes post-selection to protect against multiple erasures with state-dependent fidelity.

## Encoders

- After an EPR pair preparation, use 2 continuous CNOT and 2 continuous inverse CNOT gates to entangle a bosonic EPR pair with initial states $|\alpha \rangle$ and $|\beta \rangle$.
- Alternate optical encoder using a two-mode squeezed vacuum state and two balanced beam splitters to mix the input coherent states with the EPR pair.

## Decoders

- Optical decoder using three beam splitters, electronic gain detectors, and two phase-insensitive amplifiers as described in Ref.  ([arXiv:0710.4858](https://arxiv.org/abs/0710.4858)).

## Realizations

- Realized in Ref.  ([arXiv:1006.3941](https://arxiv.org/abs/1006.3941)) in an optical system with 3 beam splitters. The fidelity peaked around $0.6$ for the deterministic approach, and around $0.77$ for the probabilistic approach (with a 25\% chance of error).

## Relations

- _parent_: [[concepts/qec/bosonic-classical-into-quantum]]
- _cousin_: [[concepts/qec/coherent-state-c-q]] — The Niset-Andersen-Cerf code uses coherent states but functions as an erasure-protection code rather than as a modulation format.
