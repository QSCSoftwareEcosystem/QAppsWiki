---
type: concept
name: Maximal Cube Root (MCR) code
status: provisional
updated: '2026-09-29'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/generalized-bicycle
- concepts/qec/perm-self-dual-css
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/maximal_cube_root
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: maximal_cube_root
---

# Maximal Cube Root (MCR) code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/maximal_cube_root) (`code_id: maximal_cube_root`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Qubit GB code whose defining polynomials guarantee a large automorphism group and many fold-transversal CX gates.
The construction ties both properties to a nontrivial cube root of unity in a polynomial quotient ring  ([arXiv:2606.05044](https://arxiv.org/abs/2606.05044)).

Let $R_{\ell}=\mathbb{F}_2[x]/\langle x^{\ell}-1\rangle$, let $f$ divide $x^{\ell}-1$, and set $\widehat f=(x^{\ell}-1)/f$.
An MCR code is specified by $(\ell,f,p,q)$, where $\gcd(p,q,x^{\ell}-1)=1$, through
\begin{align}
  H_X=\left(\operatorname{circ}(pf)\middle|\operatorname{circ}(qf)\right)
  \quad\text{and}\quad
  H_Z=\left(\operatorname{circ}(qf)^T\middle|\operatorname{circ}(pf)^T\right).
\end{align}
The circulant size $\ell$ is odd, and every irreducible factor of $\widehat f$ over $\mathbb{F}_2$ has even degree.
The polynomial $q$ is invertible in $S=R_{\ell}/\langle\widehat f\rangle$, and the ratio $r=pq^{-1}$ obeys
\begin{align}
  r^2+r+1=0\quad\text{in }S.
\end{align}
These conditions imply that the code has length $n=2\ell$ and dimension $k=2\deg f$  ([arXiv:2606.05044](https://arxiv.org/abs/2606.05044)).

(source: raw/error-correction-zoo.md)

## Protection

Examples encoding two logical qubits have parameters $⟦18,2,5⟧$, $⟦22,2,6⟧$, $⟦30,2,7⟧$, $⟦50,2,9⟧$, $⟦54,2,10⟧$, $⟦58,2,11⟧$, and $⟦66,2,13⟧$.
Their respective minimum stabilizer-generator weights are $8,8,8,12,16,12,12$  ([arXiv:2606.05044](https://arxiv.org/abs/2606.05044)).

Higher-dimensional examples include $⟦30,6,5⟧$, $⟦66,6,8⟧$, $⟦78,6,9⟧$, $⟦90,10,10⟧$, $⟦102,6,11⟧$, $⟦102,18,d\leq 12⟧$, and $⟦110,10,10⟧$ codes  ([arXiv:2606.05044](https://arxiv.org/abs/2606.05044)).

## Transversal gates

- A multiplier satisfying $r(x^j)=r$ or $r(x^j)=r^{-1}$ simultaneously yields a qubit-permutation automorphism and two fold-transversal CX gates. The physical pairing depends on which equality holds  ([arXiv:2606.05044](https://arxiv.org/abs/2606.05044)).
- The $⟦18,2,5⟧$, $⟦22,2,6⟧$, $⟦54,2,10⟧$, and $⟦66,2,13⟧$ examples generate the full two-qubit Clifford group using automorphisms and fold-transversal gates  ([arXiv:2606.05044](https://arxiv.org/abs/2606.05044)).
- The $⟦102,18,d\leq 12⟧$ example has 76 listed logical Clifford actions from automorphisms and fold-transversal gates  ([arXiv:2606.05044](https://arxiv.org/abs/2606.05044)).

## Relations

- _parent_: [[concepts/qec/perm-self-dual-css]] — MCR codes are permutationally self-dual since they are qubit GB codes. Exchanging the two blocks of qubits while inverting the cyclic-group index within each block exchanges the $X$- and $Z$-type stabilizer spaces  ([arXiv:2606.05044](https://arxiv.org/abs/2606.05044)).
- _parent_: [[concepts/qec/generalized-bicycle]] — MCR codes are binary GB codes whose transfer ratio is a nontrivial cube root of unity in a quotient of $R_{\ell}$  ([arXiv:2606.05044](https://arxiv.org/abs/2606.05044)).
