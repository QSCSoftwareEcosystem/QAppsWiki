---
type: concept
name: Pastawski-Yoshida-Harlow-Preskill (HaPPY) code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Perfect holographic code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/ame
- concepts/qec/holographic-tensor
- concepts/qec/majorana-stab
- concepts/qec/qubit-stabilizer
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/happy
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: happy
---

# Pastawski-Yoshida-Harlow-Preskill (HaPPY) code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/happy) (`code_id: happy`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Holographic code constructed from six-leg five-qubit perfect tensors placed on hyperbolic pentagon and hexagon tilings.
The code serves as a minimal model for several aspects of the AdS/CFT holographic duality  ([arXiv:1706.08823](https://arxiv.org/abs/1706.08823)) and potentially a dS/CFT duality  ([arXiv:2201.11658](https://arxiv.org/abs/2201.11658)).

It has been generalized to higher dimensions  ([arXiv:2112.12468](https://arxiv.org/abs/2112.12468)) and to include gauge-like degrees of freedom on the links of the tensor network  ([arXiv:1611.05841](https://arxiv.org/abs/1611.05841), [arXiv:2108.11402](https://arxiv.org/abs/2108.11402)).
In the lifted version, the bulk symmetry of the HaPPY code can be interpreted as arising from restricting a bulk gauge-like theory to a fixed-flux sector  ([arXiv:2108.11402](https://arxiv.org/abs/2108.11402)).
All boundary global symmetries must be dual to bulk gauge symmetries, and vice versa  ([arXiv:1810.05338](https://arxiv.org/abs/1810.05338)).

The construction below is described for qubits, but the underlying five-leg perfect tensor also has modular-qudit and oscillator extensions, and a rotor version can be stacked into an approximately error-correcting $U(1)$-covariant holographic code  ([arXiv:1902.07714](https://arxiv.org/abs/1902.07714)).
Encoding is accomplished using a tensor network of five-qubit encoding isometries, which are six-legged perfect tensors (with five legs corresponding to the physical qubits and one for the encoded logical qubit).

To construct the encoding, one first uniformly tiles the hyperbolic AdS/CFT disc using pentagons and hexagons.
Then, one places a 6-legged five-qubit encoding tensor at each hexagon and pentagon, contracting legs between neighboring shapes and leaving one leg uncontracted at each pentagon.
This construction forms an encoding isometry from the uncontracted legs in the bulk to the uncontracted legs at the boundary.

The *single-qubit HaPPY code* has a central pentagon encoding one bulk operator and hexagons tiling all other layers.
The *pentagon-hexagon HaPPY code* has alternating layers of pentagons and hexagons in the tiling.
The *pentagon HaPPY code* (a.k.a. the hyperbolic pentagon code, or HyPeC) consists of a purely pentagonal tiling.

(source: raw/error-correction-zoo.md)

## Protection

Protects against erasure errors and Pauli errors on the boundary qubits.

## Rate

The pentagon HaPPY code has an asymptotic rate $\frac{1}{\sqrt{5}} \approx 0.447$. The pentagon-hexagon HaPPY code has a rate of $0.299$ if the last layer is a pentagon layer and a rate of $0.088$ if the last layer is a hexagon layer.

## Encoders

- Heisenberg-picture encoding is done through *tensor pushing*. Each bulk operator (logical) is pushed to an operator supported on a portion of the boundary region (physical). Pushing all the bulk operators through results in reconstruction of the boundary.
- ZX calculus based encoder for the pentagon HaPPY code  ([arXiv:2304.08363](https://arxiv.org/abs/2304.08363)).

## Transversal gates

- Any transversal gate of the five-qubit code is a transversal gate of the HaPPY code since the HaPPY code is constructed from five-qubit encoding tensors, which are covariant under such gates.
- For locality-preserving physical gates on the boundary, the set of transversally implementable logical operations in the bulk is strictly contained in the Clifford group  ([arXiv:2103.13404](https://arxiv.org/abs/2103.13404)).

## Decoders

- Hierarchical recovery model  ([arXiv:1503.06237](https://arxiv.org/abs/1503.06237)).
- The greedy algorithm reconstructs bulk operators by iteratively absorbing tensors for which at least half of the legs are already included; the resulting greedy geodesic gives an explicit boundary reconstruction region  ([arXiv:1503.06237](https://arxiv.org/abs/1503.06237)).

## Code capacity threshold

- $26\%$ for boundary erasure errors on the pentagon-hexagon HaPPY code under the greedy decoder  ([arXiv:1503.06237](https://arxiv.org/abs/1503.06237)).
- Lower bound of $1/12 \approx 8.3\%$ for boundary erasure errors on the single-qubit HaPPY code under hierarchical recovery  ([arXiv:1503.06237](https://arxiv.org/abs/1503.06237)). Numerical evidence indicates the threshold may be closer to $50\%$.
- There is no threshold for the pentagon HaPPY code as a constant number of errors (four) can make bulk recovery impossible  ([arXiv:1503.06237](https://arxiv.org/abs/1503.06237)).
- $16.3\%$ for boundary Pauli errors on the single-qubit HaPPY code with 3 layers using integer optimization decoder  ([arXiv:2008.10206](https://arxiv.org/abs/2008.10206)).
- $50\%$ against biased Pauli noise for single-qubit HaPPY code under tensor-network decoder  ([arXiv:2408.06232](https://arxiv.org/abs/2408.06232)).

## Threshold

- A single-qubit HaPPY code has a measurement threshold of one  ([arXiv:2209.12903](https://arxiv.org/abs/2209.12903)).

## Relations

- _parent_: [[concepts/qec/qubit-stabilizer]] — The HaPPY code is a stabilizer code because it is defined by a contracted network of stabilizer tensors; see  ([arXiv:1503.06237](https://arxiv.org/abs/1503.06237)).
- _parent_: [[concepts/qec/holographic-tensor]] — The encoding of a HaPPY code is a holographic tensor network consisting of pentagon and hexagon perfect tensors.
- _cousin_: [[concepts/qec/majorana-stab]] — The pentagon HaPPY code Hamiltonian can be expressed in terms of mutually commuting weight-two (two-body) Majorana operators  ([arXiv:1905.03268](https://arxiv.org/abs/1905.03268)).
- _cousin_: [[concepts/qec/ame]] — The encoding of a HaPPY code is a holographic tensor network consisting of pentagon and hexagon perfect tensors.

## Notes

- Reference  ([arXiv:2201.11658](https://arxiv.org/abs/2201.11658)) discusses the HaPPY code for an AdS_3 space and its relation to a dS_2 *braneworld* with a conformal boundary.
