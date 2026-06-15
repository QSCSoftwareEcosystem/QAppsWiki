---
type: concept
name: Modular-qudit CWS code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/quantum-concatenated
- concepts/qec/quantum-perfect
- concepts/qec/qudit-non-stabilizer
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/qudit_cws
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: qudit_cws
---

# Modular-qudit CWS code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/qudit_cws) (`code_id: qudit_cws`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A CWS code for modular qudits, defined using a modular-qudit cluster state and a set of modular-qudit $Z$-type Pauli strings defined by a $q$-ary classical code over $\mathbb{Z}_q$.

The modular-qudit CWS construction takes in $ \mathcal{Q} = (\mathcal{G},\mathcal{C}) $, where $\mathcal{G}$ is a graph, and where $\mathcal{C}$ is an $(n,K,d)_{\mathbb{Z}_q}$ $q$-ary code over $\mathbb{Z}_q$.
From the graph, we form the modular-qudit cluster state $ |\mathcal{G} \rangle $.
From the $q$-ary code, we form modular-qudit Pauli $Z$-type operators $ W_i = Z^{c_{i,1}} \otimes \cdots \otimes Z^{c_{i,n}} $, where $c_{i,j} $ is the $j$-th coordinate of the $i$-th classical codeword.
The codewords are then $ | i \rangle =  W_i | \mathcal{G} \rangle $.

In an alternative convention (not used here), CWS codes are defined from an underlying modular-qudit stabilizer state that is not necessarily a cluster state.

(source: raw/error-correction-zoo.md)

## Relations

- _parent_: [[concepts/qec/qudit-non-stabilizer]] — Any modular-qudit CWS code can be written as a modular-qudit USt whose ($K=1$) stabilizer code is the modular-qudit cluster state and whose coset representatives are constructed from the $q$-ary classical code over $\mathbb{Z}_q$. Prime-dimensional modular-qudit CWS codes have a unique representation as USt codes  ([arXiv:1303.7020](https://arxiv.org/abs/1303.7020)). Conversely, modular-qudit USt codes are equivalent to modular-qudit CWS codes via a single-modular-qudit Clifford circuit as follows  ([arXiv:0907.2038](https://arxiv.org/abs/0907.2038)) ([doi:10.1017/CBO9781139034807.012](https://doi.org/10.1017/CBO9781139034807.012)). The set of coset representatives of any modular-qudit USt can be extended to a larger set iterating over the underlying stabilizer code such that all codewords can be obtained from a single stabilizer state. Then, one can apply a single-qudit Clifford transformation to map said modular-qudit stabilizer state into a modular-qudit cluster state.
- _cousin_: [[concepts/qec/quantum-perfect]] — Generalized concatenations of modular-qudit CWS codes yield a family of codes that have larger logical dimension than stabilizer codes and that asymptotically approach the modular-qudit Hamming bound  ([arXiv:0901.1319](https://arxiv.org/abs/0901.1319)).
- _cousin_: [[concepts/qec/quantum-concatenated]] — Generalized concatenations of modular-qudit CWS codes yield a family of codes that have larger logical dimension than stabilizer codes and that asymptotically approach the modular-qudit Hamming bound  ([arXiv:0901.1319](https://arxiv.org/abs/0901.1319)).

## Notes

- See Ref.  ([arXiv:0712.1979](https://arxiv.org/abs/0712.1979)) for qudit CWS code tables.
