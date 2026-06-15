---
type: concept
name: Self-complementary qubit code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/ampdamp
- concepts/qec/small-distance-quantum
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/self_complementary
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: self_complementary
---

# Self-complementary qubit code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/self_complementary) (`code_id: self_complementary`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A qubit code which admits a basis of codewords of the form $|c\rangle+|\overline{c}\rangle$, where $c$ is a bitstring and $\overline{c}$ is its negation a.k.a. complement. 
Their codewords generalize the two-qubit Bell states and three-qubit GHZ states and are often called *(qubit) cat states* or *poor-man's GHZ states*.
Such codes were originally pointed out to perform well against AD noise  ([arXiv:0712.2586](https://arxiv.org/abs/0712.2586)).

(source: raw/error-correction-zoo.md)

## Protection

Self-complementary codes automatically protect against a single $Z$ error and lie in the $+1$-eigenspace of the all-$X$ Pauli string  ([arXiv:quant-ph/0701065](https://arxiv.org/abs/quant-ph/0701065)). 
They are at most distance-two since the minimal number of computational basis states in a logical state is two  ([arXiv:2405.01332](https://arxiv.org/abs/2405.01332)).
Codes consisting of computational basis states whose bitstrings are sufficiently spaced apart correct at least one AD error  ([arXiv:0712.2586](https://arxiv.org/abs/0712.2586)) ([arXiv:0907.5149](https://arxiv.org/abs/0907.5149)).
Self-complementary stabilizer codes are qubit CSS codes with a single $X$-type generator given by the all-$X$ string.

## Relations

- _parent_: [[concepts/qec/small-distance-quantum]] — Self-complementary quantum codes are at most distance-two since the minimal number of computational basis states in a logical state is two  ([arXiv:2405.01332](https://arxiv.org/abs/2405.01332)).
- _parent_: [[concepts/qec/ampdamp]] — Self-complementary quantum codes consisting of computational basis states whose bitstrings are sufficiently spaced apart correct at least one AD error  ([arXiv:0712.2586](https://arxiv.org/abs/0712.2586)) ([arXiv:0907.5149](https://arxiv.org/abs/0907.5149)).
- _cousin_: [`bits_into_bits`](https://errorcorrectionzoo.org/c/bits_into_bits) — A binary code is called *self-complementary* if, for each codeword $c$, its negation $\overline{c}$ is also a codeword  ([doi:10.3390/math11244950](https://doi.org/10.3390/math11244950)). Any self-complementary $(n,K,d > 1)$ classical code yields an $((n,K/2,2))$ self-complementary quantum code whose quantum codewords are superpositions of the classical codewords and their complements  ([arXiv:quant-ph/0701065](https://arxiv.org/abs/quant-ph/0701065)). Self-complementary classical code parameters are governed by the Gray-Rankin bound  ([doi:10.1109/TIT.1962.1057721](https://doi.org/10.1109/TIT.1962.1057721)).
