---
type: concept
name: Bosonic code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Continuous-variable (CV) quantum code
- Oscillator code
- Quantum modulation scheme
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/block-quantum
- concepts/qec/hybrid-qudit-oscillator
- concepts/qec/single-spin
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/oscillators
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: oscillators
---

# Bosonic code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/oscillators) (`code_id: oscillators`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Encodes logical Hilbert space, finite- or infinite-dimensional, into a physical Hilbert space that contains at least one *oscillator* (a.k.a. *bosonic mode* or *qumode*).

States of a single oscillator correspond to $L^2$-normalizable functions on $\mathbb{R}$ that have finite energy, finite variance, and finite values of all other moments (where the energy operator is defined to be the harmonic oscillator Hamiltonian); such functions form *Schwartz space* (a.k.a. nuclear space  ([doi:10.1142/9038](https://doi.org/10.1142/9038))), a subspace of Hilbert space  ([arXiv:2211.05714](https://arxiv.org/abs/2211.05714)).
Ideal codewords may not be normalizable because the space is infinite-dimensional, so approximate versions have to be constructed in practice.

States can be represented by a series via a basis expansion, such as that in the countable basis of Fock states $|n\rangle$ with $n\geq 0$ for a single oscillator.
Alternatively, states can be represented as functions over the reals by expanding in a continuous "basis" (more technically, set of tempered distributions in the space dual to Schwartz space), such as the position "basis" $|y\rangle$ with $y\in\mathbb{R}$ or the momentum "basis" $|p\rangle$ with $p\in\mathbb{R}$.
A third option is to use coherent states $|\alpha\rangle$ with $\alpha\in\mathbb{C}$, which are eigenstates of the annihilation operator, which correspond to classical electromagnetic signals, and which resolve the identity  ([arXiv:math-ph/0210005](https://arxiv.org/abs/math-ph/0210005), [doi:10.1016/0034-4877(71)90006-1](https://doi.org/10.1016/0034-4877(71)90006-1), [doi:10.1103/PhysRevB.18.6744](https://doi.org/10.1103/PhysRevB.18.6744), [doi:10.1007/978-94-007-0196-0](https://doi.org/10.1007/978-94-007-0196-0)).
States can further be represented as functions over the joint position-momentum phase space in the Wigner function formalism  ([doi:10.1103/PhysRev.40.749](https://doi.org/10.1103/PhysRev.40.749), [doi:10.1103/PhysRevA.15.449](https://doi.org/10.1103/PhysRevA.15.449)).
GKP states have negative Wigner functions, but the alternative Zak-Gross Wigner function represents them positively  ([arXiv:2407.18394](https://arxiv.org/abs/2407.18394)).

An important subset of states is formed by the *Gaussian states*, which are in one-to-one correspondence with a (displacement) vector and covariance matrix  ([doi:10.1103/PhysRevA.37.3028](https://doi.org/10.1103/PhysRevA.37.3028), [arXiv:quant-ph/0410100](https://arxiv.org/abs/quant-ph/0410100), [arXiv:quant-ph/0503237](https://arxiv.org/abs/quant-ph/0503237), [arXiv:quant-ph/0701051](https://arxiv.org/abs/quant-ph/0701051), [arXiv:0801.4604](https://arxiv.org/abs/0801.4604), [arXiv:1110.3234](https://arxiv.org/abs/1110.3234), [arXiv:2010.15518](https://arxiv.org/abs/2010.15518), [arXiv:2102.05748](https://arxiv.org/abs/2102.05748), [arXiv:2409.11628](https://arxiv.org/abs/2409.11628)).
Pure Gaussian states correspond to the pure states with positive Wigner functions, a result known as Hudson's theorem  ([doi:10.1016/0034-4877(74)90007-X](https://doi.org/10.1016/0034-4877(74)90007-X), [doi:10.1063/1.525607](https://doi.org/10.1063/1.525607)).
Pure Gaussian states can be obtained from the *vacuum Fock state* $|n=0\rangle$ via a Gaussian unitary transformation (defined below). 
Any coherent state can be obtained from the vacuum Fock state, itself a coherent state, by a displacement.
There is a de Finetti theorem for Gaussian states  ([arXiv:1612.05080](https://arxiv.org/abs/1612.05080)).

(source: raw/error-correction-zoo.md)

## Protection

\subsection{Displacement error basis}

An error set relevant to bosonic stabilizer codes is the set of *displacement operators* (a.k.a. Weyl operators ), a bosonic analogue of the Pauli string basis for qubit codes.

\begin{defterm}{Displacement operators}
\label{topic:displacements}
For a single mode, its elements are products of exponentials of the mode's position and momentum operators, acting on the mode's position states $|y\rangle$ for $y\in\mathbb{R}$ as
\begin{align}
  e^{-iq\hat{p}}\left|y\right\rangle =\left|y+q\right\rangle \,\,\text{ and }\,\,e^{iq\hat{x}}\left|y\right\rangle =e^{iq y}\left|y\right\rangle ~,
\end{align}
where $q\in\mathbb{R}$.
The former is also called a translation, while the latter is called a modulation in signal processing.
For multiple modes, error set elements are tensor products of elements of the single-oscillator error set, characterized by the vector of coefficients $\xi\in\mathbb{R}^{2n}$.
\end{defterm}

The displacement error set is a unitary basis for bounded operators on the $n$-mode Hilbert space that is Dirac-orthonormal under the Hilbert-Schmidt inner product.
Expanding a bounded operator in terms of displacements is called the *Fourier-Weyl transform* (a.k.a.  Fourier-Weyl relation)  ([doi:10.1201/9781315118727](https://doi.org/10.1201/9781315118727)) ([doi:10.1103/PhysRev.177.1857](https://doi.org/10.1103/PhysRev.177.1857)).
For the expansion of Gaussian unitary operations in terms of displacements, see  ([doi:10.1007/3-7643-7575-2](https://doi.org/10.1007/3-7643-7575-2)).

There are two definitions of code distance associated with displacements.
The definition inherited from qubit codes is the minimum weight of a displacement operator (i.e., number of nonzero entries in $\xi$) that implements a nontrivial logical operation in the code. The second definition is the minimum Euclidean distance (i.e., $\ell^2$-norm of $\xi$) such that the corresponding displacement implements a nontrivial logical operation in the code.
Quantum weight enumerators and the Cohn-Elkies bound have been extended to the case of displacement noise  ([arXiv:2502.09514](https://arxiv.org/abs/2502.09514)).

\subsection{Loss and gain operators}

An error set relevant to Fock-state bosonic codes is the set of loss operators associated with the AD channel, a common form of physical noise in bosonic systems. 
For a single mode, loss operators are proportional to powers of the mode's annihilation operator $a=(\hat{x}+i\hat{p})/\sqrt{2}$, where $\hat x$ ($\hat p$) is the mode's position (momentum) operator, and with the power signifying the number of particles lost during the error. 
For multiple modes, error set elements are tensor products of elements of the single-mode error set. 
Quantum Hamming bounds have been extended to the case of loss noise  ([arXiv:1709.05302](https://arxiv.org/abs/1709.05302)) 

\subsection{Number-phase operators}

A related error set is the set of powers of the *Susskind–Glogower phase operator* $\frac{1}{\sqrt{a a^\dagger}} a$ and its adjoint  ([doi:10.1103/PhysicsPhysiqueFizika.1.49](https://doi.org/10.1103/PhysicsPhysiqueFizika.1.49), [doi:10.1016/0003-4916(91)90037-9](https://doi.org/10.1016/0003-4916(91)90037-9), [arXiv:quant-ph/0109066](https://arxiv.org/abs/quant-ph/0109066)) along with Fock-space rotations generated by the occupation number operator $a^\dagger a$.
These can also be obtained from qudit Pauli matrices through a limiting procedure  ([arXiv:quant-ph/0109066](https://arxiv.org/abs/quant-ph/0109066)) and allow one to expand trace-class operators despite not forming an orthonormal set  ([arXiv:2211.05714](https://arxiv.org/abs/2211.05714)). These operators correspond to the *number-phase interpretation*, a polar-like decomposition of a single mode, complementing the cartesian-like decomposition in terms of position and momentum displacements.
This decomposition can be called a number-phase rotor, which differs from the ordinary $U(1)$ rotor in the absence of states of negative angular momentum.  
Mathematically, the restriction of an ordinary rotor to states of non-negative momentum is a projection onto Hardy space, and the phase operator is an example of a Toeplitz operator on that space .

\subsection{Noise channels}

*Gaussian channels* are quantum channels that map Gaussian states to Gaussian states  ([doi:10.1016/0034-4877(79)90049-1](https://doi.org/10.1016/0034-4877(79)90049-1), [arXiv:quant-ph/0505151](https://arxiv.org/abs/quant-ph/0505151), [arXiv:0707.0604](https://arxiv.org/abs/0707.0604), [arXiv:0804.0511](https://arxiv.org/abs/0804.0511), [arXiv:0809.3273](https://arxiv.org/abs/0809.3273), [arXiv:1004.0196](https://arxiv.org/abs/1004.0196), [arXiv:1009.1108](https://arxiv.org/abs/1009.1108)); their Kraus representation is calculated in Ref.  ([arXiv:1012.4266](https://arxiv.org/abs/1012.4266)).
These include the AD channel and the displacement noise channel.
The algebraic structure of the Lie algebra of Gaussian channels is the same as that of the super-Poincare algebra in three-dimensional spacetime  ([arXiv:2507.04932](https://arxiv.org/abs/2507.04932)).

An important non-Gaussian noise channel is the dephasing noise channel, which applies a random rotation in phase space about the origin.

## Rate

The quantum capacity of the AD channel  ([arXiv:quant-ph/0606132](https://arxiv.org/abs/quant-ph/0606132)) and the dephasing noise channel  ([arXiv:2205.05736](https://arxiv.org/abs/2205.05736)) are both known.
The capacity of the displacement noise channel, the quantum analogue of AWGN, has been bounded using GKP codes  ([arXiv:quant-ph/0105058](https://arxiv.org/abs/quant-ph/0105058), [arXiv:1801.07271](https://arxiv.org/abs/1801.07271)).
Exact two-way assisted capacities have been obtained for the AD channels and quantum limited amplifiers in what is known as the PLOB bound  ([arXiv:1510.08863](https://arxiv.org/abs/1510.08863)).
Bounds exist on the two-way quantum and secret-key capacities for some prominent Gaussian channels  ([arXiv:quant-ph/9912067](https://arxiv.org/abs/quant-ph/9912067), [arXiv:1310.0129](https://arxiv.org/abs/1310.0129), [arXiv:1504.06390](https://arxiv.org/abs/1504.06390), [arXiv:1511.08710](https://arxiv.org/abs/1511.08710), [arXiv:1602.08898](https://arxiv.org/abs/1602.08898), [arXiv:1609.02169](https://arxiv.org/abs/1609.02169), [arXiv:1711.09909](https://arxiv.org/abs/1711.09909), [arXiv:1801.08102](https://arxiv.org/abs/1801.08102), [arXiv:1807.05402](https://arxiv.org/abs/1807.05402), [arXiv:2303.12867](https://arxiv.org/abs/2303.12867)) and non-Markovian channels, i.e., channels with memory effects  ([arXiv:2309.17066](https://arxiv.org/abs/2309.17066)). 
The continuous-variable erasure channel has a known quantum capacity  ([arXiv:2205.09711](https://arxiv.org/abs/2205.09711), [arXiv:2510.01424](https://arxiv.org/abs/2510.01424)).
Non-Gaussian channel capacities can be bounded for single  ([arXiv:1903.12615](https://arxiv.org/abs/1903.12615)) and multiple  ([arXiv:2212.11970](https://arxiv.org/abs/2212.11970)) modes.
Non-asymptotic bounds exist for memoryless channels  ([arXiv:2502.05524](https://arxiv.org/abs/2502.05524)) as well as for those with memory effects  ([arXiv:2503.13207](https://arxiv.org/abs/2503.13207)).
The optimal asymptotic error exponent of entanglement distillation is given by the reverse relative entropy of entanglement, a single-letter quantity  ([arXiv:2510.07121](https://arxiv.org/abs/2510.07121)).

## General gates

- Displacement operations form a group called the Heisenberg-Weyl group, the oscillator analogue to the Pauli group. Analogues of (non-Pauli) Clifford-group transformations are the *Gaussian unitary transformations* (a.k.a. symplectic, Bogoliubov-Valatin, or linear canonical transformations)  ([doi:10.1063/1.1665805](https://doi.org/10.1063/1.1665805), [arXiv:1110.3234](https://arxiv.org/abs/1110.3234)) (North Holland, 1986)}}, which are unitaries generated by quadratic polynomials in positions and momenta. The Gaussian unitary transformation group permutes displacement operators amongst themselves, and, up to any phases, is equivalent to the symplectic group $Sp(2n,\mathbb{R})$. Every Gaussian unitary can be decomposed into single-mode squeezing gates sandwiched by passive linear-optical transformations in what is known as the Bloch-Messiah (a.k.a. Euler) decomposition  ([arXiv:2403.04596](https://arxiv.org/abs/2403.04596), [doi:10.1201/9781315118727](https://doi.org/10.1201/9781315118727)).
- Computing using Gaussian states and Gaussian unitaries only can be efficiently simulated on a classical computer  ([arXiv:quant-ph/0109047](https://arxiv.org/abs/quant-ph/0109047), [arXiv:1210.1783](https://arxiv.org/abs/1210.1783), [arXiv:1208.3660](https://arxiv.org/abs/1208.3660)), and there are efficient algorithms to do so  ([arXiv:quant-ph/0503237](https://arxiv.org/abs/quant-ph/0503237), [arXiv:2502.12882](https://arxiv.org/abs/2502.12882)). This remains true even if superpositions of Gaussian states are considered  ([arXiv:2010.14363](https://arxiv.org/abs/2010.14363), [arXiv:2403.19059](https://arxiv.org/abs/2403.19059)), but is no longer the case when the number of modes scales exponentially  ([arXiv:2407.06290](https://arxiv.org/abs/2407.06290)).
- A gate generated by a cubic or higher-degree polynomial is required to make a universal gate set on the oscillator (an infinite-dimensional version of the Solovay-Kitaev theorem)  ([arXiv:quant-ph/9810082](https://arxiv.org/abs/quant-ph/9810082), [arXiv:quant-ph/0410100](https://arxiv.org/abs/quant-ph/0410100), [arXiv:2501.13857](https://arxiv.org/abs/2501.13857)). 
The cubic phase gate  ([arXiv:quant-ph/0008040](https://arxiv.org/abs/quant-ph/0008040)) is a common gate used in tandem with Gaussian gates for universality, and Fock-state matrix elements of the cubic and quartic phase gates have been derived  ([arXiv:2004.11002](https://arxiv.org/abs/2004.11002)) (see also Refs.  ([arXiv:1801.06565](https://arxiv.org/abs/1801.06565), [arXiv:1811.10651](https://arxiv.org/abs/1811.10651))). 
Arbitrary-degree polynomial gates are well defined, but cubic or higher versions of squeezing admit subtle mathematical properties  ([doi:10.1103/PhysRevD.29.1107](https://doi.org/10.1103/PhysRevD.29.1107), [doi:10.1103/physreva.35.1659](https://doi.org/10.1103/physreva.35.1659), [arXiv:2508.09041](https://arxiv.org/abs/2508.09041), [arXiv:2508.09044](https://arxiv.org/abs/2508.09044)). 
Unitaries generated by polynomials of position and momentum can exactly realize any finite-dimensional unitary evolution, and any physical bosonic unitary evolution can be approximated by a finite-dimensional unitary evolution  ([arXiv:2110.06942](https://arxiv.org/abs/2110.06942), [arXiv:2501.13857](https://arxiv.org/abs/2501.13857), [arXiv:2510.08546](https://arxiv.org/abs/2510.08546)). 
Certain non-quadratic Hamiltonians yield infinite-energy states in finite time  ([arXiv:2510.08545](https://arxiv.org/abs/2510.08545)).
See Ref.  ([arXiv:2410.04274](https://arxiv.org/abs/2410.04274)) for bosonic computational complexity classes. 
The stellar rank  ([arXiv:1907.11009](https://arxiv.org/abs/1907.11009)) and symplectic rank  ([arXiv:2504.19319](https://arxiv.org/abs/2504.19319)) quantify the degree of non-Gaussianity of bosonic states. 
Functional MPS can be used to simulate evolution of non-Gaussian states  ([arXiv:2504.05860](https://arxiv.org/abs/2504.05860)).
Universal bosonic quantum computations can be simulated in exponential time on a classical computer  ([arXiv:2503.03600](https://arxiv.org/abs/2503.03600)).
- There is a bosonic analogue of the \term{Clifford hierarchy}  ([arXiv:quant-ph/0208022](https://arxiv.org/abs/quant-ph/0208022), [arXiv:2507.01146](https://arxiv.org/abs/2507.01146)).
- Controllability of bosonic states has been proven when the normalizable state space is restricted to Schwartz space  ([arXiv:quant-ph/0505063](https://arxiv.org/abs/quant-ph/0505063)) and using polynomials in position and momentum  ([arXiv:2501.13857](https://arxiv.org/abs/2501.13857)).
- Measurements can be performed by homodyne, heterodyne, and generalized homodyne measurements  ([arXiv:quant-ph/0511044](https://arxiv.org/abs/quant-ph/0511044)).
- The number-phase interpretation allows for the mapping of rotor Clifford gates into the oscillator, some of which become non-unitary (e.g., conditional occupation number addition)  ([arXiv:2311.07679](https://arxiv.org/abs/2311.07679)).
- ZX calculus has been extended to bosonic codes for both Gaussian operators  ([arXiv:2405.07246](https://arxiv.org/abs/2405.07246)), Fock-state based operators  ([arXiv:2406.02905](https://arxiv.org/abs/2406.02905)), and passive linear-optical transformations  ([arXiv:2402.17693](https://arxiv.org/abs/2402.17693)). An earlier graphical calculus exists for Gaussian pure states  ([arXiv:1007.0725](https://arxiv.org/abs/1007.0725)).
- Circuits can be decomposed into a series of primitives such as quantum lattice gates, which are exponentials of cosines and sines of position and momentum  ([arXiv:2410.17069](https://arxiv.org/abs/2410.17069)).
- Number-phase teleportation can be done using a two-mode squeezed state  ([arXiv:quant-ph/9812018](https://arxiv.org/abs/quant-ph/9812018)).

## Relations

- _parent_: [[concepts/qec/block-quantum]] — Bosonic codes are block quantum codes with $\Sigma=\mathbb{R}$.
- _parent_: [[concepts/qec/hybrid-qudit-oscillator]] — Mixed oscillator codes defined only on oscillators reduce to oscillator codes.
- _cousin_: [`analog`](https://errorcorrectionzoo.org/c/analog) — Bosonic codes are quantum counterparts of analog codes.
- _cousin_: [`t-designs`](https://errorcorrectionzoo.org/c/t-designs) — Gaussian states, under a particular measure, do not form rigged two-designs  ([arXiv:1110.1042](https://arxiv.org/abs/1110.1042)).
- _cousin_: [[concepts/qec/single-spin]] — Bosonic states are typically represented with the assumption that a common phase reference exists, and the superselection rule compliant (SSRC) framework yields expressions without this assumption  ([doi:10.1103/PhysRev.155.1428](https://doi.org/10.1103/PhysRev.155.1428), [doi:10.1103/PhysRevA.55.3195](https://doi.org/10.1103/PhysRevA.55.3195), [arXiv:quant-ph/0306076](https://arxiv.org/abs/quant-ph/0306076), [arXiv:quant-ph/0507214](https://arxiv.org/abs/quant-ph/0507214), [arXiv:1112.1778](https://arxiv.org/abs/1112.1778), [arXiv:2501.03943](https://arxiv.org/abs/2501.03943), [arXiv:2507.13245](https://arxiv.org/abs/2507.13245)). In this framework, single-mode states can be treated as two-mode states in a fixed subspace of total occupation number $N$ in the limit $N \to \infty$. Passive Gaussian operations acting on the fixed-photon subspace of two modes realize $U(2)$ transformations in the Jordan-Schwinger boson mapping  ([doi:10.1007/BF01330618](https://doi.org/10.1007/BF01330618)) (Courier Dover Publications, 2015)},doi:10.1007/978-3-662-04589-3_4,doi:10.1103/RevModPhys.63.375}.

## Notes

- For an introduction to continuous-variable quantum systems, see reviews  ([arXiv:1912.09321](https://arxiv.org/abs/1912.09321), [arXiv:2002.11008](https://arxiv.org/abs/2002.11008), [arXiv:2008.13471](https://arxiv.org/abs/2008.13471), [arXiv:2010.08699](https://arxiv.org/abs/2010.08699), [arXiv:2103.09445](https://arxiv.org/abs/2103.09445), [arXiv:2111.08894](https://arxiv.org/abs/2111.08894), [arXiv:2211.05714](https://arxiv.org/abs/2211.05714)) and books  ([doi:10.1142/p489](https://doi.org/10.1142/p489), [doi:10.1201/9781315118727](https://doi.org/10.1201/9781315118727), [arXiv:2311.08445](https://arxiv.org/abs/2311.08445)).
- See  ([arXiv:2605.29137](https://arxiv.org/abs/2605.29137)) for a pedagogical introduction to bosonic codes.
- See video tutorial by [V. V. Albert](https://www.youtube.com/watch?v=zQQI3Ov6xyw).
