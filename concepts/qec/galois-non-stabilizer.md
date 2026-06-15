---
type: concept
name: Galois-qudit USt code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Galois-qudit non-stabilizer code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/galois-into-galois
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/galois_non_stabilizer
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: galois_non_stabilizer
---

# Galois-qudit USt code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/galois_non_stabilizer) (`code_id: galois_non_stabilizer`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A Galois-qudit code whose codespace consists of a direct sum of a Galois-qudit stabilizer codespace and one or more of that stabilizer code's error spaces.

Given a subset $T$ of coset representatives of $\mathsf{N}(\mathsf{S})/\mathsf{S}$ of a Galois-qudit stabilizer code $((n,K))$ with codespace $\mathsf{C}$ and stabilizer group $\mathsf{S}$, one can construct the Galois-qudit USt with codespace
\begin{align}
  \mathsf{C}_{\text{USt}}=\bigoplus_{t\in T}t\mathsf{C}~.
\end{align}
The parameters of the USt are $((n,K|T|))$, where $|T|$ is the number of chosen coset representatives.
A Galois-qudit USt is *CSS-like* when the underlying stabilizer code is CSS and the coset representatives are chosen from the two classical codes underlying the CSS code.

Union stabilizer codes generalize stabilizer codes by modifying the original stabilizer code projection with elements of a subset $\mathsf{B}\subset\mathsf{S}$ called the *Fourier description*  ([arXiv:quant-ph/0210097](https://arxiv.org/abs/quant-ph/0210097)).
When $\mathsf{B}$ is a subgroup of $\mathsf{S}$, then the code reduces to an ordinary stabilizer code.

The $((n, \lceil\frac{q^n}{n(q^2-1)}\rceil,2))_q$ family of Galois-qudit non-stabilizer codes is constructed in Ref.  ([arXiv:quant-ph/0210097](https://arxiv.org/abs/quant-ph/0210097)).

(source: raw/error-correction-zoo.md)

## Relations

- _parent_: [[concepts/qec/galois-into-galois]]
- _cousin_: [`projective`](https://errorcorrectionzoo.org/c/projective) — Galois-qudit USt codes can be obtained from lines in projective space  ([arXiv:2107.11281](https://arxiv.org/abs/2107.11281)).
