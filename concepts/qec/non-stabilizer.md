---
type: concept
name: Union stabilizer (USt) code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Non-stabilizer code
- Quotient space quantum code (QSQC)
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/galois-non-stabilizer
- concepts/qec/qubit-css
- concepts/qec/qubits-into-qubits
- concepts/qec/qudit-non-stabilizer
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/non_stabilizer
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: non_stabilizer
---

# Union stabilizer (USt) code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/non_stabilizer) (`code_id: non_stabilizer`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A qubit code whose codespace consists of a direct sum of a qubit stabilizer codespace and one or more of that stabilizer code's error spaces.

Given a subset $T$ of coset representatives of $\mathsf{N}(\mathsf{S})/\mathsf{S}$ of a stabilizer code $⟦n,k⟧$ with codespace $\mathsf{C}$ and stabilizer group $\mathsf{S}$, one can construct the USt with codespace  ([doi:10.1017/CBO9781139034807.012](https://doi.org/10.1017/CBO9781139034807.012))
\begin{align}
  \mathsf{C}_{\text{USt}}=\bigoplus_{t\in T}t\mathsf{C}~.
\end{align}
The parameters of the USt are $((n,2^k |T|))$, where $|T|$ is the number of chosen coset representatives.
A USt is *CSS-like* when the underlying stabilizer code is CSS and the coset representatives are chosen from the two classical codes underlying the CSS code.

Union stabilizer codes constructed in Ref.  ([arXiv:quant-ph/0210097](https://arxiv.org/abs/quant-ph/0210097)) include the $((33, 155, 3))$ and $((15, 8, 3))$ codes.

(source: raw/error-correction-zoo.md)

## Protection

The distance does not exceed that of the original code $\mathsf{C}$ unless that codespace is 1D  ([arXiv:0912.3245](https://arxiv.org/abs/0912.3245)).
Distance bounds are calculated in Refs.  ([doi:10.1017/CBO9781139034807.012](https://doi.org/10.1017/CBO9781139034807.012), [arXiv:2311.07265](https://arxiv.org/abs/2311.07265)) using various formulations.
Since USt codes are equivalent to CWS codes via a single-qubit Clifford circuit, a USt code is degenerate if and only if it is impure  ([arXiv:0912.3245](https://arxiv.org/abs/0912.3245)).

## Decoders

- Error-detection algorithm  ([arXiv:0907.2038](https://arxiv.org/abs/0907.2038), [doi:10.1109/ISIT.2010.5513671](https://doi.org/10.1109/ISIT.2010.5513671)).

## Relations

- _parent_: [[concepts/qec/qubits-into-qubits]]
- _parent_: [[concepts/qec/qudit-non-stabilizer]] — Modular-qudit union stabilizer codes reduce to union stabilizer codes for $q=2$.
- _parent_: [[concepts/qec/galois-non-stabilizer]] — Galois-qudit union stabilizer codes reduce to union stabilizer codes for $q=2$.
- _cousin_: [[concepts/qec/qubit-css]] — An $⟦n,2k-n,d⟧$ CSS code can be converted to a $⟦n,k+k^{\prime}−n,\min(d,\left\lceil 3d^{\prime}/2\right\rceil )⟧$ code for particular $k^{\prime}$ and $d^{\prime}$ via \ref{topic:steane-enlargement}. This code can be treated as a union stabilizer code  ([arXiv:0801.2144](https://arxiv.org/abs/0801.2144)).

## Notes

- See Ref.  ([doi:10.1017/CBO9781139034807.012](https://doi.org/10.1017/CBO9781139034807.012)) for an overview of union stabilizer codes.
