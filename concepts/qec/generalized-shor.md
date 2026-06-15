---
type: concept
name: Generalized Shor code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/qubit-css
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/generalized_shor
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: generalized_shor
---

# Generalized Shor code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/generalized_shor) (`code_id: generalized_shor`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Qubit CSS code constructed by concatenating two classical codes in a way that generalizes the Shor and quantum parity codes.

This $⟦n_1n_2,k_1k_2,\min(d_1,d_2)⟧$ code can be defined  ([arXiv:0903.0566](https://arxiv.org/abs/0903.0566)) via the CSS construction applied to two binary linear codes, $C_X$ and $C_Z$, satisfying $C_X^{\perp}\subset C_Z$.
These codes are in turn constructed from two more binary linear codes, $C_1 = [n_1, k_1, d_1]$ and $C_2 = [n_2, k_2, d_2]$, with parity-check matrices $H_1$ and $H_2$ and generator matrices $G_1$ and $G_2$, respectively.
The parity-check matrices of $C_X$ and $C_Z$ are then
\begin{align}
\begin{split}
H_X &= H_1 \otimes I_{n_2}\\
H_Z &= G_1 \otimes H_2~.
\end{split}
\end{align}

Based on the above construction, the Hilbert space on $n_1n_2$ qubits can be decomposed as a direct sum of tensor products of Hilbert spaces of lower dimensions, as outlined in  ([arXiv:quant-ph/0506023](https://arxiv.org/abs/quant-ph/0506023)).

(source: raw/error-correction-zoo.md)

## Protection

Has distance $d=\min(d_1,d_2)$.

## Decoders

- Efficient decoder  ([doi:10.1109/ISIT.2009.5205650](https://doi.org/10.1109/ISIT.2009.5205650)).

## Realizations

- The $⟦m^2,1,m⟧$ codes for $m\leq 7$ have been realized in trapped-ion quantum devices  ([arXiv:2104.01205](https://arxiv.org/abs/2104.01205)).

## Relations

- _parent_: [[concepts/qec/qubit-css]]

## Notes

- Non-deterministic linear-optical encoding  ([arXiv:quant-ph/0501184](https://arxiv.org/abs/quant-ph/0501184)) whose success probability $P_{E}$ is determined by the efficiency $\eta$ of the photonic encoding circuit. A threshold $\eta > 0.82 $ exists for the efficiency, above which $P_{E}\to 1$ as $m_1\to\infty$ for a particular $m_2$.
- Studied in the context of error-corrected quantum repeaters  ([arXiv:1310.5291](https://arxiv.org/abs/1310.5291)).
