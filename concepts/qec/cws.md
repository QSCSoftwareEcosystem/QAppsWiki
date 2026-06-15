---
type: concept
name: Codeword stabilized (CWS) code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/ea-qubits-into-qubits
- concepts/qec/galois-cws
- concepts/qec/movassagh-ouyang
- concepts/qec/non-stabilizer
- concepts/qec/quantum-concatenated
- concepts/qec/qudit-cws
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/cws
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: cws
---

# Codeword stabilized (CWS) code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/cws) (`code_id: cws`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A code defined using a cluster state and a set of $Z$-type Pauli strings defined by a binary classical code.

The CWS construction takes in $ \mathcal{Q} = (\mathcal{G},\mathcal{C}) $, where $\mathcal{G}$ is a graph, and where $\mathcal{C}$ is an $(n,K,d)$ binary code.
From the graph, we form the unique cluster state $ |\mathcal{G} \rangle $.
From the binary code, we form Pauli $Z$-type operators $ W_i = Z^{c_{i,1}} \otimes \cdots \otimes Z^{c_{i,n}} $, where $c_{i,j} $ is the $j$-th coordinate of the $i$-th classical codeword.
The CWS codewords are then $ | i \rangle =  W_i | \mathcal{G} \rangle $.

The above definition corresponds to the *standard form* of CWS codes.
Since any stabilizer state is equivalent to a cluster state under a single-qubit Clifford circuit  ([arXiv:quant-ph/0308151](https://arxiv.org/abs/quant-ph/0308151)) ([arXiv:1910.00471](https://arxiv.org/abs/1910.00471)), any code whose underlying state is a non-cluster stabilizer state can be rewritten in standard CWS form  ([arXiv:0708.1021](https://arxiv.org/abs/0708.1021)).

The term CWS was coined in Ref.  ([arXiv:0708.1021](https://arxiv.org/abs/0708.1021)), and their approach is equivalent to another approach  ([arXiv:cs/0610159](https://arxiv.org/abs/cs/0610159)) based on Boolean functions (see Ref. ).
In an alternative convention (not used here), CWS codes are defined from an underlying stabilizer state that is not necessarily a cluster state.

(source: raw/error-correction-zoo.md)

## Protection

In standard form, error detection reduces to detecting the induced binary error patterns $C_{S}(E)$ with the underlying classical code, together with the requirement that any error satisfying $C_{S}(E)=0$ commute with every word operator  ([arXiv:0708.1021](https://arxiv.org/abs/0708.1021)).
The code distance of $\mathcal{Q} = ( \mathcal{G},\mathcal{C}) $ is upper bounded by the distance of the classical code $\mathcal{C} $.
A CWS code is degenerate if and only if it is impure  ([arXiv:0912.3245](https://arxiv.org/abs/0912.3245)).
The pure distance is upper bounded by $\delta + 1$, where $\delta$ is the minimum degree of $\mathcal{G}$  ([arXiv:0712.1979](https://arxiv.org/abs/0712.1979), [arXiv:2107.11286](https://arxiv.org/abs/2107.11286)).
For additive CWS codes realizable from a fixed graph $\mathcal{G}$, Ref.  ([arXiv:1108.5490](https://arxiv.org/abs/1108.5490)) derives upper bounds on the distance and proves a Gilbert-Varshamov existence bound matching the standard pure-stabilizer bound up to the graph-state distance $d'(\mathcal{G})$.

## Encoders

- If the classical code $ \mathcal{C} $ has an encoder of complexity $f(n)$, then the CWS code $ \mathcal{Q} = (\mathcal{G},\mathcal{C}) $ has an encoder of complexity $\max( n^2, f(n) )$, obtained by preparing the graph state and applying the classical encoder  ([arXiv:0708.1021](https://arxiv.org/abs/0708.1021)).
- Sequential encoder related to MBQC  ([arXiv:2405.06142](https://arxiv.org/abs/2405.06142)).

## Decoders

- There is no known *efficient* algorithm to decode *non-additive* (non-stabilizer) CWS codes.
- Clustered bounded-distance decoder  ([arXiv:0907.2038](https://arxiv.org/abs/0907.2038), [doi:10.1109/ISIT.2010.5513671](https://doi.org/10.1109/ISIT.2010.5513671)).
- Structured error recovery  ([arXiv:0912.3245](https://arxiv.org/abs/0912.3245)), which reduces to syndrome-based recovery for additive (i.e., stabilizer) CWS codes.

## Relations

- _parent_: [[concepts/qec/non-stabilizer]] — Any CWS code can be written as a USt whose ($K=1$) stabilizer code is the cluster state and whose coset representatives are constructed from the binary classical code. Conversely, USt codes are equivalent to CWS codes via a single-qubit Clifford circuit as follows  ([arXiv:0907.2038](https://arxiv.org/abs/0907.2038)) ([doi:10.1017/CBO9781139034807.012](https://doi.org/10.1017/CBO9781139034807.012)). The set of coset representatives of any USt can be extended to a larger set iterating over the underlying stabilizer code such that all codewords can be obtained from a single stabilizer state. Then, one can apply a single-qubit Clifford transformation to map said stabilizer state into a cluster state.
- _parent_: [[concepts/qec/qudit-cws]] — Modular-qudit CWS codes reduce to CWS codes for $q=2$.
- _parent_: [[concepts/qec/galois-cws]] — Galois-qudit CWS codes reduce to CWS codes for $q=2$.
- _cousin_: [[concepts/qec/movassagh-ouyang]] — The Movassagh-Ouyang codes overlap the CWS codes but neither family is contained in the other  ([arXiv:2012.01453](https://arxiv.org/abs/2012.01453)).
- _cousin_: [`spacetime`](https://errorcorrectionzoo.org/c/spacetime) — CWS codes have been considered in the context of spacetime replication of quantum data  ([arXiv:1210.0913](https://arxiv.org/abs/1210.0913), [arXiv:1601.02544](https://arxiv.org/abs/1601.02544)), while STCs are designed to replicate classical data.
- _cousin_: [[concepts/qec/quantum-concatenated]] — CWS codes can be concatenated by applying generalized local complementation to their underlying graphs  ([arXiv:0910.4129](https://arxiv.org/abs/0910.4129)).
- _cousin_: [[concepts/qec/ea-qubits-into-qubits]] — EA CWS codes have been formulated  ([arXiv:1109.3358](https://arxiv.org/abs/1109.3358)).

## Notes

- See Ref.  ([doi:10.1017/CBO9781139034807.012](https://doi.org/10.1017/CBO9781139034807.012)) for an overview of CWS codes.
