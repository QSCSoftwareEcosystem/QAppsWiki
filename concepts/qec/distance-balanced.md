---
type: concept
name: Distance-balanced code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/galois-css
- concepts/qec/general-qldpc
- concepts/qec/generalized-homological-product-css
- concepts/qec/gkp-cluster-state
- concepts/qec/homological-product
- concepts/qec/qubit-subsystem-stabilizer
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/distance_balanced
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: distance_balanced
---

# Distance-balanced code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/distance_balanced) (`code_id: distance_balanced`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Galois-qudit CSS code obtained from a CSS code by increasing the smaller of the $X$- and $Z$-distances using a homological-product-based balancing step or one of its generalizations.
The initial code is said to be *unbalanced*, i.e., tailored to noise biased toward either bit- or phase-flip errors, and the procedure can result in a code that treats both types of errors on a more equal footing.

In the original construction  ([arXiv:1611.03790](https://arxiv.org/abs/1611.03790)), if $C$ is a QLDPC CSS code then applying the balancing step with parameter $l$ yields $\tilde K=K$, $\tilde d_X=l d_X$, $\tilde d_Z=d_Z$, and $\tilde N=O(Nl)$, so choosing $l\approx d_Z/d_X$ balances the two distances.
In the generalized construction  ([arXiv:2004.07935](https://arxiv.org/abs/2004.07935)), combining a component quantum code $\mathcal{Q}$ with a classical code $C$ yields a new code with $K=k(\mathcal{Q})k(C)$, $D_X=d_X(\mathcal{Q})d(C)$, and $D_Z=d_Z(\mathcal{Q})$, so choosing $d(C)\approx d_Z/d_X$ balances the two distances.
The original distance-balancing procedure  ([arXiv:1611.03790](https://arxiv.org/abs/1611.03790)), later generalized in this way, can yield QLDPC codes  ([arXiv:1611.03790](https://arxiv.org/abs/1611.03790)).

\begin{defterm}{Weight reduction}
\label{topic:weight-reduction}
Various procedures performing *weight reduction*  ([arXiv:1611.03790](https://arxiv.org/abs/1611.03790), [arXiv:2102.10030](https://arxiv.org/abs/2102.10030), [arXiv:2402.05228](https://arxiv.org/abs/2402.05228)) take in a stabilizer code and output a longer code with bounded stabilizer-generator weight.
Hastings' original construction  ([arXiv:1611.03790](https://arxiv.org/abs/1611.03790)) makes a qubit CSS code QLDPC while preserving the number of logical qubits and keeping the block length polynomial in the original one.
The weight reduction procedure of Ref.  ([arXiv:2402.05228](https://arxiv.org/abs/2402.05228)) has been extended to subsystem qubit stabilizer codes  ([arXiv:2410.10194](https://arxiv.org/abs/2410.10194)).
\end{defterm}

(source: raw/error-correction-zoo.md)

## Decoders

- If the auxiliary classical LDPC code corrects all error patterns of weight $<\alpha |A|$, then the resulting product code has a polynomial-time decoder for $X$-errors of weight $< \alpha |A| d_X/2$, where $d_X$ is the $X$-distance of the component quantum code  ([arXiv:2004.07935](https://arxiv.org/abs/2004.07935)).
- If the component 2D complex has a polynomial-time decoder for $Z$-errors of weight $< w$, then the resulting distance-balanced code also has a polynomial-time decoder for $Z$-errors of weight $< w$  ([arXiv:2004.07935](https://arxiv.org/abs/2004.07935)).
- The effective distance of single-ancilla syndrome extraction QLDPC code circuits can be preserved under weight reduction  ([arXiv:2409.02193](https://arxiv.org/abs/2409.02193)). The distance balancing technique of Ref.  ([arXiv:2004.07935](https://arxiv.org/abs/2004.07935)) preserves the effective distance of single-ancilla syndrome extraction circuits  ([arXiv:2409.02193](https://arxiv.org/abs/2409.02193)).

## Fault tolerance

- Single-ancilla syndrome extraction circuits that, for the most part, preserve the effective distance of weight-reduced qLDPC codes  ([arXiv:2409.02193](https://arxiv.org/abs/2409.02193)). The distance balancing technique of Ref.  ([arXiv:2004.07935](https://arxiv.org/abs/2004.07935)) preserves effective distance  ([arXiv:2409.02193](https://arxiv.org/abs/2409.02193)).

## Relations

- _parent_: [[concepts/qec/galois-css]]
- _parent_: [[concepts/qec/generalized-homological-product-css]]
- _cousin_: [[concepts/qec/homological-product]] — Distance balancing relies on taking a homological product of chain complexes corresponding to a classical and a quantum code.
- _cousin_: [[concepts/qec/qubit-subsystem-stabilizer]] — The weight reduction procedure of Ref.  ([arXiv:2402.05228](https://arxiv.org/abs/2402.05228)) has been extended to subsystem qubit stabilizer codes  ([arXiv:2410.10194](https://arxiv.org/abs/2410.10194)).
- _cousin_: [[concepts/qec/gkp-cluster-state]] — Weight reduction has been studied in the context of GKP CV-cluster-state codes  ([arXiv:2402.05228](https://arxiv.org/abs/2402.05228)).
- _cousin_: [[concepts/qec/general-qldpc]] — Lattice surgery techniques for QLDPC codes  ([arXiv:2110.10794](https://arxiv.org/abs/2110.10794), [arXiv:2308.08648](https://arxiv.org/abs/2308.08648)) utilize weight reduction. Single-ancilla syndrome extraction circuits that, for the most part, preserve the effective distance of weight-reduced qLDPC codes  ([arXiv:2409.02193](https://arxiv.org/abs/2409.02193)).
