---
type: concept
name: Matrix-model code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/fock-state
- concepts/qec/hamiltonian
- concepts/qec/holographic
- concepts/qec/self-correct
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/matrix_qm
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: matrix_qm
---

# Matrix-model code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/matrix_qm) (`code_id: matrix_qm`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Multimode Fock-state bosonic approximate code derived from a matrix model, i.e., a bosonic theory with a large non-Abelian gauge group.
The model's degrees of freedom are matrix-valued bosons $a$, each consisting of $N^2$ harmonic oscillator modes and subject to an $SU(N)$ gauge symmetry.

A simple matrix-model code  ([arXiv:2211.08448](https://arxiv.org/abs/2211.08448)) consists of two spatially separated bosons with codewords
\begin{align}
    |\mathcal{I}\rangle :=\prod_{(m,n)\in \mathcal{I} } \frac{\text{Tr}(a_1^{\dagger m}a_2^{\dagger n})}{N^{\frac{m+n}{2}}}|0\rangle_{12}~,
\end{align}
where $\cal I$ is some set of integer two-tuples, and $n,m\geq 0$.

Gauge symmetry is assumed to be enforced in the above model.
In other variants  ([arXiv:2211.08448](https://arxiv.org/abs/2211.08448)), gauge symmetry is enforced energetically, requiring an energy penalty to scale as $\log(N)$ in order to obtain a polynomial memory lifetime below a critical temperature.

(source: raw/error-correction-zoo.md)

## Protection

For the spatially separated boson code, logical errors stemming from gauge-invariant physical errors are suppressed polynomially with the number of modes $N$, as shown by the approximate error-correction conditions.
For sufficiently low temperature, the memory time scales as $N^2$ when the model is subject to a thermal bath  ([arXiv:2211.08448](https://arxiv.org/abs/2211.08448)).

## Relations

- _parent_: [[concepts/qec/fock-state]] — Matrix-model logical states lie in a low-energy Fock-state subspace.
- _parent_: [[concepts/qec/hamiltonian]] — Matrix-model codewords for simple codes are eigenstates of a matrix-model Hamiltonian.
- _parent_: [[concepts/qec/holographic]] — Matrix-model codes are motivated by the AdS/CFT correspondence because it is manifest in continuous non-Abelian gauge theories with large gauge groups  ([arXiv:2211.08448](https://arxiv.org/abs/2211.08448)).
- _cousin_: [[concepts/qec/self-correct]] — Matrix-model codes are similar to self-correcting memories in the sense that memory time becomes infinite in the thermodynamic limit, but with corrections being polynomial in $N$.
