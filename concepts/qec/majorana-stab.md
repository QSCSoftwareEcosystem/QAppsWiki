---
type: concept
name: Majorana stabilizer code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/fermions
- concepts/qec/jw
- concepts/qec/qubit-css
- concepts/qec/qubit-stabilizer
- concepts/qec/qudit-stabilizer
- concepts/qec/stabilizer
- concepts/qec/steane
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/majorana_stab
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: majorana_stab
---

# Majorana stabilizer code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/majorana_stab) (`code_id: majorana_stab`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A stabilizer code whose stabilizers are products of an even number of Majorana fermion operators, analogous to Pauli strings for a traditional stabilizer code and referred to as *Majorana stabilizers*.
The codespace is the mutual $+1$ eigenspace of all Majorana stabilizers.

Codes can be denoted as $⟦n,k,d⟧_{f}$  ([arXiv:1703.00459](https://arxiv.org/abs/1703.00459)), where $n$ is the number of fermionic modes (equivalently, $2n$ Majorana modes).
Two copies of an $n$-Majorana mode code may be combined to form a single $n$-fermion code by using one copy for the real parts of each fermion, and the other copy for the imaginary parts  ([arXiv:2411.08955](https://arxiv.org/abs/2411.08955)).
Codes that admit a logical operator of even (odd) weight are called even (odd) Majorana codes  ([arXiv:2508.09928](https://arxiv.org/abs/2508.09928)).
Even Majorana codes encode logical qubits, and odd Majorana codes have at least one logical Majorana fermion.
For odd codes, an additional protection parameter is the minimum diameter $l_{\rm even}$ of an even logical operator  ([arXiv:1004.3791](https://arxiv.org/abs/1004.3791)).

In some cases, Majorana-based stabilizer codes are designed to protect against fermionic noise  ([arXiv:cond-mat/0010440](https://arxiv.org/abs/cond-mat/0010440)) and are thus useful for physical platforms based on fermions.
In other cases, Majorana-based frameworks are helpful for understanding conventional qubit stabilizer codes designed for qubit-based platforms.

(source: raw/error-correction-zoo.md)

## Protection

Detects products of Majorana operators with weight up to $d-1$.
Physically, protects against dephasing errors caused by coupling of fermion density to the environment and bit-flip errors caused by quasiparticle poisoning processes.
For odd Majorana codes, the physically relevant logical protection is also governed by the minimum diameter $l_{\rm even}$ of an even logical operator  ([arXiv:1004.3791](https://arxiv.org/abs/1004.3791)).

Code bounds have been developed for small codes  ([arXiv:1703.00612](https://arxiv.org/abs/1703.00612)).
LP bounds for Majorana codes have been developed based on the identification of Majorana operators with the Clifford algebra  ([arXiv:2502.14165](https://arxiv.org/abs/2502.14165)).

## Transversal gates

- Transversal Clifford operations are discussed in Ref.  ([arXiv:2508.09928](https://arxiv.org/abs/2508.09928)).

## Encoders

- Unitary encoding using fermionic Clifford operations  ([arXiv:2402.07829](https://arxiv.org/abs/2402.07829)).

## General gates

- Some gates can be implemented through braiding of the computational anyons. Circuit-based gates can be converted into braid patterns via quantum compiling algorithms  ([arXiv:2008.10790](https://arxiv.org/abs/2008.10790)).

## Relations

- _parent_: [[concepts/qec/fermions]]
- _parent_: [[concepts/qec/qubit-stabilizer]] — A Majorana stabilizer code is a stabilizer code whose stabilizers are composed of Majorana fermion operators, which are in turn realizable using Pauli strings via the Jordan-Wigner mapping.
Any $⟦n,k,d⟧$ stabilizer code can be mapped into a $⟦2n,k,2d⟧_{f}$ Majorana stabilizer code by concatenating with the tetron code  ([arXiv:cond-mat/0506438](https://arxiv.org/abs/cond-mat/0506438)) ([arXiv:1004.3791](https://arxiv.org/abs/1004.3791)).
Embedding each physical qubit into two fermions via the tetron code is useful for exactly solving the Kitaev honeycomb model Hamiltonian  ([arXiv:cond-mat/0506438](https://arxiv.org/abs/cond-mat/0506438)) and other qubit Hamiltonians on certain graphs  ([arXiv:2003.05465](https://arxiv.org/abs/2003.05465), [arXiv:2012.07857](https://arxiv.org/abs/2012.07857)).
Majorana stabilizer groups can be converted into ordinary qubit stabilizer groups via the parton mapping, while their corresponding states are converted via the Gutzwiller projection  ([arXiv:2505.02683](https://arxiv.org/abs/2505.02683)).
- _cousin_: [`dual`](https://errorcorrectionzoo.org/c/dual) — Classical self-orthogonal codes can be used to construct Majorana stabilizer codes  ([arXiv:1703.00459](https://arxiv.org/abs/1703.00459), [doi:10.1088/1751-8113/41/14/145304](https://doi.org/10.1088/1751-8113/41/14/145304), [arXiv:2503.08736](https://arxiv.org/abs/2503.08736)). The direct relationship between the two codes follows from expressing the Majorana strings as binary vectors – akin to the symplectic representation – and observing that the binary stabilizer matrix $S$ for such a Majorana stabilizer code satisfies $S\cdot S^T=0$ because it has commuting stabilizers, which is precisely the condition $G\cdot G^T=0$ on the generator matrix $G$ of a self-orthogonal classical code. A self-orthogonal classical code $C$ with parameters $[2N,k,d]$ yields a Majorana stabilizer code with parameters $⟦N,N-k,d^\perp⟧_f$, where $d^\perp$ is the code distance of the dual code $C^\perp$.
- _cousin_: [[concepts/qec/qubit-css]] — Every $⟦n,k,d⟧_f$ Majorana stabilizer code is associated with a $⟦2n,2k,d⟧$ qubit CSS code whose $X$- and $Z$-check supports coincide  ([arXiv:1004.3791](https://arxiv.org/abs/1004.3791)). An odd-length self-dual CSS code can be converted into a complex-fermion code by replacing qubit $Z$-type and $X$-type operators with $\gamma$-type and $\tilde{\gamma}$-type Majorana operators, respectively  ([arXiv:2411.08955](https://arxiv.org/abs/2411.08955)).
- _cousin_: [[concepts/qec/steane]] — Applying the CSS-to-Majorana map of  ([arXiv:1004.3791](https://arxiv.org/abs/1004.3791)) to the $⟦7,1,3⟧$ Steane code yields a seven-Majorana code encoding half a qubit; pairing two such odd-length copies gives a physical Majorana stabilizer code with odd logical operators  ([arXiv:1004.3791](https://arxiv.org/abs/1004.3791)).
- _cousin_: [`binary_linear`](https://errorcorrectionzoo.org/c/binary_linear) — When constructing a Majorana stabilizer code from a self-orthogonal classical code with an odd number of bits and generator matrix $G$, a more complex procedure must be applied to ensure that the fermion code has an even number of Majorana zero modes, and thus a physical Hilbert space  ([arXiv:1004.3791](https://arxiv.org/abs/1004.3791), [arXiv:1703.00459](https://arxiv.org/abs/1703.00459)). Rather than taking $G$ to be the stabilizer matrix as in the even case, we take $G\oplus G$. This is a concatenation of classical codes as in the CSS construction and it yields a mapping $[2n-1,k,d]\rightarrow ⟦2n-1,2n-1-k,d^\perp⟧_f$. This procedure may be further generalized by concatenating two different self-orthogonal classical codes with an odd number of bits, as is often done in the CSS construction.
- _cousin_: [`binary_cyclic`](https://errorcorrectionzoo.org/c/binary_cyclic) — Cyclic binary linear codes can be used to construct translation-invariant Majorana stabilizer codes, provided that they are also self-orthogonal  ([arXiv:1703.00459](https://arxiv.org/abs/1703.00459)).
- _cousin_: [[concepts/qec/stabilizer]] — Majorana stabilizer codes are useful for Majorana-based architectures, where the degrees of freedom are electrons, and the notion of locality is different than all other code kingdoms.
- _cousin_: [[concepts/qec/qudit-stabilizer]] — Majorana stabilizer codes can be extended to modular qudits, yielding parafermion stabilizer codes  ([arXiv:1409.4724](https://arxiv.org/abs/1409.4724)).
- _cousin_: [[concepts/qec/jw]] — A Majorana stabilizer code is a stabilizer code whose stabilizers are composed of Majorana fermion operators, which are in turn realizable using Pauli strings via the Jordan-Wigner mapping.
