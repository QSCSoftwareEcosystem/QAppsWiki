---
type: concept
name: Hyperinvariant tensor-network (HTN) code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Evenbly code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/group-4-2-2
- concepts/qec/holographic-tensor
- concepts/qec/qubit-stabilizer
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/holographic_hyperinvariant
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: holographic_hyperinvariant
---

# Hyperinvariant tensor-network (HTN) code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/holographic_hyperinvariant) (`code_id: holographic_hyperinvariant`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Holographic tensor-network code constructed out of a hyperinvariant tensor network  ([arXiv:1704.04229](https://arxiv.org/abs/1704.04229)), i.e., a MERA-like network admitting a hyperbolic geometry.
The network is defined using two layers A and B, with constituent tensors satisfying isometry conditions (a.k.a. multitensor constraints).

This code produces boundary correlation functions that align with those expected from conformal field theory (CFT) boundary states.
HTN codes exhibit state-dependent breakdown of complementary recovery, consistent with quantum gravity corrections in AdS/CFT.

(source: raw/error-correction-zoo.md)

## Code capacity threshold

- $19.1\%$ under depolarizing noise and $50\%$ under erasure noise for a $\{5,4\}$ tiling  ([arXiv:2407.11926](https://arxiv.org/abs/2407.11926)).
- $40\%$ under erasure noise for constant-rate version of the code  ([arXiv:2407.11926](https://arxiv.org/abs/2407.11926)).

## Relations

- _parent_: [[concepts/qec/qubit-stabilizer]]
- _parent_: [[concepts/qec/holographic-tensor]] — The encoding of an HTN code is a hyperinvariant tensor network.
- _cousin_: [[concepts/qec/group-4-2-2]] — The explicit 4-ququart encoding tensor $A'$ used in the HTN code is a $⟦4,1,2⟧_{\mathbb{Z}_4}$ subcode of the $⟦4,2,2⟧_{\mathbb{Z}_4}$ four group-qudit code  ([arXiv:2304.02732](https://arxiv.org/abs/2304.02732)).
