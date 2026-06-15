---
type: concept
name: Dynamical code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Dynamical automorphism (DA) code
- Floquet code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/approximate-qecc
- concepts/qec/majorana-stab
- concepts/qec/monitored-random-circuits
- concepts/qec/qldpc
- concepts/qec/qubit-subsystem-stabilizer
- concepts/qec/qubits-into-qubits
- concepts/qec/qudit-da
- concepts/qec/topological-abelian
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/da
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: da
---

# Dynamical code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/da) (`code_id: da`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Dynamically generated stabilizer-based code whose (not necessarily periodic) sequence of few-body measurements implements state initialization, logical gates and error detection.

After each measurement in the sequence, the codespace is a joint $+1$ eigenspace of an *instantaneous stabilizer group (ISG)*, i.e., a particular stabilizer group corresponding to the measurement.
The ISG specifies the state of the system as a Pauli stabilizer state at a particular round of measurement, and it evolves into a (potentially) different ISG via code switching using the group $\mathsf{F}$ of check operators measured in the next step in the sequence.

As opposed to subsystem codes, only specific measurement sequences maintain the codespace, and not all sequences implement error detection.
Aperiodic measurement sequences provide a way to implement logical gates  ([arXiv:2307.10353](https://arxiv.org/abs/2307.10353)).

For dynamical codes based on topological phases, the phase associated with each ISG of the code can be obtained from a single *parent topological phase* associated with the dynamical code  ([arXiv:2212.00042](https://arxiv.org/abs/2212.00042)) via anyon condensation.
In this way, measurements cycle logical quantum information between the various condensed phases.

(source: raw/error-correction-zoo.md)

## Protection

\subsection{Classification of stabilizers by masking}
There exists an efficient classical algorithm that tracks information learned by syndrome extraction at each step  ([arXiv:2403.04163](https://arxiv.org/abs/2403.04163)).
The algorithm performs the following classification of stabilizers into unmasked, temporarily masked, and permanently masked stabilizers.

An unmasked stabilizer is a stabilizer whose outcome can be obtained by measurements.
In general, it is not obvious to determine if a stabilizer can be unmasked as its eigenvalue may only be revealed indirectly as a product of several measurements.
A temporarily masked stabilizer is a stabilizer whose syndrome cannot be obtained by the given sequence but could possibly be obtained with future measurements.
A permanently masked stabilizer is a stabilizer whose outcome is irreversibly lost by the given sequence.

For a masked stabilizer code with a set $U$ of $l$ masked stabilizers, its *masked distance* is given by:
\begin{equation}
    d_{\mathrm{u}} = \min\:\text{wt}\{ \mathsf{N}(U)\backslash \mathsf{G}\}~.
\end{equation}
Above, $\mathsf{G}$ is a gauge group defined from the algorithm that depends partly on the freedom in the choice of destabilizers for the temporarily masked stabilizers, and partly on the measurement sequence which fixes the destabilizers for the permanently masked stabilizers.

## Encoders

- A dynamical code with $r$ stabilizer generators can be initialized by a measurement sequence in at most $r$ cycles  ([arXiv:2403.04163](https://arxiv.org/abs/2403.04163)).

## General gates

- Code bounds for gates in the \term{Clifford hierarchy} (similar to the BK bounds) can be formulated for QLDPC codes that are embedded in a $D$-dimensional lattice but that admit some long-range connectivity  ([arXiv:2403.04163](https://arxiv.org/abs/2403.04163)).

## Decoders

- Temporal Petz recovery map  ([arXiv:2502.09177](https://arxiv.org/abs/2502.09177)).

## Relations

- _parent_: [[concepts/qec/qubits-into-qubits]]
- _parent_: [[concepts/qec/qudit-da]]
- _cousin_: [[concepts/qec/topological-abelian]] — Useful measurement sequences of dynamical codes can be extracted from topological quantum field theory  ([arXiv:2307.10353](https://arxiv.org/abs/2307.10353)).
- _cousin_: [[concepts/qec/approximate-qecc]] — Approximate versions of dynamical codes have been formulated  ([arXiv:2502.09177](https://arxiv.org/abs/2502.09177)).
- _cousin_: [[concepts/qec/qubit-subsystem-stabilizer]] — A dynamical code can be viewed as a subsystem qubit stabilizer code, albeit one with fewer logical qubits.
- _cousin_: [[concepts/qec/monitored-random-circuits]] — Both dynamical and monitored random circuit codes can have an instantaneous stabilizer group which evolves through unitary evolution and measurements. However, dynamical codewords are generated via a specific prescribed sequence of measurements, while random-circuit codes maintain a stabilizer group after any measurement. Dynamical codes have the additional capability of detecting errors induced during the measurement process; see Appx. A of Ref.  ([arXiv:2107.02194](https://arxiv.org/abs/2107.02194)).
- _cousin_: [[concepts/qec/majorana-stab]] — Dynamical codes are viable candidates for storage in Majorana-qubit devices  ([arXiv:2202.11829](https://arxiv.org/abs/2202.11829)).
- _cousin_: [[concepts/qec/qldpc]] — Using ZX calculus, an $⟦n,k,d⟧$ qubit stabilizer code admitting stabilizer generators of weight no more than $m$ can be *Floquetified* into an $⟦n+\lceil m/2 \rceil+\ell,k,d^{\prime}⟧$ dynamical code with single- and two-qubit operations, where $\ell \leq \log_{2} m$ and $d^{\prime} \geq d$  ([arXiv:2410.17240](https://arxiv.org/abs/2410.17240)) (see also Ref.  ([arXiv:2307.11136](https://arxiv.org/abs/2307.11136))). 
A more general locality-preserving *spacetime concatenation* procedure yields a dynamical code out of any qubit stabilizer code by structuring measurement gadgets using low-weight measurements while ensuring the preservation of logical information  ([arXiv:2504.08918](https://arxiv.org/abs/2504.08918)). 
In particular, spacetime concatenation reformulates the notion of a dynamical code associated with a stabilizer code in terms of code concatenation for every qubit (spatial concatenation) and measurements between these codes (temporal concatenation), leading to a temporal evolution of the stabilizer state  ([arXiv:2504.08918](https://arxiv.org/abs/2504.08918)). 
A matrix rank condition on the bond operators connecting the gadgets, called the Bond-Kernel-Rank Condition, and a strict locality preservation condition (SLPC), along with preservation of the operator algebra of the stabilizer code under the gadget action, preserves fault-tolerance and the spacetime distance of the code  ([arXiv:2504.08918](https://arxiv.org/abs/2504.08918)).
