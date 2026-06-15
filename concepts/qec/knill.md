---
type: concept
name: Knill code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Clifford code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/group-representation
- concepts/qec/oecc
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/knill
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: knill
---

# Knill code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/knill) (`code_id: knill`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A group representation code whose projection is onto an irrep of a normal subgroup of the group $G$ formed by a nice error basis.
More general definitions dropping the normality requirement also exist  ([arXiv:2506.01843](https://arxiv.org/abs/2506.01843)).
Knill codes yield stabilizer-like codes based on error bases that are non-Pauli but that nevertheless maintain many of the useful features of Pauli-type bases.

\begin{defterm}{Nice error basis}
\label{topic:nice-error-basis}
  A nice error basis  ([arXiv:quant-ph/9608048](https://arxiv.org/abs/quant-ph/9608048), [arXiv:quant-ph/9608049](https://arxiv.org/abs/quant-ph/9608049), [arXiv:quant-ph/0010082](https://arxiv.org/abs/quant-ph/0010082)) for a $q$-dimensional vector space is a set $\{E_g~,~g\in G\}$ of unitary operators, where $G$ is a (not necessarily Abelian) group of order $q^2$ that is represented projectively. Namely,
  \begin{align}
    \text{tr}(E_{g})&=q\delta^{G}_{g,1}\\
    E_{g}E_{h}&=\omega_{g,h}E_{gh}
  \end{align}
for all group elements $g,h$.
Above, $\delta^{G}_{g,1}$ is the group Kronecker-delta function.
This definition can naturally be extended to continuous groups.
\end{defterm}

The first example of an error basis based on a non-Abelian error group is due to S. Egner and consists of products of $S$, Pauli, and Hadamard gates  ([arXiv:quant-ph/9608049](https://arxiv.org/abs/quant-ph/9608049)).
An example of a small non-stabilizer Knill code is presented in  ([doi:10.1201/9781420035377-11](https://doi.org/10.1201/9781420035377-11)). 
Certain nice error bases have been classified and are related to the braid group  ([arXiv:0902.0383](https://arxiv.org/abs/0902.0383)).

(source: raw/error-correction-zoo.md)

## Relations

- _parent_: [[concepts/qec/group-representation]] — Knill codes project onto a single irrep sector associated with a normal subgroup of the group formed by a nice error basis  ([arXiv:quant-ph/9608049](https://arxiv.org/abs/quant-ph/9608049)).
- _cousin_: [[concepts/qec/oecc]] — Subsystem Knill codes can be formulated  ([arXiv:quant-ph/0604161](https://arxiv.org/abs/quant-ph/0604161)).

## Notes

- Catalogue of nice error bases, managed by A. Klappenecker and M. Rotteler, is available on [this website](https://people.engr.tamu.edu/andreas-klappenecker/ueb/ueb.html).
- Many Knill codes are qubit stabilizer codes  ([arXiv:quant-ph/0010076](https://arxiv.org/abs/quant-ph/0010076)). A table of non-stabilizer Knill codes is available in Ref. . An infinite family is constructed in Ref.  ([arXiv:quant-ph/0402060](https://arxiv.org/abs/quant-ph/0402060)).
