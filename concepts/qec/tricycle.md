---
type: concept
name: Tricycle code
status: provisional
updated: '2026-09-29'
concept_kind: qec
aliases:
- Three-block Abelian group-algebra code
- Trivariate tricycle (TT) code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/3d-color
- concepts/qec/abelian-2bga
- concepts/qec/higher-dimensional-toric
- concepts/qec/multisector-hypergraph
- concepts/qec/multivariate-multicycle
- concepts/qec/qubit-generalized-homological-product-css
- concepts/qec/single-shot
- concepts/qec/three-block-quantum
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/tricycle
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: tricycle
---

# Tricycle code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/tricycle) (`code_id: tricycle`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A three-block CSS code whose commuting matrices represent three elements $a,b,c$ of the group algebra $\mathbb{F}_2[G]$ of a finite Abelian group $G$.
The code is the balanced product over $\mathbb{F}_2[G]$ of the three classical group-algebra codes defined by $a$, $b$, and $c$, extending the two-block 2BGA construction to three homological dimensions  ([arXiv:2508.08191](https://arxiv.org/abs/2508.08191), [arXiv:2508.10714](https://arxiv.org/abs/2508.10714)).
The third dimension provides $Z$-type metachecks, which make the code single-shot decodable in the $Z$ basis, and a cup product, which yields constant-depth transversal $CCZ$ circuits for magic-state generation  ([arXiv:2508.10714](https://arxiv.org/abs/2508.10714)).

Each element defines a two-term complex $\mathbb{F}_2[G]\xrightarrow{a}\mathbb{F}_2[G]$, and the product of the three complexes is a four-term complex $\mathbb{F}_2[G]\to\mathbb{F}_2[G]^3\to\mathbb{F}_2[G]^3\to\mathbb{F}_2[G]$  ([arXiv:2508.10714](https://arxiv.org/abs/2508.10714)).
The $n=3|G|$ qubits sit at the second term, the $X$-type checks at the first, the $Z$-type checks at the third, and the $Z$-type metachecks at the fourth, giving check and metacheck matrices
\begin{align}
  H_X = \left[A^T\, B^T\, C^T\right],\quad
  H_Z = \left[
  \begin{array}{ccc}
    C&0&A\\ 0&C&B\\ B&A&0
  \end{array}
  \right],\quad
  H_{\text{meta}} = \left[B\, A\, C\right]~,
\end{align}
where $A$, $B$, and $C$ are Kronecker products of circulant matrices representing $a$, $b$, and $c$, and where $H_{\text{meta}} H_Z = 0$  ([arXiv:2508.10714](https://arxiv.org/abs/2508.10714)).
Each cyclic factor in the chosen decomposition of $G$ contributes one circulant tensor factor  ([arXiv:2508.10714](https://arxiv.org/abs/2508.10714)).
There are $|G|$ $X$-type checks of weight $\text{wt}(a)+\text{wt}(b)+\text{wt}(c)$ and $3|G|$ $Z$-type checks.
Codes are often labeled by their element weights, e.g., $2$-$2$-$2$ or $4$-$2$-$2$.
Bivariate tricycle codes, i.e., those over $\mathbb{Z}_{\ell_x}\times\mathbb{Z}_{\ell_y}$, can be laid out on a triangular lattice on a 2D torus with three qubits per site  ([arXiv:2510.07269](https://arxiv.org/abs/2510.07269)).
All $X$-type checks are then translates of a single check, and so are the $Z$-type checks within each of the three rows of $H_Z$  ([arXiv:2510.07269](https://arxiv.org/abs/2510.07269)).

Tricycle codes are *connected* when the supports of $a$, $b$, and $c$ generate $G$  ([arXiv:2508.10714](https://arxiv.org/abs/2508.10714)).
A $4$-$2$-$2$ example is the $⟦48,6,(8,4)⟧$ code, with distances listed as $(d_X,d_Z)$  ([arXiv:2508.10714](https://arxiv.org/abs/2508.10714)).
See Refs.  ([arXiv:2508.10714](https://arxiv.org/abs/2508.10714)) and  ([arXiv:2508.08191](https://arxiv.org/abs/2508.08191)) for further instances.

(source: raw/error-correction-zoo.md)

## Protection

All connected tricycle codes satisfy $d_Z \leq d_X$, and their distance is bounded below as $d \geq \frac{1}{|N|}\min(d_A,d_B,d_C)$  ([arXiv:2508.10714](https://arxiv.org/abs/2508.10714)).
Here, $d_M$ is the distance of the classical code whose parity-check matrix is $M^T$, and $N$ is the intersection of the support subgroups of $a$, $b$, and $c$.
The single-shot distance associated with the $Z$-type metachecks is equal to $d_Z$  ([arXiv:2508.08191](https://arxiv.org/abs/2508.08191)).

## Rate

Tricycle code rates are lower than those of comparable bivariate bicycle codes  ([arXiv:2508.10714](https://arxiv.org/abs/2508.10714)).
They are much higher than the rates of three-dimensional homological product codes of comparable block length, including the 3D color code  ([arXiv:2508.10714](https://arxiv.org/abs/2508.10714)).

## General gates

- Constant-depth circuits of physical $CCZ$ gates acting across three code blocks realize logical $CCZ$ circuits  ([arXiv:2508.10714](https://arxiv.org/abs/2508.10714)).
Such circuits are constructed via a symmetric triple cup product modifying the framework of Ref.  ([arXiv:2410.16250](https://arxiv.org/abs/2410.16250)).
Applying them to logical $|+\rangle$ states yields hypergraph magic states  ([arXiv:2508.10714](https://arxiv.org/abs/2508.10714)).
Weight $4$-$2$-$2$ codes host depth-eight circuits  ([arXiv:2508.10714](https://arxiv.org/abs/2508.10714)).
Several codes with binomial elements host depth-two circuits  ([arXiv:2510.07269](https://arxiv.org/abs/2510.07269)).
The pre-orientation conditions for such *copy-cup* gates are determined combinatorially in Ref.  ([arXiv:2602.23307](https://arxiv.org/abs/2602.23307)).
The non-associative 3-copy-cup gate forces distance two, whereas the symmetric variant used for tricycle codes can reach higher distance  ([arXiv:2602.23307](https://arxiv.org/abs/2602.23307)).
- Transversal dimension jump, a code-switching protocol with the qubit Abelian 2BGA code defined by $a$ and $b$, a 2D component code of the tricycle code  ([arXiv:2510.07269](https://arxiv.org/abs/2510.07269)).
Physical CNOTs from the $a$- and $b$-block qubits of the tricycle code onto the corresponding Abelian 2BGA qubits form a one-way transversal logical CNOT  ([arXiv:2510.07269](https://arxiv.org/abs/2510.07269)).
When $|G|$ is odd and $c$ lies in the ideal $(a,b)$, the CNOT couples each Abelian 2BGA logical qubit to a distinct tricycle logical qubit  ([arXiv:2510.07269](https://arxiv.org/abs/2510.07269)).
One-bit teleportation through it then switches logical qubits between the two codes  ([arXiv:2510.07269](https://arxiv.org/abs/2510.07269)).

## Fault tolerance

- Fault-tolerant logical operations include transversal $CZ$ gates between code blocks and shift-automorphism Clifford gates within a block  ([arXiv:2508.08191](https://arxiv.org/abs/2508.08191)).
Selected constructions also admit constant-depth logical $CCZ$ circuits  ([arXiv:2508.08191](https://arxiv.org/abs/2508.08191)).
- Single-shot magic-state generation protocol combining single-shot logical-state preparation, constant-depth $CCZ$ circuits, and single-shot error correction  ([arXiv:2508.10714](https://arxiv.org/abs/2508.10714)).
An error-detection variant postselects on the final $X$-type detectors after a depth-two $CCZ$ circuit  ([arXiv:2510.07269](https://arxiv.org/abs/2510.07269)).
- Optimal-depth syndrome-extraction circuits, along with an implementation protocol for reconfigurable qubit arrays  ([arXiv:2508.10714](https://arxiv.org/abs/2508.10714)).

## Decoders

- BP+LSD decoding combined with cluster-based post-selection  ([arXiv:2508.10714](https://arxiv.org/abs/2508.10714)).
With full error detection, a $⟦48,6,(8,4)⟧$ code reaches logical error rates of about $6\times 10^{-10}$ at a $30\%$ acceptance fraction  ([arXiv:2508.10714](https://arxiv.org/abs/2508.10714)).
- MWPM decoder for $Z$-type errors of codes with binomial elements, whose $X$-type check matrix has column weight two  ([arXiv:2510.07269](https://arxiv.org/abs/2510.07269)).

## Threshold

- Circuit-level noise threshold above $0.5\%$ for a family of $4$-$2$-$2$ codes, and about $0.4\%$ for $4$-$4$-$4$ codes  ([arXiv:2508.10714](https://arxiv.org/abs/2508.10714)).
- Circuit-level depolarizing noise without idling errors: pseudo-threshold of about $0.4\%$ for the $⟦27,3,3⟧$, $⟦45,3,4⟧$, and $⟦81,3,5⟧$ bivariate codes under MWPM decoding  ([arXiv:2510.07269](https://arxiv.org/abs/2510.07269)).

## Relations

- _parent_: [[concepts/qec/qubit-generalized-homological-product-css]] — Tricycle codes are three-dimensional balanced products of classical group-algebra codes  ([arXiv:2508.10714](https://arxiv.org/abs/2508.10714)).
- _parent_: [[concepts/qec/multivariate-multicycle]] — Tricycle codes are MM codes with $t=3$, with qubits placed at a level admitting $Z$-type metachecks  ([arXiv:2508.10714](https://arxiv.org/abs/2508.10714)).
- _parent_: [[concepts/qec/three-block-quantum]] — Tricycle codes are three-block CSS codes whose commuting matrices are constructed from an Abelian group algebra  ([arXiv:2508.08191](https://arxiv.org/abs/2508.08191), [arXiv:2508.10714](https://arxiv.org/abs/2508.10714)).
- _cousin_: [[concepts/qec/single-shot]] — Tricycle codes support single-shot decoding in the $Z$ basis, with single-shot distance equal to $d_Z$  ([arXiv:2508.08191](https://arxiv.org/abs/2508.08191)).
Soundness has been proven for a subclass of codes, and there is numerical evidence for single-shot logical-state preparation  ([arXiv:2508.10714](https://arxiv.org/abs/2508.10714)).
- _cousin_: [[concepts/qec/higher-dimensional-toric]] — Tricycle codes with weight-two elements $a_i = 1+x_i$ are locally equivalent to 3D toric codes  ([arXiv:2506.16910](https://arxiv.org/abs/2506.16910)).
- _cousin_: [[concepts/qec/3d-color]] — Both 3D color codes and tricycle codes admit constant-depth $CCZ$ circuits stemming from cup products on three-dimensional chain complexes  ([arXiv:2508.10714](https://arxiv.org/abs/2508.10714)).
Tricycle codes attain much higher rates at comparable block lengths  ([arXiv:2508.10714](https://arxiv.org/abs/2508.10714)).
- _cousin_: [[concepts/qec/multisector-hypergraph]] — Connected tricycle codes are three-fold homological product codes over the ring $\mathbb{F}_2[N]$ of the intersection subgroup $N$  ([arXiv:2508.10714](https://arxiv.org/abs/2508.10714)).
They are binary three-dimensional hypergraph-product codes only in special cases, such as when $N$ is trivial  ([arXiv:2508.10714](https://arxiv.org/abs/2508.10714)).
- _cousin_: [[concepts/qec/abelian-2bga]] — The qubit Abelian 2BGA code defined by $a$ and $b$ is a 2D component code of the tricycle code defined by $a$, $b$, and $c$  ([arXiv:2510.07269](https://arxiv.org/abs/2510.07269)).
A one-way transversal CNOT from the tricycle code to the Abelian 2BGA code yields teleportation-based code switching between the two codes  ([arXiv:2510.07269](https://arxiv.org/abs/2510.07269)).
This holds when $|G|$ is odd and $c$ lies in the ideal $(a,b)$  ([arXiv:2510.07269](https://arxiv.org/abs/2510.07269)).
