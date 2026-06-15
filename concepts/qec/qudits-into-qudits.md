---
type: concept
name: Modular-qudit code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- $\mathbb{Z}_q$-qudit code
- Modular-qudit subspace code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/block-quantum
- concepts/qec/group-quantum
- concepts/qec/qecc-finite
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/qudits_into_qudits
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: qudits_into_qudits
---

# Modular-qudit code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/qudits_into_qudits) (`code_id: qudits_into_qudits`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Encodes a $K$-dimensional Hilbert space into a $q^n$-dimensional ($n$-qudit) Hilbert space, with canonical qudit states $|k\rangle$ labeled by elements $k$ of the group $\mathbb{Z}_q$ of integers *modulo* $q$.
Usually denoted as $((n,K))_{\mathbb{Z}_q}$ or $((n,K,d))_{\mathbb{Z}_q}$, whenever the code's distance $d$ is defined, and with $q=p$ when the dimension is prime.

There exists an analogue of the Wigner function for modular qudits  ([arXiv:quant-ph/0401155](https://arxiv.org/abs/quant-ph/0401155), [arXiv:quant-ph/0410117](https://arxiv.org/abs/quant-ph/0410117), [arXiv:2503.09353](https://arxiv.org/abs/2503.09353)).

(source: raw/error-correction-zoo.md)

## Protection

An $((n,K,d))_{\mathbb{Z}_q}$ code with distance $d$ detects errors acting on up to $d-1$ modular qudits, corrects erasure errors on up to $d-1$ modular qudits, or corrects errors acting on up to $\lfloor (d-1)/2 \rfloor$ modular qudits.

\subsection{Modular-qudit Pauli-string error basis}

A convenient and often considered error set is the modular-qudit analogue  ([arXiv:quant-ph/9802007](https://arxiv.org/abs/quant-ph/9802007), [arXiv:2302.07966](https://arxiv.org/abs/2302.07966)) of the Pauli string basis for qubit codes.

\begin{defterm}{Modular-qudit Pauli strings}
\label{topic:qudit-pauli}
For a single qudit, this set consists of products of powers of the modular-qudit Pauli matrices $X$ and $Z$, which act on computational basis states $|k\rangle$ for $k\in\mathbb{Z}_q$ as
\begin{align}
  X\left|k\right\rangle =\left|k+1\right\rangle \,\,\text{ and }\,\,Z\left|k\right\rangle =e^{i\frac{2\pi}{q}k}\left|k\right\rangle ~,
\end{align}
with addition performed modulo $q$.
For multiple qudits, error set elements are tensor products of elements of the single-qudit error set.
Tensor products of $X$ ($Z$) modular-qudit Paulis acting on different qudits are called $X$*-type* ($Z$*-type*) modular-qudit Pauli strings.
Combining the $X$-type and $Z$-type strings with a primitive $2q$th root of unity forms a group called the *modular-qudit Pauli group*  ([arXiv:quant-ph/0412001](https://arxiv.org/abs/quant-ph/0412001)).
\end{defterm}

For prime $q$, this Pauli structure agrees with the usual prime-qudit Pauli group, but for prime-power $q=p^m$ with $m>1$ it differs from the Galois-qudit choice based on field structure. 
Modular-qudit Pauli matrices  ([doi:10.1007/BF01457956](https://doi.org/10.1007/BF01457956), [doi:10.1201/9780429497933](https://doi.org/10.1201/9780429497933)) are also known as Weyl operators , Sylvester-t'Hooft generators , vol. 3 (University Press, 1909)},doi:10.1016/0550-3213(78)90153-0}, shift and boost operators  ([arXiv:quant-ph/0602001](https://arxiv.org/abs/quant-ph/0602001)), or clock and shift matrices  ([doi:10.1007/978-1-4684-9148-7_43](https://doi.org/10.1007/978-1-4684-9148-7_43)); they are special cases of Manin's quantum plane  ([doi:10.5802/aif.1117](https://doi.org/10.5802/aif.1117), [doi:10.1143/PTP.102.219](https://doi.org/10.1143/PTP.102.219), [arXiv:math/0307393](https://arxiv.org/abs/math/0307393), [arXiv:math/0402401](https://arxiv.org/abs/math/0402401)).

The Pauli error set is a unitary basis for linear operators on the multi-qudit Hilbert space that is orthonormal under the Hilbert-Schmidt inner product; it is a nice error basis. The distance associated with this set is often the minimum weight of a qudit Pauli string that implements a nontrivial logical operation in the code.

## Rate

Non-stabilizer states yield higher quantum capacity of the discrete beamsplitter channel  ([arXiv:2401.12105](https://arxiv.org/abs/2401.12105)).

## General gates

- The normalizer of the modular-qudit Pauli group is the *modular-qudit Clifford group*  ([arXiv:quant-ph/9802007](https://arxiv.org/abs/quant-ph/9802007), [arXiv:quant-ph/0412001](https://arxiv.org/abs/quant-ph/0412001), [arXiv:quant-ph/0408190](https://arxiv.org/abs/quant-ph/0408190), [arXiv:quant-ph/0512155](https://arxiv.org/abs/quant-ph/0512155), [arXiv:quant-ph/0605094](https://arxiv.org/abs/quant-ph/0605094), [doi:10.1088/1751-8113/43/4/042001](https://doi.org/10.1088/1751-8113/43/4/042001), [arXiv:1101.1519](https://arxiv.org/abs/1101.1519), [arXiv:1102.3354](https://arxiv.org/abs/1102.3354), [arXiv:2008.00959](https://arxiv.org/abs/2008.00959)).
There is a standard form for modular-qudit Clifford-group operators  ([arXiv:quant-ph/0412001](https://arxiv.org/abs/quant-ph/0412001)), and any modular-qudit Clifford gate can be constructed from phase-shift and quantum Fourier transform gates  ([arXiv:1307.5087](https://arxiv.org/abs/1307.5087)).
For prime qudit dimension $p$, the discrete Fourier transform, quadratic phase gate, and SUM gate generate the Clifford group .
Clifford circuits on prime qudits, together with Pauli measurements and classical feedforward, admit efficient classical simulation by tracking stabilizer and logical generators; when measuring a Pauli outside the stabilizer normalizer, the outcome is uniformly distributed in $\mathbb{Z}_p$ .
Universal computing can be achieved using qudit Clifford gates and a single type of non-Clifford gate, such as the $T$ gate  ([arXiv:1503.08800](https://arxiv.org/abs/1503.08800)).
Non-Clifford gates are typically more difficult to implement than Clifford gates and so are treated as a resource.
There is a normal form for Clifford+$T$ operators for qutrits  ([arXiv:1803.03228](https://arxiv.org/abs/1803.03228)) and, more generally, odd prime qudits  ([arXiv:2011.07970](https://arxiv.org/abs/2011.07970)).
Optimizing non-Clifford-gate count can be done using various procedures; see Refs.  ([arXiv:1504.03383](https://arxiv.org/abs/1504.03383), [arXiv:1810.04710](https://arxiv.org/abs/1810.04710), [arXiv:2311.08696](https://arxiv.org/abs/2311.08696), [arXiv:2401.16120](https://arxiv.org/abs/2401.16120), [arXiv:2405.08147](https://arxiv.org/abs/2405.08147)) for qutrit codes.
There are simulation algorithms for modular-qudit Clifford-dominated circuits  ([arXiv:1808.02406](https://arxiv.org/abs/1808.02406)).
- \begin{defterm}{Qudit Clifford hierarchy} \label{topic:qudit-clifford-hierarchy} The modular-qudit Clifford hierarchy  ([arXiv:quant-ph/9908010](https://arxiv.org/abs/quant-ph/9908010), [arXiv:1206.1598](https://arxiv.org/abs/1206.1598), [arXiv:1408.1720](https://arxiv.org/abs/1408.1720), [arXiv:1608.06596](https://arxiv.org/abs/1608.06596)) is a tower of gate sets which includes modular-qudit Pauli and modular-qudit Clifford gates at its first two levels, and non-Clifford qudit gates at higher levels. The $k$th level is defined recursively by \begin{align} C_k = \{ U | U P U^{\dagger} \in C_{k-1} \}~, \end{align} where $P$ is any modular-qudit Pauli matrix, and $C_1$ is the modular-qudit Pauli group. Gates for one prime-dimensional qudit have been classified  ([arXiv:2501.07939](https://arxiv.org/abs/2501.07939)). \end{defterm}

## Decoders

- For few-qudit codes ($n$ is small), decoding can be based on a lookup table. For infinite code families, the size of such a table scales exponentially with $n$, so approximate decoding algorithms scaling polynomially with $n$ have to be used. The decoder determining the most likely error given a noise channel is called the *maximum-likelihood* (ML) decoder.

## Relations

- _parent_: [[concepts/qec/block-quantum]] — Modular-qudit codes are block quantum codes with $\Sigma=\mathbb{Z}_q$.
- _parent_: [[concepts/qec/qecc-finite]]
- _parent_: [[concepts/qec/group-quantum]] — Group quantum codes whose physical spaces are constructed using modular-integer groups $\mathbb{Z}_q$ are modular-qudit codes.
- _cousin_: [`unitary_design`](https://errorcorrectionzoo.org/c/unitary_design) — The prime-qudit Pauli group is a unitary 1-design.

## Notes

- Review of qudit quantum computation  ([arXiv:2008.00959](https://arxiv.org/abs/2008.00959)).
- For odd prime qudit dimension, the discrete-Wigner-function analysis of  ([arXiv:1011.2497](https://arxiv.org/abs/1011.2497)) determines depolarizing-noise thresholds beyond which non-stabilizer states and non-Clifford gates become Clifford-simulable, and identifies maximally robust such resources.
- Weight distribution of a code depends on the average entanglement of codewords  ([arXiv:quant-ph/0310137](https://arxiv.org/abs/quant-ph/0310137), [arXiv:2209.07607](https://arxiv.org/abs/2209.07607)).
- Qudit Cirq library  ([arXiv:2501.07812](https://arxiv.org/abs/2501.07812)).
- See  ([doi:10.1007/978-3-319-44906-7](https://doi.org/10.1007/978-3-319-44906-7)) for a side-by-side introduction to modular and Galois qudits.
