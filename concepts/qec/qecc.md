---
type: concept
name: Quantum error-correcting code (QECC)
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/approximate-qecc
- concepts/qec/metrological
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/qecc
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: qecc
---

# Quantum error-correcting code (QECC)

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/qecc) (`code_id: qecc`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Encodes quantum information in a (*logical*) subspace of a
(*physical*) Hilbert space such that it is possible to recover said
information from errors that act as linear maps on the physical space.
The state space of a QECC is contained in the space of complex $L^2$-normalizable functions of some configuration space, which usually corresponds to the alphabet of a classical code.

Since quantum information is encoded in quantum superpositions, an additional source of noise (not relevant to classical encodings) can affect the relative phase of such superpositions.
Quantum error-correcting codes have to protect against such *phase-flip noise* while also protecting against conventional classical *bit-flip* noise.
The better a code is at protecting against phase-flip noise, the worse it is at protecting against bit-flip noise, and vice versa, so there is a tradeoff between the two types of noise.

The logical subspace is spanned by a basis comprised of *code basis states*
or *codewords*. Codewords may not be normalizable if the physical
Hilbert space is infinite-dimensional, so approximate versions have to be constructed in
practice.

While all considered QECC states are complex functions, real or quaternionic function spaces can also be considered for QEC  ([arXiv:quant-ph/9911074](https://arxiv.org/abs/quant-ph/9911074), [arXiv:2504.19833](https://arxiv.org/abs/2504.19833)).

(source: raw/error-correction-zoo.md)

## Protection

Denoting Hilbert spaces by the letter $\mathsf{H}$, a quantum code
$(U,\cal{E})$ is a partial isometry
$U:\mathsf{H}_{\text{logical}}\to\mathsf{H}_{\text{physical}}$ with a set of
correctable errors $\cal{E}$ with the following property: there exists a
quantum operation $\cal{D}$ such that for all $E\in\cal{E}$ and states
$|\psi\rangle\in\mathsf{H}_{\text{logical}}$,
\begin{align}
  {\cal D} (EU|\psi\rangle\langle\psi|U^{\dagger}E^{\dagger})
  = c(E)|\psi\rangle\langle\psi|
\end{align}
for some constant $c$ .

Equivalently, correction capability is determined by the \term{Knill-Laflamme conditions}, which may admit infinite terms due to non-normalizability of ideal code states in the case of codes with infinite-dimensional physical spaces. A code that satisfies these conditions approximately, i.e., up to some small quantifiable error, is called an approximate code. These conditions can also be formulated in terms of a dual Heisenberg picture, where correctability is checked for some algebra of observables  ([arXiv:0811.0421](https://arxiv.org/abs/0811.0421)).

\begin{defterm}{Pseudo-threshold (a.k.a. break-even point)}
\label{topic:pseudo-threshold}
The ultimate goal of error correction is to make sure that the logical error rate is smaller than the underlying physical error rate.
For a noise model parameterized by a single physical error rate $p$, the *pseudo-threshold* or *break-even point* is the smallest $p$ at which the logical error rate after error correction is equal to $p$.
\end{defterm}

## Decoders

- The effect of an error is a mapping of the code subspace into another, potentially overlapping, subspace. To determine, or diagnose, the effect of the error in what is known as *syndrome-based decoding*, one can measure one or more operators called *check operators*, which resolve code and error spaces without collapsing the quantum information inside the spaces. The eigenvalues of check operators are called *error syndromes*. One *round* or *cycle* of quantum error correction proceeds by extracting syndromes and performing correcting operations to map the error space containing the logical information back into the codespace. For some codes, correcting operations are not necessary because one can instead track which error space contains the logical information.

## Relations

- _parent_: [`oaecc`](https://errorcorrectionzoo.org/c/oaecc) — An OAQECC which has no gauge structure (e.g., gauge qubits) and no block structure is a QECC.
- _cousin_: [[concepts/qec/approximate-qecc]] — QAECCs correcting a noise channel exactly reduce to QECCs.
- _cousin_: [`ecc`](https://errorcorrectionzoo.org/c/ecc) — Quantum information cannot be copied using a linear process  ([doi:10.1038/299802a0](https://doi.org/10.1038/299802a0)), so one cannot send several copies of a quantum state through a channel as can be done for classical information. The \term{Knill-Laflamme conditions} can similarly be formulated for classical codes  ([arXiv:2109.08691](https://arxiv.org/abs/2109.08691)), although they are not as widely used as those for quantum codes.
- _cousin_: [[concepts/qec/metrological]] — Metrological codes are logical-qubit codes that satisfy the \term{Knill-Laflamme conditions} conditions only partially, and codes that satisfy them fully are QECCs.

## Notes

- See Refs.  ([arXiv:quant-ph/9712048](https://arxiv.org/abs/quant-ph/9712048), [arXiv:quant-ph/0004072](https://arxiv.org/abs/quant-ph/0004072), [doi:10.1090/gsm/047](https://doi.org/10.1090/gsm/047), [doi:10.1017/CBO9780511976667](https://doi.org/10.1017/CBO9780511976667), [arXiv:quant-ph/0507174](https://arxiv.org/abs/quant-ph/0507174), [arXiv:quant-ph/0612185](https://arxiv.org/abs/quant-ph/0612185), [arXiv:0904.2557](https://arxiv.org/abs/0904.2557), [arXiv:0905.2794](https://arxiv.org/abs/0905.2794), [arXiv:1302.3428](https://arxiv.org/abs/1302.3428), [doi:10.1103/RevModPhys.88.041001](https://doi.org/10.1103/RevModPhys.88.041001), [doi:10.1002/9783527805785.ch1](https://doi.org/10.1002/9783527805785.ch1), [arXiv:1508.03695](https://arxiv.org/abs/1508.03695), [arXiv:1907.11157](https://arxiv.org/abs/1907.11157), [arXiv:1910.03672](https://arxiv.org/abs/1910.03672), [arXiv:2007.05992](https://arxiv.org/abs/2007.05992), [doi:10.1002/9781119790327.ch10](https://doi.org/10.1002/9781119790327.ch10), [arXiv:2407.12737](https://arxiv.org/abs/2407.12737), [arXiv:2605.29137](https://arxiv.org/abs/2605.29137)) for overviews of quantum error correction.
- See Refs.  ([doi:10.1017/CBO9781139034807](https://doi.org/10.1017/CBO9781139034807), [doi:10.1201/b15868](https://doi.org/10.1201/b15868)) for books on quantum error correction.
- See video tutorials by [V. V. Albert](https://www.youtube.com/watch?v=_ls3KczZL2c), [S. M. Girvin](https://www.youtube.com/watch?v=uD69GCYF9Zg), [P. Shor](https://www.youtube.com/watch?v=buIbd_aXAHw), [B. Terhal](https://www.youtube.com/watch?v=Je7sVJGKMgU), and [J. Wright](https://www.youtube.com/watch?v=mcwpe8iJ5uo).
- Quantum error correction was initially claimed not to be theoretically possible  ([arXiv:hep-th/9406058](https://arxiv.org/abs/hep-th/9406058), [doi:10.1098/rsta.1995.0106](https://doi.org/10.1098/rsta.1995.0106)) and has been criticized since  ([arXiv:1310.8457](https://arxiv.org/abs/1310.8457)).
- Resource-theoretic interpretations of quantum error correction have been developed, including those that think of codes together with recovery operations as superchannels (a.k.a. quantum combs or bipartite operations)  ([arXiv:1105.4464](https://arxiv.org/abs/1105.4464), [arXiv:1210.4722](https://arxiv.org/abs/1210.4722), [arXiv:1406.7142](https://arxiv.org/abs/1406.7142), [arXiv:2405.17567](https://arxiv.org/abs/2405.17567), [arXiv:2409.09416](https://arxiv.org/abs/2409.09416)).
- QECC can be used as a mechanism for securing quantum computation  ([arXiv:2506.16614](https://arxiv.org/abs/2506.16614)).
