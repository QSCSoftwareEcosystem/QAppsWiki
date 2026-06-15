---
type: concept
name: Expander LP code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/good-qldpc
- concepts/qec/lifted-product
- concepts/qec/topological
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/expander_lifted_product
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: expander_lifted_product
---

# Expander LP code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/expander_lifted_product) (`code_id: expander_lifted_product`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Family of $G$-lifted product codes constructed using two classical expander codes, equivalently two regular Tanner codes defined on the same expander graph  ([doi:10.1090/S0273-0979-06-01126-8](https://doi.org/10.1090/S0273-0979-06-01126-8)). For certain parameters, this construction yields the first asymptotically good QLDPC codes. Classical codes resulting from the same lifted-product complexes are one of the first two families of $c^3$-LTCs  ([arXiv:2111.03654](https://arxiv.org/abs/2111.03654)).

An expander lifted-product code family is constructed as follows. First, take the Cayley graph of a finite group $G$.
Second, take the double cover of the graph, resulting in a graph that satisfies the requirements of participating in a $G$-lifted product (i.e., the resulting graph is a free ${\mathbb{F}}_q G$-module). Third, create two Tanner codes on that graph, in which parity-check supports are defined by the graph and the local constraints are specified by two short classical codes (chosen randomly in the original proof). Fourth, take the $G$-lifted product of those two Tanner codes.

The small classical codes used in the construction of good QLDPC codes are required to have a certain product-expansion property  ([arXiv:2111.03654](https://arxiv.org/abs/2111.03654)); it is proven that random codes satisfy said property in the thermodynamic limit.

(source: raw/error-correction-zoo.md)

## Protection

Code performance strongly depends on $G$. Certain non-Abelian groups yield asymptotically good QLDPC codes with parameters $⟦n,k=\Theta(n),d=\Theta(n)⟧$  ([arXiv:2111.03654](https://arxiv.org/abs/2111.03654)). For cyclic Abelian groups $G=\mathbb{Z}_{\ell}$ with $\ell=\Theta(n/\log n)$, quasi-cyclic expander LP codes yield families with parameters $⟦n,k=\Theta(\log n),d=\Theta(n/\log n)⟧$  ([arXiv:2012.04068](https://arxiv.org/abs/2012.04068)).

## Rate

Expander lifted-product codes for non-Abelian groups include the first examples  ([arXiv:2111.03654](https://arxiv.org/abs/2111.03654)) of (asymptotically) *good QLDPC codes*, i.e., codes with asymptotically constant rate and linear distance. For cyclic Abelian groups $G=\mathbb{Z}_{\ell}$ with $\ell=\Theta(n/\log n)$, quasi-cyclic expander LP codes yield families with parameters $⟦n,k=\Theta(\log n),d=\Theta(n/\log n)⟧$  ([arXiv:2012.04068](https://arxiv.org/abs/2012.04068)). Related balanced-product reformulations and other explicit Abelian LP constructions appear in  ([arXiv:2012.09271](https://arxiv.org/abs/2012.09271), [arXiv:2112.01647](https://arxiv.org/abs/2112.01647)).

## General gates

- Certain qubit expander LP codes can admit a cup product structure and can thus have logical gates in the \term{Clifford hierarchy} implemented by constant-depth Clifford circuits  ([arXiv:2410.16250](https://arxiv.org/abs/2410.16250)).

## Decoders

- Linear-time decoder  ([arXiv:2206.07571](https://arxiv.org/abs/2206.07571)).
- Logarithmic-time subroutine  ([arXiv:2208.05537](https://arxiv.org/abs/2208.05537)).

## Relations

- _parent_: [[concepts/qec/lifted-product]]
- _cousin_: [[concepts/qec/good-qldpc]] — Lifted products of certain classical Tanner codes are the first asymptotically good QLDPC codes.
- _cousin_: [`q-ary_ltc`](https://errorcorrectionzoo.org/c/q-ary_ltc) — Classical codes resulting from the expander lifted-product construction are one of the first two families of $c^3$-LTCs  ([arXiv:2111.03654](https://arxiv.org/abs/2111.03654)).
- _cousin_: [`expander`](https://errorcorrectionzoo.org/c/expander) — Expander LP codes are lifted products of expander codes with different local codes  ([arXiv:2111.03654](https://arxiv.org/abs/2111.03654)).
- _cousin_: [`random`](https://errorcorrectionzoo.org/c/random) — Expander lifted-product codes are quantum CSS codes that utilize short classical codes in their construction which need to satisfy some properties  ([arXiv:2111.03654](https://arxiv.org/abs/2111.03654)). It is shown that such codes exist, but they are not explicitly constructed. Such codes can be obtained by repeated random sampling or by performing a search of all codes of desired length. Nevertheless, since the length of the desired short codes does not scale with $n$, this construction is effectively explicit.
- _cousin_: [[concepts/qec/topological]] — Expander lifted-product codes are expected to realize topological quantum spin glass order  ([arXiv:2412.13248](https://arxiv.org/abs/2412.13248)).

## Notes

- Construction outlined in talk by [R. O'Donnell](https://www.youtube.com/watch?v=k7LuOiOBYyQ).
- Popular summary in [Quanta Magazine](https://www.quantamagazine.org/qubits-can-be-as-safe-as-bits-researchers-show-20220106).
