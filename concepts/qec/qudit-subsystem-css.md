---
type: concept
name: Subsystem modular-qudit CSS code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/qudit-css
- concepts/qec/qudit-subsystem-stabilizer
- concepts/qec/subsystem-css
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/qudit_subsystem_css
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: qudit_subsystem_css
---

# Subsystem modular-qudit CSS code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/qudit_subsystem_css) (`code_id: qudit_subsystem_css`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Modular-qudit subsystem stabilizer code which admits a set of gauge-group generators which consist of either all-$Z$ or all-$X$ modular-qudit Pauli strings.
This ensures that the code's stabilizer group is also CSS.

The gauge group generators can be expressed as a matrix using the symplectic reprensetation. This matrix is of the form
\begin{align}
H=\begin{pmatrix}0 & H_{Z}\\
H_{X} & 0
\end{pmatrix}~.
\label{eq:parity}
\end{align}
The two matrix blocks, $H_{Z}$ and $H_X$, correspond to the parity-check matrices of two $q$-ary linear codes, an $[n,k_X,d_X]_q$ code $C_X$ and $[n,k_Z,d_Z]_q$ code $C_Z$, respectively.
For prime-dimensional qudits, code parameters and code basis states have been expressed in terms of only data associated with these two classical codes  ([arXiv:quant-ph/0610153](https://arxiv.org/abs/quant-ph/0610153), [arXiv:2311.18003](https://arxiv.org/abs/2311.18003)).

\begin{defterm}{Symplectic doubling}
\label{topic:symplectic-doubling}
Any $⟦n,k,r,d⟧_{\mathbb{Z}_q}$ subsystem stabilizer code can be mapped onto a $⟦2n,2k,2r,\geq d⟧_{\mathbb{Z}_q}$ subsystem CSS code, with the mapping preserving geometric locality of a code up to a constant factor  ([arXiv:2311.18003](https://arxiv.org/abs/2311.18003)) (see also  ([arXiv:1004.3791](https://arxiv.org/abs/1004.3791)) ([arXiv:1212.6703](https://arxiv.org/abs/1212.6703))).
In the modular symplectic representation, the gauge-group generator matrix of the former is mapped into that of latter as follows,
\begin{align}
  \begin{pmatrix}G_{X} & G_{Z}\end{pmatrix}
  \to
  \begin{pmatrix}
  0     &     0 & G_{Z} & -G_{X}\\
  G_{X} & G_{Z} &     0 &      0
  \end{pmatrix}~,
\end{align}
where the first two columns of the latter matrix correspond to the $X$-type part of the gauge-group generator matrix of the output subsystem CSS code.
In the case of a stabilizer code, the stabilizer generator matrix is mapped instead to yield a two-block CSS code (see  ([arXiv:1212.6703](https://arxiv.org/abs/1212.6703)) for the case of qubit stabilizer codes).
For geometrically local 2D stabilizer codes with twist defects, this mapping yields a twisted double cover of the underlying qudit geometry  ([arXiv:2406.09951](https://arxiv.org/abs/2406.09951)).
\end{defterm}

(source: raw/error-correction-zoo.md)

## Decoders

- Steane-type decoder utilizing data from the underlying classical codes  ([arXiv:2311.18003](https://arxiv.org/abs/2311.18003)).

## Relations

- _parent_: [[concepts/qec/qudit-subsystem-stabilizer]] — Subsystem modular-qudit CSS codes are subsystem modular-qudit stabilizer codes whose gauge groups admit a generating set of pure-$X$ and pure-$Z$ Pauli strings. Any $⟦n,k,r,d⟧_{\mathbb{Z}_q}$ subsystem stabilizer code can be mapped onto a $⟦2n,2k,2r,\geq d⟧_{\mathbb{Z}_q}$ subsystem CSS code via symplectic doubling, which preserves geometric locality of a code up to a constant factor. Every subsystem prime-qudit stabilizer code can be constructed from two nested subsystem prime-qudit CSS codes satisfying certain constraints  ([arXiv:2311.18003](https://arxiv.org/abs/2311.18003)).
- _parent_: [[concepts/qec/subsystem-css]]
- _cousin_: [[concepts/qec/qudit-css]] — Subsystem modular-qudit CSS codes reduce to (subspace) modular-qudit CSS codes when there is no gauge subsystem.
