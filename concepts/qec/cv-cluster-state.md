---
type: concept
name: Analog cluster-state code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- CV cluster-state code
- CV graph-state code
- Bosonic cluster-state code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/1d-stabilizer
- concepts/qec/ame
- concepts/qec/analog-stabilizer
- concepts/qec/graph-quantum
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/cv_cluster_state
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: cv_cluster_state
---

# Analog cluster-state code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/cv_cluster_state) (`code_id: cv_cluster_state`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A code based on a continuous-variable (CV), or analog, cluster state.
Such a state can be used to perform MBQC of logical modes, which substitutes the temporal dimension necessary for decoding a conventional code with a spatial dimension.
The exact analog cluster state is non-normalizable, so approximate constructions have to be considered.

Analog cluster states are analog stabilizer states defined on a graph.
There is one nullifier $\hat{\eta}_j$ per graph vertex $j$ of the form
\begin{align}
  \hat{\eta}_j = \hat{p}_{j} - \sum_{k\in N(j)} V_{jk} \hat{x}_k~,
\end{align}
where the neighborhood $N(j)$ is the set of vertices which share an edge with $j$, and where $V_{jk}$ is a weighted (real-valued) adjacency matrix of a graph  ([arXiv:1912.06463](https://arxiv.org/abs/1912.06463)).

Analog cluster states, like cluster states, can be defined on various geometries.
Analog cluster states defined on a 1D array of modes are called quantum wires  ([arXiv:0804.4468](https://arxiv.org/abs/0804.4468), [arXiv:0811.2799](https://arxiv.org/abs/0811.2799)), not to be confused with the Kitaev quantum wire, a fermion code.
Analog cluster states defined on a 1D ladder are sometimes called dual-rail, not to be confused with the dual-rail code.

(source: raw/error-correction-zoo.md)

## Protection

Protection is related to the analog stabilizer code underlying the analog cluster state.

## Encoders

- Initialization of all modes in momentum eigenstates and action of gates of the form $\exp(iV_{jk}\hat{x}_{j}\hat{x}_{k})$. The normalizable version substitutes momentum eigenstates with finitely squeezed states.
- Squeezers and beam-splitters  ([arXiv:1007.3434](https://arxiv.org/abs/1007.3434)).

## General gates

- Combination of linear-optical gates and homodyne measurements on subsets of vertices  ([arXiv:quant-ph/0605198](https://arxiv.org/abs/quant-ph/0605198), [arXiv:0903.3233](https://arxiv.org/abs/0903.3233)).
- Gaussian operations can be realized as operations acting on graphs underlying a cluster state. They can be done in any order, demonstrating parallelism  ([arXiv:quant-ph/0605198](https://arxiv.org/abs/quant-ph/0605198), [arXiv:0903.3233](https://arxiv.org/abs/0903.3233)).
- Magic-state distillation is required for universal computation  ([arXiv:quant-ph/0605198](https://arxiv.org/abs/quant-ph/0605198), [arXiv:0903.3233](https://arxiv.org/abs/0903.3233)).

## Realizations

- Analog cluster states on a number of modes ranging from tens to millions  ([arXiv:1306.3366](https://arxiv.org/abs/1306.3366), [arXiv:1311.2957](https://arxiv.org/abs/1311.2957), [arXiv:1606.06688](https://arxiv.org/abs/1606.06688)) have been synthesized in photonic degrees of freedom. A $12\times N$ mode cluster state, where $N$ is the number of clock cycles of the experiment, has been realized in a photonic device by Xanadu  ([doi:10.1038/s41586-024-08406-9](https://doi.org/10.1038/s41586-024-08406-9)).
- Required primitives for Gaussian gates have been realized  ([arXiv:0906.3141](https://arxiv.org/abs/0906.3141)).

## Relations

- _parent_: [[concepts/qec/analog-stabilizer]] — Analog cluster-state codes are particular analog stabilizer codes. Any analog stabilizer state is equivalent to an analog cluster state under a single-mode Gaussian circuit  ([arXiv:2503.15698](https://arxiv.org/abs/2503.15698)). Relaxing the real weighted adjacency matrix of an analog cluster state to be complex yields a description of a general analog (i.e., Gaussian) stabilizer state  ([arXiv:1007.0725](https://arxiv.org/abs/1007.0725)). Pure Gaussian states, which are normalizable approximate versions of analog stabilizer states, are not equivalent to finitely squeezed analog cluster states via Gaussian local unitaries  ([arXiv:1912.06463](https://arxiv.org/abs/1912.06463)).
- _parent_: [[concepts/qec/graph-quantum]] — Graph quantum codes for $G=\mathbb{R}$ reduce to analog cluster-state codes.
- _cousin_: [[concepts/qec/ame]] — Analog cluster states are generically CV AME  ([arXiv:0901.1488](https://arxiv.org/abs/0901.1488)), and explicit constructions exist for any number of modes  ([arXiv:2503.15698](https://arxiv.org/abs/2503.15698)).
- _cousin_: [[concepts/qec/1d-stabilizer]] — Analog cluster states defined on a 1D array of modes are called quantum wires  ([arXiv:0804.4468](https://arxiv.org/abs/0804.4468), [arXiv:0811.2799](https://arxiv.org/abs/0811.2799)), not to be confused with the Kitaev quantum wire, a fermion code. Analog cluster states defined on a 1D ladder are sometimes called dual-rail, not to be confused with the dual-rail code.

## Notes

- See Ref.  ([doi:10.1002/9783527635283](https://doi.org/10.1002/9783527635283)) for a review of analog cluster states and their applications.
