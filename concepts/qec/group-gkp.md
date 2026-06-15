---
type: concept
name: Group GKP code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Non-Abelian CSS code
- Group coset code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/covariant
- concepts/qec/group-quantum
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/group_gkp
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: group_gkp
---

# Group GKP code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/group_gkp) (`code_id: group_gkp`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Group-based quantum code whose construction is based on nested subgroups $H\subset K
\subset G$. 
The group GKP code was originally formulated as an extension of the GKP code construction to other group-valued spaces.
In other words, the only requirement to construct group GKP codes is that the configuration space $G$ is a group under some operation.

Group GKP codes are based on the following decomposition of the underlying group,
\begin{align}
  G \cong \frac{G}{K} \times \frac{K}{H} \times \widehat{H}~,
\end{align}  
where $\widehat{H}$ is the Fourier space of $H$ obtained from the Peter-Weyl theorem.
For generalized GKP codes, detectable position shifts are labeled by elements of the coset space $G/K$, logical position shifts are labeled by elements of $K/H$ (i.e., cosets of $H$ in $K$), and undetectable logical phase errors are labeled by representations of $G$ that represent $H$ trivially but $K$ nontrivially  ([arXiv:1911.00099](https://arxiv.org/abs/1911.00099)).

The codes' logical subspace is spanned by basis states that are equal
superpositions of elements of $K/H$, and can be finite- or
infinite-dimensional depending on the chosen groups.
Codes are stabilized by $X$-type group-based right-multiplication error operators representing $H$, all $Z$-type operators that are constant on $K$, and any left-multiplication error operators that are constant on the codespace.
The $Z$-type operators are non-unitary matrix product operators for non-Abelian groups.

The construction encompasses all Pauli-type CSS codes since those are Abelian group GKP codes; relevant $G$ and $H$ are tabulated in \ref{table:group-gkp-codes}.
An $n$-qudit Galois CSS code corresponds to the $\mathbb{F}_q^{k_1} \subseteq \mathbb{F}_q^{k_2} \subset \mathbb{F}_q^{n}$ group construction, where $k=k_2-k_1$, and where the group operation is addition; this construction should be extendable to additive $q$-ary codes since those are also groups under addition.  
An $⟦n,k,d⟧_{\mathbb{R}}$ analog CSS code corresponds to the $\mathbb{R}^{ k_1} \subseteq \mathbb{R}^{ k_2} \subset \mathbb{R}^{n}$ group construction, where $k=k_2-k_1$.
A single-mode qubit GKP CSS code corresponds to the $2\mathbb{Z}\subset\mathbb{Z}\subset\mathbb{R}$ group construction, and multimode GKP CSS codes can be similarly described.
Oscillator-into-oscillator GKP CSS codes for $n$ modes correspond to subgroups $\mathbb{Z}^m$ for $m<n$.
Rotor GKP codes correspond to the $\mathbb{Z}_{k_1} \subseteq \mathbb{Z}_{k_2} \subset U(1)$ group construction, where $k=k_2/k_1$.
\begin{table}
  \begin{cells}
  \celldata<c H, c H, c H, l H>{Space & $G$ & $K$ & Related code}
  \celldata<c, c, c, l>{
  $n$ qubits & $\mathbb{Z}_2^n$ & $\mathbb{Z}_2^m$
      & qubit CSS
      \\
  $n$ modular qudits & $\mathbb{Z}_q^n$ & $\mathbb{Z}_q^m$
      & modular-qudit CSS
      \\
  $n$ Galois qudits & $\mathbb{F}_q^n$ & $\mathbb{F}_q^m$
      & Galois-qudit CSS
      \\
  $n$ modes & $ \mathbb{R}^n $ & $ \mathbb{R}^m $
      & analog CSS
      \\
  $n$ modes & $ \mathbb{R}^n $ & $ \mathbb{Z}^n $
      & multimode GKP
      \\
  $n$ modes & $ \mathbb{R}^n $ & $ \mathbb{Z}^m $
      & oscillator-into-oscillator GKP
      \\
  $n$ rotors & $ \mathbb{Z}^n $ & $ \mathbb{Z}^m $
      & homological rotor
      \\
  rotor & $U(1)$ & $\mathbb{Z}_n$
      & rotor GKP
      \\
  rigid body & $SO(3)$ & $K$
      & molecular
      \\
  1 mode, 1 qudit & $ \mathbb{R} \times \mathbb{Z}_q $ & $ \mathbb{Z} $
      & simple LCA
  }
  \end{cells}
  \caption{
  Special cases of group GKP codes.
  }
  \label{table:group-gkp-codes}
\end{table}

(source: raw/error-correction-zoo.md)

## Protection

Protects against generalized bit-flip errors $g\in G$ that are inside the fundamental domain of $G/K$. Protection against phase-flip errors determined by branching rules of irreps of $G$ into those of $K$, and further into those of $H$.

## Transversal gates

- Group-GKP codes corresponding to the $G^{k_1} \subseteq G^{k_2} \subset G^{n}$ group construction admit $X$-type logical group-multiplication gates, and are thus covariant with respect to the induced $G^{k_2}$-action  ([arXiv:1911.00099](https://arxiv.org/abs/1911.00099)).

## Realizations

- Cryptographic applications stemming from the monogamy of entanglement of group GKP codes and their error words  ([arXiv:2212.03935](https://arxiv.org/abs/2212.03935)).

## Relations

- _parent_: [[concepts/qec/group-quantum]]
- _cousin_: [[concepts/qec/covariant]] — Group-GKP codes corresponding to the $G^{k_1} \subseteq G^{k_2} \subset G^{n}$ group construction admit $X$-type logical group-multiplication gates, and are thus covariant with respect to the induced $G^{k_2}$-action  ([arXiv:1911.00099](https://arxiv.org/abs/1911.00099)).
