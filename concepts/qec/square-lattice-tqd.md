---
type: concept
name: Square-lattice TQD code
status: provisional
updated: '2026-09-29'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/brickwork
- concepts/qec/cubic-theory
- concepts/qec/hexagonal-cz
- concepts/qec/quantum-double-dihedral
- concepts/qec/surface
- concepts/qec/tqd-abelian
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/square_lattice_tqd
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: square_lattice_tqd
---

# Square-lattice TQD code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/square_lattice_tqd) (`code_id: square_lattice_tqd`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A square-lattice Clifford-stabilizer realization of the $2+1$D $l=m=n=1$ cubic theory code, equivalently the Type-III $\mathbb{Z}_2^3$ TQD phase.
The square-lattice TQD code places three qubits on every edge and provides an intermediate non-Pauli encoding for fault-tolerant non-Clifford operations on 2D topological codes  ([arXiv:2405.11719](https://arxiv.org/abs/2405.11719), [arXiv:2511.02900](https://arxiv.org/abs/2511.02900), [arXiv:2604.02033](https://arxiv.org/abs/2604.02033)).

For each of the three qubit colors, every face supports a weight-four Pauli-$Z$ plaquette generator.
Every vertex supports a Clifford generator consisting of Pauli-$X$ operators on the four incident qubits of one color and two $CZ$ gates acting on nearby qubits of the other two colors  ([arXiv:2604.02033](https://arxiv.org/abs/2604.02033)).
Vertex generators of different colors need not commute on the full Hilbert space, but they commute within the simultaneous $+1$ eigenspace of the plaquette generators  ([arXiv:2405.11719](https://arxiv.org/abs/2405.11719), [arXiv:2511.02900](https://arxiv.org/abs/2511.02900)).

A syndrome-extraction circuit follows by slicing the Type-III Dijkgraaf-Witten path integral on a cubic spacetime cellulation.
The circuit augments three square-lattice toric-code syndrome-extraction circuits with $CCZ$ gates that implement the cocycle twist  ([arXiv:2403.12119](https://arxiv.org/abs/2403.12119), [arXiv:2503.15751](https://arxiv.org/abs/2503.15751)).

(source: raw/error-correction-zoo.md)

## Protection

For the phenomenological noise model studied on an $L\times L$ torus, numerical simulations indicate an effective distance of approximately $L/2$ for both just-in-time and global decoding of $X$-like errors, as well as exponential suppression of the logical error rate with $L$ below threshold  ([arXiv:2604.02033](https://arxiv.org/abs/2604.02033)).

## Transversal gates

- On a square-lattice patch with three gapped boundaries encoding one logical qubit, a constant-depth automorphism circuit implements a logical $T^\dagger$ gate  ([arXiv:2511.02900](https://arxiv.org/abs/2511.02900)).

## Decoders

- A minimum-weight perfect-matching just-in-time decoder commits the required $X$ corrections using only the syndrome history available at each time step  ([arXiv:2604.02033](https://arxiv.org/abs/2604.02033)).
- A completing-the-loop and graph-reduction heuristic uses the committed $X$ corrections to reweight the subsequent global decoder for twisted $Z$ errors  ([arXiv:2604.02033](https://arxiv.org/abs/2604.02033)).

## Fault tolerance

- Code switching between a folded surface code and the square-lattice TQD code, combined with just-in-time decoding and the logical $T^\dagger$ gate, fault-tolerantly prepares a logical $T$ magic state in $O(d)$ rounds  ([arXiv:2511.02900](https://arxiv.org/abs/2511.02900)).

## Threshold

- Under equal-rate phenomenological Pauli-$X$ and plaquette-measurement noise, the matching-based just-in-time decoder has threshold $2.51\pm0.31\%$, compared with $2.90\pm0.12\%$ for a global decoder  ([arXiv:2604.02033](https://arxiv.org/abs/2604.02033)).
- For the full phenomenological noise model with equal $X$-like and $Z$-like error rates, just-in-time $X$ decoding followed by the reweighted global $Z$ decoder has threshold $2.17\pm0.17\%$, compared with $1.81\pm0.11\%$ for naive unheralded $Z$ decoding  ([arXiv:2604.02033](https://arxiv.org/abs/2604.02033)).

## Relations

- _parent_: [[concepts/qec/cubic-theory]] — The square-lattice TQD code is the $D=3$, $l=m=n=1$ hypercubic specialization of the cubic theory code  ([arXiv:2405.11719](https://arxiv.org/abs/2405.11719)).
- _parent_: [[concepts/qec/tqd-abelian]] — The square-lattice TQD code is a Type-III $\mathbb{Z}_2^3$ Abelian TQD code whose codewords realize non-Abelian topological order  ([arXiv:2405.11719](https://arxiv.org/abs/2405.11719), [arXiv:2511.02900](https://arxiv.org/abs/2511.02900)).
- _cousin_: [[concepts/qec/hexagonal-cz]] — The square-lattice TQD code and the hexagonal $CZ$ code are distinct microscopic lattice realizations of the same Type-III $\mathbb{Z}_2^3$ TQD phase  ([arXiv:1508.03468](https://arxiv.org/abs/1508.03468), [arXiv:2405.11719](https://arxiv.org/abs/2405.11719), [arXiv:2503.15751](https://arxiv.org/abs/2503.15751), [arXiv:2604.02033](https://arxiv.org/abs/2604.02033)).
- _cousin_: [[concepts/qec/brickwork]] — The square-lattice TQD code and the brickwork $XS$ stabilizer code are distinct microscopic codes realizing the same Type-III $\mathbb{Z}_2^3$ TQD phase  ([arXiv:2503.15751](https://arxiv.org/abs/2503.15751), [arXiv:2604.02033](https://arxiv.org/abs/2604.02033)).
- _cousin_: [[concepts/qec/quantum-double-dihedral]] — The square-lattice TQD code realizes the same topological order as the $G=D_4$ member of the dihedral quantum-double code family  ([arXiv:hep-th/9511195](https://arxiv.org/abs/hep-th/9511195), [arXiv:2405.11719](https://arxiv.org/abs/2405.11719)).
- _cousin_: [[concepts/qec/surface]] — Code switching by gauging measurements connects a folded surface code to the square-lattice TQD code while preserving the encoded logical state  ([arXiv:2511.02900](https://arxiv.org/abs/2511.02900)).
