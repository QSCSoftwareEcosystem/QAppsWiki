---
type: concept
name: Concatenated cat code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/fusion
- concepts/qec/lhz
- concepts/qec/oscillators-concatenated
- concepts/qec/qsc
- concepts/qec/qubit-css
- concepts/qec/qubit-golay
- concepts/qec/rotated-surface
- concepts/qec/steane
- concepts/qec/xzzx
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/cat_concatenated
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: cat_concatenated
---

# Concatenated cat code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/cat_concatenated) (`code_id: cat_concatenated`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A concatenated code obtained by encoding the physical qubits of an inner qubit code into cat-code states.
Most examples concatenate a qubit stabilizer code with the two-component cat code in its cat-state basis.

(source: raw/error-correction-zoo.md)

## Protection

The cat code can exponentially suppress one effective Pauli error channel with the size of its coherent states, so an inner qubit code such as a quantum repetition code can exploit a large noise bias while still ensuring good performance  ([arXiv:1904.09474](https://arxiv.org/abs/1904.09474), [arXiv:1905.00450](https://arxiv.org/abs/1905.00450), [arXiv:2009.10756](https://arxiv.org/abs/2009.10756), [arXiv:2212.11927](https://arxiv.org/abs/2212.11927)).

## Relations

- _parent_: [[concepts/qec/qsc]]
- _parent_: [[concepts/qec/oscillators-concatenated]]
- _cousin_: [[concepts/qec/qubit-css]] — Stabilizers of CSS codes concatenated with two-component cat codes in their coherent-state basis come directly from the CSS codes via the mapping $X \to (-1)^{\hat n}$ and $Z \to \hat a$  ([arXiv:2302.11593](https://arxiv.org/abs/2302.11593)). Stabilizers of CSS codes concatenated with two-component cat codes in their cat-state basis come directly from the CSS codes via the mapping $Z \to (-1)^{\hat n}$ and $X \to \hat a$. In both cases, one type of noise is handled actively via syndrome extraction and correction, while the other type is handled passively via stabilizing dissipation.
- _cousin_: [[concepts/qec/rotated-surface]] — Cat codes have been concatenated with rotated surface codes  ([arXiv:2012.04108](https://arxiv.org/abs/2012.04108)).
- _cousin_: [`ldpc`](https://errorcorrectionzoo.org/c/ldpc) — Cat codes have been concatenated with LDPC codes (treated as qubit stabilizer codes)  ([arXiv:2401.09541](https://arxiv.org/abs/2401.09541)).
- _cousin_: [[concepts/qec/lhz]] — LHZ parity-codes have been concatenated with cat codes  ([arXiv:2404.11332](https://arxiv.org/abs/2404.11332)).
- _cousin_: [[concepts/qec/steane]] — Two-component cat codes concatenated with Steane and Golay codes are estimated to be fault tolerant against photon loss noise with rate $\eta < 5\times 10^{-4}$ provided that $\alpha > 1.2$  ([arXiv:0707.0327](https://arxiv.org/abs/0707.0327)).
- _cousin_: [[concepts/qec/qubit-golay]] — Two-component cat codes concatenated with Steane and Golay codes are estimated to be fault tolerant against photon loss noise with rate $\eta < 5\times 10^{-4}$ provided that $\alpha > 1.2$  ([arXiv:0707.0327](https://arxiv.org/abs/0707.0327)).
- _cousin_: [[concepts/qec/xzzx]] — The four-component cat code can be concatenated with the XZZX code to yield a fusion-based computation scheme on a 2D lattice  ([arXiv:2508.03796](https://arxiv.org/abs/2508.03796)).
- _cousin_: [[concepts/qec/fusion]] — The four-component cat code can be concatenated with the XZZX code to yield a fusion-based computation scheme on a 2D lattice  ([arXiv:2508.03796](https://arxiv.org/abs/2508.03796)).
