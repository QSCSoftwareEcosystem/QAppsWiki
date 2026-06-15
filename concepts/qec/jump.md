---
type: concept
name: Jump code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/ampdamp
- concepts/qec/chuang-leung-yamamoto
- concepts/qec/constant-excitation
- concepts/qec/iceberg
- concepts/qec/qubits-into-qubits
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/jump
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: jump
---

# Jump code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/jump) (`code_id: jump`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A CE code designed to detect and correct AD errors.
An $((n,K))$ jump code is denoted as $((n,K,t))_w$ (which conflicts with modular-qudit notation), where $t$ is the maximum number of qubits that can be corrected after each one has undergone a jump error $|0\rangle\langle 1|$, and where each codeword is a uniform superposition of qubit basis states with Hamming weight $w$.

(source: raw/error-correction-zoo.md)

## Protection

Various code bounds, including an upper bound on $K$ given the other parameters, are provided in Ref.  ([doi:10.1023/A:1024188005329](https://doi.org/10.1023/A:1024188005329)).
For example, one can apply bit flips to all qubits of an $((n,K,t))_w$ jump code to obtain an $((n,K,t))_{n-w}$ jump code.

## Rate

An infinite family of jump codes asymptotically attains an upper bound on $K$  ([doi:10.1023/A:1024188005329](https://doi.org/10.1023/A:1024188005329)).

## General gates

- Two-qubit entangling gate  ([arXiv:quant-ph/0506037](https://arxiv.org/abs/quant-ph/0506037)).

## Relations

- _parent_: [[concepts/qec/qubits-into-qubits]]
- _parent_: [[concepts/qec/ampdamp]] — Jump codes are designed to protect against qubit AD noise.
- _parent_: [[concepts/qec/constant-excitation]]
- _cousin_: [[concepts/qec/chuang-leung-yamamoto]] — Jump codes can be thought of as qubit analogues of uniform CLY codes.
- _cousin_: [[concepts/qec/iceberg]] — The subcode of the $⟦2m,2m-2,2⟧$ error-detecting code consisting of codewords labeled by weight-$m$ bitstrings is a $((2m,\frac{1}{2}{2m \choose m},1))_{m}$ optimal jump code  ([arXiv:quant-ph/0208140](https://arxiv.org/abs/quant-ph/0208140)) ([doi:10.1023/A:1024188005329](https://doi.org/10.1023/A:1024188005329)).
- _cousin_: [`combinatorial_design`](https://errorcorrectionzoo.org/c/combinatorial_design) — Certain types of combinatorial designs can be used to obtain jump codes  ([arXiv:quant-ph/0208140](https://arxiv.org/abs/quant-ph/0208140), [doi:10.1023/A:1024188005329](https://doi.org/10.1023/A:1024188005329), [doi:10.1007/s10623-013-9829-0](https://doi.org/10.1007/s10623-013-9829-0)).
- _cousin_: [`self_dual`](https://errorcorrectionzoo.org/c/self_dual) — Iso-dual codes can be used to construct jump codes  ([doi:10.1023/A:1024188005329](https://doi.org/10.1023/A:1024188005329)).

## Notes

- Survey of jump codes .
