---
type: concept
name: Triorthogonal code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/css-t
- concepts/qec/quantum-k-orthogonal
- concepts/qec/quantum-reed-muller
- concepts/qec/qudit-triorthogonal
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/quantum_triorthogonal
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: quantum_triorthogonal
---

# Triorthogonal code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/quantum_triorthogonal) (`code_id: quantum_triorthogonal`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Qubit CSS code whose $X$-type logicals and stabilizer generators form a triorthogonal matrix (defined below) in the symplectic representation.

An $m \times n$ binary matrix is triorthogonal if its rows $r_1, \ldots, r_m$ satisfy $|r_i \cdot r_j| = 0$ and $|r_i \cdot r_j \cdot r_k| = 0$ modulo $2$, with binary addition and multiplication.
The triorthogonal CSS code associated with the matrix is constructed by mapping nonzero entries in even-weight rows to $X$-type stabilizer generators, odd-weight rows to $X$-type logical operators, and $Z$ operators for each row in the orthogonal complement.

Generalized versions of triorthogonality allow odd pair and triple overlaps inside the logical-row block $K$ while keeping every overlap involving an $S$-row even, which yields quasitransversal logical gates beyond a single logical $T$ gate  ([arXiv:1606.01904](https://arxiv.org/abs/1606.01904)) ([arXiv:1709.02832](https://arxiv.org/abs/1709.02832)).

(source: raw/error-correction-zoo.md)

## Protection

Weight $t$ Pauli errors, where $t$ depends on the family. For example, Ref.  ([arXiv:1209.2426](https://arxiv.org/abs/1209.2426)) provides a family of distance $2$ codes.

## Encoders

- Encoder for magic states for the code constructed in  ([arXiv:1209.2426](https://arxiv.org/abs/1209.2426)).

## Transversal gates

- Transversal action of $T$ gates on all qubits, followed by a particular pattern of $CZ$ and $S$ gates, will realize a logical $T$ gate  ([arXiv:1209.2426](https://arxiv.org/abs/1209.2426)) ([arXiv:2408.12752](https://arxiv.org/abs/2408.12752)). When an additional condition on logical-$X$ operators is satisfied, the $CZ$ and $S$ gates are no longer necessary  ([arXiv:1910.09333](https://arxiv.org/abs/1910.09333)).
- Triorthogonality is necessary but not sufficient for physical transversal $T$ gates on each qubit to realize the identity logical gate  ([arXiv:1910.09333](https://arxiv.org/abs/1910.09333)).
- Certain codes realize controlled-controlled-$Z$ gates  ([arXiv:1304.3709](https://arxiv.org/abs/1304.3709)), realized via physical $CCZ$ gates on three code blocks.
- Triorthogonal codes realizing logical $T$ gates using only physical $T$ gates can be paired up with self-dual CSS codes to yield a transversal CNOT gate  ([arXiv:2510.05708](https://arxiv.org/abs/2510.05708)).

## Decoders

- Steane error correction  ([arXiv:2510.05708](https://arxiv.org/abs/2510.05708)).

## Fault tolerance

- Universal fault-tolerant gates can be performed without magic-state distillation  ([arXiv:1304.3709](https://arxiv.org/abs/1304.3709), [arXiv:2210.14074](https://arxiv.org/abs/2210.14074)).
- Universal fault-tolerant gates can be achieved by pairing with a self-dual CSS code and using Steane error correction  ([arXiv:2510.05708](https://arxiv.org/abs/2510.05708)).

## Relations

- _parent_: [[concepts/qec/quantum-k-orthogonal]] — $k$-orthogonal codes reduce to triorthogonal codes for $k=3$.
- _parent_: [[concepts/qec/qudit-triorthogonal]] — Prime-qudit triorthogonal codes reduce to triorthogonal codes when $p=2$.
- _cousin_: [[concepts/qec/quantum-reed-muller]] — Classification of triorthogonal codes yields a connection to RM code polynomials  ([arXiv:2107.09684](https://arxiv.org/abs/2107.09684)).
- _cousin_: [`self_dual`](https://errorcorrectionzoo.org/c/self_dual) — Self-dual binary codes can be used to construct triorthogonal codes  ([arXiv:2408.09685](https://arxiv.org/abs/2408.09685)).
- _cousin_: [[concepts/qec/css-t]] — Triorthogonal and CSS-T codes overlap, but neither is a subset of the other  ([arXiv:2408.12752](https://arxiv.org/abs/2408.12752)). CSS-T codes reduce to triorthogonal codes when the logical action of the physical transversal $T$ gate is a logical $T$ gate on all encoded qubits. Triorthogonality is necessary for physical transversal $T$ gates on each qubit to realize the identity logical gate  ([arXiv:1910.09333](https://arxiv.org/abs/1910.09333)). The $X$-type stabilizer generator matrix for a CSS-T code is always triorthogonal  ([arXiv:2312.17518](https://arxiv.org/abs/2312.17518)).

## Notes

- Reference  ([arXiv:2107.09684](https://arxiv.org/abs/2107.09684)) presents a classification of triorthogonal codes up to $n + k \leq 38$ by associating each triorthogonal code with a RM code polynomial.
- A database of triorthogonal codes is available in QECDB .
