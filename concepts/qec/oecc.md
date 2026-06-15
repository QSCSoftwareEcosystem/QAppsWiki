---
type: concept
name: Subsystem QECC
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Operator QECC (OQECC)
- Gauge QECC
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/qecc
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/oecc
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: oecc
---

# Subsystem QECC

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/oecc) (`code_id: oecc`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A quantum code which encodes quantum information in a tensor factor of a subspace that is decomposed into a tensor product of subsystems.

A subsystem code encodes information in a subsystem $\mathsf{A}$ of the code space $\mathsf{C}$, which is part of the system Hilbert space $\mathsf{H}$, as
\begin{align}
\mathsf{H}=\mathsf{C} \oplus \mathsf{C}^{\perp} = \mathsf{A} \otimes \mathsf{B} \oplus \mathsf{C}^{\perp}~.
\end{align}
Following an error, the encoded quantum information in subsystem $\mathsf{A}$ can be recovered modulo an arbitrary error on the auxiliary or *gauge* subsystem $\mathsf{B}$. 
The gauge subsystem provides additional freedom to the error correction process: errors that act trivially on the information subsystem $\mathsf{A}$ but nontrivially on $\mathsf{B}$ need not be corrected.
The subsystem $\mathsf{B}$ can encode *gauge qubits* when its dimension is a power of two.
While all operator QECCs are also ordinary QECCs, the attachment of a gauge subsystem to a code allows for a wider variety of encoding procedures, fault-tolerant logical operations, and efficient error-correction protocols.

(source: raw/error-correction-zoo.md)

## Protection

The necessary and sufficient error-correction conditions are, for all errors $E_a,E_b$ in an error set $\cal{E}$  ([arXiv:quant-ph/0506069](https://arxiv.org/abs/quant-ph/0506069)):
\begin{align}
\Pi E^{\dagger}_a E_b \Pi = I_{\mathsf{A}} \otimes g_{ab}^{\mathsf{B}}
\end{align}
where $\Pi$ is a projector onto the codespace $\mathsf{C}$, and $g_{ab}^{\mathsf{B}}$ is an arbitrary operator on the gauge subsystem $\mathsf{B}$.
This condition ensures that distinguishing and correcting errors based on their effect on subsystem $\mathsf{A}$ is sufficient; errors that act identically on $\mathsf{A}$ but differ on $\mathsf{B}$ are considered equivalent.

These can be studied in the presence of continuous noise  ([arXiv:0806.3145](https://arxiv.org/abs/0806.3145)).

A *unitarily recoverable subsystem* is a correctable subsystem whose logical information can be restored by a unitary operation, possibly into a different subsystem representation; thus, recovery is more relaxed than correction  ([arXiv:quant-ph/0608045](https://arxiv.org/abs/quant-ph/0608045)). In fact, every correctable subsystem is unitarily recoverable  ([arXiv:quant-ph/0608045](https://arxiv.org/abs/quant-ph/0608045)). For unital noise channels, *unitarily correctable subsystems* are precisely the noiseless subsystems of $\mathcal{E}^{\dagger}\circ\mathcal{E}$  ([arXiv:quant-ph/0608045](https://arxiv.org/abs/quant-ph/0608045)); these are related to the multiplicative domain of the channel  ([arXiv:0811.0947](https://arxiv.org/abs/0811.0947)) (see also  ([arXiv:quant-ph/9609015](https://arxiv.org/abs/quant-ph/9609015))).

No additional OQEC conditions are needed to tolerate imperfect initialization: under the standard subsystem-code conditions, the effective noise induced by population outside the code can only increase the fidelity with an ideally encoded state, and this robustness persists under encoded CPTP operations  ([arXiv:0709.3533](https://arxiv.org/abs/0709.3533)).

## Encoders

- Subsystem QECCs are robust to initialization errors without modifying the standard OQEC conditions  ([arXiv:0709.3533](https://arxiv.org/abs/0709.3533)).

## Decoders

- Petz recovery map provides a recovery operation that is near-optimal for certain subsystem codes  ([arXiv:1202.5139](https://arxiv.org/abs/1202.5139)).

## Realizations

- A two-qubit unitarily recoverable subsystem code recovery has been realized in an optical system  ([arXiv:0909.1584](https://arxiv.org/abs/0909.1584)).

## Relations

- _parent_: [`oaecc`](https://errorcorrectionzoo.org/c/oaecc) — An OAQECC which has gauge structure (e.g., gauge qubits) but no block structure is a subsystem QECC.
- _cousin_: [[concepts/qec/qecc]] — A subsystem QECC reduces to an ordinary (i.e., subspace) QECC when the gauge subsystem is trivial. Conversely, any QECC with a tensor-product logical subspace can be turned into a subsystem code by treating a logical tensor factor as a gauge subsystem.

## Notes

- See Refs.  ([arXiv:math/0404553](https://arxiv.org/abs/math/0404553), [arXiv:math/0506491](https://arxiv.org/abs/math/0506491), [doi:10.1017/CBO9781139034807.008](https://doi.org/10.1017/CBO9781139034807.008)) for an introduction to operator QEC.
- See  ([arXiv:2605.29137](https://arxiv.org/abs/2605.29137)) for a pedagogical introduction to subsystem codes.
