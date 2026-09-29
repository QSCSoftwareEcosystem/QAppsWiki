---
type: concept
name: Galois-qudit RS code
status: provisional
updated: '2026-09-29'
concept_kind: qec
aliases:
- Galois-qudit polynomial code (QPyC)
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/galois-fqrs
- concepts/qec/galois-grs
- concepts/qec/galois-reed-muller
- concepts/qec/quantum-concatenated
- concepts/qec/quantum-mds
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/galois_polynomial
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: galois_polynomial
---

# Galois-qudit RS code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/galois_polynomial) (`code_id: galois_polynomial`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A Galois-qudit CSS code family (with $n\leq q$) constructed using two RS codes over $\mathbb{F}_q$.

Let $C_1$ be a $[n,k_1,d_1]_q$ RS code and $C_2^\perp$ be a $[n,k_1-k_2,d_2]_q$ RS code, modified such that $C_2^\perp \subseteq C_1$ and $0\le k_2 \le k_1 \le n$.
Then, a Galois-qudit RS code is a pure $⟦n,k_2,d⟧_q$ Galois-qudit CSS code with $d=\min(n-k_1+1,k_1-k_2+1)$.
The code is the span of the basis codewords over $\mathbb{F}_q$,
\begin{align}
|\overline{\beta_0,\cdots,\beta_{k_2-1}}\rangle
=
\sum_{(\beta_{k_2},\cdots,\beta_{k_1-1})\in \mathbb{F}_q^{k_1-k_2}}
\bigotimes_{i=1}^{n}
\left| \sum_{j=0}^{k_1-1} \beta_j \alpha_i^j \right\rangle,
\end{align}
where $(\alpha_1, \cdots, \alpha_n)$ are $n$ distinct points chosen for code $C_1$ from $\mathbb{F}_q\setminus \{0\}$, so that $n<q$ .

Logical states can instead be labeled by the $k_2$ highest-degree coefficients, with the superposition running over the $k_1-k_2$ lowest-degree ones.
Inverting the evaluation points and applying single-Galois-qudit multiplication gates maps the code above onto a code of this form with the same parameters.
This second form also allows zero as an evaluation point, so that $n\leq q$.
The case $n=q$, for which the evaluation points exhaust $\mathbb{F}_q$, is constructed from extended GRS codes.

(source: raw/error-correction-zoo.md)

## Protection

Galois-qudit RS codes can be adapted for insertion and deletion noise  ([arXiv:2306.13399](https://arxiv.org/abs/2306.13399)).

## Magic scaling exponent

Punctured RS codes can be used for magic-state distillation with a spacetime overhead of $(\log \frac{1}{\epsilon})^{\gamma}$, with the magic-state scaling exponent $\gamma \to 0$ with decreasing $\epsilon$  ([arXiv:2411.03632](https://arxiv.org/abs/2411.03632)).

## Transversal gates

- There exists an order $⟦n,\Theta(n),\Theta(n)⟧_{n^2}$ punctured RS code family that admits transversal $CCZ$ gates for any three logical qubits  ([arXiv:2502.01864](https://arxiv.org/abs/2502.01864)). This code can be treated as a qubit code by decomposing each Galois qudit into a Kronecker product of several qubits; see  ([doi:10.1109/18.959288](https://doi.org/10.1109/18.959288)) ([arXiv:quant-ph/0501074](https://arxiv.org/abs/quant-ph/0501074)) ([arXiv:2408.10140](https://arxiv.org/abs/2408.10140), [arXiv:2408.09254](https://arxiv.org/abs/2408.09254)). This yields a qubit code family that is asymptotically good up to poly-logarithmic factors  ([arXiv:2502.01864](https://arxiv.org/abs/2502.01864)).
- Galois-qudit RS codes can be concatenated with quantum multiplication-friendly codes to yield CSS codes over a constant prime-power alphabet $q$ admitting a transversal $CCZ_q$ gate (and, for $q \geq 5$, also a transversal $U_q$ gate) with nearly linear code dimension and distance, $k,d = \Omega(n/2^{O(\log^* n)})$, where $\log^* n$ is the iterated logarithm (the number of times $\log$ must be applied to $n$ before the result is $\leq 1$)  ([arXiv:2408.09254](https://arxiv.org/abs/2408.09254)).

## Fault tolerance

- The original prime-field construction admits a fault-tolerant universal gate set beyond the standard transversal gates for qudit CSS codes  ([arXiv:quant-ph/9906129](https://arxiv.org/abs/quant-ph/9906129)). Generalized NOT, SUM, SWAP, scalar multiplication, and phase gates are implemented transversally. A logical Fourier transform is implemented by weighted physical Fourier transforms followed by code switching: a length-$m$ degree-$d$ code is mapped to the corresponding Fourier-dual code of degree $m-d-1$. A transversal product gate $|a\rangle|b\rangle|c\rangle \mapsto |a\rangle|b\rangle|c+ab\rangle$ maps into a degree-$2d$ code, after which degree reduction switches back to the original degree.
- Aharonov and Ben-Or performed the code switching needed for their Fourier and product gates using concatenation and degree reduction  ([arXiv:quant-ph/9906129](https://arxiv.org/abs/quant-ph/9906129)). The same switching between Galois-qudit RS codes of different degree can also be implemented by teleportation using encoded Bell states. This uses the transversal SUM gate between the two codes, with the lower-degree code serving as the control.
- Galois-qudit RS codes yield fault-tolerant quantum computation with constant space and optimal time overheads  ([arXiv:2411.03632](https://arxiv.org/abs/2411.03632)), improving over previous schemes  ([arXiv:2207.08826](https://arxiv.org/abs/2207.08826), [arXiv:2402.09606](https://arxiv.org/abs/2402.09606)).

## Relations

- _parent_: [[concepts/qec/galois-grs]]
- _parent_: [[concepts/qec/galois-reed-muller]] — Galois-qudit RS codes are the Galois-qudit RM codes from the CSS construction with $m=1$ whose two GRM codes are punctured to the same $n$ evaluation points. For $m=1$, GRM codes are extended RS codes  ([arXiv:quant-ph/0502001](https://arxiv.org/abs/quant-ph/0502001)). Every Galois-qudit RS code takes this form when its logical states are labeled by the highest-degree coefficients, possibly after inverting the evaluation points and applying single-Galois-qudit multiplication gates.
- _cousin_: [[concepts/qec/galois-fqrs]] — A FQRS code with no extra grouping ($m=1$) reduces to a Galois-qudit RS code that is CSS.
- _cousin_: [`reed_solomon`](https://errorcorrectionzoo.org/c/reed_solomon) — Galois-qudit RS codes are CSS codes constructed from RS codes.
- _cousin_: [`extended_reed_solomon`](https://errorcorrectionzoo.org/c/extended_reed_solomon) — Galois-qudit RS codes of length $n=q$, whose evaluation points exhaust $\mathbb{F}_q$, are constructed from extended GRS codes.
- _cousin_: [[concepts/qec/quantum-mds]] — A Galois-qudit RS code is a quantum MDS code when $n-k_1=k_1-k_2$.
- _cousin_: [[concepts/qec/quantum-concatenated]] — Recursive concatenations of Galois-qudit RS codes can be asymptotically good  ([arXiv:0901.0042](https://arxiv.org/abs/0901.0042)).
