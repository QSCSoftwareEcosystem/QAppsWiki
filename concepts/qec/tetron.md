---
type: concept
name: Tetron code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Kitaev-Wen Majorana mapping
- Kitaev honeycomb mapping
- Bravyi-Leemhuis-Terhal (BLT) Majorana mapping
- Majorana representation
- Parton construction
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/hamiltonian
- concepts/qec/majorana-surface
- concepts/qec/mbq
- concepts/qec/quantum-repetition
- concepts/qec/qubit-stabilizer
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/tetron
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: tetron
---

# Tetron code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/tetron) (`code_id: tetron`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A $⟦2,1,2⟧_{f}$ Majorana box qubit encoding a logical qubit into four Majorana modes, equivalently into the fixed-total-parity sector of two physical fermionic modes.
Four Majorana zero modes are the smallest aggregate that supports a qubit in a fixed fermion-parity sector  ([arXiv:1610.05289](https://arxiv.org/abs/1610.05289)).
This code can be concatenated with various qubit codes such as surface codes and color codes.
Four-boundary Majorana surface-code patches are logical tetrons, i.e., higher-distance analogues of this physical tetron block  ([arXiv:1801.08143](https://arxiv.org/abs/1801.08143)).

Embedding each physical qubit into two fermions via the tetron code is useful for exactly solving the Kitaev honeycomb model Hamiltonian  ([arXiv:cond-mat/0506438](https://arxiv.org/abs/cond-mat/0506438)) and other qubit Hamiltonians on certain graphs  ([arXiv:2003.05465](https://arxiv.org/abs/2003.05465), [arXiv:2012.07857](https://arxiv.org/abs/2012.07857)).
It has been used throughout condensed matter physics under the name of the Majorana representation  ([arXiv:cond-mat/9305017](https://arxiv.org/abs/cond-mat/9305017), [arXiv:cond-mat/9504006](https://arxiv.org/abs/cond-mat/9504006)) or parton construction  ([arXiv:2204.11888](https://arxiv.org/abs/2204.11888)), allowing for a mean-field treatment of many models that are otherwise not amenable.
Majorana stabilizer groups can be converted into ordinary qubit stabilizer groups via the parton mapping, while their corresponding states are converted via the Gutzwiller projection  ([arXiv:2505.02683](https://arxiv.org/abs/2505.02683)).

(source: raw/error-correction-zoo.md)

## Relations

- _parent_: [[concepts/qec/mbq]] — The Majorana box qubit for $n=2$ is the tetron code.
- _parent_: [[concepts/qec/quantum-repetition]] — The tetron code is a special case of the quantum repetition code with $n=2$.
- _cousin_: [[concepts/qec/hamiltonian]] — Embedding each physical qubit into two fermions via the tetron code is useful for exactly solving the Kitaev honeycomb model Hamiltonian  ([arXiv:cond-mat/0506438](https://arxiv.org/abs/cond-mat/0506438)) and other qubit Hamiltonians on certain graphs  ([arXiv:2003.05465](https://arxiv.org/abs/2003.05465), [arXiv:2012.07857](https://arxiv.org/abs/2012.07857)). Majorana stabilizer groups can be converted into ordinary qubit stabilizer groups via the parton mapping, while their corresponding states are converted via the Gutzwiller projection  ([arXiv:2505.02683](https://arxiv.org/abs/2505.02683)).
- _cousin_: [[concepts/qec/majorana-surface]] — Four-boundary Majorana surface-code patches are logical tetrons, i.e., higher-distance versions of the tetron code  ([arXiv:1801.08143](https://arxiv.org/abs/1801.08143)).
- _cousin_: [[concepts/qec/qubit-stabilizer]] — Any $⟦n,k,d⟧$ stabilizer code can be mapped into a $⟦2n,k,2d⟧_{f}$ Majorana stabilizer code by concatenating with the tetron code  ([arXiv:cond-mat/0506438](https://arxiv.org/abs/cond-mat/0506438)) ([arXiv:1004.3791](https://arxiv.org/abs/1004.3791)).
Embedding each physical qubit into two fermions via the tetron code is useful for exactly solving the Kitaev honeycomb model Hamiltonian  ([arXiv:cond-mat/0506438](https://arxiv.org/abs/cond-mat/0506438)) and other qubit Hamiltonians on certain graphs  ([arXiv:2003.05465](https://arxiv.org/abs/2003.05465), [arXiv:2012.07857](https://arxiv.org/abs/2012.07857)). Majorana stabilizer groups can be converted into ordinary qubit stabilizer groups via the parton mapping, while their corresponding states are converted via the Gutzwiller projection  ([arXiv:2505.02683](https://arxiv.org/abs/2505.02683)).
