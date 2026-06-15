---
type: concept
name: One-hot quantum code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Single-excitation subspace code
- Direct mapping
- Multi-rail code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/chuang-leung-yamamoto
- concepts/qec/group-representation
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/one_hot_quantum
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: one_hot_quantum
---

# One-hot quantum code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/one_hot_quantum) (`code_id: one_hot_quantum`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Encoding of a $q$-dimensional qudit into the single-excitation subspace of $q$ modes. The $j$th logical state is the multi-mode Fock state with one photon in mode $j$ and zero photons in the other modes.
This code is useful for encoding and performing operations on qudits in multiple modes  ([arXiv:quant-ph/0512209](https://arxiv.org/abs/quant-ph/0512209), [arXiv:1505.04990](https://arxiv.org/abs/1505.04990), [arXiv:1811.04069](https://arxiv.org/abs/1811.04069), [arXiv:1812.10495](https://arxiv.org/abs/1812.10495), [arXiv:1909.12847](https://arxiv.org/abs/1909.12847)).

Another name for this code  ([arXiv:1903.05068](https://arxiv.org/abs/1903.05068)), not used here, is a unary code. This term is reserved for a mapping between the natural numbers $N$ and binary strings with the first $N$ coordinates being 1 and the rest 0.

(source: raw/error-correction-zoo.md)

## Protection

This is an error-detecting code against one photon loss event.

## General gates

- Non-deterministic gates using linear optics and photon-number resolving detectors  ([arXiv:2302.07357](https://arxiv.org/abs/2302.07357)).
- The group $SU(q)$ can be realized via Gaussian rotations  ([arXiv:2306.11621](https://arxiv.org/abs/2306.11621)).

## Relations

- _parent_: [[concepts/qec/chuang-leung-yamamoto]]
- _parent_: [[concepts/qec/group-representation]] — One-hot quantum codes are group-representation codes with the $G = SU(q)$ subgroup of Gaussian rotations  ([arXiv:2306.11621](https://arxiv.org/abs/2306.11621)).
- _cousin_: [`one_hot`](https://errorcorrectionzoo.org/c/one_hot) — The one-hot quantum code is the quantum version of the one-hot code.
