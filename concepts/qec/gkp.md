---
type: concept
name: Square-lattice GKP code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/approximate-qecc
- concepts/qec/fusion
- concepts/qec/multimodegkp
- concepts/qec/oscillator-css
- concepts/qec/rotor
- concepts/qec/single-mode
- concepts/qec/spt
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/gkp
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: gkp
---

# Square-lattice GKP code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/gkp) (`code_id: gkp`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Single-mode GKP qudit-into-oscillator CSS code based on the rectangular lattice.
Its stabilizer generators are oscillator displacement operators $\hat{S}_q(2\alpha)=e^{-2i\alpha \hat{p}}$ and $\hat{S}_p(2\beta)=e^{2i\beta \hat{x}}$.
To ensure $\hat{S}_q(2\alpha)$ and $\hat{S}_p(2\beta)$ generate a stabilizer group that is Abelian, there is a constraint that $\alpha\beta=2q\pi$ where $q$ is an integer denoting the logical dimension.

Codewords can be expressed as equal weight superpositions of coherent states on a rectangular lattice in phase space with spatial period $2\sqrt{\pi}$.
The exact GKP state is non-normalizable, so approximate constructions have to be considered.

The $q=1$ trivial encoding is spanned by the *canonical GKP state* (a.k.a. *grid state* or qunaught state  ([arXiv:2008.12791](https://arxiv.org/abs/2008.12791))),
\begin{align}
  |GKP\rangle=\sum_{\ell\in\mathbb{Z}}|x=\ell\sqrt{2\pi}\rangle~,
\end{align}
where $|x\rangle$ are single-mode position states.

Single-mode GKP states have been introduced in quantum foundations research defining modular conjugate variables  ([doi:10.1007/BF00670008](https://doi.org/10.1007/BF00670008)) and in coherent-state theory associated with the Heisenberg-Weyl group  ([doi:10.1515/9781400889921](https://doi.org/10.1515/9781400889921)) ([doi:10.1007/BF01077648](https://doi.org/10.1007/BF01077648)) ([doi:10.1007/978-3-642-61629-7](https://doi.org/10.1007/978-3-642-61629-7)).
The Dirac-delta orthonormal and complete  ([doi:10.1103/PhysRevB.12.1118](https://doi.org/10.1103/PhysRevB.12.1118)) basis formed by the GKP canonical states and their error states is known as the *Zak basis*, discovered independently by Gelfand  and Zak  ([doi:10.1103/PhysRevLett.19.1385](https://doi.org/10.1103/PhysRevLett.19.1385)).
It is also called the Gelfand mapping, Weil-Brezin transform, and $kq$ representation in condensed-matter physics and signal processing  ([doi:10.1007/BF02391012](https://doi.org/10.1007/BF02391012)) ([doi:10.1007/978-1-4612-2016-9](https://doi.org/10.1007/978-1-4612-2016-9)) ([doi:10.1515/9781400882427](https://doi.org/10.1515/9781400882427)) (see Refs.  ([doi:10.1109/18.179336](https://doi.org/10.1109/18.179336)) for more history).
Expansion of a function on $\mathbb{R}$ in terms of this basis is called the *Zak transform*. 
The Segal-Bargmann representations of GKP states are the theta functions of the lowest Landau level on a torus  ([arXiv:2002.07718](https://arxiv.org/abs/2002.07718)) ([arXiv:2106.11093](https://arxiv.org/abs/2106.11093)) (see also Refs.  ([doi:10.1103/PhysRevB.31.2529](https://doi.org/10.1103/PhysRevB.31.2529), [doi:10.1007/978-0-8176-4577-9](https://doi.org/10.1007/978-0-8176-4577-9))).

(source: raw/error-correction-zoo.md)

## Protection

For stabilizers $\hat{S}_q(2\alpha),\hat{S}_p(2\beta)$, the code can correct displacement errors up to $\alpha/2$ in the $q$-direction and $\beta/2$ in the $p$-direction. Approximately protects against photon loss errors  ([arXiv:1506.05033](https://arxiv.org/abs/1506.05033), [arXiv:1708.05010](https://arxiv.org/abs/1708.05010)), outperforming most other codes designed to explicitly protect against loss  ([arXiv:1708.05010](https://arxiv.org/abs/1708.05010)). An analytical expression can be derived for the effective logical channel after loss  ([arXiv:2504.13497](https://arxiv.org/abs/2504.13497)). Very sensitive to dephasing errors  ([arXiv:2106.12989](https://arxiv.org/abs/2106.12989)). A biased-noise GKP error correcting code can be prepared by choosing $\alpha\neq \beta$. Expectation values of observables versus energy may be fit to a power law  ([arXiv:2512.03583](https://arxiv.org/abs/2512.03583)).

## Encoders

- Dissipative stabilization of finite-energy square-lattice GKP states using stabilizers conjugated by a *cooling* ( ([arXiv:1310.7596](https://arxiv.org/abs/1310.7596)), Appx. B) or *damping* operator, i.e., a damped exponential of the total occupation number  ([arXiv:2009.07941](https://arxiv.org/abs/2009.07941), [arXiv:2010.09681](https://arxiv.org/abs/2010.09681)). Preparation of approximate square-lattice GKP states has been studied both theoretically and experimentally  ([arXiv:1506.05033](https://arxiv.org/abs/1506.05033), [arXiv:1709.08580](https://arxiv.org/abs/1709.08580), [arXiv:1907.12487](https://arxiv.org/abs/1907.12487), [arXiv:1910.03673](https://arxiv.org/abs/1910.03673)). Various damped versions of GKP states are equivalent  ([arXiv:1910.08301](https://arxiv.org/abs/1910.08301), [arXiv:2012.12488](https://arxiv.org/abs/2012.12488)), and there exists a Fock-state expansion  ([arXiv:2002.11008](https://arxiv.org/abs/2002.11008)).
- Two Josephson junctions coupled by a gyrator  ([arXiv:2002.07718](https://arxiv.org/abs/2002.07718)).
- Periodic driving (a.k.a. Floquet engineering)  ([arXiv:2303.03541](https://arxiv.org/abs/2303.03541)).
- Approximate GKP states can be prepared using Gaussian operations and photon detectors  ([arXiv:1902.02323](https://arxiv.org/abs/1902.02323)).
- An optimal-size circuit using ancillary qubits can be used to prepare an approximate GKP state  ([arXiv:2410.19610](https://arxiv.org/abs/2410.19610)). The size of the circuit is linear in the logarithm of the approximation parameters of the GKP codes.
- Numerically optimized preparation from the vacuum Fock state using a universal bosonic gate set  ([arXiv:2506.13643](https://arxiv.org/abs/2506.13643)).
- Dissipative stabilization using a high-impedance LRC circuit and a Josephson junction  ([arXiv:2405.05671](https://arxiv.org/abs/2405.05671)).

## General gates

- Clifford gates can be realized by performing linear-optical operations, symplectic transformations and displacements, all of which are Gaussian operations. Pauli gates can be performed using displacement operators. Clifford gates are fault tolerant in the sense that they map bounded-size errors to bounded-size errors  ([arXiv:quant-ph/0008040](https://arxiv.org/abs/quant-ph/0008040)).
- By applying square-lattice GKP error correction to Gaussian input states, universality can be achieved without non-Gaussian elements  ([arXiv:1903.00012](https://arxiv.org/abs/1903.00012)).
- Square-root of the Hadamard gate performed via a Kerr interaction  ([arXiv:2507.09684](https://arxiv.org/abs/2507.09684)).
- $\sqrt{T}$ gate using a quadratic potential  ([arXiv:2507.19713](https://arxiv.org/abs/2507.19713)).

## Fault tolerance

- Clifford gates can be realized by performing linear-optical operations, symplectic transformations and displacements, all of which are Gaussian operations. Pauli gates can be performed using displacement operators. Clifford gates are fault tolerant in the sense that they map bounded-size errors to bounded-size errors  ([arXiv:quant-ph/0008040](https://arxiv.org/abs/quant-ph/0008040)).
- Error correction scheme is fault-tolerant to displacement noise as long as all input states have displacement errors less than $\sqrt{\pi}/6$  ([arXiv:quant-ph/0510107](https://arxiv.org/abs/quant-ph/0510107)).

## Decoders

- Syndrome measurement can be done by applying a controlled displacement controlled by an ancilla qubit. The syndrome information can be obtained by measuring the ancilla qubit after the controlled-displacement operation; see  ([arXiv:2106.12989](https://arxiv.org/abs/2106.12989)).
- Decoder  ([arXiv:2008.12791](https://arxiv.org/abs/2008.12791)) based on Knill error correction (a.k.a. telecorrection  ([arXiv:quant-ph/0601066](https://arxiv.org/abs/quant-ph/0601066))), which is based on teleportation  ([arXiv:quant-ph/0410199](https://arxiv.org/abs/quant-ph/0410199), [arXiv:quant-ph/0312190](https://arxiv.org/abs/quant-ph/0312190)).
- Pauli $X$, $Y$, and $Z$ measurements can be performed by measuring $-\hat{p}$, $\hat{x}-\hat{p}$, and $\hat{x}$, respectively. If the measurement outcome is close to an even multiple of $\sqrt{\pi}$, then the outcome is +1. If the measurement outcome is close to an odd multiple of $\sqrt{\pi}$, then the outcome is -1; see  ([arXiv:2106.12989](https://arxiv.org/abs/2106.12989)).
- Reinforcement learning decoder that uses only one ancilla qubit  ([arXiv:2211.09116](https://arxiv.org/abs/2211.09116)). It has been extended to utilize previously measured syndrome information  ([arXiv:2312.07391](https://arxiv.org/abs/2312.07391)).
- Knill and Steane error correction have been analytically compared  ([arXiv:2505.14775](https://arxiv.org/abs/2505.14775)).

## Realizations

- Motional degree of freedom of a trapped ion: square-lattice GKP encoding realized with the help of post-selection by Home group  ([arXiv:1807.01033](https://arxiv.org/abs/1807.01033), [arXiv:1907.06478](https://arxiv.org/abs/1907.06478)), followed by realization of reduced form of GKP error correction, where displacement error syndromes are measured to one bit of precision using an ion electronic state  ([arXiv:2010.09681](https://arxiv.org/abs/2010.09681)). State preparation also realized by Tan group  ([arXiv:2310.15546](https://arxiv.org/abs/2310.15546)). Universal gate set, including a two-qubit entangling gate, realized by Tan group  ([arXiv:2409.05455](https://arxiv.org/abs/2409.05455)). State initialization and application to measuring displacements  ([arXiv:2412.04865](https://arxiv.org/abs/2412.04865)).
- Microwave cavity coupled to superconducting circuits: reduced form of square-lattice GKP error correction, where displacement error syndromes are measured to one bit of precision using an ancillary transmon  ([arXiv:1907.12487](https://arxiv.org/abs/1907.12487)). Subsequent paper by Devoret group  ([arXiv:2211.09116](https://arxiv.org/abs/2211.09116)) uses reinforcement learning for error-correction cycle design and is the first to go beyond break-even error-correction, with the lifetime of a logical qubit exceeding the cavity lifetime by about a factor of two (see also  ([arXiv:2211.09319](https://arxiv.org/abs/2211.09319))). See Ref.  ([arXiv:2111.07965](https://arxiv.org/abs/2111.07965)) for another experiment. A feed-forward-free, i.e., fully autonomous protocol has also been implemented by Nord Quantique  ([arXiv:2310.11400](https://arxiv.org/abs/2310.11400)). Qudit encodings with $q=3,4$ have been realized, with logical error rates also beyond break even  ([arXiv:2409.15065](https://arxiv.org/abs/2409.15065)).
- Optical systems: GKP states and homodyne measurements have been realized in propagating telecom light by the Furusawa group  ([arXiv:2309.02306](https://arxiv.org/abs/2309.02306)) and on-chip by Xanadu Quantum Technologies  ([doi:10.1038/s41586-025-09044-5](https://doi.org/10.1038/s41586-025-09044-5)).
- Single-qubit $Z$-gate has been demonstrated  ([arXiv:1904.01351](https://arxiv.org/abs/1904.01351)) in the single-photon subspace of an infinite-mode space  ([arXiv:2310.12618](https://arxiv.org/abs/2310.12618)), in which time and frequency become bosonic conjugate variables of a single effective bosonic mode. In this context, GKP position-state wavefunctions are called Dirac combs or frequency combs.

## Relations

- _parent_: [[concepts/qec/multimodegkp]]
- _parent_: [[concepts/qec/oscillator-css]]
- _parent_: [[concepts/qec/single-mode]]
- _cousin_: [[concepts/qec/approximate-qecc]] — Square-lattice GKP codes approximately protect against photon loss  ([arXiv:1506.05033](https://arxiv.org/abs/1506.05033), [arXiv:1708.05010](https://arxiv.org/abs/1708.05010), [arXiv:1801.07271](https://arxiv.org/abs/1801.07271)).
- _cousin_: [[concepts/qec/rotor]] — Because square-lattice GKP error states are parameterized by two modular (i.e., periodic) variables of position and momentum, measuring one of the GKP stabilizers constrains the oscillator Hilbert space into that of a rotor.
- _cousin_: [`hypercubic`](https://errorcorrectionzoo.org/c/hypercubic) — GKP codewords, when written in terms of coherent states, form a square lattice in phase space.
- _cousin_: [[concepts/qec/fusion]] — GKP states can be used to perform computation in a fusion-based encoding .
- _cousin_: [[concepts/qec/spt]] — The Segal-Bargmann representations of GKP states are the theta functions of the lowest Landau level on a torus  ([arXiv:2002.07718](https://arxiv.org/abs/2002.07718)) ([arXiv:2106.11093](https://arxiv.org/abs/2106.11093)) (see also Refs.  ([doi:10.1103/PhysRevB.31.2529](https://doi.org/10.1103/PhysRevB.31.2529), [doi:10.1007/978-0-8176-4577-9](https://doi.org/10.1007/978-0-8176-4577-9), [arXiv:1507.08966](https://arxiv.org/abs/1507.08966))).

## Notes

- GKP syndrome extraction can be used for QKD with squeezed states  ([arXiv:quant-ph/0008046](https://arxiv.org/abs/quant-ph/0008046)).
