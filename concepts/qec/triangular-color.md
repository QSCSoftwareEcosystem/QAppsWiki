---
type: concept
name: Honeycomb (6.6.6) color code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/2d-color
- concepts/qec/lifted-product
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/triangular_color
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: triangular_color
---

# Honeycomb (6.6.6) color code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/triangular_color) (`code_id: triangular_color`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

2D color code defined on a (typically triangular) patch of the 6.6.6 (honeycomb) tiling.
The usual triangular patch has three differently colored boundaries, encodes one logical qubit, and is local-Clifford equivalent to a folded surface/toric code with two smooth and two rough boundaries  ([arXiv:1503.02065](https://arxiv.org/abs/1503.02065)).

Stabilizer generators are shown in \ref{figure:6.6.6-operators}.

(source: raw/error-correction-zoo.md)

## Protection

There is a $⟦(3d^2+1)/4, 1, d⟧$ code family  ([arXiv:1108.5738](https://arxiv.org/abs/1108.5738)) and a $⟦(3d-1)^2/4, 1, d⟧$ code family  ([arXiv:1911.00355](https://arxiv.org/abs/1911.00355)).

## Transversal gates

- CNOT gate because the code is CSS.
- Hadamard gates for any qubit geometry which yields a self-dual CSS code.

## General gates

- Lattice surgery scheme for a hybrid 6.6.6-4.8.8 layout yields lower resource overhead when compared to analogous surface code scheme  ([arXiv:2201.07806](https://arxiv.org/abs/2201.07806)).
- Low-overhead magic-state distillation circuit using flag qubits  ([arXiv:2003.03049](https://arxiv.org/abs/2003.03049)) or lattice surgery  ([arXiv:2409.07707](https://arxiv.org/abs/2409.07707)).

## Decoders

- Distance-three measurement schedule based on detector error models  ([arXiv:2407.13826](https://arxiv.org/abs/2407.13826)).
- Message-passing decoder  ([arXiv:1111.0831](https://arxiv.org/abs/1111.0831)).
- Adaptation of the restriction decoder  ([arXiv:1911.00355](https://arxiv.org/abs/1911.00355)).
- Neural-network decoder  ([arXiv:1802.08680](https://arxiv.org/abs/1802.08680)).
- Möbius matching decoder gives low logical failure rate  ([arXiv:2108.11395](https://arxiv.org/abs/2108.11395)) and has an open-source implementation called Chromöbius  ([arXiv:2312.08813](https://arxiv.org/abs/2312.08813)).
- AMBP4, a quaternary version  ([arXiv:2202.06612](https://arxiv.org/abs/2202.06612)) of the MBP decoder  ([arXiv:2104.13659](https://arxiv.org/abs/2104.13659)).
- MaxSAT-based decoder  ([arXiv:2303.14237](https://arxiv.org/abs/2303.14237)).
- Height-bound decision-tree decoder (DTD)  ([arXiv:2502.16408](https://arxiv.org/abs/2502.16408)).
- Most likely error (MLE) decoder  ([arXiv:2412.14256](https://arxiv.org/abs/2412.14256)).
- Neural network decoder  ([arXiv:2412.14256](https://arxiv.org/abs/2412.14256)).

## Fault tolerance

- Fault-tolerant syndrome extraction circuits using flag qubits  ([arXiv:1708.02246](https://arxiv.org/abs/1708.02246), [arXiv:1911.00355](https://arxiv.org/abs/1911.00355)).

## Code capacity threshold

- Independent $X,Z$ noise: $p_X = 7.8\%$ under message-passing decoder  ([arXiv:1111.0831](https://arxiv.org/abs/1111.0831)), $8.7\%$ under projection decoder  ([arXiv:1308.6207](https://arxiv.org/abs/1308.6207)), $\geq 6\%$ under rescaling decoder  ([arXiv:2112.09584](https://arxiv.org/abs/2112.09584)), $9.0\%$ under Möbius matching decoder  ([arXiv:2108.11395](https://arxiv.org/abs/2108.11395)), $10.1\%$ under MaxSAT-based decoder  ([arXiv:2303.14237](https://arxiv.org/abs/2303.14237)), and $8.2\%$ under concatenated MWPM decoder  ([arXiv:2404.07482](https://arxiv.org/abs/2404.07482)). The threshold under ML decoding corresponds to the value of a critical point of the two-dimensional three-body random-bond Ising model (RBIM) on the Nishimori line  ([doi:10.1143/JPSJ.55.3305](https://doi.org/10.1143/JPSJ.55.3305), [arXiv:0902.4845](https://arxiv.org/abs/0902.4845)), calculated to be $10.9(2)\%$ in Ref.  ([arXiv:0902.4845](https://arxiv.org/abs/0902.4845)) and $10.97(1)\%$ in Ref.  ([arXiv:0903.2102](https://arxiv.org/abs/0903.2102)).
- Depolarizing channel: $12.6\%$ under the restriction decoder  ([arXiv:1911.00355](https://arxiv.org/abs/1911.00355)) and the projection decoder  ([arXiv:1308.6207](https://arxiv.org/abs/1308.6207)), and $\approx 14.5\%$ under AMBP4 decoding  ([arXiv:2202.06612](https://arxiv.org/abs/2202.06612)).

## Threshold

- The threshold under ML decoding with measurement errors corresponds to the value of a critical point of a three-dimensional disordered Ising model, estimated to be $4.8(2)\%$  ([arXiv:1005.0777](https://arxiv.org/abs/1005.0777)).
- Circuit-level noise: $0.2\%$ using two flag qubits per stabilizer generator and the restriction decoder  ([arXiv:1911.00355](https://arxiv.org/abs/1911.00355)), and $0.46\%$ under concatenated MWPM decoder  ([arXiv:2404.07482](https://arxiv.org/abs/2404.07482)).
- A measurement threshold of one  ([arXiv:2402.00145](https://arxiv.org/abs/2402.00145)).

## Realizations

- Superconducting qubits: transversal Clifford gates, randomized logical benchmarking, and magic-state injection demonstrated on distance-three and five 6.6.6 color codes on the Willow device by Google Quantum AI  ([arXiv:2412.14256](https://arxiv.org/abs/2412.14256)). 
Logical state teleportation using lattice surgery performed between two distance-three color codes.
Magic-state cultivation was demonstrated on a device by Google Quantum AI by code switching between a distance-three 6.6.6 color code and distance-five $XZZX$ surface code and decoding with the Tesseract decoder  ([arXiv:2512.13908](https://arxiv.org/abs/2512.13908)).

## Relations

- _parent_: [[concepts/qec/2d-color]]
- _parent_: [[concepts/qec/lifted-product]] — The 6.6.6 color code can be formulated directly as an LP code  ([arXiv:2312.08462](https://arxiv.org/abs/2312.08462)).
- _cousin_: [`honeycomb`](https://errorcorrectionzoo.org/c/honeycomb) — The 6.6.6 color code is defined on the honeycomb tiling.
