---
type: concept
name: Entanglement-assisted (EA) c-q code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Entanglement-assisted classical communication (EACC) code
- Entanglement-assisted classical code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/bosonic-classical-into-quantum
- concepts/qec/eaqecc
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/ea_classical_into_quantum
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: ea_classical_into_quantum
---

# Entanglement-assisted (EA) c-q code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/ea_classical_into_quantum) (`code_id: ea_classical_into_quantum`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Classical-quantum code whose encoding and decoding utilize pre-shared entanglement between sender and receiver.
The sender encodes classical information into quantum systems sent through a quantum channel, while the receiver decodes using the channel outputs together with retained halves of pre-shared entangled states.

(source: raw/error-correction-zoo.md)

## Protection

A finite-block EACC code is often denoted by $[n,k,d;c]_q$, where $n$ is the number of $q$-dimensional channel uses, $q^k$ is the number of classical messages, $d$ is the minimum distance, and $c$ is the number of pre-shared maximally entangled qudit pairs.
Such a code corrects $d-1$ erasures or $\left\lfloor(d-1)/2\right\rfloor$ errors in the setting of Ref.  ([arXiv:2310.19774](https://arxiv.org/abs/2310.19774)).

## Rate

The entanglement-assisted classical capacity $C^{\rm ea}(T)$ is the highest asymptotic rate for reliable classical communication through a quantum channel $T$ when arbitrary pre-shared entanglement is available  ([doi:10.1103/PhysRevLett.83.3081](https://doi.org/10.1103/PhysRevLett.83.3081), [doi:10.1109/TIT.2002.802612](https://doi.org/10.1109/TIT.2002.802612)).
For lossy bosonic channels with high thermal noise and low transmitted photon number, pre-shared entanglement can yield a capacity ratio scaling as $\log(1/N_S)$ relative to the unassisted Holevo capacity  ([arXiv:2001.03934](https://arxiv.org/abs/2001.03934), [arXiv:2208.07979](https://arxiv.org/abs/2208.07979)).
If the encoding and decoding circuits themselves are noisy, the fault-tolerant EA capacity approaches the usual EA capacity as the gate error tends to zero  ([arXiv:2210.02939](https://arxiv.org/abs/2210.02939)).

## Encoders

- Super-dense coding maps two $q$-ary classical symbols to one transmitted qudit when one maximally entangled qudit pair is available  ([doi:10.1103/PhysRevLett.69.2881](https://doi.org/10.1103/PhysRevLett.69.2881)).

## Relations

- _parent_: [`eaoaecc`](https://errorcorrectionzoo.org/c/eaoaecc) — An EAOA QECC that has no gauge structure (e.g., gauge qubits), that has a block structure that corresponds to a classical code, that stores no quantum information, and that utilizes pre-shared entanglement is an EA c-q code.
- _cousin_: [[concepts/qec/bosonic-classical-into-quantum]] — Bosonic EA c-q schemes use pre-shared continuous-variable entanglement to assist bosonic c-q communication, including structured transceivers for lossy thermal-noise channels  ([arXiv:2001.03934](https://arxiv.org/abs/2001.03934), [arXiv:2208.07979](https://arxiv.org/abs/2208.07979)).
- _cousin_: [`eacq`](https://errorcorrectionzoo.org/c/eacq) — EA c-q codes transmit only classical information with entanglement assistance, while EA hybrid QECCs transmit both classical and quantum information with entanglement assistance.
- _cousin_: [[concepts/qec/eaqecc]] — EA c-q codes transmit classical information with entanglement assistance, while EAQECCs transmit quantum information with entanglement assistance.
