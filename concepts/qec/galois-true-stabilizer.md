---
type: concept
name: True Galois-qudit stabilizer code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Linear stabilizer code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/galois-stabilizer
- concepts/qec/iceberg
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/galois_true_stabilizer
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: galois_true_stabilizer
---

# True Galois-qudit stabilizer code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/galois_true_stabilizer) (`code_id: galois_true_stabilizer`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A $⟦n,k,d⟧_q$ stabilizer code whose stabilizer's Galois symplectic representation forms a linear subspace. In other words, the set of $q$-ary vectors representing the stabilizer group is closed under both addition and multiplication by elements of $\mathbb{F}_q$. In contrast, Galois-qudit stabilizer codes admit sets of vectors that are closed under addition only.

The number of generators $r$ for a true stabilizer code is a multiple of $m$ (recall that $q=p^m$ for Galois qudits). As a result, the number $k=n-r/m$ of logical qudits is an integer.

Each code can be represented by a stabilizer generator matrix $H=(A|B)$, where each row $(a|b)$ is the Galois symplectic representation of a stabilizer generator.

(source: raw/error-correction-zoo.md)

## Protection

Detects errors on up to $d-1$ qudits, and corrects erasure errors on up to $d-1$ qudits.

## Relations

- _parent_: [[concepts/qec/galois-stabilizer]]
- _cousin_: [`q-ary_linear`](https://errorcorrectionzoo.org/c/q-ary_linear) — A true Galois-qudit stabilizer code is the closest quantum analogue of a linear code over $\mathbb{F}_q$ because the $q$-ary vectors corresponding to the Galois symplectic representation of the stabilizers form a linear subspace.
- _cousin_: [[concepts/qec/iceberg]] — A naive extension of the iceberg code to Galois qudits keeps only two CSS-type generators, $M_1(1)=X_{\alpha_1}\otimes\cdots\otimes X_{\alpha_n}$ and $M_2(1)=Z_{\beta_1}\otimes\cdots\otimes Z_{\beta_n}$, with nonzero $\alpha_i,\beta_i\in\mathbb{F}_q$ satisfying $\sum_i \alpha_i\beta_i=0$. For prime-power dimensions with $q=p^m$ and $m>1$, this yields a Galois-qudit code of distance one that is generally not a true stabilizer code because the stabilizer is not closed under multiplication by arbitrary $\gamma\in\mathbb{F}_q$. Adding all $M_1(\gamma)$ and $M_2(\gamma)$ to the stabilizer group recovers the corresponding true Galois-qudit CSS code of distance two .

## Notes

- See Ref.  ([doi:10.1017/CBO9781139034807.014](https://doi.org/10.1017/CBO9781139034807.014)) for introductions to various stabilizer code constructions.
