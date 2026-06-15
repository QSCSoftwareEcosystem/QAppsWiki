---
type: concept
name: Dual-rail quantum code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/ampdamp
- concepts/qec/cluster-state
- concepts/qec/one-hot-quantum
- concepts/qec/oscillators-concatenated
- concepts/qec/quantum-parity
- concepts/qec/quantum-repetition
- concepts/qec/single-mode
- concepts/qec/stab-4-2-2
- concepts/qec/steane
- concepts/qec/two-mode-binomial
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/dual_rail
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: dual_rail
---

# Dual-rail quantum code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/dual_rail) (`code_id: dual_rail`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Two-mode bosonic code encoding a logical qubit in Fock states with one excitation.
The logical-zero state is represented by $|10\rangle$, while the logical-one state is represented by $|01\rangle$.
This encoding is often realized in temporal or spatial modes, corresponding to a *time-bin* or *frequency-bin* encoding.
Two different types of photon polarization can also be used.

This code is a DFS  ([arXiv:quant-ph/9807004](https://arxiv.org/abs/quant-ph/9807004), [arXiv:quant-ph/9902041](https://arxiv.org/abs/quant-ph/9902041), [arXiv:quant-ph/9908064](https://arxiv.org/abs/quant-ph/9908064), [arXiv:quant-ph/0007013](https://arxiv.org/abs/quant-ph/0007013)) with respect to phase errors  ([arXiv:quant-ph/0210072](https://arxiv.org/abs/quant-ph/0210072)).

(source: raw/error-correction-zoo.md)

## Protection

This is an error-detecting code against one photon loss event; it is often used in photonic quantum devices because of its ease of realization. A single loss event can be detected because, after the loss occurs, the output state $|00\rangle$ is orthogonal to the codespace. Recovery is not possible, so a successful run of a quantum circuit is conditioned on not losing a photon during the circuit.

Photon loss from a dual-rail or polarization encoding maps the qubit outside its two-dimensional codespace into a vacuum state, so it is naturally modeled as an erasure rather than as a qubit amplitude-damping channel .

For Deutsch''s  problem specifically, this code protects against errors resulting in states that have the correct photon number, but in the wrong modes  ([arXiv:quant-ph/9505011](https://arxiv.org/abs/quant-ph/9505011)).

## Encoders

- Optimal control pulses  ([arXiv:2311.04423](https://arxiv.org/abs/2311.04423))

## General gates

- General gates are performed using two-body Hamiltonian rotations  ([arXiv:quant-ph/0210072](https://arxiv.org/abs/quant-ph/0210072)).
- Bosonic gates include beamsplitters  ([doi:10.1038/s41467-023-41104-0](https://doi.org/10.1038/s41467-023-41104-0)) and Kerr nonlinearities. In particular, a cross Kerr rotation at angle $\pi$ induces a $CZ$ gate. Universal quantum computing can be achieved using the KLM protocol  ([doi:10.1038/35051009](https://doi.org/10.1038/35051009)) with only linear optical elements and photon detectors.
- Photon-number-conserving universal quantum logic can be implemented using continuous-time quantum walks on dual-rail transmon arrays  ([doi:10.1038/s41534-025-01147-1](https://doi.org/10.1038/s41534-025-01147-1)).
- Dynamical-decoupling protocols  ([arXiv:quant-ph/0210072](https://arxiv.org/abs/quant-ph/0210072), [arXiv:0712.1480](https://arxiv.org/abs/0712.1480)).
- A probabilistic CZ gate via a non-linear sign-shift gate, which transforms the Fock states $ \alpha|0\rangle+\beta|1\rangle+\gamma|2\rangle$ into $\alpha|0\rangle+\beta|1\rangle-\gamma|2\rangle $, followed by measurement  ([arXiv:quant-ph/0307015](https://arxiv.org/abs/quant-ph/0307015)).
- Error-detecting $CCZ$ and $cSWAP$ gates using three-level ancilla  ([arXiv:2212.11196](https://arxiv.org/abs/2212.11196)).
- Cavity-assisted bias-preserving CNOT gate  ([arXiv:2503.10935](https://arxiv.org/abs/2503.10935)).

## Fault tolerance

- Dual-rail qubits can be used to convert leakage and AD noise into erasure noise  ([arXiv:0710.1052](https://arxiv.org/abs/0710.1052), [arXiv:2208.05461](https://arxiv.org/abs/2208.05461)).

## Realizations

- The dual-rail code is ubiquitous in linear-optical quantum devices and is behind the KLM protocol, one of the first proposals for fault-tolerant computation. See reviews  ([arXiv:quant-ph/0512104](https://arxiv.org/abs/quant-ph/0512104), [arXiv:quant-ph/0512071](https://arxiv.org/abs/quant-ph/0512071), [arXiv:1907.06331](https://arxiv.org/abs/1907.06331)) for more details.
- Superconducting circuit devices: Gates have been demonstrated in the Schoelkopf group at Yale University  ([doi:10.1038/s41467-023-41104-0](https://doi.org/10.1038/s41467-023-41104-0)). Error detection has been demonstrated in 3D cavities in the Devoret group at Yale University  ([arXiv:2311.04423](https://arxiv.org/abs/2311.04423)) and Amazon Web Services  ([arXiv:2307.08737](https://arxiv.org/abs/2307.08737)) using transmon qubits, following earlier theoretical proposals  ([arXiv:2212.12077](https://arxiv.org/abs/2212.12077), [arXiv:2208.05461](https://arxiv.org/abs/2208.05461)). GHZ and Bell states as well as universal gates have been implemented on a four-qubit dual-rail code by the Yu group  ([arXiv:2504.12099](https://arxiv.org/abs/2504.12099)). Logical readout in 3D cavities has been demonstrated by Quantum Circuits Inc.  ([arXiv:2307.03169](https://arxiv.org/abs/2307.03169)). Cavity-assisted bias-preserving CNOT gate has been demonstrated  ([arXiv:2503.10935](https://arxiv.org/abs/2503.10935)).
- Photonic platforms: state preparation and measurement fidelity of $99.98\%$ in the C telecom band by PsiQuantum  ([arXiv:2404.17570](https://arxiv.org/abs/2404.17570)).

## Relations

- _parent_: [[concepts/qec/one-hot-quantum]]
- _parent_: [[concepts/qec/two-mode-binomial]] — The two-mode binomial code for $S=N=0$ reduces to the dual-rail code.
- _cousin_: [[concepts/qec/oscillators-concatenated]] — The KLM protocol, one of the first protocols for fault-tolerant quantum computation, utilizes concatenations of the dual-rail code with a stabilizer code such as the Steane code  ([doi:10.1038/35051009](https://doi.org/10.1038/35051009), [arXiv:quant-ph/0405112](https://arxiv.org/abs/quant-ph/0405112), [arXiv:quant-ph/0502101](https://arxiv.org/abs/quant-ph/0502101)). Concatenating the dual-rail code with an $⟦n,k,d⟧$ stabilizer code yields an $⟦2n,k,d⟧$ constant-excitation code  ([arXiv:2010.00538](https://arxiv.org/abs/2010.00538)) that protects against $d-1$ AD errors  ([arXiv:1001.2356](https://arxiv.org/abs/1001.2356)). Using the concatenation convention of the Zoo, concatenating the inner dual-rail code with an outer single-mode bosonic code yields several gates that are independent of the outer code  ([arXiv:1605.09278](https://arxiv.org/abs/1605.09278)).
- _cousin_: [[concepts/qec/steane]] — The KLM protocol, one of the first protocols for fault-tolerant quantum computation, utilizes concatenations of the dual-rail code with a stabilizer code such as the Steane code  ([doi:10.1038/35051009](https://doi.org/10.1038/35051009), [arXiv:quant-ph/0405112](https://arxiv.org/abs/quant-ph/0405112), [arXiv:quant-ph/0502101](https://arxiv.org/abs/quant-ph/0502101)).
- _cousin_: [[concepts/qec/single-mode]] — Using the concatenation convention of the Zoo, concatenating the inner dual-rail code with an outer single-mode bosonic code yields several gates that are independent of the outer code  ([arXiv:1605.09278](https://arxiv.org/abs/1605.09278)).
- _cousin_: [[concepts/qec/ampdamp]] — Dual-rail qubits can be used to convert leakage and AD noise into erasure noise  ([arXiv:0710.1052](https://arxiv.org/abs/0710.1052), [arXiv:2208.05461](https://arxiv.org/abs/2208.05461)). Concatenating the dual-rail code with an $⟦n,k,d⟧$ stabilizer code yields an $⟦2n,k,d⟧$ constant-excitation code  ([arXiv:2010.00538](https://arxiv.org/abs/2010.00538)) that protects against $d-1$ AD errors  ([arXiv:1001.2356](https://arxiv.org/abs/1001.2356)).
- _cousin_: [[concepts/qec/quantum-parity]] — An $⟦8,1,2⟧$ QPC correcting a single AD error is equivalent to a concatenation of the $\{|\overline{01}\rangle,|\overline{11}\rangle\}$ (constant-excitation) subcode of the $⟦4,2,2⟧$ code with the dual-rail code  ([arXiv:quant-ph/0103042](https://arxiv.org/abs/quant-ph/0103042), [arXiv:quant-ph/0501184](https://arxiv.org/abs/quant-ph/0501184), [arXiv:2010.00538](https://arxiv.org/abs/2010.00538)). More generally, an $⟦m^2,1,m⟧$ QPC corrects $m-1$ AD errors  ([arXiv:1001.2356](https://arxiv.org/abs/1001.2356)).
- _cousin_: [[concepts/qec/stab-4-2-2]] — An $⟦8,1,2⟧$ QPC correcting a single AD error is equivalent to a concatenation of the $\{|\overline{01}\rangle,|\overline{11}\rangle\}$ (constant-excitation) subcode of the $⟦4,2,2⟧$ code with the dual-rail code  ([arXiv:quant-ph/0103042](https://arxiv.org/abs/quant-ph/0103042), [arXiv:quant-ph/0501184](https://arxiv.org/abs/quant-ph/0501184), [arXiv:2010.00538](https://arxiv.org/abs/2010.00538)). More generally, an $⟦m^2,1,m⟧$ QPC corrects $m-1$ AD errors  ([arXiv:1001.2356](https://arxiv.org/abs/1001.2356)).
- _cousin_: [[concepts/qec/cluster-state]] — The KLM protocol can be combined with cluster states in various ways to yield MBQC protocols  ([arXiv:quant-ph/0303008](https://arxiv.org/abs/quant-ph/0303008), [arXiv:quant-ph/0402005](https://arxiv.org/abs/quant-ph/0402005), [arXiv:quant-ph/0405157](https://arxiv.org/abs/quant-ph/0405157)); see review  ([arXiv:1907.06331](https://arxiv.org/abs/1907.06331)).
- _cousin_: [[concepts/qec/quantum-repetition]] — The dual-rail code is an error space of the quantum repetition code for $n=2$ and is stabilized by $-ZZ$.
