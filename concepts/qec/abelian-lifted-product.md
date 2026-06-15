---
type: concept
name: Abelian LP code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/asymmetric-qecc
- concepts/qec/expander-lifted-product
- concepts/qec/lifted-product
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/abelian_lifted_product
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: abelian_lifted_product
---

# Abelian LP code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/abelian_lifted_product) (`code_id: abelian_lifted_product`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A lifted-product code whose lift group $G$ is Abelian.
The case of $G$ being a cyclic group is a GB code (a.k.a. a quasi-cyclic LP code)  ([arXiv:2012.04068](https://arxiv.org/abs/2012.04068)).
A particular family with $G=\mathbb{Z}_{\ell}$ yields codes with parameters $⟦n,k=\Theta(\log n),d=\Theta(n/\log n)⟧$  ([arXiv:2012.04068](https://arxiv.org/abs/2012.04068)).

The Abelian LP construction has been adapted to accommodate noise bias, yielding *bias-tailored LP codes*  ([arXiv:2202.01702](https://arxiv.org/abs/2202.01702)).
See Refs.  ([arXiv:1904.02703](https://arxiv.org/abs/1904.02703), [arXiv:2012.04068](https://arxiv.org/abs/2012.04068), [arXiv:2111.07029](https://arxiv.org/abs/2111.07029), [arXiv:2308.08648](https://arxiv.org/abs/2308.08648)) for other explicit examples.

(source: raw/error-correction-zoo.md)

## Rate

For cyclic groups $G=\mathbb{Z}_{\ell}$ with $\ell=\Theta(n/\log n)$, quasi-cyclic expander LP codes yield families with parameters $⟦n,k=\Theta(\log n),d=\Theta(n/\log n)⟧$  ([arXiv:2012.04068](https://arxiv.org/abs/2012.04068)). Related balanced-product reformulations and other explicit Abelian LP constructions appear in  ([arXiv:2012.09271](https://arxiv.org/abs/2012.09271), [arXiv:2112.01647](https://arxiv.org/abs/2112.01647)).

## Decoders

- Ensemble BP decoder for codes without short cycles of length 4  ([arXiv:2401.06874](https://arxiv.org/abs/2401.06874)).
- Efficient decoder correcting order $\Theta(n/\log n)$ errors  ([arXiv:2411.04464](https://arxiv.org/abs/2411.04464)).

## Relations

- _parent_: [[concepts/qec/lifted-product]]
- _cousin_: [`qc_ldpc`](https://errorcorrectionzoo.org/c/qc_ldpc) — QC-LDPC codes can be lifted to yield various Abelian LP codes  ([arXiv:2111.07029](https://arxiv.org/abs/2111.07029), [arXiv:2401.06874](https://arxiv.org/abs/2401.06874), [arXiv:2406.14445](https://arxiv.org/abs/2406.14445)). Conversely, the Abelian LP construction yields notable families of QC-LDPC codes  ([arXiv:2112.01647](https://arxiv.org/abs/2112.01647)).
- _cousin_: [`pg_ldpc`](https://errorcorrectionzoo.org/c/pg_ldpc) — FG-LDPC codes can be used to construct Abelian LP codes  ([arXiv:2401.06874](https://arxiv.org/abs/2401.06874)).
- _cousin_: [[concepts/qec/expander-lifted-product]] — For cyclic groups $G=\mathbb{Z}_{\ell}$ with $\ell=\Theta(n/\log n)$, quasi-cyclic expander LP codes yield families with parameters $⟦n,k=\Theta(\log n),d=\Theta(n/\log n)⟧$  ([arXiv:2012.04068](https://arxiv.org/abs/2012.04068)). Related balanced-product reformulations and other explicit Abelian LP constructions appear in  ([arXiv:2012.09271](https://arxiv.org/abs/2012.09271), [arXiv:2112.01647](https://arxiv.org/abs/2112.01647)).
- _cousin_: [[concepts/qec/asymmetric-qecc]] — The Abelian LP construction has been adapted to accommodate noise bias, yielding bias-tailored LP codes  ([arXiv:2202.01702](https://arxiv.org/abs/2202.01702)).
