---
type: concept
name: XYZ$^2$ hexagonal stabilizer code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/dual-rail
- concepts/qec/matching
- concepts/qec/qubit-concatenated
- concepts/qec/xzzx
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/xyz_hexagonal
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: xyz_hexagonal
---

# XYZ$^2$ hexagonal stabilizer code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/xyz_hexagonal) (`code_id: xyz_hexagonal`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

An instance of the matching code based on the Kitaev honeycomb model. It is described on a honeycomb tiling with $XYZXYZ$ stabilizers on each hexagonal plaquette. Each vertical pair of qubits has an $XX$, $YY$, or $ZZ$ link stabilizer depending on the orientation of the plaquette stabilizers.

(source: raw/error-correction-zoo.md)

## Protection

As a stabilizer code with boundaries, protects a single qubit with parameters $⟦2 d^2, 1, d⟧$. Isolated $X$, $Y$, and $Z$ errors lead to unidirectional pairs of plaquette defects along the three directions of the honeycomb tiling.

## Decoders

- Maximum-likelihood decoding using the EWD decoder  ([arXiv:2112.01977](https://arxiv.org/abs/2112.01977)).
- Sequential decoder  ([arXiv:2505.03691](https://arxiv.org/abs/2505.03691)).

## Code capacity threshold

- $50\%$ for pure $Z$, $Y$, or $Z$ noise under maximum-likelihood decoding.
- Threshold matches that of the $XZZX$ code for various bias levels of $X$, $Y$, or $Z$ biased noise  under maximum-likelihood decoding.
- $\approx 18\%$ for depolarizing noise under maximum-likelihood decoding.
- $18.3\%$ under biased noise  ([arXiv:2505.03691](https://arxiv.org/abs/2505.03691)).

## Relations

- _parent_: [[concepts/qec/matching]]
- _parent_: [[concepts/qec/qubit-concatenated]] — The XYZ$^2$ hexagonal stabilizer code can be viewed as a concatenation of the $YZZY$ surface code with one of the possible $⟦2,1⟧$ repetition codes, with the case of the bit-flip repetition code yielding a concatenation of the surface code with the dual-rail code  ([arXiv:2505.03691](https://arxiv.org/abs/2505.03691)).
- _cousin_: [[concepts/qec/xzzx]] — The XYZ$^2$ hexagonal stabilizer code can be viewed as a concatenation of the $YZZY$ surface code with one of the possible $⟦2,1⟧$ repetition codes, with the case of the bit-flip repetition code yielding a concatenation of the surface code with the dual-rail code  ([arXiv:2505.03691](https://arxiv.org/abs/2505.03691)).
- _cousin_: [[concepts/qec/dual-rail]] — The XYZ$^2$ hexagonal stabilizer code can be viewed as a concatenation of the $YZZY$ surface code with one of the possible $⟦2,1⟧$ repetition codes, with the case of the bit-flip repetition code yielding a concatenation of the surface code with the dual-rail code  ([arXiv:2505.03691](https://arxiv.org/abs/2505.03691)).
