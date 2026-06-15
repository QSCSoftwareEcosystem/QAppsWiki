---
type: concept
name: Bosonic rotation code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Rotationally symmetric bosonic (RSB) code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/fock-state
- concepts/qec/quantum-random
- concepts/qec/single-mode
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/bosonic_rotation
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: bosonic_rotation
---

# Bosonic rotation code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/bosonic_rotation) (`code_id: bosonic_rotation`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A single-mode Fock-state bosonic code whose codespace is preserved by a phase-space rotation by a multiple of $2\pi/N$ for some $N$. The rotation symmetry ensures that encoded states have support only on every $N^{\textrm{th}}$ Fock state. For example, single-mode Fock-state codes for $N=2$ encoding a qubit admit basis states that are, respectively, supported on Fock state sets $\{|0\rangle,|4\rangle,|8\rangle,\cdots\}$ and $\{|2\rangle,|6\rangle,|10\rangle,\cdots\}$.


Codewords can be uniquely specified by choosing a *primitive* state $|\Theta\rangle$. To ensure valid (orthogonal and nonzero) codewords, $|\Theta\rangle$ must satisfy the following requirement: for each $j \in \mathbb{Z}_q$, $|\Theta\rangle$ must have support on at least one Fock state $|(k_j q+j)N\rangle$ for some $k_j \in \mathbb{N}_0$. A set of logical codewords is then obtained by projecting $|\Theta\rangle$ onto the $q$ eigenspaces of the discrete rotation operator, equivalently by summing the $qN$ rotated copies of $|\Theta\rangle$ with appropriate phases.

(source: raw/error-correction-zoo.md)

## Protection

Losses or gains less than $N$ are detectable. Dephasing rotations $\exp(\mathrm{i}\theta \hat{n})$ can be detected whenever $\theta$ is roughly less than $\pi/N$. To get precise bounds on $\theta$, one needs to analyze the particular bosonic rotation code.

## General gates

- The logical Pauli-$Z$ gate can be the discrete rotation operator $\mathrm{e}^{\mathrm{i} \pi \hat n /N}$, and the logical Pauli-$X$ gate can be the Susskind–Glogower phase operator $\sum_{n=0}^\infty |n\rangle\bra{n+N}$.
- For qubit codes, a logical phase gate is $S = \mathrm{e}^{\pi \mathrm{i} \hat n^2 / 2N^2}$.
- The $T = \mathrm{diag}(1,\exp(\mathrm{i}\pi/4))$ gate can be done via gate teleportation and a resource state $\vert 0_N\rangle + \exp(\mathrm{i}\pi/4) \vert 1_N \rangle$.
- A controlled-rotation gate between an order $N$ rotation code and an order $M$ rotation code is $\mathrm{CROT}_{NM} = \mathrm{e}^{(2\pi\mathrm{i} / qNM) \hat n \otimes \hat n}$.

## Decoders

- For qubit rotation codes, one can distinguish the computational-basis codewords destructively by performing a Fock-state number measurement. If a Fock state $|n\rangle$ is measured, then one rounds to the nearest multiple of $N$ and infers the logical value from the parity of that multiple  ([arXiv:1901.08071](https://arxiv.org/abs/1901.08071)).
- One can distinguish states in the dual basis by performing phase estimation on $\mathrm{e}^{\mathrm{i} \theta \hat n}$. One then rounds the resulting $\theta$ to the nearest number $2\pi j / qN$ in order to determine which dual basis state $j \in \mathbb Z_q$ it came from  ([arXiv:1901.08071](https://arxiv.org/abs/1901.08071)).
- Autonomous QEC for $S=1$ codes  ([arXiv:2203.09234](https://arxiv.org/abs/2203.09234)).
- Decoder  ([arXiv:1901.08071](https://arxiv.org/abs/1901.08071)) based on measuring in the phase-state basis and using Knill error correction (a.k.a. telecorrection  ([arXiv:quant-ph/0601066](https://arxiv.org/abs/quant-ph/0601066))), which is based on teleportation  ([arXiv:quant-ph/0410199](https://arxiv.org/abs/quant-ph/0410199), [arXiv:quant-ph/0312190](https://arxiv.org/abs/quant-ph/0312190)).
- Performance under non-Markovian noise has been investigated  ([arXiv:2505.08670](https://arxiv.org/abs/2505.08670)).

## Encoders

- The optimal way to prepare codewords depends on the exact rotation code in question  ([arXiv:1901.08071](https://arxiv.org/abs/1901.08071)).

## Fault tolerance

- Decoder based on measuring in the phase-state basis and using Knill error correction  ([arXiv:1901.08071](https://arxiv.org/abs/1901.08071)) is fault-tolerant under circuit-level noise  ([arXiv:2406.04157](https://arxiv.org/abs/2406.04157)).

## Relations

- _parent_: [[concepts/qec/fock-state]] — Single-mode Fock-state codes are typically rotationally invariant.
- _parent_: [[concepts/qec/single-mode]]
- _cousin_: [[concepts/qec/quantum-random]] — Random bosonic rotation codes can outperform cat and binomial codes when loss rate is large relative to dephasing rate  ([arXiv:2311.16089](https://arxiv.org/abs/2311.16089)).
