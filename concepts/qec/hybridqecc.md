---
type: concept
name: Hybrid QECC
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/classical-into-quantum
- concepts/qec/qecc
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/hybridqecc
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: hybridqecc
---

# Hybrid QECC

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/hybridqecc) (`code_id: hybridqecc`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A quantum code which encodes both quantum and classical information.

Hybrid QECCs arise as the $e=0$ subclass of the EACQ formalism, i.e., the classically enhanced quantum codes that do not require pre-shared entanglement  ([arXiv:0802.2414](https://arxiv.org/abs/0802.2414)).

In general, a different quantum code $\mathsf{C}_j$ is associated with each classical
value $j \in \{0, 1, \ldots, l-1\}$, and the Hilbert space decomposes as
\begin{align}
  \mathsf{H} = \bigoplus_{j=0}^{l-1} \mathsf{C}_j \oplus \mathsf{C}^{\perp}~,
\end{align}
where $\mathsf{C}^{\perp}$ is the combined error space of all $l$ codes.
The simplest example encodes a single qubit and a single classical bit ($l = 2$):
a different quantum code is associated with each value $j \in \{0,1\}$, giving
$\mathsf{H} = \mathsf{C}_0 \oplus \mathsf{C}_1 \oplus \mathsf{C}^{\perp}$.
The error-correction conditions require the \term{Knill-Laflamme conditions} to hold within
each quantum code subspace $\mathsf{C}_j$  ([arXiv:1701.06963](https://arxiv.org/abs/1701.06963)), and that error operators
map different code subspaces to mutually orthogonal subspaces  ([arXiv:1701.06963](https://arxiv.org/abs/1701.06963)).

(source: raw/error-correction-zoo.md)

## Rate

The capacity of a hybrid quantum memory is determined by a convex region in the classical-quantum entropy plane  ([arXiv:quant-ph/0203105](https://arxiv.org/abs/quant-ph/0203105)). The quantum capacity for simultaneous transmission of classical and quantum information has been derived  ([arXiv:quant-ph/0311131](https://arxiv.org/abs/quant-ph/0311131)). The existence of a hybrid code protecting against a channel depends on certain matricial ranges  ([arXiv:1911.12744](https://arxiv.org/abs/1911.12744)).

## Relations

- _parent_: [`oaecc`](https://errorcorrectionzoo.org/c/oaecc) — An OAQECC which has no gauge structure (e.g., gauge qubits) but has a block structure that corresponds to a classical code is a hybrid QECC.
- _cousin_: [[concepts/qec/qecc]] — A hybrid QECC storing no classical information reduces to a QECC. Conversely, any QECC can be converted into a hybrid QECC by using a portion of its logical subspace to store only classical information.
- _cousin_: [[concepts/qec/classical-into-quantum]] — A hybrid QECC storing no quantum information reduces to a c-q code.
