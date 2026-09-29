---
type: concept
name: Entanglement-assisted (EA) hybrid QECC
status: provisional
updated: '2026-09-29'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/eaoaecc
- concepts/qec/hybridqecc
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/eacq
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: eacq
---

# Entanglement-assisted (EA) hybrid QECC

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/eacq) (`code_id: eacq`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Code that encodes quantum and classical information and requires pre-shared
entanglement for transmission.

EA hybrid block quantum codes on $n$ Galois qudits of dimension $q$ are denoted by $((n,k:c,d;e))_q$, where $k$ ($c$) is the number of encoded logical qudits (classical symbols), where $d$ is the distance, and where $e$ is the required number of pre-shared ebits.
Similarly, block codes on $n$ modular qudits are denoted by $((n,k:c,d;e))_{\mathbb{Z}_q}$.


In alternative conventions (not used here), EA hybrid codes are called entanglement-assisted classical-quantum (EACQ) codes.
Here, we use the term classical-quantum for codes for transmitting classical information over quantum channels.

(source: raw/error-correction-zoo.md)

## Protection

If an EA hybrid code is viewed as transmitting $C$ cbits,
$Q$ qubits, and consuming $E$ ebits, then the EA hybrid Singleton bound is
the set of triples $(C,Q,E)$ for which there exists a parameter
$t\in[0,\log q]$ such that
\begin{align}
  C + 2Q & \leq (n-d+1)(\log q + t)~,\\
  Q - E & \leq (n-2d+2)t~,\\
  C + Q - E & \leq (n-d+1)\log q - (d-1)t~,
\end{align}
for $q$-ary physical systems  ([arXiv:2202.02184](https://arxiv.org/abs/2202.02184)).

## Rate

Trade-off between classical communication, quantum communication, and entanglement distribution has been examined  ([arXiv:0811.4227](https://arxiv.org/abs/0811.4227), [arXiv:0901.3038](https://arxiv.org/abs/0901.3038), [arXiv:0903.3920](https://arxiv.org/abs/0903.3920)); see also Ref.  ([arXiv:quant-ph/0501045](https://arxiv.org/abs/quant-ph/0501045)).

## Relations

- _parent_: [[concepts/qec/eaoaecc]] — An EAOA QECC that has no gauge structure (e.g., gauge qubits), that has a block structure that corresponds to a classical code, and that utilizes pre-shared entanglement is an EA hybrid QECC.
- _cousin_: [[concepts/qec/hybridqecc]] — EA hybrid codes utilize additional ancillary subsystems in a pre-shared entangled state, but reduce to hybrid QECCs when said subsystems are interpreted as noiseless physical subsystems.

## Notes

- Examples from the original paper include a $⟦9,1:3,3;0⟧$ code obtained from the Shor code, a $⟦8,1:3,3;1⟧$ code obtained from an $⟦8,1,3;1⟧$ EAQECC, and a $⟦63,21:12,7;6⟧$ code obtained from the $⟦63,21,9;6⟧$ EAQECC built from a classical $[63,39,9]$ BCH code  ([arXiv:0802.2414](https://arxiv.org/abs/0802.2414)).
- Inside the EAOAQEC stabilizer framework, hybrid stabilizer codes are a proper subclass of the broader EA hybrid subspace codes because the EACQ transversal operators obey additional constraints not required in general  ([arXiv:2411.14389](https://arxiv.org/abs/2411.14389)).
