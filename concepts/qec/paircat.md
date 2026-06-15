---
type: concept
name: Pair-cat code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/cat
- concepts/qec/fock-state
- concepts/qec/hamiltonian
- concepts/qec/tiger
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/paircat
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: paircat
---

# Pair-cat code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/paircat) (`code_id: paircat`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Two- or higher-mode extension of cat codes whose codewords are right eigenstates of powers of products of the modes' lowering operators. Many gadgets for cat codes have two-mode pair-cat analogues, with the advantage being that such gates can be done in parallel with a dissipative error-correction process.

Two-mode codewords are supported by Fock states with occupation number $\hat{n}_2-\hat{n}_1$ fixed to some integer $\Delta$. 
In the *two-component* case, $|\overline{0}_{\gamma,\Delta}\rangle \sim (|\gamma_\Delta\rangle + (-1)^\Delta |i\gamma_\Delta\rangle)/\sqrt{2}$ and $|\overline{1}_{\gamma,\Delta}\rangle \sim (|\gamma_\Delta\rangle - (-1)^\Delta |i\gamma_\Delta\rangle)/\sqrt{2}$  ([doi:10.1103/PhysRevA.51.1698](https://doi.org/10.1103/PhysRevA.51.1698), [arXiv:1801.05897](https://arxiv.org/abs/1801.05897)), where
\begin{align}
|\gamma_\Delta \rangle \propto \sum_{n=0}^\infty \frac{\gamma^{2n+\Delta}}{\sqrt{n! (n+\Delta)!}} |n,n+\Delta\rangle
\end{align}
is the corresponding pair-coherent state  ([doi:10.1088/0305-4470/9/9/011](https://doi.org/10.1088/0305-4470/9/9/011), [doi:10.1007/BF01646483](https://doi.org/10.1007/BF01646483), [doi:10.1103/PhysRevLett.57.827](https://doi.org/10.1103/PhysRevLett.57.827), [doi:10.1364/JOSAB.5.001940](https://doi.org/10.1364/JOSAB.5.001940)) with amplitude $\gamma > 0$, up to normalization.
The asymptotic expression of the codewords is valid in the limit of large energy, $|\gamma|^2\to\infty$.

(source: raw/error-correction-zoo.md)

## Protection

The occupation-number differences form the syndromes, as opposed to the photon-number parity for the single-mode cat code. Any loss event or combination of losses that changes the relative occupation-number differences between modes is detectable.

## Decoders

- Lindbladian-based dissipative encoding and autonomous QEC utilizing two-mode two-photon absorption  ([doi:10.1103/PhysRevLett.57.827](https://doi.org/10.1103/PhysRevLett.57.827)). Encoding passively protects against cavity dephasing, suppressing dephasing noise exponentially with $\gamma^2$.

## General gates

- Hamiltonian $X$, $XX$, $Z$ gates, holonomic $Z$ gate, control-phase gate.
- Bias-preserving gates  ([arXiv:2208.06913](https://arxiv.org/abs/2208.06913)).

## Realizations

- Microwave cavities coupled to superconducting circuits by the Wang group  ([arXiv:2209.11643](https://arxiv.org/abs/2209.11643)).

## Relations

- _parent_: [[concepts/qec/tiger]] — The pair-cat code is a tiger code with $G = (2,2)$ and $H = (1,-1)$  ([arXiv:2411.09668](https://arxiv.org/abs/2411.09668)).
- _parent_: [[concepts/qec/fock-state]]
- _cousin_: [[concepts/qec/cat]] — Cat (pair-cat) codewords are superpositions of coherent (pair-coherent) states. Many cat-code protocols have analogues for the two-mode pair-cat codes.
- _cousin_: [[concepts/qec/hamiltonian]] — Two-component pair-cat codewords form ground-state subspace of a multimode Kerr Hamiltonian.
