---
type: concept
name: $((7,2,3))$ Pollatsek-Ruskai code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- $((7,2,3))$ icosahedral code
- $((7,2,3))$ Kubischta-Teixeira code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/combinatorial-permutation-invariant
- concepts/qec/icosahedral-fock
- concepts/qec/icosahedral-spin
- concepts/qec/steane
- concepts/qec/t-group
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/icosahedral_permutation_invariant
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: icosahedral_permutation_invariant
---

# $((7,2,3))$ Pollatsek-Ruskai code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/icosahedral_permutation_invariant) (`code_id: icosahedral_permutation_invariant`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Seven-qubit PI code that realizes gates from the binary icosahedral group transversally.
Can also be interpreted as a spin-$7/2$ single-spin code.
The codespace projection is a projection onto an irrep of the binary icosahedral group $2I$.
See Ref.  ([arXiv:2504.20847](https://arxiv.org/abs/2504.20847)) for other non-PI codes realizing $2I$ gates transversally.

In terms of Dicke states, the unnormalized logical states of one version  ([arXiv:2305.07023](https://arxiv.org/abs/2305.07023)) of this code are
\begin{align}
  \begin{split}
    |0_{L}\rangle&\propto \sqrt{15}|D_{0}^{7}\rangle+\sqrt{21}|D_{4}^{7}\rangle\\&\quad+\sqrt{7}\;|D_{2}^{7}\rangle-\sqrt{21}|D_{6}^{7}\rangle\,,\\|1_{L}\rangle&\propto X^{\otimes7}|0_{L}\rangle\,.
  \end{split}
\end{align}
Another version  ([arXiv:2005.10910](https://arxiv.org/abs/2005.10910)) of this code, converted into Dicke states, has unnormalized logical states
\begin{align}
  \begin{split}
    |0_{L}\rangle&\propto\sqrt{3}|D_{0}^{7}\rangle+\sqrt{7}|D_{5}^{7}\rangle\\
    |1_{L}\rangle&\propto\sqrt{7}|D_{2}^{7}\rangle-\sqrt{3}|D_{7}^{7}\rangle\,.
  \end{split}
\end{align}

(source: raw/error-correction-zoo.md)

## Transversal gates

- Binary icosahedral group $2I$ gates can be realized transversally  ([arXiv:2305.07023](https://arxiv.org/abs/2305.07023)). See Ref.  ([arXiv:2504.20847](https://arxiv.org/abs/2504.20847)) for other non-PI codes realizing $2I$ gates transversally.

## Relations

- _parent_: [[concepts/qec/combinatorial-permutation-invariant]] — The Pollatsek-Ruskai code is equivalent to the $Q_{2,1,2,-}$ combinatorial PI code  ([arXiv:2310.05358](https://arxiv.org/abs/2310.05358)). It is a seven-qubit PI code that realizes gates from the binary icosahedral group transversally.
- _parent_: [[concepts/qec/t-group]] — The $((7,2,3))$ Pollatsek-Ruskai code admits a transversal representation of the twisted $1$-group $2I$  ([arXiv:2402.01638](https://arxiv.org/abs/2402.01638)).
- _cousin_: [[concepts/qec/steane]] — The Pollatsek-Ruskai code can be continuously deformed to the Steane code  ([arXiv:2410.07983](https://arxiv.org/abs/2410.07983)).
- _cousin_: [`icosahedron`](https://errorcorrectionzoo.org/c/icosahedron) — Binary icosahedral group $2I$ gates can be realized transversally in the Pollatsek-Ruskai code  ([arXiv:2305.07023](https://arxiv.org/abs/2305.07023)).
- _cousin_: [[concepts/qec/icosahedral-spin]] — The $((7,2,3))$ Pollatsek-Ruskai code maps to the icosahedral spin code via the Dicke state mapping  ([arXiv:2305.07023](https://arxiv.org/abs/2305.07023)).
- _cousin_: [[concepts/qec/icosahedral-fock]] — The $((7,2,3))$ Pollatsek-Ruskai code maps to the icosahedral Fock-state code via the simplex mapping  ([arXiv:2509.20545](https://arxiv.org/abs/2509.20545)).
