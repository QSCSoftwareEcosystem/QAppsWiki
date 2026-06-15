---
type: concept
name: Analog stabilizer code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Gaussian stabilizer code
- Linear stabilizer code
- Symplectic stabilizer code
- Wavepacket code
- Infinitely squeezed state code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/ame
- concepts/qec/galois-stabilizer
- concepts/qec/gkp-stabilizer
- concepts/qec/oscillator-stabilizer
- concepts/qec/oscillators-into-oscillators
- concepts/qec/qudit-stabilizer
- concepts/qec/stab-8-3-3
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/analog_stabilizer
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: analog_stabilizer
---

# Analog stabilizer code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/analog_stabilizer) (`code_id: analog_stabilizer`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

An oscillator-into-oscillator stabilizer code encoding logical oscillator modes into $n$ physical modes. If the code is defined by $r$ independent nullifiers, then it is denoted by $⟦n,n-r⟧_{\mathbb{R}}$ and encodes $k=n-r$ logical modes  ([arXiv:2503.15698](https://arxiv.org/abs/2503.15698)).
Any analog stabilizer state can be thought of as a pure Gaussian state that has been infinitely squeezed on all modes  ([arXiv:2503.15698](https://arxiv.org/abs/2503.15698)).

Analog stabilizer codes admit a continuous stabilizer group of displacements. This group can equivalently be defined in terms of its Lie algebra. The codespace is equivalently the common $0$-eigenvalue eigenspace of the Lie algebra generators, which are mutually commuting linear combinations of oscillator position and momentum operators called *nullifiers*  ([arXiv:0903.3233](https://arxiv.org/abs/0903.3233)) or *annihilators*.
An analog stabilizer code admitting a set of nullifiers such that each nullifier consists of either position or momentum operators is called an *analog CSS code*.

(source: raw/error-correction-zoo.md)

## Protection

Protects against erasures of, or any errors on, at most $d-1$ modes.
If an error operator does not commute with a nullifier, then that error is detectable. 
There are conditions on the encoding circuit which guarantee that the code can correct errors  ([doi:10.1103/PhysRevA.81.062305](https://doi.org/10.1103/PhysRevA.81.062305)).
The code can be further optimized to increase resolution between syndrome spaces for certain noise  ([doi:10.1103/PhysRevA.81.062305](https://doi.org/10.1103/PhysRevA.81.062305)).

Protection of logical modes against small displacements or other errors acting in every physical mode cannot be done using only Gaussian resources  ([arXiv:0811.3128](https://arxiv.org/abs/0811.3128)). For Gaussian displacement noise, linear oscillator encodings can at best squeeze the logical noise between conjugate quadratures rather than suppressing it in both simultaneously  ([arXiv:1810.00047](https://arxiv.org/abs/1810.00047)) (see also  ([arXiv:quant-ph/0204052](https://arxiv.org/abs/quant-ph/0204052), [arXiv:quant-ph/0204085](https://arxiv.org/abs/quant-ph/0204085))). 
There are no such restrictions for non-Gaussian noise  ([arXiv:0811.3616](https://arxiv.org/abs/0811.3616), [doi:10.1103/PhysRevA.81.062305](https://doi.org/10.1103/PhysRevA.81.062305)).

## Encoders

- Gaussian circuit applied to $k$ modes storing logical information and $n-k$ modes initialized in a position state.

## Decoders

- Homodyne measurement of nullifiers yields real-valued syndromes, and recovery can be performed by displacements conditional on the syndromes.

## Realizations

- One-sided device-independent QKD  ([arXiv:2212.03935](https://arxiv.org/abs/2212.03935)).

## Relations

- _parent_: [[concepts/qec/oscillator-stabilizer]] — Analog stabilizer codes are bosonic stabilizer codes with a continuous stabilizer group, corresponding to linear constraints on positions and momenta.
- _parent_: [[concepts/qec/oscillators-into-oscillators]]
- _cousin_: [[concepts/qec/gkp-stabilizer]] — Analog stabilizer codes protect logical modes against arbitrarily large displacements on a few modes, while oscillator-into-oscillator GKP codes protect an infinite-dimensional logical space against sufficiently small displacements in any number of modes. Encoding in analog-stabilizer (oscillator-into-oscillator GKP) codes can be done by a Gaussian operation acting on a tensor product of an arbitrary state in the first mode and position states (GKP states) on the remaining modes. For Gaussian displacement noise, linear oscillator encodings only squeeze the logical noise between conjugate quadratures  ([arXiv:1810.00047](https://arxiv.org/abs/1810.00047)), and protection of logical modes against small displacements cannot be done using only Gaussian resources  ([arXiv:quant-ph/0204052](https://arxiv.org/abs/quant-ph/0204052), [arXiv:0811.3128](https://arxiv.org/abs/0811.3128)), so oscillator-into-oscillator GKP codes can be thought of as analog stabilizer encodings utilizing non-Gaussian GKP resource states.
- _cousin_: [[concepts/qec/qudit-stabilizer]] — Prime-qudit stabilizer codes can be transformed into analog stabilizer codes on the same number of modes and logical modes, with distance at least as large as that of the original code  ([arXiv:2303.17000](https://arxiv.org/abs/2303.17000)).
- _cousin_: [[concepts/qec/galois-stabilizer]] — Galois-qudit stabilizer codes can be transformed into analog stabilizer codes; if the original code has $r$ linearly independent generators in the symplectic representation, the resulting analog code has parameters $⟦n,n-r,d^{\prime}⟧_{\mathbb{R}}$ with $d^{\prime}\geq d$  ([arXiv:2303.17000](https://arxiv.org/abs/2303.17000)).
- _cousin_: [[concepts/qec/stab-8-3-3]] — The eight-qubit Gottesman code has been extended to an analog stabilizer code  ([arXiv:quant-ph/0405064](https://arxiv.org/abs/quant-ph/0405064)).
- _cousin_: [[concepts/qec/ame]] — Analog stabilizer states are generically CV AME  ([arXiv:0901.1488](https://arxiv.org/abs/0901.1488)), and explicit constructions exist for any number of modes  ([arXiv:2503.15698](https://arxiv.org/abs/2503.15698)). The codespace of an analog stabilizer code with pure distance $d_{\textnormal{pure}}$ is a $(d_{\textnormal{pure}}-1)$-uniform space  ([arXiv:2503.15698](https://arxiv.org/abs/2503.15698)). Normalizable finitely squeezed versions of infinitely squeezed Gaussian states are locally thermal, up to corrections in the squeezing parameter  ([arXiv:0710.2868](https://arxiv.org/abs/0710.2868), [arXiv:0908.0114](https://arxiv.org/abs/0908.0114)).
- _cousin_: [`real_block`](https://errorcorrectionzoo.org/c/real_block) — Analog stabilizer codes are quantum counterparts of real block codes.
