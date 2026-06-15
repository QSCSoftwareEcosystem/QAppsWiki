---
type: concept
name: Hermitian Galois-qudit code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- $\mathbb{F}_{q^2}$-linear stabilizer code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/galois-subsystem-stabilizer
- concepts/qec/galois-true-stabilizer
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/stabilizer_over_gfqsq
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: stabilizer_over_gfqsq
---

# Hermitian Galois-qudit code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/stabilizer_over_gfqsq) (`code_id: stabilizer_over_gfqsq`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

An $⟦n,k,d⟧_q$ true Galois-qudit stabilizer code constructed from a Hermitian self-orthogonal linear code over $\mathbb{F}_{q^2}$ using the one-to-one correspondence between the Galois-qudit Pauli matrices and elements of the Galois field $\mathbb{F}_{q^2}$.

Galois-qudit stabilizer codes are in one-to-one correspondence with trace-alternating self-orthogonal additive codes of length $n$ over $\mathbb{F}_{q^2}$ via the $\mathbb{F_{q^2}$ representation}.
Hermitian self-orthogonal linear codes over $\mathbb{F}_{q^2}$ are automatically trace-alternating self-orthogonal, and applying this mapping to such codes yields Hermitian codes  ([arXiv:quant-ph/0508070](https://arxiv.org/abs/quant-ph/0508070)).

More generally, a trace-alternating self-orthogonal additive code $C \subseteq \mathbb{F}_{q^2}^n$ of size $q^r$ yields an $⟦n,n-r⟧_q$ true stabilizer code  ([doi:10.1109/18.959288](https://doi.org/10.1109/18.959288)).
When $C$ is Hermitian self-orthogonal and $\mathbb{F}_{q^2}$-linear of parameters $[n,k]_{q^2}$, the construction specializes to a Hermitian $⟦n,n-2k⟧_q$ true stabilizer code; this is called the *Hermitian Galois-qudit construction*  ([arXiv:quant-ph/0508070](https://arxiv.org/abs/quant-ph/0508070)).
The Hermitian construction was first proven via the Galois symplectic representation (showing self-orthogonality under the trace-symplectic inner product; see Ref.  ([doi:10.1109/18.959288](https://doi.org/10.1109/18.959288)), Corr. 1).
There is an isomorphism between the Galois-symplectic and $\mathbb{F_{q^2}$ representations} .

It has also been extended to $q^{2m}$-ary Hermitian self-orthogonal linear codes  ([arXiv:2012.11998](https://arxiv.org/abs/2012.11998)), and similar constructions were formulated in Ref.  ([arXiv:1002.4088](https://arxiv.org/abs/1002.4088)).
*Quantum construction X* , related to (classical) Construction X and Construction XX, allows for the use of nearly self-orthogonal codes  ([doi:10.1007/s10623-014-9934-8](https://doi.org/10.1007/s10623-014-9934-8)),arxiv:2405.15057}; see Ref.  ([arXiv:2011.06996](https://arxiv.org/abs/2011.06996)) for a review.

(source: raw/error-correction-zoo.md)

## Protection

For a trace-alternating self-orthogonal additive code $C \subseteq \mathbb{F}_{q^2}^n$, the resulting true stabilizer code has distance
\begin{align}
d=\min\{\operatorname{wt}(v):v \in C^{\perp}\setminus C\}~,
\end{align}
where $\perp$ denotes duality under the trace-alternating inner product  ([doi:10.1109/18.959288](https://doi.org/10.1109/18.959288)).
If $C$ is Hermitian self-orthogonal and $\mathbb{F}_{q^2}$-linear, then
\begin{align}
d=\min\{\operatorname{wt}(v):v \in C^{\perp_h}\setminus C\}~,
\end{align}
so the code distance is bounded below by the Hermitian dual distance of $C$  ([arXiv:quant-ph/0508070](https://arxiv.org/abs/quant-ph/0508070)).

## Relations

- _parent_: [[concepts/qec/galois-true-stabilizer]] — Hermitian codes are true stabilizer codes because they are based on Hermitian self-orthogonal linear (as opposed to additive) codes over $\mathbb{F}_{q^2}$.
- _cousin_: [`dual`](https://errorcorrectionzoo.org/c/dual) — Hermitian codes are constructed from Hermitian self-orthogonal linear codes over $\mathbb{F}_{q^2}$ via the $\mathbb{F_{q^2}$ representation}.
- _cousin_: [`matrix_product`](https://errorcorrectionzoo.org/c/matrix_product) — Hermitian self-orthogonal matrix-product codes over $\mathbb{F}_{q^2}$ can be used to construct quantum codes via the Hermitian construction  ([doi:10.1007/s11128-020-02921-0](https://doi.org/10.1007/s11128-020-02921-0), [arXiv:1604.05823](https://arxiv.org/abs/1604.05823)).
- _cousin_: [[concepts/qec/galois-subsystem-stabilizer]] — The Hermitian construction has been extended to subsystem Galois-qudit stabilizer codes  ([arXiv:quant-ph/0610153](https://arxiv.org/abs/quant-ph/0610153)).
