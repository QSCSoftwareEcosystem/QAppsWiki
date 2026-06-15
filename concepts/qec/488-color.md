---
type: concept
name: Square-octagon (4.8.8) color code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/2d-color
- concepts/qec/triangular-color
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/488_color
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: 488_color
---

# Square-octagon (4.8.8) color code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/488_color) (`code_id: 488_color`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

2D color code defined on a patch of the 4.8.8 (square-octagon) tiling, which itself is obtained by applying a fattening procedure to the square lattice  ([arXiv:cond-mat/0607736](https://arxiv.org/abs/cond-mat/0607736)).
An equivalent description uses the Tetrakis square tiling (a.k.a. the Union Jack lattice), which is dual to the 4.8.8 lattice  ([arXiv:0910.0573](https://arxiv.org/abs/0910.0573)).
Among the three semiregular triangular 2D color-code families, the 4.8.8 family uses the fewest physical qubits for a given distance and is the only one of the three with transversal implementations of the full Clifford group  ([arXiv:1108.5738](https://arxiv.org/abs/1108.5738)).

Stabilizer generators are shown in \ref{figure:4.8.8-operators}.
  

Different boundaries affect the logical dimension  ([doi:10.1088/2399-6528/aad062](https://doi.org/10.1088/2399-6528/aad062)).

(source: raw/error-correction-zoo.md)

## Protection

There is a $⟦(d^2-1)/2+d, 1, d⟧$ code family for any odd distance $d$  ([arXiv:1108.5738](https://arxiv.org/abs/1108.5738)).

## Transversal gates

- CNOT gate because the code is CSS.
- Hadamard gates for any qubit geometry which yields a self-dual CSS code.
- Transversal $S$ gate  ([arXiv:quant-ph/0605138](https://arxiv.org/abs/quant-ph/0605138), [arXiv:1108.5738](https://arxiv.org/abs/1108.5738)).
- Transversal logical Clifford gates in the Union Jack formulation  ([arXiv:0910.0573](https://arxiv.org/abs/0910.0573)).
- Single-qubit Clifford and CNOT gates between qubits encoded in holes in the lattice can be implemented via braiding  ([arXiv:0806.4827](https://arxiv.org/abs/0806.4827)).

## General gates

- Color-code lattice surgery  ([arXiv:1407.5103](https://arxiv.org/abs/1407.5103)).
- Lattice surgery scheme for a hybrid 6.6.6-4.8.8 layout yields lower resource overhead when compared to analogous surface code scheme  ([arXiv:2201.07806](https://arxiv.org/abs/2201.07806)).

## Decoders

- Fault-tolerant syndrome extraction circuits  ([arXiv:1108.5738](https://arxiv.org/abs/1108.5738)).
- Matching decoder  ([arXiv:0907.1708](https://arxiv.org/abs/0907.1708), [arXiv:1407.5103](https://arxiv.org/abs/1407.5103)).
- Integer-program (IP) decoder  ([arXiv:1108.5738](https://arxiv.org/abs/1108.5738)).
- Two-copy surface-code decoder .

## Fault tolerance

- Color-code lattice surgery  ([arXiv:1407.5103](https://arxiv.org/abs/1407.5103)).
- Fault-tolerant syndrome extraction circuits  ([arXiv:1108.5738](https://arxiv.org/abs/1108.5738)).

## Code capacity threshold

- Independent $X,Z$ noise: $p_X = 10.56(1)\%$ under IP decoder  ([arXiv:1108.5738](https://arxiv.org/abs/1108.5738)), $8.87\%$ under matching decoder  ([arXiv:0907.1708](https://arxiv.org/abs/0907.1708)), $7.60(2)\%$ under projection decoder  ([arXiv:1402.3037](https://arxiv.org/abs/1402.3037)), and $8.7\%$ under two-copy surface-code decoder  (see  ([arXiv:1108.5738](https://arxiv.org/abs/1108.5738))). The threshold under ML decoding corresponds to the value of a critical point of a two-dimensional three-body random-bond Ising model (RBIM) on the Nishimori line  ([doi:10.1143/JPSJ.55.3305](https://doi.org/10.1143/JPSJ.55.3305), [arXiv:0902.4845](https://arxiv.org/abs/0902.4845)), calculated to be $10.9(2)\%$ in Ref.  ([arXiv:0902.4845](https://arxiv.org/abs/0902.4845)) (and in the Union Jack formulation in Ref.  ([arXiv:0910.0573](https://arxiv.org/abs/0910.0573))) and $10.925(5)\%$ in Ref.  ([arXiv:0903.2102](https://arxiv.org/abs/0903.2102)).

## Threshold

- Phenomenological noise: $3.05(4)\%$ under IP decoder  ([arXiv:1108.5738](https://arxiv.org/abs/1108.5738)) and $2.08(1)\%$ under projection decoder  ([arXiv:1402.3037](https://arxiv.org/abs/1402.3037)).
- Circuit-level noise: $0.082(3)\%$ under IP decoder, $0.143(1)\%$ under projection decoder  ([arXiv:1402.3037](https://arxiv.org/abs/1402.3037)), $0.143\%$ under matching decoder  ([arXiv:1407.5103](https://arxiv.org/abs/1407.5103)), and an analytic lower bound of $\approx 0.1\%$  ([arXiv:0907.1708](https://arxiv.org/abs/0907.1708)) (see  ([arXiv:1108.5738](https://arxiv.org/abs/1108.5738))).

## Realizations

- Neutral atom arrays: logical magic-state distillation using distance-three and five 4.8.8 color codes, observing an improvement in logical fidelity on a device by Quera  ([arXiv:2412.15165](https://arxiv.org/abs/2412.15165)).

## Relations

- _parent_: [[concepts/qec/2d-color]]
- _cousin_: [[concepts/qec/triangular-color]] — Lattice surgery scheme for a hybrid 6.6.6-4.8.8 layout yields lower resource overhead when compared to analogous surface code scheme  ([arXiv:2201.07806](https://arxiv.org/abs/2201.07806)).
- _cousin_: [`hypercubic`](https://errorcorrectionzoo.org/c/hypercubic) — The 4.8.8 (square-octagon) tiling is obtained by applying a fattening procedure to the square lattice  ([arXiv:cond-mat/0607736](https://arxiv.org/abs/cond-mat/0607736)).
