---
type: concept
name: EA qubit stabilizer code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/ea-galois-stabilizer
- concepts/qec/ea-mds
- concepts/qec/ea-qubits-into-qubits
- concepts/qec/eaoa-stabilizer
- concepts/qec/hybrid-qudit-oscillator
- concepts/qec/qubit-concatenated
- concepts/qec/qubit-css
- concepts/qec/qubit-stabilizer
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/eastab
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: eastab
---

# EA qubit stabilizer code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/eastab) (`code_id: eastab`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A code constructed using a variation of the stabilizer formalism designed to utilize pre-shared entanglement between sender and receiver.
A code is typically denoted as $⟦n,k;e⟧$ or $⟦n,k,d;e⟧$, where $d$ is the distance of the EA code and $e$ is the number of required pre-shared maximally entangled Bell states (ebits).
While other entangled states can be used, there is always a choice of generators such that Bell states suffice while still using the fewest ebits.

The dual of an EA qubit stabilizer code is also an EA qubit stabilizer code whose logical qubits and ebits are interchanged, $k\leftrightarrow e$  ([arXiv:1010.5506](https://arxiv.org/abs/1010.5506)).

An $⟦n,k+e;e⟧$ EA stabilizer code can be constructed from an ordinary $⟦n,k⟧$ stabilizer code with check matrix $H=(A|B)$, where the required number of ebits is $e = \text{rank}(AB^T+BA^T)/2$  ([arXiv:0804.1404](https://arxiv.org/abs/0804.1404)).
Alternatively, given a linear $[n,k,d]_{q^2}$ code $C$ with parity check matrix $H$, the Hermitian dual $C^{\perp_H}$ stabilizes an EA-QEC with parameters $⟦n,2k-n+c,d;c⟧_q$, where $c=\text{rank}(HH^\dagger)$ is the number of required ebits .

(source: raw/error-correction-zoo.md)

## Protection

Ancillary shared entanglement is assumed to be perfect, but this assumption can be relaxed  ([arXiv:1302.5081](https://arxiv.org/abs/1302.5081)).
There are quantum Griesmer  ([doi:10.1007/s11128-015-1143-5](https://doi.org/10.1007/s11128-015-1143-5)) and Plotkin  ([doi:10.1103/PhysRevA.87.032309](https://doi.org/10.1103/PhysRevA.87.032309)) bounds for EA qubit stabilizer codes.

## Rate

Asymptotically good EA qubit stabilizer codes exist  ([doi:10.1007/s10623-014-9997-6](https://doi.org/10.1007/s10623-014-9997-6)).

## Encoders

- Encoders and decoders of a minimal EA qubit stabilizer code should be realizable using hyper-entangled states  ([arXiv:0807.4906](https://arxiv.org/abs/0807.4906)).
- Fault-tolerant encoders utilizing pre-shared entanglement  ([arXiv:2405.07242](https://arxiv.org/abs/2405.07242)).

## Decoders

- Encoders and decoders of a minimal EA qubit stabilizer code should be realizable using hyper-entangled states  ([arXiv:0807.4906](https://arxiv.org/abs/0807.4906)).

## Relations

- _parent_: [[concepts/qec/ea-qubits-into-qubits]]
- _parent_: [[concepts/qec/eaoa-stabilizer]] — An EAOA qubit stabilizer code with no gauge or hybrid structure is an EA qubit stabilizer code. Conversely, any $⟦n,q+c,d_1;e⟧$ EA qubit stabilizer code can be converted into an $⟦n,q:c,d_2;e⟧$ EA hybrid stabilizer code by repurposing $c$ logical qubits as classical bits, and any $⟦n,q:c,d_2;e⟧$ EA hybrid code can be converted into an $⟦n,q,d_3;e⟧$ EA qubit stabilizer code by absorbing the classical degrees of freedom back into the quantum code, with $d_1 \leq d_2 \leq d_3$  ([arXiv:0802.2414](https://arxiv.org/abs/0802.2414)).
- _parent_: [[concepts/qec/ea-galois-stabilizer]] — EA Galois-qudit stabilizer codes reduce to EA qubit stabilizer codes for $q=2$.
- _cousin_: [[concepts/qec/qubit-stabilizer]] — EA qubit stabilizer codes utilize additional ancillary qubits in a pre-shared entangled state, but reduce to qubit stabilizer codes when said qubits are interpreted as noiseless physical qubits. Qubit stabilizer codes can be used to obtain shortened EA qubit stabilizer codes  ([arXiv:2205.13732](https://arxiv.org/abs/2205.13732)).
- _cousin_: [`binary_linear`](https://errorcorrectionzoo.org/c/binary_linear) — Any linear binary code can be used to construct an EA qubit stabilizer code  ([arXiv:quant-ph/0608027](https://arxiv.org/abs/quant-ph/0608027), [arXiv:quant-ph/0610092](https://arxiv.org/abs/quant-ph/0610092), [doi:10.1007/s10623-014-9997-6](https://doi.org/10.1007/s10623-014-9997-6)).
- _cousin_: [`q-ary_linear`](https://errorcorrectionzoo.org/c/q-ary_linear) — Any quaternary linear code can be used to construct an EA qubit stabilizer code  ([arXiv:quant-ph/0610092](https://arxiv.org/abs/quant-ph/0610092)).
- _cousin_: [[concepts/qec/qubit-css]] — As opposed to CSS codes, EA qubit stabilizer codes can be constructed from any linear binary code.
- _cousin_: [[concepts/qec/hybrid-qudit-oscillator]] — Encoders and decoders of a minimal EA qubit stabilizer code should be realizable using hyper-entangled states  ([arXiv:0807.4906](https://arxiv.org/abs/0807.4906)).
- _cousin_: [[concepts/qec/qubit-concatenated]] — There exist concatenated EA qubit stabilizer codes that saturate the EA quantum Griesmer and Plotkin bounds  ([arXiv:2412.16082](https://arxiv.org/abs/2412.16082)).
- _cousin_: [[concepts/qec/ea-mds]] — There exist concatenated EA qubit stabilizer codes that saturate the EA quantum Singleton bound  ([arXiv:2412.16082](https://arxiv.org/abs/2412.16082)).
- _cousin_: [`q-ary_additive`](https://errorcorrectionzoo.org/c/q-ary_additive) — There is a relation between quaternary additive codes and EA qubit stabilizer codes  ([arXiv:2501.15465](https://arxiv.org/abs/2501.15465)).

## Notes

- Tables of bounds and examples of EA qubit (and EA qutrit) stabilizer codes for various $n$ and $k$, based on algorithms developed in Refs.  ([arXiv:2007.01249](https://arxiv.org/abs/2007.01249), [arXiv:2207.05647](https://arxiv.org/abs/2207.05647)), are maintained by M. Grassl at this [website](https://www.codetables.de/).
- See Ref.  ([arXiv:2207.05647](https://arxiv.org/abs/2207.05647)) for code tables and bounds on performance.
- See Ref.  ([arXiv:quant-ph/9604024](https://arxiv.org/abs/quant-ph/9604024)) for related notions.
