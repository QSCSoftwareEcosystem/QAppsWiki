---
type: concept
name: Perfect-tensor code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Absolutely maximally entangled (AME) code
- Maximally multipartite entangled state (MMES) code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/block-perfect
- concepts/qec/covariant
- concepts/qec/cws
- concepts/qec/galois-polynomial
- concepts/qec/quantum-mds
- concepts/qec/quantum-secret-sharing
- concepts/qec/qubit-stabilizer
- concepts/qec/qudit-cluster-state
- concepts/qec/reinforcement-learning
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/ame
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: ame
---

# Perfect-tensor code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/ame) (`code_id: ame`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Block quantum code encoding one subsystem into an odd number $n$ subsystems whose encoding isometry is a perfect tensor.
This code stems from an AME$(n,q)$ AME state, or equivalently, a $((n+1,1,\lfloor (n+1)/2 \rfloor + 1))$ code.

\begin{defterm}{Absolutely maximally entangled (AME) state}
\label{topic:ame}
A state on $n$ subsystems is $d$*-uniform*  ([arXiv:quant-ph/0005031](https://arxiv.org/abs/quant-ph/0005031), [arXiv:quant-ph/0310137](https://arxiv.org/abs/quant-ph/0310137), [arXiv:1404.3586](https://arxiv.org/abs/1404.3586)) (a.k.a. $d$-undetermined  ([arXiv:0809.3081](https://arxiv.org/abs/0809.3081)) or $d$-maximally mixed  ([arXiv:1211.4118](https://arxiv.org/abs/1211.4118))) if all reduced density matrices on up to $d$ subsystems are maximally mixed.
A $K$-dimensional subspace of $(d-1)$-uniform states of $n$ subsystems is equivalent to a pure $((n,K,d))$ block quantum code  ([arXiv:0704.0251](https://arxiv.org/abs/0704.0251), [arXiv:1907.07733](https://arxiv.org/abs/1907.07733)).
An AME state (a.k.a. maximally multi-partite entangled state or MMES  ([arXiv:0710.2868](https://arxiv.org/abs/0710.2868), [arXiv:1002.2592](https://arxiv.org/abs/1002.2592))) is a $\lfloor n/2 \rfloor$-uniform state, corresponding to a pure $((n,1,\lfloor n/2 \rfloor + 1))$ code.
The rank-$n$ tensor formed by the encoding isometry of such codes is a *perfect tensor* (a.k.a. multi-unitary tensor), meaning that it is proportional to an isometry for any bipartition of its indices into a set $A$ and a complementary set $A^{\perp}$ such that $|A|\leq|A^{\perp}|$.
Absolutely maximal entanglement exists for non-normalizable states of continuous-variable (CV) systems, whose reduced density matrices are proportional to the infinite-dimensional identity matrix; such states are called CV AME or CV MMES  ([arXiv:0901.1488](https://arxiv.org/abs/0901.1488), [arXiv:2503.15698](https://arxiv.org/abs/2503.15698)).
Explicit Gaussian and non-Gaussian CV AME constructions are known  ([arXiv:2503.15698](https://arxiv.org/abs/2503.15698)).
\end{defterm}

Stabilizer Galois-qudit perfect-tensor codes can be converted to AME states via established shortening/lengthening procedures  ([arXiv:quant-ph/0508070](https://arxiv.org/abs/quant-ph/0508070)) ([arXiv:1502.05267](https://arxiv.org/abs/1502.05267)).
For example, an $⟦n,0,d⟧$ AME state can be reinterpreted as an $⟦n-1,1,d-1⟧$ perfect-tensor code by designating one subsystem as the logical input leg of the encoding isometry  ([arXiv:quant-ph/9705052](https://arxiv.org/abs/quant-ph/9705052)).
There exist infinite families of inequivalent AME states  ([arXiv:2003.13639](https://arxiv.org/abs/2003.13639)).

(source: raw/error-correction-zoo.md)

## Encoders

- Fault-tolerant $d$-uniform state preparation  ([arXiv:2503.14506](https://arxiv.org/abs/2503.14506)).
- Quantum circuits for non-stabilizer AME states  ([arXiv:2504.05394](https://arxiv.org/abs/2504.05394)).

## Fault tolerance

- Fault-tolerant $d$-uniform state preparation  ([arXiv:2503.14506](https://arxiv.org/abs/2503.14506)).

## Relations

- _parent_: [[concepts/qec/block-perfect]] — Planar-perfect tensors are automatically perfect tensors.
- _cousin_: [[concepts/qec/quantum-mds]] — AME states for even $n$ are examples of quantum MDS codes with no logical qubits  ([arXiv:quant-ph/0310137](https://arxiv.org/abs/quant-ph/0310137), [arXiv:1701.03359](https://arxiv.org/abs/1701.03359), [arXiv:1907.11253](https://arxiv.org/abs/1907.11253)).
A family of conjectured perfect-tensor codes is quantum MDS  ([arXiv:quant-ph/0312164](https://arxiv.org/abs/quant-ph/0312164)).
- _cousin_: [`combinatorial_design`](https://errorcorrectionzoo.org/c/combinatorial_design) — Combinatorial designs and $d$-uniform quantum states are related  ([arXiv:1506.08857](https://arxiv.org/abs/1506.08857), [arXiv:1708.05946](https://arxiv.org/abs/1708.05946), [arXiv:2111.04055](https://arxiv.org/abs/2111.04055)).
- _cousin_: [`orthogonal_array`](https://errorcorrectionzoo.org/c/orthogonal_array) — Orthogonal arrays and $d$-uniform quantum states are related  ([arXiv:1404.3586](https://arxiv.org/abs/1404.3586), [arXiv:1708.05946](https://arxiv.org/abs/1708.05946), [arXiv:2303.15001](https://arxiv.org/abs/2303.15001), [doi:10.1038/s41534-019-0165-8](https://doi.org/10.1038/s41534-019-0165-8), [doi:10.1103/PhysRevA.99.042332](https://doi.org/10.1103/PhysRevA.99.042332), [doi:10.3390/e25040680](https://doi.org/10.3390/e25040680)).
- _cousin_: [`mds`](https://errorcorrectionzoo.org/c/mds) — MDS codes can be used to obtain cluster states that are AME with minimal support  ([arXiv:1306.2536](https://arxiv.org/abs/1306.2536), [arXiv:1306.2879](https://arxiv.org/abs/1306.2879), [arXiv:1506.08857](https://arxiv.org/abs/1506.08857), [arXiv:1701.03359](https://arxiv.org/abs/1701.03359), [arXiv:1706.08318](https://arxiv.org/abs/1706.08318)).
- _cousin_: [[concepts/qec/qudit-cluster-state]] — MDS codes can be used to obtain cluster states that are AME with minimal support  ([arXiv:1306.2536](https://arxiv.org/abs/1306.2536), [arXiv:1306.2879](https://arxiv.org/abs/1306.2879), [arXiv:1506.08857](https://arxiv.org/abs/1506.08857), [arXiv:1701.03359](https://arxiv.org/abs/1701.03359), [arXiv:1706.08318](https://arxiv.org/abs/1706.08318)).
- _cousin_: [[concepts/qec/galois-polynomial]] — AME states for even $n$ are examples of quantum MDS codes with no logical qubits  ([arXiv:quant-ph/0310137](https://arxiv.org/abs/quant-ph/0310137), [arXiv:1701.03359](https://arxiv.org/abs/1701.03359), [arXiv:1907.11253](https://arxiv.org/abs/1907.11253)). MDS RS codes can yield perfect tensors via the CSS and Hermitian constructions  ([arXiv:quant-ph/0312164](https://arxiv.org/abs/quant-ph/0312164)) (see also Refs.  ([arXiv:1801.09623](https://arxiv.org/abs/1801.09623), [arXiv:1812.04057](https://arxiv.org/abs/1812.04057))).
- _cousin_: [[concepts/qec/quantum-secret-sharing]] — Perfect tensors are useful for quantum secret sharing and open-destination multi-party teleportation  ([arXiv:1204.2289](https://arxiv.org/abs/1204.2289), [arXiv:1306.2536](https://arxiv.org/abs/1306.2536), [doi:10.1007/s11128-022-03723-2](https://doi.org/10.1007/s11128-022-03723-2)).
- _cousin_: [[concepts/qec/qubit-stabilizer]] — The codespace of a qubit stabilizer code with pure distance $d_{\textnormal{pure}}$ is a $(d_{\textnormal{pure}}-1)$-uniform space.
- _cousin_: [[concepts/qec/reinforcement-learning]] — Reinforcement learning  ([arXiv:1806.08781](https://arxiv.org/abs/1806.08781)) and graph-based optimizers like PyTheus  ([arXiv:2210.09980](https://arxiv.org/abs/2210.09980)) can be used to find AME states.
- _cousin_: [[concepts/qec/cws]] — CWS codes can be constructed from $(d-1)$-uniform states  ([arXiv:2405.06142](https://arxiv.org/abs/2405.06142)).
- _cousin_: [[concepts/qec/covariant]] — An $SU(2)$-invariant three-qudit perfect tensor exists  ([arXiv:1612.04504](https://arxiv.org/abs/1612.04504)), but invariant perfect tensors do not exist on four parties  ([arXiv:quant-ph/0005013](https://arxiv.org/abs/quant-ph/0005013), [arXiv:1612.04504](https://arxiv.org/abs/1612.04504), [arXiv:2210.02483](https://arxiv.org/abs/2210.02483)).

## Notes

- See Ref.  ([arXiv:1708.06298](https://arxiv.org/abs/1708.06298)) and corresponding [Table of AME states](https://tp.nt.uni-siegen.de/ame/ame.html).
- $d$-uniform states are useful for masking quantum information  ([arXiv:2009.12497](https://arxiv.org/abs/2009.12497)).
- Quantum simulation of approximately $d$-uniform states is similar to that with random-state inputs in terms of Trotter error  ([arXiv:2406.02379](https://arxiv.org/abs/2406.02379)).
- See Ref.  ([arXiv:2508.04777](https://arxiv.org/abs/2508.04777)) for a review.
