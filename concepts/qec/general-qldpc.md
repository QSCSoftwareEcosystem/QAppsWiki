---
type: concept
name: QLDPC code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Sparse stabilizer code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/dynamic-gen
- concepts/qec/hamiltonian
- concepts/qec/qlwc
- concepts/qec/quantum-locally-recoverable
- concepts/qec/topological
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/general_qldpc
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: general_qldpc
---

# QLDPC code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/general_qldpc) (`code_id: general_qldpc`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Member of a family of stabilizer codes for which the number of sites participating in each stabilizer generator and the number of stabilizer generators that each site participates in are both bounded by a constant as $n\to\infty$.
Sometimes, the two parameters are explicitly stated: each site of an $(l,w)$*-regular QLDPC code* is acted on by $\leq l$ generators of weight $\leq w$.

Notable QLDPC codes are summarized in \ref{table:qldpc-codes}, demonstrating the steady improvement in code parameters that culminated in the first asymptotically good QLDPC codes.
  \begin{table}
    \begin{cells}
    \celldata<c H, c H, c H>{$k$ & $d$ & Code}
    \celldata<c, c, c>{
    $2$ & $\sqrt{n}$ & Kitaev toric
        \\
    $\Theta(n)$ & $\Theta(\log n)$ & 2D hyperbolic surface
        \\
    $\Theta(n)$ & $\Omega (n^{1/10})$ & Guth-Lubotzky
        \\
    $2$ & $\Omega (\sqrt{n\sqrt{\log n}})$ & Freedman-Meyer-Luo
        \\
    $\Theta(n)$ & $\Theta(\sqrt{n})$ & hypergraph product
        \\
    $\Theta (\sqrt{n}/\log n)$ & $\Omega (\sqrt{n} \log n)$ & high-dimensional expander (HDX)
        \\
    $\Theta (\sqrt{n})$ & $\Omega (\sqrt{n} \log^c n)$ & tensor-product HDX
        \\
    $\Theta (n^{3/5}/\text{polylog}(n) )$ & $\Omega (n^{3/5}/\text{polylog}(n) )$ & fiber-bundle
        \\
    $\Theta (\log n)$ & $\Omega (n/\log n)$ & lifted-product (LP)
        \\
    $\Theta (n^{4/5})$ & $\Omega (n^{3/5})$ & balanced product (BP)
        \\
    $\Theta(n)$ & $\Theta(n)$ & expander LP
        \\
    $\Theta(n)$ & $\Theta(n)$ & quantum Tanner
        \\
    $\Theta(n)$ & $\Theta(n)$ & Dinur-Hsieh-Lin-Vidick
    }
    \end{cells}
    \caption{Notable QLDPC codes and their asymptotic scaling (see also Ref.  ([arXiv:2103.06309](https://arxiv.org/abs/2103.06309))); $c$ is a positive integer.}
    \label{table:qldpc-codes}
  \end{table}

A *geometrically local stabilizer code* is a QLDPC code where the sites involved in any syndrome value are contained in a fixed volume that does not scale with $n$.
As opposed to general stabilizer codes, syndrome extraction of the constant-weight check operators of a QLDPC code can be done using a constant-depth circuit.

Strictly speaking, the term *parity check* describes only bitwise qubit error syndromes. Nevertheless, qudit and bosonic stabilizer codes satisfying the above criteria are also called QLDPC codes.
This entry includes general code constructions which are generally intended to yield QLDPC codes, but may include code families that have non-QLDPC members.

(source: raw/error-correction-zoo.md)

## Protection

Detects errors on $d-1$ sites, corrects errors on $\left\lfloor (d-1)/2 \right\rfloor$ sites.
Code distance may not be a reliable marker of code performance.

## Decoders

- Non-binary decoding algorithm for CSS-type QLDPC codes  ([doi:10.1109/ACCESS.2015.2503267](https://doi.org/10.1109/ACCESS.2015.2503267)).
- GD-CSS Decoder for Galois-qudit CSS QLDPC codes  ([arXiv:2507.11534](https://arxiv.org/abs/2507.11534))}

## Relations

- _parent_: [[concepts/qec/qlwc]] — QLDPC codes are QLWC codes for which the number of stabilizer generators that each site participates in is bounded by a constant as $n\to\infty$.
- _cousin_: [[concepts/qec/quantum-locally-recoverable]] — Finite-dimensional block QLDPC stabilizer codes are QLRCs whose locality $r \leq w$, where $w$ is the maximum stabilizer-generator weight  ([arXiv:2311.08653](https://arxiv.org/abs/2311.08653)).
- _cousin_: [`q-ary_ldpc`](https://errorcorrectionzoo.org/c/q-ary_ldpc) — Galois-qudit QLDPC codes are quantum analogues of $q$-ary LDPC codes.
- _cousin_: [[concepts/qec/topological]] — Topological codes are not generally defined using Pauli strings or their qudit and bosonic generalizations. However, for appropriate tessellations, the codespace is the ground-state subspace of a geometrically local Hamiltonian. In this sense, topological codes are QLDPC codes. Geometrically local commuting-projector code Hamiltonians on Euclidean manifolds are stable with respect to small perturbations when they satisfy the TQO conditions, meaning that a notion of a phase can be defined  ([arXiv:1001.4363](https://arxiv.org/abs/1001.4363), [arXiv:1001.0344](https://arxiv.org/abs/1001.0344), [arXiv:1810.02428](https://arxiv.org/abs/1810.02428), [arXiv:2010.15337](https://arxiv.org/abs/2010.15337)). This notion can be extended to semi-hyperbolic manifolds  ([arXiv:2405.19412](https://arxiv.org/abs/2405.19412)) and non-geometrically local QLDPC codes exhibiting check soundness  ([arXiv:2411.01002](https://arxiv.org/abs/2411.01002)) (see also  ([arXiv:2411.02384](https://arxiv.org/abs/2411.02384))).
- _cousin_: [[concepts/qec/dynamic-gen]] — QLDPC codes can arise from a dynamical process  ([arXiv:2004.09560](https://arxiv.org/abs/2004.09560)).
- _cousin_: [[concepts/qec/hamiltonian]] — QLDPC code Hamiltonians can be simulated, with the help of perturbation theory, by two-dimensional Hamiltonians with non-commuting terms whose interactions scale with $n$  ([arXiv:2308.13277](https://arxiv.org/abs/2308.13277)).

## Notes

- Infleqtion QLDPC software library for estimating distance and creating various qubit and Galois-qudit QLDPC CSS codes }
- LDPC Python software library for decoding LDPC and QLDPC codes  ([arXiv:2005.07016](https://arxiv.org/abs/2005.07016)).
- Reviews of QLDPC codes provided in Refs.  ([doi:10.1109/ACCESS.2015.2503267](https://doi.org/10.1109/ACCESS.2015.2503267), [arXiv:2103.06309](https://arxiv.org/abs/2103.06309), [arXiv:2510.14090](https://arxiv.org/abs/2510.14090)).
