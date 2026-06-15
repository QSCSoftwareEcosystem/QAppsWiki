---
type: concept
name: Wasilewski-Banaszek code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/constant-excitation-permutation-invariant
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/wasilewski-banaszek
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: wasilewski-banaszek
---

# Wasilewski-Banaszek code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/wasilewski-banaszek) (`code_id: wasilewski-banaszek`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Three-oscillator constant-excitation Fock-state code encoding a single logical qubit.

A basis of codewords is
\begin{align}
\begin{split}
|\overline{0}\rangle &= \frac{1}{\sqrt{3}}(|003\rangle+|030\rangle+|300\rangle)\\
|\overline{1}\rangle &= |111\rangle
\end{split}.
\end{align}

(source: raw/error-correction-zoo.md)

## Protection

Protects against single photon loss in any one mode.

## Encoders

- A qubit in the dual-rail code can be transferred to this code via a linear optical network using four ancillary modes, each with one photon input. Successful encoding is conditioned on measuring the state $|110\rangle$ on the last three modes.

## General gates

- Single-qubit gates implemented using linear optical networks, sometimes with the addition of auxiliary modes with vacuum input and (conditional) output.

## Decoders

- Destructive measurement with photon number measurements on each mode.

## Relations

- _parent_: [[concepts/qec/constant-excitation-permutation-invariant]] — The Wasilewski-Banaszek code is a simple example of an Ouyang-Chao PI code  ([arXiv:1809.09801](https://arxiv.org/abs/1809.09801)).
