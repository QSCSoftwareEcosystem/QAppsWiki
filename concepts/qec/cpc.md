---
type: concept
name: Coherent-parity-check (CPC) code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/qubit-stabilizer
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/cpc
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: cpc
---

# Coherent-parity-check (CPC) code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/cpc) (`code_id: cpc`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A qubit stabilizer code for which two binary linear codes are used to directly construct encoding and decoding circuits against $X$- and $Z$-type errors, respectively, via ZX calculus  ([doi:10.1007/978-3-540-70583-3_25](https://doi.org/10.1007/978-3-540-70583-3_25), [arXiv:0906.4725](https://arxiv.org/abs/0906.4725)).
CPC codes can be obtained from numerical search  ([arXiv:1709.01866](https://arxiv.org/abs/1709.01866)).

(source: raw/error-correction-zoo.md)

## Relations

- _parent_: [[concepts/qec/qubit-stabilizer]] — CPC codes are a type of stabilizer code. A teleported version of the CPC construction, the Clifford noise reduction (CliNR) scheme, can reduce noise in Clifford circuits with Pauli measurements with at most a three-fold overhead in the number of qubits and gates  ([arXiv:2407.06583](https://arxiv.org/abs/2407.06583), [arXiv:2504.13356](https://arxiv.org/abs/2504.13356)). There is a simple formula for the probability that a Clifford circuit contains a logical error  ([arXiv:2009.07752](https://arxiv.org/abs/2009.07752)).
- _cousin_: [`binary_linear`](https://errorcorrectionzoo.org/c/binary_linear) — The CPC Construction uses two binary linear codes.
- _cousin_: [`hamming`](https://errorcorrectionzoo.org/c/hamming) — *Tripartite CPC codes* are constructed from Hamming codes via the CPC construction  ([arXiv:1611.08012](https://arxiv.org/abs/1611.08012)).
