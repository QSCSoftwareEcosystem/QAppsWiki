---
type: concept
name: Dihedral $G=D_m$ quantum-double code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/quantum-double
- concepts/qec/spt
- concepts/qec/tqd-abelian
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/quantum_double_dihedral
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: quantum_double_dihedral
---

# Dihedral $G=D_m$ quantum-double code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/quantum_double_dihedral) (`code_id: quantum_double_dihedral`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Quantum-double code whose codewords realize topological order associated with the dihedral group $D_m$ of order $2m$.
For $m \geq 3$, these codes are non-Abelian, with the simplest case given by $D_3=S_3$, the permutation group on three objects.
On an oriented lattice, each edge hosts a $2m$-dimensional group qudit, and the codespace is the ground-state subspace of the corresponding quantum double Hamiltonian  ([arXiv:quant-ph/9707021](https://arxiv.org/abs/quant-ph/9707021)).

(source: raw/error-correction-zoo.md)

## Transversal gates

- On a triangular patch encoding one logical qubit, a transversal $T^{1/N}=\mathrm{diag}(1,e^{i\pi/(4N)})$ gate can be implemented when $G=D_{4N}$  ([arXiv:2512.13777](https://arxiv.org/abs/2512.13777), [arXiv:2603.05502](https://arxiv.org/abs/2603.05502)).

## General gates

- Universal topological quantum computation is possible for certain groups such as $G=D_3=S_3$  ([arXiv:quant-ph/0306063](https://arxiv.org/abs/quant-ph/0306063), [arXiv:0901.1345](https://arxiv.org/abs/0901.1345)).
- For $G=S_3$, Ref.  ([arXiv:1401.7096](https://arxiv.org/abs/1401.7096)) gives measurement-assisted universal gate sets; circuit-level fault tolerance can be improved using an anyon interferometer  ([arXiv:2411.09697](https://arxiv.org/abs/2411.09697)).

## Code capacity threshold

- Behavior under $X$-type noise (namely, diffusion of certain anyons) for the $G=D_4$ case is related to the phase diagram of a disordered net model  ([arXiv:2409.12948](https://arxiv.org/abs/2409.12948)).

## Fault tolerance

- Universal topological quantum computation is possible for certain groups such as $G=D_3=S_3$  ([arXiv:quant-ph/0306063](https://arxiv.org/abs/quant-ph/0306063), [arXiv:0901.1345](https://arxiv.org/abs/0901.1345)).
- For $G=S_3$, Ref.  ([arXiv:1401.7096](https://arxiv.org/abs/1401.7096)) gives measurement-assisted universal gate sets; circuit-level fault tolerance can be improved using an anyon interferometer  ([arXiv:2411.09697](https://arxiv.org/abs/2411.09697)).

## Realizations

- Trapped ions: ground state of the model for $G = D_3$, encoding of logical qutrits in the anyon fusion space, and a universal anyon-based gate set realized on 54 qubits by Quantinuum  ([arXiv:2601.20956](https://arxiv.org/abs/2601.20956)).

## Relations

- _parent_: [[concepts/qec/quantum-double]]
- _cousin_: [[concepts/qec/tqd-abelian]] — A Type-III $\mathbb{Z}_2^3$ Abelian TQD realizes the same topological order as the $G=D_4$ quantum double model  ([arXiv:hep-th/9511195](https://arxiv.org/abs/hep-th/9511195), [arXiv:1508.03468](https://arxiv.org/abs/1508.03468)).
- _cousin_: [[concepts/qec/spt]] — The $D_4$ quantum double model can be obtained by gauging  ([arXiv:1202.3120](https://arxiv.org/abs/1202.3120), [arXiv:1407.1025](https://arxiv.org/abs/1407.1025), [arXiv:1603.04442](https://arxiv.org/abs/1603.04442), [arXiv:1603.05182](https://arxiv.org/abs/1603.05182), [arXiv:1605.01640](https://arxiv.org/abs/1605.01640), [arXiv:1805.01836](https://arxiv.org/abs/1805.01836), [arXiv:1806.08679](https://arxiv.org/abs/1806.08679), [arXiv:2108.11402](https://arxiv.org/abs/2108.11402), [arXiv:2310.16032](https://arxiv.org/abs/2310.16032), [arXiv:2410.02213](https://arxiv.org/abs/2410.02213)) symmetries of a Type III $\mathbb{Z}_2^3$ SPT  ([arXiv:1508.03468](https://arxiv.org/abs/1508.03468), [arXiv:2411.04181](https://arxiv.org/abs/2411.04181)).

## Notes

- See  ([doi:10.1017/CBO9780511792908](https://doi.org/10.1017/CBO9780511792908)) ([arXiv:2502.14974](https://arxiv.org/abs/2502.14974)) for introductions to this code.
- The $\Phi,\Lambda$ [Decodoku game](https://web.archive.org/web/20161223121819/http://citizensciencegames.com/games/decodoku/) is based on the quantum double model for the group $D_3=S_3$ of permutations on three letters.
