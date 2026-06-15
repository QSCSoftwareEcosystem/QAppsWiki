---
type: concept
name: Covariant block quantum code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Equivariant block quantum code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/approximate-qecc
- concepts/qec/block-quantum
- concepts/qec/eth
- concepts/qec/quantum-random
- concepts/qec/quantum-reed-muller
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/covariant
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: covariant
---

# Covariant block quantum code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/covariant) (`code_id: covariant`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A block code on $n$ subsystems that admits a group $G$ of transversal gates. The group has to be finite for finite-dimensional codes due to the Eastin-Knill theorem.
Continuous-$G$ covariant codes, necessarily infinite-dimensional, are relevant to error correction of quantum reference frames  ([arXiv:1709.04471](https://arxiv.org/abs/1709.04471)) and error-corrected parameter estimation.

Denoting the code's encoding map as $U$, covariance is equivalent to
\begin{align}
  \left(\bigotimes_{j=1}^{n}V_{j}\left(g\right)\right)U=UV_{L}\left(g\right)\quad\quad\forall g\in G\,,
\end{align}
where $V_j(g)$ is a unitary representation of $g$ acting on the $j$ subsystem, and $V_L$ is a unitary representation acting on the unencoded logical information.
In this way, covariant encoding maps are equivariant (i.e., commute) with group actions on the logical and physical spaces.

Almost always, the physical representation is defined to be the transversal one (with respect to some tensor-product decomposition), but can reduce to any representation when the code is a subspace of a larger space that is not expressed as a tensor product ($n=1$). More generally, a code is sometimes said to be *time-covariant* if it admits a continuous-parameter $U(1)$ family of gates, not necessarily transversal  ([arXiv:2207.13707](https://arxiv.org/abs/2207.13707)).

(source: raw/error-correction-zoo.md)

## Protection

Finite-dimensional codes correcting a single-subsystem erasure and admitting a continuous-parameter family of transversal gates (assuming $n>1$) cannot exist in finite
dimensions due to the Eastin-Knill theorem. As a result, there is generally a tradeoff between covariance and error correction.

Exact error-correcting $G$-covariant codes can exist in infinite dimensions, but their codewords are non-normalizable, meaning that approximate constructions have to be considered that are only approximately error correcting.
On the other hand, there exist exact error-correcting codes in finite dimensions that are approximately covariant  ([arXiv:2111.06360](https://arxiv.org/abs/2111.06360), [arXiv:2111.06355](https://arxiv.org/abs/2111.06355)).
Various bounds quantify the covariance-performance tradeoff  ([arXiv:1902.07714](https://arxiv.org/abs/1902.07714), [arXiv:2005.11918](https://arxiv.org/abs/2005.11918), [arXiv:2004.11893](https://arxiv.org/abs/2004.11893), [arXiv:2111.06360](https://arxiv.org/abs/2111.06360), [arXiv:2111.06355](https://arxiv.org/abs/2111.06355), [arXiv:2410.07045](https://arxiv.org/abs/2410.07045), [arXiv:2505.00427](https://arxiv.org/abs/2505.00427), [arXiv:2510.04453](https://arxiv.org/abs/2510.04453)).
In particular, an approximate Eastin-Knill theorem implies that an $SU(d_{L})$-covariant code satisfies $\epsilon_{\mathrm{worst}}\gtrsim [2n \max_{i}\ln d_{i}]^{-1}$, so for fixed $n$ the local subsystem dimensions must grow exponentially in $1/\epsilon_{\mathrm{worst}}$ to support a universal transversal gate set  ([arXiv:1902.07714](https://arxiv.org/abs/1902.07714)).

## Transversal gates

- $G$-covariant codes defined on a tensor product space consisting of $n$ subsystems are equivalent to codes with a transversal gate set realizing $G$.

## Relations

- _parent_: [[concepts/qec/block-quantum]] — Covariant codes for $n>1$ are block quantum codes.
- _cousin_: [[concepts/qec/approximate-qecc]] — Normalizable constructions of infinite-dimensional $G$-covariant codes for continuous $G$ are approximately error-correcting.
- _cousin_: [[concepts/qec/quantum-reed-muller]] — Quantum RM codes are approximately covariant and nearly saturate certain covariance-performance bounds  ([arXiv:2111.06360](https://arxiv.org/abs/2111.06360)).
- _cousin_: [[concepts/qec/eth]] — ETH codes consisting of Dicke states are approximately $U(1)$-covariant and nearly saturate certain covariance-performance bounds  ([arXiv:1902.07714](https://arxiv.org/abs/1902.07714), [arXiv:2111.06360](https://arxiv.org/abs/2111.06360)).
- _cousin_: [[concepts/qec/quantum-random]] — Random $U(1)$-covariant  ([arXiv:2102.11835](https://arxiv.org/abs/2102.11835)) and $U(d)$-covariant  ([arXiv:1902.07714](https://arxiv.org/abs/1902.07714), [arXiv:2112.01498](https://arxiv.org/abs/2112.01498)) approximate QECCs exist.
