---
type: concept
name: Asymmetric quantum code (AQC)
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Noise-biased quantum code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/bacon-shor
- concepts/qec/binomial
- concepts/qec/clifford-deformed-surface
- concepts/qec/concatenated-steane
- concepts/qec/css
- concepts/qec/distance-balanced
- concepts/qec/eastab
- concepts/qec/floquet
- concepts/qec/galois-css
- concepts/qec/galois-polynomial
- concepts/qec/gkp
- concepts/qec/qecc
- concepts/qec/qsc
- concepts/qec/quantum-cyclic
- concepts/qec/quantum-hermitian-ag
- concepts/qec/quantum-mds
- concepts/qec/quantum-parity
- concepts/qec/quantum-reed-muller
- concepts/qec/subsystem-surface
- concepts/qec/surface
- concepts/qec/twisted-xzzx
- concepts/qec/two-dimensional-hyperbolic-surface
- concepts/qec/xysurface
- concepts/qec/xyz-color
- concepts/qec/xyz-hexagonal
- concepts/qec/xyz-product
- concepts/qec/xzzx
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/asymmetric_qecc
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: asymmetric_qecc
---

# Asymmetric quantum code (AQC)

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/asymmetric_qecc) (`code_id: asymmetric_qecc`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Quantum systems can be roughly characterized by two types of noise, a bit-flip noise that maps canonical basis states into each other, and a phase-flip noise that induces relative phases between superpositions of such basis states.
A code cannot protect against both types of noise arbitrarily well, and there is a tradeoff between the two types of protection.
An AQC is one that performs much better against one type of noise than the other type.
Such codes typically have tunable distances against each noise type and include CSS codes, GKP codes, and QSCs.

(source: raw/error-correction-zoo.md)

## Protection

Noise channels for which one type of noise is more prominent than the other are called *asymmetric-noise channels* or *biased-noise channels*.
An example of a noise-biased channel is a Pauli channel of independent $X$ and $Z$-type noise with $p_X \gg p_Z$ or vice versa.

In the context of comparing weight as well as of determining distances for noise models biased toward $X$- or $Z$-type errors, an extended notation for asymmetric CSS block quantum codes is $⟦n,k,(d_X,d_Z)⟧$ or $⟦n,k,d_X/d_Z⟧$, where $d_{X,Z}$ are the $X$- and $Z$-distances, respectively  ([arXiv:1207.6512](https://arxiv.org/abs/1207.6512)).
An asymmetric Singleton bound and linear programming bounds for asymmetric CSS codes have been formulated  ([doi:10.1098/rspa.2008.0439](https://doi.org/10.1098/rspa.2008.0439)), as well as asymmetric quantum GV bounds  ([arXiv:1705.04087](https://arxiv.org/abs/1705.04087)) and Hamming and Singleton bounds for general asymmetric subsystem codes  ([arXiv:0803.0764](https://arxiv.org/abs/0803.0764)).
Asymmetric MDS codes have been characterized  ([arXiv:0803.0764](https://arxiv.org/abs/0803.0764), [arXiv:1006.1694](https://arxiv.org/abs/1006.1694)).

## General gates

- Taking into account noise bias can reduce resource overhead in magic-state distillation schemes  ([arXiv:1509.05032](https://arxiv.org/abs/1509.05032)).
- A CNOT gate continuously connected to the identity cannot be noise-bias-preserving in finite dimensions  ([arXiv:0806.0383](https://arxiv.org/abs/0806.0383)) ([arXiv:1904.09474](https://arxiv.org/abs/1904.09474)).
- Qubit gates that preserve noise bias (after but not during each gate) correspond to permutations in the Pauli-$X$ basis  ([arXiv:2305.02045](https://arxiv.org/abs/2305.02045)). There is a bias-preserving Hadamard test  ([arXiv:2305.02045](https://arxiv.org/abs/2305.02045)) (see also Ref.  ([arXiv:2510.07532](https://arxiv.org/abs/2510.07532))).

## Decoders

- Measurement-free error correction has been optimized for biased noise  ([arXiv:2505.15669](https://arxiv.org/abs/2505.15669)).

## Threshold

- A lower bound on concatenated thresholds with CSS codes under biased noise  ([arXiv:0710.1301](https://arxiv.org/abs/0710.1301)).

## Fault tolerance

- Fault-tolerant noise-bias-preserving computation scheme  ([arXiv:0806.0383](https://arxiv.org/abs/0806.0383)).
- Fault-tolerant circuits converting between asymmetric and symmetric subsystem codes  ([arXiv:0708.3969](https://arxiv.org/abs/0708.3969), [arXiv:0709.3875](https://arxiv.org/abs/0709.3875)).

## Relations

- _parent_: [[concepts/qec/qecc]]
- _cousin_: [[concepts/qec/distance-balanced]] — Distance balancing is a procedure that can convert an asymmetric CSS code into a less asymmetric one.
- _cousin_: [[concepts/qec/subsystem-surface]] — Subsystem surface codes perform well against biased circuit-level noise  ([arXiv:2010.09626](https://arxiv.org/abs/2010.09626)).
- _cousin_: [[concepts/qec/clifford-deformed-surface]] — Random Clifford deformation can improve performance of surface codes against biased noise  ([arXiv:2201.07802](https://arxiv.org/abs/2201.07802), [arXiv:2211.02116](https://arxiv.org/abs/2211.02116)).
- _cousin_: [[concepts/qec/xysurface]] — XY surface codes perform well against biased noise  ([arXiv:1708.08474](https://arxiv.org/abs/1708.08474)).
- _cousin_: [[concepts/qec/xyz-product]] — XYZ product codes can be used to protect against biased noise  ([arXiv:2408.03123](https://arxiv.org/abs/2408.03123)).
- _cousin_: [[concepts/qec/xyz-color]] — XYZ color codes perform well against biased noise  ([arXiv:2203.16534](https://arxiv.org/abs/2203.16534)).
- _cousin_: [[concepts/qec/twisted-xzzx]] — Twisted XZZX codes perform well against biased noise  ([arXiv:1703.08179](https://arxiv.org/abs/1703.08179), [arXiv:2009.07851](https://arxiv.org/abs/2009.07851), [arXiv:2203.16486](https://arxiv.org/abs/2203.16486)); see also Ref.  ([arXiv:1112.1613](https://arxiv.org/abs/1112.1613)).
- _cousin_: [[concepts/qec/xzzx]] — The XZZX surface code can be foliated for a noise-bias preserving MBQC  ([arXiv:2201.10566](https://arxiv.org/abs/2201.10566)) or FBQC  ([arXiv:2303.16122](https://arxiv.org/abs/2303.16122)) protocol; see also  ([arXiv:1308.4776](https://arxiv.org/abs/1308.4776)).
- _cousin_: [[concepts/qec/concatenated-steane]] — Concatenating while taking into account noise bias can reduce resource overhead  ([arXiv:0709.3875](https://arxiv.org/abs/0709.3875)).
- _cousin_: [[concepts/qec/quantum-mds]] — An asymmetric Singleton bound and linear programming bounds for asymmetric CSS codes have been formulated   ([doi:10.1098/rspa.2008.0439](https://doi.org/10.1098/rspa.2008.0439)). Asymmetric MDS codes have been characterized  ([arXiv:1006.1694](https://arxiv.org/abs/1006.1694)).
- _cousin_: [[concepts/qec/two-dimensional-hyperbolic-surface]] — Asymmetric 2D hyperbolic surface codes have been constructed  ([arXiv:2105.01144](https://arxiv.org/abs/2105.01144)).
- _cousin_: [[concepts/qec/surface]] — The surface code on the honeycomb tiling is an asymmetric CSS code  ([arXiv:2105.01144](https://arxiv.org/abs/2105.01144)).
- _cousin_: [[concepts/qec/css]] — In the context of comparing weight as well as of determining distances for noise models biased toward $X$- or $Z$-type errors, an extended notation for asymmetric CSS block quantum codes is $⟦n,k,(d_X,d_Z),w⟧$ or $⟦n,k,d_X/d_Z,w⟧$.
- _cousin_: [[concepts/qec/galois-css]] — Most known Galois-qudit AQC families are derived from the asymmetric Galois-qudit CSS construction , and assuming the MDS conjecture, all possible parameters for pure Galois-qudit CSS asymmetric MDS codes have been determined .
- _cousin_: [[concepts/qec/quantum-reed-muller]] — Asymmetric quantum RM codes have been constructed  ([doi:10.1098/rspa.2008.0439](https://doi.org/10.1098/rspa.2008.0439)).
- _cousin_: [`pg_ldpc`](https://errorcorrectionzoo.org/c/pg_ldpc) — FG-LDPC codes can be used to construct asymmetric CSS codes  ([doi:10.1098/rspa.2008.0439](https://doi.org/10.1098/rspa.2008.0439)) ([arXiv:0804.4316](https://arxiv.org/abs/0804.4316)).
- _cousin_: [[concepts/qec/quantum-hermitian-ag]] — One-point and two-point Hermitian codes can be used to construct asymmetric Galois-qudit CSS codes, and the two-point construction can improve on the corresponding one-point codes  ([arXiv:1102.3605](https://arxiv.org/abs/1102.3605)).
- _cousin_: [[concepts/qec/galois-polynomial]] — Asymmetric Galois-qudit RS codes have been constructed  ([arXiv:0812.5104](https://arxiv.org/abs/0812.5104)) ([doi:10.1007/s11128-011-0269-3](https://doi.org/10.1007/s11128-011-0269-3)).
- _cousin_: [[concepts/qec/bacon-shor]] — Bacon-Shor code parameters against bit- and phase-noise can be optimized by changing the block geometry, yielding good performance against biased noise  ([arXiv:1209.0794](https://arxiv.org/abs/1209.0794)). A fault-tolerant teleportation-based computation scheme for asymmetric Bacon-Shor codes is effective against highly biased noise  ([arXiv:1211.1400](https://arxiv.org/abs/1211.1400)).
- _cousin_: [[concepts/qec/gkp]] — GKP code parameters against position and momentum displacements can be tuned by the choice of lattice (e.g., square vs rectangular).
- _cousin_: [[concepts/qec/binomial]] — Binomial code parameters against loss/gain errors and dephasing can be tuned.
- _cousin_: [[concepts/qec/qsc]] — QSC code parameters against loss/gain errors and Gaussian rotations can be tuned.
- _cousin_: [[concepts/qec/quantum-parity]] — QPC parameters against bit- and phase-noise can be tuned.
- _cousin_: [[concepts/qec/eastab]] — Entanglement can help decode asymmetric quantum codes  ([arXiv:1104.5004](https://arxiv.org/abs/1104.5004)).
- _cousin_: [[concepts/qec/floquet]] — Floquet codes can be adapted for asymmetric noise  ([arXiv:2411.04974](https://arxiv.org/abs/2411.04974)).
- _cousin_: [[concepts/qec/quantum-cyclic]] — Cyclic quantum codes can be adapted for asymmetric noise  ([arXiv:2501.16827](https://arxiv.org/abs/2501.16827)).
- _cousin_: [[concepts/qec/xyz-hexagonal]] — The XYZ$^2$ hexagonal stabilizer code has high thresholds under biased noise  ([arXiv:2505.03691](https://arxiv.org/abs/2505.03691)).

## Notes

- See Ref.  ([arXiv:1403.7755](https://arxiv.org/abs/1403.7755)) for a brief review of asymmetric quantum codes.
