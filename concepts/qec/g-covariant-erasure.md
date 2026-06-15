---
type: concept
name: $G$-covariant erasure code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/covariant
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/g_covariant_erasure
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: g_covariant_erasure
---

# $G$-covariant erasure code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/g_covariant_erasure) (`code_id: g_covariant_erasure`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A $G$-covariant block code that serves as a proof-of-principle construction to demonstrate the existence of
$G$-covariant codes where $G$ is a finite
group, and the physical space is finite-dimensional.
This construction can be done for any erasure-correcting code.

Consider a finite group $G$ acting on a finite set
$A$ as a subgroup of the symmetric group on $|A|$ elements, $G \subset S_{|A|}$.
Let $U_0: \mathsf{H}_{\text{logical}} \rightarrow \mathsf{H}_{\text{physical}}
= \mathsf{H}^{\otimes n}$ be any QECC, possibly non-covariant.  Define the covariant
encoder $U \equiv U_0^{\otimes |A|}: \mathsf{H}_{\text{logical}}^{\otimes |A|}
\rightarrow \mathsf{H}_{\text{physical}}^{\otimes |A|}$ on $|A|$.  Then, the group acts on codewords by index
permutation:
\begin{align}
V(g) | \phi_{a_1} \rangle | \phi_{a_2} \rangle \cdots | \phi_{a_{|A|}} \rangle = | \phi_{g^{-1} a_1} \rangle | \phi_{g^{-1} a_2} \rangle \cdots | \phi_{g^{-1} a_{|A|}} \rangle~,
\end{align}
where $V(g)$ is the unitary representation of $g \in G$ acting on the physical space. The action of $V(g)$ is transversal with respect to the partition $\mathsf{H}_{\text{physical}}^{\otimes |A|}$.

(source: raw/error-correction-zoo.md)

## Protection

Depends on the base encoding $U_0$.

## Relations

- _parent_: [[concepts/qec/covariant]] — In a proof of principle demonstration, error-correcting codes that are finite-$G$ covariant can be constructed from a base encoding $U_0$.
