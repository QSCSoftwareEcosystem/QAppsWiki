---
type: concept
name: Quantum Tanner code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/expander-lifted-product
- concepts/qec/generalized-quantum-tanner
- concepts/qec/good-qldpc
- concepts/qec/single-shot
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/quantum_tanner
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: quantum_tanner
---

# Quantum Tanner code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/quantum_tanner) (`code_id: quantum_tanner`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Member of a family of QLDPC codes based on two compatible classical Tanner codes defined on a two-dimensional Cayley complex, a complex constructed from Cayley graphs of groups.
For certain choices of codes and complex, the resulting codes have asymptotically good parameters.
See Ref.  ([arXiv:2508.05095](https://arxiv.org/abs/2508.05095)) for explicit instances based on dihedral groups.
This construction has been generalized to Schreier graphs  ([arXiv:2405.07980](https://arxiv.org/abs/2405.07980)).

The underlying geometric complex of the code is a left-right Cayley complex $\operatorname{Cay}_2(A,G,B)$, where $G$ is a finite group and $A=A^{-1}$, $B=B^{-1}$ are two symmetric generating sets satisfying the total no-conjugacy condition: $ag\ne gb$ for any $g\in G$, $a\in A$, and $b\in B$.
The vertices of the complex are group elements, i.e., $V=G$. If necessary, the double cover of the graph should be taken so that the graph is bipartite, $V=V_0\sqcup V_1$.

There are two types of edges in the resulting complex,
  \begin{align}
  \begin{split}
    E_A &= \{(g,ag): g\in G, a\in A\}\\
    E_B &= \{(g,gb): g\in G, b\in B\}~.
  \end{split}
  \end{align}
The faces are squares defined by quadruples,
  \begin{align}
    Q = \{(g,ag,gb,agb): g\in G, a\in A, b\in B\}~.
  \end{align}
Two additional graphs can be obtained from $\operatorname{Cay}_2(A,G,B)$ by taking the diagonals of the squares as edges, $\mathcal G_0^\square = (V_0, Q)$ and $\mathcal G_1^\square = (V_1, Q)$.

In the quantum Tanner construction, qubits are placed on the squares of the left-right Cayley complex.
Two classical codes $C_A$ and $C_B$ of blocklengths $|A|$ and $|B|$, respectively, are chosen, yielding local codes $C_0 = C_A\otimes C_B$ and $C_1 = C_A^\perp\otimes C_B^\perp$.
The quantum Tanner code is a CSS code defined by the classical Tanner codes $C_Z = T(\mathcal G_0^\square, C_0^\perp)$ and $C_X = T(\mathcal G_1^\square, C_1^\perp)$.
The figure below depicts an example of a stabilizer generator.



To achieve asymptotically good parameters, fixed classical local codes are chosen so that their dual tensor codes are sufficiently robust, and the left-right Cayley complexes are chosen to be sufficiently expanding. The family is defined using a family of groups $G$ of increasing size but constant-size generating sets $A$, $B$.

(source: raw/error-correction-zoo.md)

## Protection

For correctly chosen complexes and local codes, the distance scales as $d=\Theta(n)$. Minimum distance bound obtained using robustness of dual tensor-product codes  ([arXiv:2208.05537](https://arxiv.org/abs/2208.05537)).

## Rate

Asymptotically good QLDPC codes. When $C_A$ and $C_B$ are chosen to have rates not equal to a half, the number of encoded qubits scales as $k=\Theta(n)$.

## Decoders

- Linear-time potential-based decoder similar to the small-set-flip decoder for quantum expander codes  ([arXiv:2206.06557](https://arxiv.org/abs/2206.06557)).
- Linear-time decoder  ([arXiv:2206.07571](https://arxiv.org/abs/2206.07571)).
- Logarithmic-time mismatch decomposition decoder  ([arXiv:2208.05537](https://arxiv.org/abs/2208.05537)).

## Code capacity threshold

- Independent $X,Z$ noise: lower bound under potential-based decoder  ([arXiv:2206.06557](https://arxiv.org/abs/2206.06557)).

## Realizations

- Used to obtain explicit lower bounds in the sum-of-squares game  ([arXiv:2204.11469](https://arxiv.org/abs/2204.11469)).
- States that, on average, achieve small violations of check operators for quantum Tanner codes require a circuit of non-constant depth to make. They are used in the proof  ([arXiv:2206.13228](https://arxiv.org/abs/2206.13228)) of the NLTS conjecture  ([arXiv:1301.1363](https://arxiv.org/abs/1301.1363)).

## Relations

- _parent_: [[concepts/qec/generalized-quantum-tanner]] — Generalized quantum Tanner codes constructed out of bipartite double covers of Cayley graphs reduce to quantum Tanner codes  ([arXiv:2405.07980](https://arxiv.org/abs/2405.07980)).
- _cousin_: [[concepts/qec/single-shot]] — Certain quantum Tanner codes facilitate single-shot decoding  ([arXiv:2306.12470](https://arxiv.org/abs/2306.12470)).
- _cousin_: [[concepts/qec/good-qldpc]] — Quantum Tanner code construction yields asymptotically good QLDPC codes.
- _cousin_: [`regular_binary_tanner`](https://errorcorrectionzoo.org/c/regular_binary_tanner) — Regular binary Tanner codes are used in constructing quantum Tanner codes.
- _cousin_: [`tensor`](https://errorcorrectionzoo.org/c/tensor) — Tensor codes are used in constructing quantum Tanner codes.
- _cousin_: [[concepts/qec/expander-lifted-product]] — Quantum Tanner codes are an attempt to construct asymptotically good QLDPC codes that are similar to but simpler than expander lifted-product codes; see Ref.  ([arXiv:2206.07571](https://arxiv.org/abs/2206.07571)) for connection between the codes.

## Notes

- For details, see talk by [A. Leverrier](https://www.youtube.com/watch?v=5GO3BtJuo3I).
