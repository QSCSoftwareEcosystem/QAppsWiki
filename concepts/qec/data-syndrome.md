---
type: concept
name: Quantum data-syndrome (QDS) code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/galois-quad-residue
- concepts/qec/quantum-convolutional
- concepts/qec/quantum-hamming-css
- concepts/qec/quantum-mds
- concepts/qec/quantum-perfect
- concepts/qec/qubit-stabilizer
- concepts/qec/qubit-subsystem-stabilizer
- concepts/qec/single-shot
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/data_syndrome
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: data_syndrome
---

# Quantum data-syndrome (QDS) code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/data_syndrome) (`code_id: data_syndrome`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Stabilizer code designed to correct both data qubit errors and syndrome measurement errors simultaneously due to extra redundancy in its stabilizer generators.

The redundancy can be added to any $⟦n,n-m⟧$ qubit stabilizer code by expanding its stabilizer generator matrix $H$ as
\begin{align}
  H_{DS}=\begin{pmatrix}H & I_{m} & 0\\
  0 & A^{T} & I_{r}
  \end{pmatrix}~,
\end{align}
where the redundancy is provided by the underlying $[m+r,m]$ *syndrome measurement code* with generator matrix $G= (I_m|A)$  ([arXiv:1907.01393](https://arxiv.org/abs/1907.01393)).

(source: raw/error-correction-zoo.md)

## Protection

Protects against both physical qubit and syndrome measurement errors.
An $⟦n,k,d:r⟧$ QDS code corrects any combination of $t_{\mathrm{D}}$ data-qubit errors and $t_{\mathrm{S}}$ syndrome-bit errors whenever $t_{\mathrm{D}}+t_{\mathrm{S}}<d/2$, and its distance cannot exceed that of the underlying stabilizer code  ([arXiv:1907.01393](https://arxiv.org/abs/1907.01393)).

Random QDS codes with $r\leq n-k$ can attain the stabilizer Gilbert-Varshamov bound  ([arXiv:1907.01393](https://arxiv.org/abs/1907.01393)).
Quantum Singleton bounds, quantum Hamming bounds, and quantum MacWilliams identities can be extended to QDS codes.
Single-error-correcting QDS codes stemming from impure stabilizer codes must satisfy a variant of the quantum Hamming bound  ([arXiv:2302.01527](https://arxiv.org/abs/2302.01527)).

## Decoders

- Syndrome errors are decoded using redundant stabilizer measurements.
- Syndrome-measurement codes can outperform repeated syndrome extraction; for the Steane code, a $[15,3]$ syndrome-measurement code uses the same 15 measurements as five-fold repetition of three syndrome bits while achieving lower syndrome-decoding error  ([arXiv:1907.01393](https://arxiv.org/abs/1907.01393)).

## General gates

- Fault-tolerant flag-based non-transversal logical gates  ([arXiv:2510.08402](https://arxiv.org/abs/2510.08402)).

## Fault tolerance

- Shor error correction can be recast as a QDS code whose underlying matrix $A$ is the identity matrix $I_m$ repeated $\ell$ times  ([arXiv:1907.01393](https://arxiv.org/abs/1907.01393)).
- Fault-tolerant flag-based non-transversal logical gates  ([arXiv:2510.08402](https://arxiv.org/abs/2510.08402)).

## Relations

- _parent_: [[concepts/qec/qubit-stabilizer]] — QDS codes are stabilizer codes whose stabilizer generators encode extra redundancy (via a linear binary code) so as to protect from syndrome measurement errors.
- _cousin_: [[concepts/qec/quantum-hamming-css]] — Because every stabilizer generator has the same weight $2^{r-1}$, quantum Hamming codes admit QDS extensions based on good binary syndrome-measurement codes  ([arXiv:1907.01393](https://arxiv.org/abs/1907.01393)).
- _cousin_: [[concepts/qec/quantum-mds]] — The quantum Singleton bound can be extended to QDS codes  ([arXiv:1907.01393](https://arxiv.org/abs/1907.01393)).
- _cousin_: [[concepts/qec/quantum-perfect]] — The quantum Hamming bound can be extended to QDS codes  ([arXiv:1907.01393](https://arxiv.org/abs/1907.01393)).
- _cousin_: [`binary_linear`](https://errorcorrectionzoo.org/c/binary_linear) — The QDS code construction employs a particular binary linear code to provide protection against syndrome measurement errors.
- _cousin_: [[concepts/qec/quantum-convolutional]] — The QDS code framework has been extended to quantum convolutional codes  ([arXiv:1902.07395](https://arxiv.org/abs/1902.07395)).
- _cousin_: [[concepts/qec/single-shot]] — QDS codes are closely related to single-shot codes because both use redundant syndrome information to suppress measurement errors in a single round of syndrome extraction  ([arXiv:1805.09271](https://arxiv.org/abs/1805.09271)).
- _cousin_: [`narrow_sense_q-ary_bch`](https://errorcorrectionzoo.org/c/narrow_sense_q-ary_bch) — Primitive narrow-sense BCH codes can be used as the syndrome measurement codes of a QDS code  ([arXiv:2311.16044](https://arxiv.org/abs/2311.16044)). This construction requires fewer measurements than a previous general construction  ([arXiv:1409.2559](https://arxiv.org/abs/1409.2559)).
- _cousin_: [[concepts/qec/qubit-subsystem-stabilizer]] — The DS construction can be extended to subsystem qubit stabilizer codes  ([arXiv:2302.01527](https://arxiv.org/abs/2302.01527)).
- _cousin_: [[concepts/qec/galois-quad-residue]] — CSS QDS codes can be constructed from dual-containing cyclic codes without reducing distance; for $p=8j-1$, quantum QR codes yield $⟦p,1,d:r⟧$ QDS codes with $r\leq p+1$  ([arXiv:1907.01393](https://arxiv.org/abs/1907.01393)).

## Notes

- QDS codes can be used to estimate physical Pauli noise up to their pure distance  ([arXiv:2107.14252](https://arxiv.org/abs/2107.14252)), and logical Pauli noise for any correctable physical noise  ([arXiv:2209.09267](https://arxiv.org/abs/2209.09267)).
