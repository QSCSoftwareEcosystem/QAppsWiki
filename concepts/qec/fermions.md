---
type: concept
name: Fermion code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/constant-excitation
- concepts/qec/fermions-into-qubits
- concepts/qec/oscillators
- concepts/qec/qubits-into-qubits
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/fermions
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: fermions
---

# Fermion code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/fermions) (`code_id: fermions`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Finite-dimensional quantum error-correcting code encoding a logical qudit or fermionic Hilbert space into a physical Fock space of fermionic modes.
Codes are typically described using Majorana operators, which are linear combinations of fermionic creation and annihilation operators  ([arXiv:quant-ph/0003137](https://arxiv.org/abs/quant-ph/0003137)).
Majorana operators may either be considered individually or paired in various ways into creation and annihilation operators to yield fermionic modes.
They form a Clifford algebra and can be interpreted as Ising anyons in certain contexts.

Admissible codewords include fermionic states, a subset of which is the Gaussian fermionic states  ([arXiv:quant-ph/0108033](https://arxiv.org/abs/quant-ph/0108033), [arXiv:quant-ph/0108010](https://arxiv.org/abs/quant-ph/0108010), [arXiv:quant-ph/0404180](https://arxiv.org/abs/quant-ph/0404180), [arXiv:2010.15518](https://arxiv.org/abs/2010.15518), [arXiv:2409.11628](https://arxiv.org/abs/2409.11628)).
Gaussian fermionic states are analogues of (non-displaced) Gaussian bosonic states; they are labeled by points in a Grassmannian and are sometimes called fermionic coherent states  ([doi:10.1002/9783527628285](https://doi.org/10.1002/9783527628285)). 
Fermionic analogues of ordinary (bosonic) coherent states are the fermionic coherent states labeled by Grassmann numbers  ([doi:10.1007/978-94-007-0196-0](https://doi.org/10.1007/978-94-007-0196-0)).
A Wigner function formalism has been developed for fermionic states  ([arXiv:2004.13860](https://arxiv.org/abs/2004.13860)).

(source: raw/error-correction-zoo.md)

## Protection

Majorana analogues of common qubit noise channels have been developed  ([arXiv:1806.01275](https://arxiv.org/abs/1806.01275)).

## Encoders

- A fermionic code using fermion Fock states as codewords cannot protect against occupation-number errors (i.e., dephasing) and does not admit fermionic logical operators  ([arXiv:2411.08955](https://arxiv.org/abs/2411.08955), [arXiv:2412.16081](https://arxiv.org/abs/2412.16081)).

## General gates

- Clifford operations on fermionic codes, shown  ([arXiv:quant-ph/0108033](https://arxiv.org/abs/quant-ph/0108033)) to be equivalent to match gates  ([doi:10.1145/380752.380785](https://doi.org/10.1145/380752.380785)), can be formulated using *Fermionic Linear Optics*, a classically simulable model of computation  ([arXiv:quant-ph/0108033](https://arxiv.org/abs/quant-ph/0108033), [arXiv:quant-ph/0108010](https://arxiv.org/abs/quant-ph/0108010), [arXiv:quant-ph/0404180](https://arxiv.org/abs/quant-ph/0404180), [arXiv:0804.4050](https://arxiv.org/abs/0804.4050), [arXiv:2010.15518](https://arxiv.org/abs/2010.15518), [arXiv:2409.11628](https://arxiv.org/abs/2409.11628)). The structure of the Majorana Clifford group has been studied  ([arXiv:2407.11319](https://arxiv.org/abs/2407.11319)).
- Non-Clifford gates can be done using gate teleportation, in which a gate can be obtained from a particular magic state (a.k.a. resource state)  ([arXiv:0804.4050](https://arxiv.org/abs/0804.4050), [arXiv:1308.1463](https://arxiv.org/abs/1308.1463), [arXiv:1602.03539](https://arxiv.org/abs/1602.03539), [arXiv:1905.08584](https://arxiv.org/abs/1905.08584), [arXiv:2501.06179](https://arxiv.org/abs/2501.06179)).
- General gates include qubit-like $S$, $T$, and $CZ$ gates acting on either logical qubit or logical fermionic encodings. Fermionic gates include braiding gates which correspond to exchanging Majorana modes. Hybrid gates include $CZ_{qf}$ gates between a logical qubit and a logical fermion. The braiding, $CZ_{f}$, $CZ_{qf}$, Hadamard, $S$, and $T$ gates are universal  ([arXiv:2411.08955](https://arxiv.org/abs/2411.08955)).
- Logical-fermion circuits constructed out of certain transversal gates do not admit a lower $T$ gate count than logical-qubit circuits  ([arXiv:2411.08955](https://arxiv.org/abs/2411.08955)).
- Using fermion codes with logical fermion encodings and the fermionic fast Fourier transform  ([arXiv:1706.00023](https://arxiv.org/abs/1706.00023)) can yield exponential improvements in circuit depth over fermion-into-qubit encodings  ([arXiv:2411.08955](https://arxiv.org/abs/2411.08955)).

## Relations

- _parent_: [[concepts/qec/qubits-into-qubits]] — The Majorana operator algebra is isomorphic to the qubit Pauli-operator algebra via various fermion-into-qubit encodings.
- _cousin_: [[concepts/qec/oscillators]] — Bosonic (fermionic) codes are associated with bosonic (fermionic) degrees of freedom.
- _cousin_: [[concepts/qec/fermions-into-qubits]] — Fermion (fermion-into-qubit) codes encode logical information into a physical space of fermionic modes (qubits).
The Majorana operator algebra is isomorphic to the qubit Pauli-operator algebra via various fermion-into-qubit encodings.
Using fermion codes with logical fermion encodings and the fermionic fast Fourier transform  ([arXiv:1706.00023](https://arxiv.org/abs/1706.00023)) can yield exponential improvements in circuit depth over fermion-into-qubit encodings  ([arXiv:2411.08955](https://arxiv.org/abs/2411.08955)).
- _cousin_: [[concepts/qec/constant-excitation]] — Fermion codewords lying in a fixed fermion-number subspace have to lie in the same subspace in order to protect against changes in fermion number  ([arXiv:2411.08955](https://arxiv.org/abs/2411.08955)).

## Notes

- See Ref.  ([arXiv:1404.0897](https://arxiv.org/abs/1404.0897)) for an introduction to Majorana-based qubits.
