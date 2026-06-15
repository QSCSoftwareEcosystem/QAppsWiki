---
type: concept
name: Fusion-based quantum computing (FBQC) code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/dual-rail
- concepts/qec/dynamic-gen
- concepts/qec/qubit-stabilizer
- concepts/qec/topological
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/fusion
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: fusion
---

# Fusion-based quantum computing (FBQC) code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/fusion) (`code_id: fusion`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Code whose codewords are resource states used in an FBQC scheme.

FBQC is a fault-tolerant model of quantum computation built from small constant-sized entangled resource states together with destructive entangling measurements called *fusions*  ([arXiv:2101.09310](https://arxiv.org/abs/2101.09310)).
Resource states are stabilizer states and can be described, up to local Clifford transformations, by graph states  ([arXiv:2101.09310](https://arxiv.org/abs/2101.09310)).
Unlike standard MBQC, which first prepares a large cluster state and then computes using single-qubit measurements, FBQC integrates entanglement generation, syndrome extraction, and logical processing into the fusion measurements themselves.
This makes FBQC particularly natural for photonic platforms, where Bell-type fusion measurements are native operations.

(source: raw/error-correction-zoo.md)

## Protection

Protects against erasure, Pauli errors, photon loss, fusion failure from non-determinism, and faults in resource-state preparation. Redundancy in fusion outcomes is captured by the check-operator group. Fusion measurement outcomes form a syndrome that can be decoded to infer the logical Pauli frame, rather than by applying physical recovery operations  ([arXiv:2101.09310](https://arxiv.org/abs/2101.09310)).

## Encoders

- Resource-state generators, which produce small constant-sized stabilizer states, together with Bell-fusion measurements.

## Decoders

- Surface-code-based FBQC schemes often admit a syndrome-graph description, allowing the use of decoders such as minimum-weight matching and union-find  ([arXiv:2101.09310](https://arxiv.org/abs/2101.09310), [arXiv:2112.12160](https://arxiv.org/abs/2112.12160)).

## General gates

- Clifford gates are performed by introducing and manipulating topological features such as boundaries, defects, or twists through modified fusion bases and, in some constructions, single-qubit measurements. Logical gates can also be performed by code deformation.
Non-Clifford gates are performed by magic-state injection.

## Fault tolerance

- Fusion networks can be constructed so that the surviving stabilizers and check operators realize topological surface-code fault tolerance  ([arXiv:2101.09310](https://arxiv.org/abs/2101.09310)).
- More generally, any three-dimensional cell complex in which each edge has four incident faces defines a surface-code fusion complex, yielding a large family of FBQC fault-tolerant protocols  ([arXiv:2308.07844](https://arxiv.org/abs/2308.07844)).

## Threshold

- Under the hardware-agnostic fusion error model, pedagogical FBQC schemes have reported thresholds of $11.98\%$ against erasure in each fusion measurement and $1.07\%$ against Pauli error  ([arXiv:2101.09310](https://arxiv.org/abs/2101.09310)).
- For a linear-optical ballistic scheme, reported thresholds include $43.2\%$ against fusion failure and $10.4\%$ photon loss per fusion  ([arXiv:2101.09310](https://arxiv.org/abs/2101.09310)).
- For surface-code logical blocks compiled to FBQC, the threshold for fault-tolerant logical gates was found to agree, within numerical uncertainty, with the bulk memory threshold  ([arXiv:2112.12160](https://arxiv.org/abs/2112.12160)).

## Relations

- _parent_: [[concepts/qec/qubit-stabilizer]] — The resource states in FBQC are small stabilizer states, and the surviving stabilizers after fusion determine the encoded output state (conditioned on measurement outcomes).
- _cousin_: [[concepts/qec/topological]] — Surface-code-based topological fault-tolerant protocols can be realized in FBQC, including topological features such as boundaries, defects, and twists, by modifying fusion measurements and, in some constructions, adding single-qubit measurements  ([arXiv:2112.12160](https://arxiv.org/abs/2112.12160), [arXiv:2308.07844](https://arxiv.org/abs/2308.07844)).
- _cousin_: [[concepts/qec/dual-rail]] — FBQC resource states are concatenated with dual-rail codes to increase loss detection.
- _cousin_: [[concepts/qec/dynamic-gen]] — Building a fusion network is done using a measurement-based dynamical process.
