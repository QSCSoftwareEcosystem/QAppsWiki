---
type: concept
name: GKP CV-cluster-state code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Hybrid cluster-state code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/cluster-state
- concepts/qec/cv-cluster-state
- concepts/qec/gkp-concatenated
- concepts/qec/gkp-stabilizer
- concepts/qec/qudits-into-oscillators
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/gkp-cluster-state
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: gkp-cluster-state
---

# GKP CV-cluster-state code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/gkp-cluster-state) (`code_id: gkp-cluster-state`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A cluster-state code that utilizes a generalized analog cluster state with some of its physical modes initialized in GKP (resource) states.
Alternatively, it can be thought of as a multimode GKP code whose encoding consists of initializing $k$ modes in momentum states (or, in the normalizable case, squeezed vacua), $n-k$ modes in (normalizable) GKP states, and applying a Gaussian circuit consisting of two-body gates $e^{i V_{jk} \hat{x}_j \hat{x}_k }$ for some angles $V_{jk}$.
The code provides a way to perform fault-tolerant MBQC, with the required number $n-k$ of GKP-encoded physical modes determined by the particular protocol  ([arXiv:1310.7596](https://arxiv.org/abs/1310.7596), [arXiv:2010.02905](https://arxiv.org/abs/2010.02905), [arXiv:1712.00294](https://arxiv.org/abs/1712.00294), [arXiv:2104.03241](https://arxiv.org/abs/2104.03241)).

(source: raw/error-correction-zoo.md)

## Encoders

- Initializing $k$ modes in momentum states (or, in the normalizable case, squeezed vacua), $n-k$ modes in (normalizable) GKP states, and applying a Gaussian circuit consisting of two-body gates $e^{i V_{jk} \hat{x}_j \hat{x}_k }$ for some angles $V_{jk}$.

## General gates

- Logical Clifford gates are performed on the cluster state via a combination of linear-optical gates and homodyne measurements on subsets of vertices  ([arXiv:quant-ph/0605198](https://arxiv.org/abs/quant-ph/0605198), [arXiv:0903.3233](https://arxiv.org/abs/0903.3233)). Magic-state distillation is required for universal computation.
- Single-mode logical Clifford gates can be performed using Gaussian operations and measurements on a 1D GKP cluster state, while two-mode logical Clifford gates require a 2D cluster state. Magic-state distillation using photon-counting can be used for a non-Clifford logical $\pi/8$ gate.
- Gate teleportation and error correction can be performed without active squeezing  ([arXiv:2008.12791](https://arxiv.org/abs/2008.12791)).

## Decoders

- GKP error correction can be naturally combined with CV MBQC protocols since the performance of both is quantified by a squeezing parameter  ([arXiv:1310.7596](https://arxiv.org/abs/1310.7596)).

## Threshold

- A lower bound on the squeezing required to obtain a particular error rate can be formulated in terms of the displacement noise strength. This in turn determines how much squeezing is required in order to be below threshold for a particular concatenated code. For a qubit-level fault-tolerance threshold of $10^{-6}$, the required squeezing is above 20.5 dB  ([arXiv:1310.7596](https://arxiv.org/abs/1310.7596)). Anti-squeezing does not affect this threshold estimate  ([arXiv:1903.02162](https://arxiv.org/abs/1903.02162)).
- For topologically protected MBQC on 3D cluster states built from finitely squeezed GKP qubits, analog QEC together with postselected measurements during cluster-state construction reduces the required squeezing to $9.8$ dB  ([arXiv:1712.00294](https://arxiv.org/abs/1712.00294)).

## Realizations

- A distance-two repetition code using a GKP CV cluster state consisting of squeezed states and GKP states has been implemented in a photonic device by Xanadu  ([doi:10.1038/s41586-024-08406-9](https://doi.org/10.1038/s41586-024-08406-9)).

## Relations

- _parent_: [[concepts/qec/gkp-stabilizer]] — A GKP CV-cluster-state code can be created by initializing $k$ modes in momentum states (or, in the normalizable case, squeezed vacua), $n-k$ modes in (normalizable) GKP states, and applying a Gaussian circuit consisting of two-body $e^{i V_{jk} \hat{x}_j \hat{x}_k }$ for some angles $V_{jk}$.
- _parent_: [[concepts/qec/qudits-into-oscillators]]
- _cousin_: [[concepts/qec/cv-cluster-state]] — GKP CV-cluster-state codes reduce to analog-cluster-state codes when all physical modes are initialized in momentum states.
- _cousin_: [[concepts/qec/cluster-state]] — GKP CV-cluster-state codes reduce to cluster-state codes concatenated with single-mode GKP codes  ([arXiv:1712.00294](https://arxiv.org/abs/1712.00294)) when all physical modes are initialized in GKP states.
- _cousin_: [[concepts/qec/gkp-concatenated]] — GKP CV-cluster-state codes reduce to cluster-state codes concatenated with single-mode GKP codes  ([arXiv:1712.00294](https://arxiv.org/abs/1712.00294)) when all physical modes are initialized in GKP states. Analog QEC with GKP codes concatenated with surface-code and 3D-cluster-state fault-tolerant schemes can reach a threshold displacement standard deviation of about $0.607$ for ideal syndrome measurements and reduce the squeezing required for topologically protected MBQC to $9.8$ dB  ([arXiv:1712.00294](https://arxiv.org/abs/1712.00294)).
