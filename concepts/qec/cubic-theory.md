---
type: concept
name: Cubic theory code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Magic stabilizer code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/clifford-hierarchy
- concepts/qec/color
- concepts/qec/quantum-double-dihedral
- concepts/qec/self-correct
- concepts/qec/yetter-gauge-theory
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/cubic_theory
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: cubic_theory
---

# Cubic theory code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/cubic_theory) (`code_id: cubic_theory`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A geometrically local commuting-projector code family defined on triangulations in arbitrary spatial dimensions.
Its Hamiltonian contains Pauli-$Z$ flux terms and non-Pauli Gauss-law terms built from products of Pauli-$X$ operators and $CZ$ gates.
These commuting non-Pauli stabilizers realize higher-form $\mathbb{Z}_2^3$ gauge theories with Abelian electric excitations and non-Abelian magnetic excitations.

For $l=m=n=2$ in $D=6$ spacetime dimensions, the code is a candidate non-Abelian self-correcting quantum memory with Abelian loop excitations and non-Abelian membrane excitations  ([arXiv:2405.11719](https://arxiv.org/abs/2405.11719)).

The construction is based on first constructing a model for an SPT phase  ([arXiv:1106.4772](https://arxiv.org/abs/1106.4772), [arXiv:1908.02613](https://arxiv.org/abs/1908.02613)), gauging its symmetries  ([arXiv:1202.3120](https://arxiv.org/abs/1202.3120), [arXiv:1407.1025](https://arxiv.org/abs/1407.1025), [arXiv:1603.04442](https://arxiv.org/abs/1603.04442), [arXiv:1603.05182](https://arxiv.org/abs/1603.05182), [arXiv:1605.01640](https://arxiv.org/abs/1605.01640), [arXiv:1805.01836](https://arxiv.org/abs/1805.01836), [arXiv:1806.08679](https://arxiv.org/abs/1806.08679), [arXiv:2108.11402](https://arxiv.org/abs/2108.11402), [arXiv:2310.16032](https://arxiv.org/abs/2310.16032), [arXiv:2410.02213](https://arxiv.org/abs/2410.02213)), and making all terms commute outside of the ground-state subspace by projecting them to zero flux.

(source: raw/error-correction-zoo.md)

## Protection

On suitable triangulations of the Wu 5-manifold, a family of five-dimensional cubic theory codes has parameters $⟦O(n),3,O(n^{2/5})⟧$  ([arXiv:2405.11719](https://arxiv.org/abs/2405.11719)).

## General gates

- In five spatial dimensions, a constant-depth circuit built from physical $CCZ$ and SWAP gates implements the logical gate $\overline{\mathrm{SWAP}}_{1,2}\overline{\mathrm{CCZ}}_{1,2,3}$ on the three logical qubits supported by the Wu-manifold family  ([arXiv:2405.11719](https://arxiv.org/abs/2405.11719)).

## Decoders

- Probabilistic local cellular-automaton decoder  ([arXiv:2405.11719](https://arxiv.org/abs/2405.11719)).

## Fault tolerance

- The Wu-manifold family combines the logical non-Clifford gate with code parameters $⟦O(n),3,O(n^{2/5})⟧$, giving $O(d^{5/2})$ space-time overhead for this topological scheme  ([arXiv:2405.11719](https://arxiv.org/abs/2405.11719)).

## Relations

- _parent_: [[concepts/qec/clifford-hierarchy]] — Cubic theory codes are joint eigenspaces of commuting non-Pauli stabilizers built from Pauli $X$, Pauli $Z$, and $CZ$ operators, placing them at the second level of the Clifford hierarchy.
- _parent_: [[concepts/qec/yetter-gauge-theory]] — Cubic theory codes realize higher-form $\mathbb{Z}_2^3$ gauge theories with non-Abelian excitations in arbitrary dimensions.
- _cousin_: [[concepts/qec/self-correct]] — A family of five-dimensional cubic theory codes with Abelian loop excitations and non-Abelian membrane excitations is argued to be self-correcting below a critical temperature via a Peierls argument  ([arXiv:2405.11719](https://arxiv.org/abs/2405.11719)).
- _cousin_: [[concepts/qec/color]] — The cubic theory in $D$ spacetime dimensions can be obtained by twisted compactification of a generalized color code in $D+1$ spacetime dimensions; in particular, the five-dimensional cubic theory arises from a twisted compactification of the 6D color code  ([arXiv:2405.11719](https://arxiv.org/abs/2405.11719)).
- _cousin_: [[concepts/qec/quantum-double-dihedral]] — For $D=3$ with $l=m=n=1$, the cubic theory is equivalent to the $G=D_4$ quantum double, i.e. the non-Abelian Type-III $\mathbb{Z}_2^3$ twisted quantum double  ([arXiv:2405.11719](https://arxiv.org/abs/2405.11719)).
