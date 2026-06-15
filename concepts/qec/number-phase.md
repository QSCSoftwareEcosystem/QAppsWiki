---
type: concept
name: Number-phase code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Single-mode translationally invariant Fock-state code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/bosonic-rotation
- concepts/qec/gkp
- concepts/qec/gkp-stabilizer
- concepts/qec/oscillator-stabilizer
- concepts/qec/rotor-gkp
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/number_phase
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: number_phase
---

# Number-phase code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/number_phase) (`code_id: number_phase`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Bosonic rotation code consisting of superpositions of Pegg-Barnett phase states  ([doi:10.1088/0305-4470/19/18/030](https://doi.org/10.1088/0305-4470/19/18/030)).

Pegg-Barnett phase states are expressed in terms of Fock states as
\begin{align}
|\phi\rangle \equiv \frac{1}{\sqrt{2\pi}}\sum_{n=0}^{\infty} \mathrm{e}^{\mathrm{i} n \phi} \ket{n}.
\end{align}
Since phase states and thus the ideal codewords are not normalizable, approximate versions need to be constructed. The codes' key feature is that, in the ideal case, phase measurement has zero uncertainty, making it a good candidate for a syndrome measurement.

Logical states of an order-$N$ number-phase qubit encoding are $|\overline{0}\rangle= \sum_{m=0}^{2N-1} |\phi = m\pi/N\rangle$ and $|\overline{1}\rangle = \sum_{m=0}^{2N-1} (-1)^m |\phi=m\pi/N\rangle$. By performing the summation over $m$, one finds that $|\overline{0}\rangle$ is supported on Fock states $|2kN\rangle$, while $|\overline{1}\rangle$ is supported on states $|(2k+1)N\rangle$, for $k \geq 0$.

(source: raw/error-correction-zoo.md)

## Protection

Number-phase codes detect up to $N$ photon loss or gain errors, and approximately correct rotations up to $\theta = \pi/N$.
However, the code is only approximately error-correcting due to the non-orthogonality of Pegg-Barnett phase states  ([doi:10.1088/0305-4470/19/18/030](https://doi.org/10.1088/0305-4470/19/18/030)), which act as the angular position states in the number-phase interpretation of the oscillator.

## Decoders

- Modular phase measurement done in the logical $X$, or dual, basis has zero uncertainty in the case of ideal number-phase codes. This is equivalent to a quantum measurement of the spectrum of the Susskind-Glogower phase operator  ([arXiv:1901.08071](https://arxiv.org/abs/1901.08071)). Approximate number-phase codes are characterized by vanishing phase uncertainty  ([arXiv:1901.08071](https://arxiv.org/abs/1901.08071)). Such measurements can be utilized for Knill error correction (a.k.a. telecorrection  ([arXiv:quant-ph/0601066](https://arxiv.org/abs/quant-ph/0601066))), which is based on teleportation  ([arXiv:quant-ph/0410199](https://arxiv.org/abs/quant-ph/0410199), [arXiv:quant-ph/0312190](https://arxiv.org/abs/quant-ph/0312190)). This type of error correction avoids the complicated correction procedures typical in Fock-state codes, but requires a supply of clean codewords  ([arXiv:1901.08071](https://arxiv.org/abs/1901.08071)). Performance of this method was analyzed in Ref.  ([arXiv:2108.01009](https://arxiv.org/abs/2108.01009)), and it was extended in Ref.  ([arXiv:2412.15134](https://arxiv.org/abs/2412.15134)).
- Number measurement can be done by extracting modular number information using a CROT gate $\mathrm{e}^{(2\pi \mathrm{i} / NM) \hat n \otimes \hat n}$ and performing phase measurements  ([doi:10.1007/978-88-7642-378-9](https://doi.org/10.1007/978-88-7642-378-9)) on an ancillary mode  ([arXiv:1901.08071](https://arxiv.org/abs/1901.08071)).

## Fault tolerance

- Fault-tolerant computation schemes with number-phase codes have been proposed based on concatenation with Bacon-Shor subsystem codes  ([arXiv:1901.08071](https://arxiv.org/abs/1901.08071)).

## Realizations

- Motional degree of freedom of a trapped ion: state initialization  ([arXiv:2412.04865](https://arxiv.org/abs/2412.04865)).

## Relations

- _parent_: [[concepts/qec/bosonic-rotation]] — Number-phase codes are bosonic rotation codes whose primitive state is a Pegg-Barnett phase state  ([doi:10.1088/0305-4470/19/18/030](https://doi.org/10.1088/0305-4470/19/18/030)).
- _cousin_: [[concepts/qec/rotor-gkp]] — Number-phase codes are obtained by projecting planar-rotor GKP codes onto the non-negative angular-momentum subspace and identifying that subspace with oscillator Fock space  ([arXiv:2311.07679](https://arxiv.org/abs/2311.07679)).
- _cousin_: [[concepts/qec/oscillator-stabilizer]] — Number-phase codewords span the joint right eigenspace of the $N$th power of the Susskind-Glogower phase operator and the bosonic rotation operator  ([arXiv:1901.08071](https://arxiv.org/abs/1901.08071)). These operators no longer form a group since the phase operator is not unitary.
- _cousin_: [[concepts/qec/gkp]] — Square-lattice GKP codes utilize translational symmetry in phase space, while number-phase codes utilize rotational symmetry. The two are related via a mapping  ([arXiv:2206.01751](https://arxiv.org/abs/2206.01751)).
- _cousin_: [[concepts/qec/gkp-stabilizer]] — Number-phase codes can serve as resource states for number-phase-rotor GKP-stabilizer codes, a polar analogue of oscillator-into-oscillator GKP codes that protects against photon loss and dephasing  ([arXiv:2311.07679](https://arxiv.org/abs/2311.07679)).
- _cousin_: [`t-designs`](https://errorcorrectionzoo.org/c/t-designs) — Pegg-Barnett phase states undergoing Kerr evolution, together with Fock states, form a rigged 2-design for a single mode  ([arXiv:2211.05127](https://arxiv.org/abs/2211.05127)).
