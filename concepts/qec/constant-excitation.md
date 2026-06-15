---
type: concept
name: Constant-excitation (CE) code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/ampdamp
- concepts/qec/hamiltonian
- concepts/qec/qubit-css
- concepts/qec/qubit-stabilizer
- concepts/qec/stab-5-1-3
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/constant_excitation
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: constant_excitation
---

# Constant-excitation (CE) code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/constant_excitation) (`code_id: constant_excitation`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Code whose codewords lie in an eigenspace of fixed total energy or fixed total excitation number for the underlying quantum system.
For qubit codes, such a Hamiltonian is often the *total spin Hamiltonian*, $H=\sum_i Z_i$.
For spin-$S$ codes, this generalizes to $H=\sum_i J_z^{(i)}$, where $J_z$ is the spin-$S$ $Z$-operator.
For bosonic (and, similarly, for fermion) codes, such as Fock-state codes, codewords are often in an eigenspace with eigenvalue $N>0$ of the *total excitation* or *energy Hamiltonian*, $H=\sum_i \hat{n}_i$.

(source: raw/error-correction-zoo.md)

## Protection

CE codewords have to lie in the same excitation subspace in order to protect against changes in the total excitation number.

Fock-state CE codes lie in the constant-excitation Fock space and are in one-to-one correspondence with points on the discrete simplex.
They are protected from identical AD acting on all modes because the damping acts on all codewords identically  ([arXiv:quant-ph/9704002](https://arxiv.org/abs/quant-ph/9704002), [doi:10.1103/PhysRevA.56.1114](https://doi.org/10.1103/PhysRevA.56.1114)).
The all-zero AD Kraus operator acts identically on every state and so can be exactly correctable in the case of Fock-state CE codes.
For example, this operator's acting on a Fock state $|\boldsymbol{m}\rangle$ depends only on the total occupation number $|\boldsymbol{m}|=\sum_j m_j$ and not on the individual occupation numbers $m_j$,
\begin{align}
  E_{0}^{\otimes n}|\boldsymbol{m}\rangle=\left(1-\gamma\right)^{|\boldsymbol{m}|/2}|\boldsymbol{m}\rangle~.
\end{align}
This effect extends to the damping portion, $\left(1-\gamma\right)^{\hat{n}/2}$, of any $\ell\neq 0$ AD Kraus operators.

In similar fashion, qubit CE codes are protected from coherent noise in the form of transversal $Z$-rotations because such rotations act identically on all codewords  ([doi:10.1109/ISIT45174.2021.9518206](https://doi.org/10.1109/ISIT45174.2021.9518206), [arXiv:2011.00197](https://arxiv.org/abs/2011.00197)).
In the case of CSS codes, all codes oblivious to such rotations are CE codes  ([doi:10.1109/ISIT45174.2021.9518206](https://doi.org/10.1109/ISIT45174.2021.9518206), [arXiv:2011.00197](https://arxiv.org/abs/2011.00197)).
Stabilizer codes can be extended to codes that are protected against such coherent noise via an enlargement procedure  ([arXiv:2011.00197](https://arxiv.org/abs/2011.00197)).

## Rate

Fock-state CE codes can be used in a protocol that achieves the two-way quantum capacity of the AD Gaussian channel  ([arXiv:2203.13924](https://arxiv.org/abs/2203.13924)). For every $K,t \geq 2$, there are explicitly constructible $K$-dimensional Fock-state CE codes with $q=N=(K-1)t(t+1)$ modes, total excitation $N$, and distance $t+1$; there also exist families with logical dimension $K = o(2^N)$ and distance of order $o(N/\log N)$  ([arXiv:2509.20545](https://arxiv.org/abs/2509.20545)).

## Fault tolerance

- Fault-tolerant QEC framework for CE CSS codes using modified Shor and Steane syndrome extraction, where weight-$2w$ stabilizers are measured using $w$-CE cat states and zero-controlled NOT ($\mathrm{C}_0 X$) gates replace standard CNOT gates to preserve the constant-excitation structure  ([arXiv:2507.10395](https://arxiv.org/abs/2507.10395)).

## Relations

- _parent_: [[concepts/qec/hamiltonian]] — Constant-excitation codes are associated with a Hamiltonian governing the total excitations of the system.
- _cousin_: [[concepts/qec/ampdamp]] — Fock-state and qubit CE codes exactly protect against the AD Kraus operator $E_{0}^{\otimes n}$ because it acts identically on all Fock (and qubit) states with the same excitation number  ([arXiv:quant-ph/9704002](https://arxiv.org/abs/quant-ph/9704002), [doi:10.1103/PhysRevA.56.1114](https://doi.org/10.1103/PhysRevA.56.1114)).
- _cousin_: [[concepts/qec/qubit-css]] — Qubit CE codes are protected from coherent noise in the form of transversal $Z$-rotations because such rotations act identically on all codewords  ([doi:10.1109/ISIT45174.2021.9518206](https://doi.org/10.1109/ISIT45174.2021.9518206), [arXiv:2011.00197](https://arxiv.org/abs/2011.00197)).
In the case of qubit CSS codes, all codes oblivious to such rotations are CE codes  ([doi:10.1109/ISIT45174.2021.9518206](https://doi.org/10.1109/ISIT45174.2021.9518206), [arXiv:2011.00197](https://arxiv.org/abs/2011.00197)).
Any $⟦n,k,d⟧$ CSS code can be made into an $⟦mn,k,>d⟧$ CE code  ([doi:10.1109/ISIT45174.2021.9518206](https://doi.org/10.1109/ISIT45174.2021.9518206)).
Concatenating the dual-rail code with an inner $⟦n,k,d⟧$ qubit stabilizer code yields a degenerate $⟦2n,k,d⟧$ constant-excitation stabilizer code that avoids coherent phase errors and is equivalent to a Pauli-rotated repetition-concatenated stabilizer code  ([arXiv:2010.00538](https://arxiv.org/abs/2010.00538)). CSS structure is preserved when the original code is CSS  ([arXiv:2507.10395](https://arxiv.org/abs/2507.10395)).
- _cousin_: [[concepts/qec/stab-5-1-3]] — The five-qubit code can be concatenated with a particular decoherence-free subspace (DFS)  ([arXiv:quant-ph/9807004](https://arxiv.org/abs/quant-ph/9807004), [arXiv:quant-ph/9902041](https://arxiv.org/abs/quant-ph/9902041), [arXiv:quant-ph/9908064](https://arxiv.org/abs/quant-ph/9908064), [arXiv:quant-ph/0007013](https://arxiv.org/abs/quant-ph/0007013)) to yield a 20-qubit CE code  ([arXiv:quant-ph/9809081](https://arxiv.org/abs/quant-ph/9809081), [arXiv:quant-ph/9907096](https://arxiv.org/abs/quant-ph/9907096)). Dual-rail concatenation of the five-qubit code yields a $⟦10,1,3⟧$ CE stabilizer code  ([arXiv:2507.10395](https://arxiv.org/abs/2507.10395)).
- _cousin_: [[concepts/qec/qubit-stabilizer]] — Concatenating the dual-rail code with an inner $⟦n,k,d⟧$ qubit stabilizer code yields a degenerate $⟦2n,k,d⟧$ constant-excitation stabilizer code that avoids coherent phase errors and is equivalent to a Pauli-rotated repetition-concatenated stabilizer code  ([arXiv:2010.00538](https://arxiv.org/abs/2010.00538)). CSS structure is preserved when the original code is CSS  ([arXiv:2507.10395](https://arxiv.org/abs/2507.10395)).
