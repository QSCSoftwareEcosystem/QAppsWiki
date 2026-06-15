---
type: concept
name: XZZX surface code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Wen plaquette model
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/chamon
- concepts/qec/cluster-state
- concepts/qec/fracton
- concepts/qec/heavy-hex
- concepts/qec/quantum-double-abelian
- concepts/qec/rotated-surface
- concepts/qec/surface
- concepts/qec/twist-defect-surface
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/xzzx
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: xzzx
---

# XZZX surface code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/xzzx) (`code_id: xzzx`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A variant of the rotated surface code whose generators are $XZZX$ Pauli strings associated, clockwise, to the vertices of each face of a two-dimensional lattice (with a qubit located at each vertex of the tessellation).

*XZZX toric code* often either refers to the construction on the two-dimensional torus or is an alternative name for the general construction.
*Twisted XZZX toric code* refers to the construction on a torus with twisted (a.k.a. shifted) boundary conditions; these need not be equivalent to twisted toric codes because they can be non-CSS.
The construction on surfaces with boundaries is often called the
*XZZX planar code*.
On a closed lattice, the Wen plaquette realization of the XZZX toric code has the same $\mathbb{Z}_2$ topological order as the toric code, and translation by one lattice unit exchanges the $e$ and $m$ anyons  ([arXiv:1605.01640](https://arxiv.org/abs/1605.01640)).

Stabilizer generators for this code are shown in \ref{figure:xzzx-operators}.

(source: raw/error-correction-zoo.md)

## Protection

As a stabilizer code, $⟦n=O(d^2), k=O(1), d⟧$.

## Decoders

- MWPM decoder, which can be used for $X$ and $Z$ noise. For $Y$ noise, a variant of the matching decoder could be used like it is used for the XY code in Ref.  ([arXiv:1907.02554](https://arxiv.org/abs/1907.02554)). Decoding complexity scales as order $O(n^3)$ because the code is non-CSS  ([arXiv:1907.02554](https://arxiv.org/abs/1907.02554)) ([arXiv:2202.06612](https://arxiv.org/abs/2202.06612)).

## Code capacity threshold

- For large but finite $X$- or $Z$-biased noise, the code's thresholds exceed the zero-rate hashing bound.  The difference of the threshold from the hashing bound exceeds $2.9\%$ at a $Z$ or $X$ bias of 300.
- $50\%$ threshold for noise infinitely biased towards $X$ or $Y$ or $Z$ errors using a maximum-likelihood decoder.
- Depolarizing noise: $18.7(1)\%$ under tensor-network decoder  ([arXiv:1708.08474](https://arxiv.org/abs/1708.08474)) and $17.5\%$ under AMBP4  ([arXiv:2104.13659](https://arxiv.org/abs/2104.13659)).

## Threshold

- $\approx 4.5\%$ using minimum-weight perfect matching decoder for depolarizing noise (bias $\eta=0.5$); $\approx 10\%$ for infinite $Z$ bias.
- $4.15\%$ when $98\%$ of depolarizing errors are converted into erasure errors with union-find decoder on a planar code, vs. $0.937\%$ for pure depolarizing noise. The dominant source of noise in neutral atom arrays is spontaneous decay into detectable energy levels outside of the computational subspace. Since that decay occurs in a Rydberg level that is accessible from only one of the hyperfine states used for storage, the resulting channel is biased erasure  ([arXiv:2201.03540](https://arxiv.org/abs/2201.03540)).
- $0.817\%$ and $0.940\%$ with minimum-weight perfect matching and belief-matching decoder, respectively, for biased circuit-level noise  ([arXiv:2203.04948](https://arxiv.org/abs/2203.04948)).

## Realizations

- Superconducting circuits: Distance-five 25-qubit code implemented on a superconducting quantum processor by Google Quantum AI  ([arXiv:2207.06431](https://arxiv.org/abs/2207.06431)).
This code outperformed the average of several instances of the smaller distance-three nine-qubit $XZZX$ variant of the surface-17 code realized on the same device, both in terms of logical error probability over 25 cycles and in terms of logical error per cycle.
This increase in error-correcting capabilities while using more physical qubits supports the notion of an error threshold.
Braiding of defects has been demonstrated for the distance-five code  ([arXiv:2210.10255](https://arxiv.org/abs/2210.10255)). Leakage errors have been handled in a separate work in a distance-three code  ([arXiv:2211.04728](https://arxiv.org/abs/2211.04728)).
Google Quantum AI follow-up experiment realizing distance-5 and distance-7 codes with 100 rounds of correction using the Libra and transformer-based decoders. The logical error rate is suppressed by a factor of $\approx 2$, demonstrating beyond-break-even error correction with a block quantum code  ([arXiv:2408.13687](https://arxiv.org/abs/2408.13687)).
Magic-state cultivation was demonstrated on a device by Google Quantum AI by code switching between a distance-three 6.6.6 color code and distance-five $XZZX$ surface code and decoding with the Tesseract decoder  ([arXiv:2512.13908](https://arxiv.org/abs/2512.13908)).
- Neutral atom arrays: Lukin group. Transversal CNOT gates performed on distance $3$, $5$, and $7$ codes  ([arXiv:2312.03982](https://arxiv.org/abs/2312.03982)). Below-threshold performance on distance $3$ and $5$ codes with multiple rounds of syndrome extraction and error correction  ([arXiv:2506.20661](https://arxiv.org/abs/2506.20661)).

## Relations

- _parent_: [[concepts/qec/twist-defect-surface]] — XZZX toric and planar codes can be treated in the general twist-defect surface code formalism  ([arXiv:2101.09349](https://arxiv.org/abs/2101.09349)).
- _cousin_: [[concepts/qec/quantum-double-abelian]] — The XZZX surface code is an example of $\mathbb{Z}_2$ topological order as manifest in the Wen plaquette model  ([arXiv:quant-ph/0205004](https://arxiv.org/abs/quant-ph/0205004)).
- _cousin_: [[concepts/qec/rotated-surface]] — The XZZX code is obtained from the rotated surface code by applying Hadamard gates on a subset of qubits such that $XXXX$ and $ZZZZ$ generators are both mapped to $XZXZ$. Both rotated and XZZX codes offer improved performance over the original surface code for biased noise  ([arXiv:2312.17057](https://arxiv.org/abs/2312.17057)).
- _cousin_: [[concepts/qec/chamon]] — The Chamon model code can be obtained from an XYZ product of three repetition codes ; see  ([arXiv:2011.09746](https://arxiv.org/abs/2011.09746)). Using only two repetition codes in the analogous 2D construction yields the XZZX code, making it a 2D analogue of the Chamon code  ([arXiv:2011.09746](https://arxiv.org/abs/2011.09746)).
- _cousin_: [`repetition`](https://errorcorrectionzoo.org/c/repetition) — The Chamon model code can be obtained from an XYZ product of three repetition codes ; see  ([arXiv:2011.09746](https://arxiv.org/abs/2011.09746)). Using only two repetition codes in the analogous 2D construction yields the XZZX code, making it a 2D analogue of the Chamon code  ([arXiv:2011.09746](https://arxiv.org/abs/2011.09746)).
- _cousin_: [[concepts/qec/fracton]] — Subsystem symmetries play a role in finite-bias decoders for both XZZX and fracton codes  ([arXiv:1901.08061](https://arxiv.org/abs/1901.08061)). The XZZX surface code resembles a Type-I fracton code with lineons in the limit of infinite noise bias  ([arXiv:2203.16534](https://arxiv.org/abs/2203.16534)).
- _cousin_: [[concepts/qec/heavy-hex]] — XZZX surface code can be adapted for a heavy-hexagonal point set  ([arXiv:2211.14038](https://arxiv.org/abs/2211.14038)).
- _cousin_: [[concepts/qec/cluster-state]] — XZZX surface code can be foliated for a noise-bias preserving MBQC  ([arXiv:2201.10566](https://arxiv.org/abs/2201.10566)) or FBQC  ([arXiv:2303.16122](https://arxiv.org/abs/2303.16122)) protocol; see also  ([arXiv:1308.4776](https://arxiv.org/abs/1308.4776)).
- _cousin_: [[concepts/qec/surface]] — The XZZX surface code on a square lattice with non-twisted periodic boundary conditions is obtained from a surface code by applying Hadamard gates on a subset of qubits such that $XXXX$ and $ZZZZ$ generators are both mapped to $XZXZ$. While this code is equivalent to a CSS surface code with the same distance, other properties like noise-bias performance can differ significantly. Twisted XZZX surface codes are generally not equivalent to CSS surface codes via a single-qubit Clifford circuit and permutation.

## Notes

- A single $X$ or $Z$ error gives rise to two nearby defects, which can be viewed as endpoints of a string. That way, multiple $Z$ errors can be decomposed into a combination of diagonal strings.
- Originally formulated as an example of $\mathbb{Z}_2$ topological order in the Wen plaquette model  ([arXiv:quant-ph/0205004](https://arxiv.org/abs/quant-ph/0205004)).
- Popular summary of the Google Quantum AI above-threshold result in [Quanta Magazine](https://www.quantamagazine.org/quantum-computers-cross-critical-error-threshold-20241209/).
