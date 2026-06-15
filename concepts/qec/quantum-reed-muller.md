---
type: concept
name: Quantum Reed-Muller (RM) code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/eastab
- concepts/qec/quantum-convolutional
- concepts/qec/quantum-divisible
- concepts/qec/quantum-pin
- concepts/qec/quantum-polar
- concepts/qec/quantum-tensor-product
- concepts/qec/qudit-reed-muller
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/quantum_reed_muller
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: quantum_reed_muller
---

# Quantum Reed-Muller (RM) code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/quantum_reed_muller) (`code_id: quantum_reed_muller`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A CSS code formed from a classical RM code or its punctured/shortened versions.
Such codes often admit transversal logical gates in the \term{Clifford hierarchy}.

Ordinary, punctured, or shortened RM codes can be used to construct quantum RM codes.
For example, the original construction  ([arXiv:quant-ph/9608026](https://arxiv.org/abs/quant-ph/9608026)) uses a general RM$(r,m)$ code for the $X$-type stabilizers, and an RM$(r-1,m)$ code for the $Z$-type stabilizers.

Non-CSS codes can be derived from such codes by modifying the $X$-type stabilizers  ([arXiv:quant-ph/9608026](https://arxiv.org/abs/quant-ph/9608026)).

(source: raw/error-correction-zoo.md)

## Protection

Detects errors on $d-1$ qubits, corrects errors on $\left\lfloor (d-1)/2 \right\rfloor$ qubits.

## Transversal gates

- Stabilizer generators can be defined as Pauli strings acting on subsets of qubits corresponding to subcubes of the Hamming $n$-cube (a.k.a. Boolean hypercube)  ([arXiv:2410.07595](https://arxiv.org/abs/2410.07595)). Transversal $Z$-rotations by angles $\pi/2^k$ acting on subcubes can implement logical multi-controlled-$Z$ gates  ([arXiv:2410.07595](https://arxiv.org/abs/2410.07595)).
- The $⟦2^m,{m \choose r}, 2^{\min(r,m-r)}⟧$ family, where $r$ divides $m$, admits diagonal gates in the form of $Z$-rotations by angle $\pi/2^{m/r}$  ([arXiv:1910.09333](https://arxiv.org/abs/1910.09333)) ([arXiv:1606.01904](https://arxiv.org/abs/1606.01904), [arXiv:1606.01906](https://arxiv.org/abs/1606.01906), [arXiv:1709.02832](https://arxiv.org/abs/1709.02832)). Of these, the self-dual sub-family for $m=2r$ admits logical Clifford group gates via permutations, transversal gates, and fold-transversal gates with the help of ancillas  ([arXiv:2410.23263](https://arxiv.org/abs/2410.23263)); the ancilla requirement was later removed  ([arXiv:2602.09788](https://arxiv.org/abs/2602.09788)).
- The $⟦64,15,4⟧$ member is highlighted in Ref.  ([arXiv:2404.19005](https://arxiv.org/abs/2404.19005)) as a candidate for transversal IQP sampling because a transversal $T$ gate implements a logical circuit consisting of 15 $CCZ$ gates.
- The family constructed out of shortened RM codes with parameters $⟦\sum_{i=w+1}^m \binom{m}{i}, \sum_{i=0}^{w} \binom{m}{i}, \sum_{i=w+1}^{r+1} \binom{r+1}{i}⟧$ for integers $m > 2r$ and $r > w \geq 0$ admits a transversal gate at the $\nu$th level in the hierarchy whenever $m > \nu r$  ([arXiv:1709.03543](https://arxiv.org/abs/1709.03543)).

## Magic scaling exponent

The family constructed out of shortened RM codes with parameters $⟦\sum_{i=w+1}^m \binom{m}{i}, \sum_{i=0}^{w} \binom{m}{i}, \sum_{i=w+1}^{r+1} \binom{r+1}{i}⟧$ for integers $m > 2r$ and $r > w \geq 0$ yields protocols with an exponent of $\gamma < 0.678$, with the fewest-resource protocol with $\gamma < 1$ requiring a code with parameters $\{r,w,m\} = \{19,14,3r+1\}$ such that $n \approx 2^{58}$ qubits  ([arXiv:1709.03543](https://arxiv.org/abs/1709.03543)). This refutes a conjecture that no protocol could achieve $\gamma < 1$  ([arXiv:1209.2426](https://arxiv.org/abs/1209.2426)).

## Rate

Dimension is $k = 2^r - {r \choose t} + 2 \sum_{i=0}^{t-1} {r \choose i}$. CSS codes formed from RM codes achieve channel capacity on erasure channels  ([doi:10.1109/ISIT.2016.7541599](https://doi.org/10.1109/ISIT.2016.7541599)).

## Fault tolerance

- Gate switching protocol for universal computation  ([arXiv:1403.2734](https://arxiv.org/abs/1403.2734)).
- Fault-tolerant universal computation can be achieved via code switching between the $⟦127,1,15⟧$ self-dual doubly even punctured quantum RM code and the $⟦127,1,7⟧$ triply even punctured quantum RM code  ([arXiv:2410.23263](https://arxiv.org/abs/2410.23263)).

## Relations

- _parent_: [[concepts/qec/quantum-pin]] — Quantum RM codes are special cases of quantum pin codes  ([arXiv:1906.11394](https://arxiv.org/abs/1906.11394)).
- _parent_: [[concepts/qec/qudit-reed-muller]] — Prime-qudit RM codes reduce to quantum RM codes when $q=p=2$.
- _cousin_: [`reed_muller`](https://errorcorrectionzoo.org/c/reed_muller) — Quantum RM codes are constructed from RM codes via the CSS construction. There is a relation between RM code performance against correlated generalizations of multiple-access channels (MACs) and quantum RM code performance against Pauli channels  ([arXiv:2506.08651](https://arxiv.org/abs/2506.08651)).
- _cousin_: [[concepts/qec/quantum-convolutional]] — Quantum convolutional codes can be derived from quantum RM codes  ([arXiv:quant-ph/0701037](https://arxiv.org/abs/quant-ph/0701037)).
- _cousin_: [[concepts/qec/eastab]] — EA versions of quantum RM codes and their quantum tensor-product variants can be constructed  ([arXiv:2303.08294](https://arxiv.org/abs/2303.08294)).
- _cousin_: [[concepts/qec/quantum-tensor-product]] — EA versions of quantum RM codes and their quantum tensor-product variants can be constructed  ([arXiv:2303.08294](https://arxiv.org/abs/2303.08294)).
- _cousin_: [[concepts/qec/quantum-divisible]] — Fault-tolerant universal computation can be achieved via code switching between the $⟦127,1,15⟧$ self-dual doubly even punctured quantum RM code and the $⟦127,1,7⟧$ triply even punctured quantum RM code  ([arXiv:2410.23263](https://arxiv.org/abs/2410.23263)).
- _cousin_: [[concepts/qec/quantum-polar]] — There are codes interpolating between quantum RM and quantum polar codes  ([arXiv:2505.22142](https://arxiv.org/abs/2505.22142)).
