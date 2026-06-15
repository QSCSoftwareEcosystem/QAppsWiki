---
type: concept
name: Galois-qudit quantum RM code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/galois-css
- concepts/qec/galois-true-stabilizer
- concepts/qec/stabilizer-over-gfqsq
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/galois_reed_muller
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: galois_reed_muller
---

# Galois-qudit quantum RM code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/galois_reed_muller) (`code_id: galois_reed_muller`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

True Galois-qudit stabilizer code constructed from generalized Reed-Muller (GRM) codes via the Galois-qudit Hermitian construction, the Galois-qudit CSS construction, or directly from their parity-check matrices  ([arXiv:quant-ph/0502001](https://arxiv.org/abs/quant-ph/0502001)) ([arXiv:0712.0103](https://arxiv.org/abs/0712.0103)).

The CSS construction yields the code
\begin{align}
  ⟦q^m,k(v_2)-k(v_1),\min\{d(v_1^{\perp}),d(v_2)\}⟧_q
\end{align}
constructed from the generalized Reed-Muller codes RM$_q(v_1,m)$ and RM$_q(v_2,m)$, with $0\leq v_1 \leq v_2 \leq m(q-1)-1$  ([arXiv:quant-ph/0502001](https://arxiv.org/abs/quant-ph/0502001)).
The parameters are
\begin{align}
  k(v) &= \sum_{j=0}^{m}(-1)^{j}\dbinom{m}{j}\dbinom{m+v-jq}{v-jq} \\
  d(v) &= (R+1)q^{Q}~,
\end{align}
where $m(q-1)-v=(q-1)Q+R$ so that $0\leq R\leq q-1$.
Here $0\leq v_1,v_2 \leq m(q-1)-1$, $q$ is a prime power, and $m$ is a positive integer.

Using the code GRM$_{q^2}(v,m)$ for $0\leq v \leq m(q-1)-1$, the Hermitian construction yields the pure quantum code
\begin{align}
  ⟦q^{2m},q^{2m}-2k(v),d(v^{\perp})⟧_q
\end{align}
 ([arXiv:quant-ph/0502001](https://arxiv.org/abs/quant-ph/0502001)), where
\begin{align}
  k(v) &= \sum_{j=0}^{m}(-1)^{j}\dbinom{m}{j}\dbinom{m+v-jq^2}{v-jq^2} \\
  d(v^{\perp}) &= (R+1)q^{2Q}~,
\end{align}
with $v+1 = (q^2 - 1)Q + R$.

For a CSS code constructed from classical codes $C_1$ and $C_2$, the punctured code is defined as
\begin{align}
  P(C) = \{(a_ib_i)_{i=1}^{n} \mid a \in C_1, b \in C_2^{\perp}\}^{\perp}~.
\end{align}
Quantum RM codes can be punctured to any length $r$, provided
\begin{align}
  P(C) = \mathcal{R}_q(v_2-v_1,m)
\end{align}
has a codeword of this weight.
Likewise, the Hermitian puncture code contains $\mathcal{R}_{q^2}(\mu,m)^\perp|_{\mathbb{F}_q}$ for $(q+1)\nu \leq \mu \leq m(q^2-1)-1$, yielding punctured descendants with distance at least that of the parent code  ([arXiv:quant-ph/0502001](https://arxiv.org/abs/quant-ph/0502001)).

(source: raw/error-correction-zoo.md)

## Protection

The CSS family is pure with distance $\min\{d(v_1^\perp),d(v_2)\}$, while the Hermitian family is pure with distance $d(v^\perp)$; punctured descendants retain at least the parent distance  ([arXiv:quant-ph/0502001](https://arxiv.org/abs/quant-ph/0502001)).
QRM$_{d}(m)$ quantum codes are $\mathcal{M}_{d}^{m}$ distillation codes of distance $D=2$. We define a $\mathcal{M}_{d}^{m}$ distillation code as any $n$ Galois-qudit stabilizer code $C$ having the following properties: (a) All $M \in \mathcal{M}_{d}^{m}$ are transversal so that $M^{\otimes n}C(M^{\otimes n})^{\dagger} = M_{L}^{\dagger}CM_{L}$, (b) the code has distance $D \geq 2$, and (c) the code has logical pauli operators $X_{L} = X[\mathbf{1}]$ and $Z_{L} = Z[(d-1)\mathbf{1}]$. Here, $\mathbf{1}$ is a shorthand for the vector $(1,1, \dots, 1)$.

## Rate

The CSS family has rate $ (k(v_2)-k(v_1) )/q^m$, while the Hermitian family has rate $1-2k(v)/q^{2m}$  ([arXiv:quant-ph/0502001](https://arxiv.org/abs/quant-ph/0502001)).

## Relations

- _parent_: [[concepts/qec/galois-true-stabilizer]] — Galois-qudit RM codes can be constructed via the Galois-qudit Hermitian construction, the Galois-qudit CSS construction, or directly from their parity-check matrices  ([arXiv:quant-ph/0502001](https://arxiv.org/abs/quant-ph/0502001)) ([arXiv:0712.0103](https://arxiv.org/abs/0712.0103)).
- _cousin_: [`generalized_reed_muller`](https://errorcorrectionzoo.org/c/generalized_reed_muller) — Generalized RM codes can be used to construct Galois-qudit RM codes via the Galois-qudit Hermitian construction, the Galois-qudit CSS construction, or directly from their parity-check matrices  ([arXiv:quant-ph/0502001](https://arxiv.org/abs/quant-ph/0502001)) ([arXiv:0712.0103](https://arxiv.org/abs/0712.0103)).
- _cousin_: [`projective_reed_muller`](https://errorcorrectionzoo.org/c/projective_reed_muller) — Projective RM codes can be used to construct Galois-qudit RM codes  ([doi:10.1201/9781584889007-18](https://doi.org/10.1201/9781584889007-18)) ([arXiv:0812.5104](https://arxiv.org/abs/0812.5104)).
- _cousin_: [[concepts/qec/galois-css]] — Galois-qudit RM codes admit a CSS subfamily built from nested GRM codes $ \mathrm{GRM}_q(v_1,m) \subseteq \mathrm{GRM}_q(v_2,m) $  ([arXiv:quant-ph/0502001](https://arxiv.org/abs/quant-ph/0502001)).
- _cousin_: [[concepts/qec/stabilizer-over-gfqsq]] — Galois-qudit RM codes admit a Hermitian subfamily built from $\mathrm{GRM}_{q^2}(v,m)$ codes contained in their Hermitian duals  ([arXiv:quant-ph/0502001](https://arxiv.org/abs/quant-ph/0502001)).
