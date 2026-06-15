---
type: concept
name: Block quantum code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/qecc
- concepts/qec/single-subsystem
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/block_quantum
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: block_quantum
---

# Block quantum code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/block_quantum) (`code_id: block_quantum`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

An encoding of quantum information into a subspace of a *multi-partite* (a.k.a. *many-body*) quantum system, a physical space consisting of a tensor product of $n > 1$ identical factors.
Each factor is referred to as a *subsystem*, *register*, *site*, *party*, or *body*, depending on context.
The subsystems include qubits, modular qudits, Galois qudits, oscillators, groups, or categories.
For finite dimensional codes, the dimension of the underlying subsystem is denoted by $q$ and is sometimes called the *local dimension*.

While codewords $c$ of block codes are elements of $\Sigma^n$ for some alphabet $\Sigma$, quantum states of block quantum codes are $L^2$-normalizable functions on $\Sigma^n$.
Put differently, the configuration space of the canonical (a.k.a. computational) basis states $|c\rangle$ of an $n$-body quantum system is the classical $n$-coordinate alphabet $\Sigma^n \ni c$.

(source: raw/error-correction-zoo.md)

## Protection

A block quantum code over a finite alphabet $\Sigma$ with *distance* $d$ detects errors acting on up to $d-1$ subsystems, corrects erasure errors on up to $d-1$ subsystems, or corrects errors acting on up to $\lfloor (d-1)/2 \rfloor$ subsystems.
The subsystems that are erased are known to the receiver, and erasures of subsystems at unknown locations are called *deletion errors*  ([arXiv:2001.08405](https://arxiv.org/abs/2001.08405), [arXiv:2004.00814](https://arxiv.org/abs/2004.00814), [arXiv:2102.02494](https://arxiv.org/abs/2102.02494), [arXiv:2102.03015](https://arxiv.org/abs/2102.03015)).
More general forms of noise are caused by *insertion errors*  ([arXiv:2001.08405](https://arxiv.org/abs/2001.08405), [arXiv:2004.00814](https://arxiv.org/abs/2004.00814), [arXiv:2102.02494](https://arxiv.org/abs/2102.02494), [arXiv:2102.03015](https://arxiv.org/abs/2102.03015)), where subsystems are inserted into the block, and *synchronization errors* (a.k.a. misalignment)  ([arXiv:1206.0260](https://arxiv.org/abs/1206.0260)), where the code block is misplaced in a larger block by one or more locations.
There are relations between deletion and insertion errors  ([arXiv:2105.07214](https://arxiv.org/abs/2105.07214), [arXiv:2501.07027](https://arxiv.org/abs/2501.07027)).

The *weight* of an operator on a tensor-product Hilbert space is the number of subsystems on which the operator acts non-trivially.
For example, an operator acting on two subsystems is called a weight-two operator or a two-body operator.

General noise models for block codes include *stochastic noise*, in which every possible error is assigned a probability.
In the case of *local stochastic noise*, the probability decreases rapidly (typically, exponentially) with the number of subsystems that an error acts on.
On the other hand, the *adversarial noise* model consists of errors acting on at most a fixed number of subsystems.
Independent channels that are close to the identity can be approximated by adversarial $t$-subsystem error maps with an error that is exponentially small in $t+1$, motivating the study of $t$-subsystem errors even when the physical noise is memoryless .
Errors acting on subsystems in a geometrically local region are called *burst errors*  ([arXiv:quant-ph/0002020](https://arxiv.org/abs/quant-ph/0002020), [doi:10.1109/18.771250](https://doi.org/10.1109/18.771250)).

\subsection{Bounds on code parameters}
Bounds on finite dimensional block code performance include the quantum Singleton bound, quantum Hamming bound, quantum GV bound, various quantum linear programming (LP) bounds  ([arXiv:quant-ph/9611001](https://arxiv.org/abs/quant-ph/9611001), [arXiv:quant-ph/9709049](https://arxiv.org/abs/quant-ph/9709049)) (see the book ), and other bounds  ([doi:10.1109/TIT.2005.862086](https://doi.org/10.1109/TIT.2005.862086), [arXiv:1007.3655](https://arxiv.org/abs/1007.3655)).
A code whose parameters attain the quantum Hamming bound (quantum Singleton bound) is called a perfect quantum code (a quantum MDS code).
We are often interested in how parameters of particular infinite block quantum code families scale with increasing block length $n$, necessitating the use of asymptotic notation.
A code family is called *good* when its rate $k/n$ and relative error-correction capability $t/n$, equivalently relative distance up to constant factors, remain bounded away from zero as $n\to\infty$ .

\begin{defterm}{Quantum GV bound}
\label{topic:quantum-gv-bound}
The quantum GV bound  ([doi:10.1109/TIT.2004.838088](https://doi.org/10.1109/TIT.2004.838088)) (see also Refs.  ([arXiv:quant-ph/9602022](https://arxiv.org/abs/quant-ph/9602022), [arXiv:quant-ph/9906131](https://arxiv.org/abs/quant-ph/9906131), [doi:10.7907/m0xg-zs21](https://doi.org/10.7907/m0xg-zs21), [doi:10.1109/18.959288](https://doi.org/10.1109/18.959288), [doi:10.1016/j.jmaa.2007.08.023](https://doi.org/10.1016/j.jmaa.2007.08.023))) for Galois qudits states that a pure $⟦n,k,d⟧_q$ Galois-qudit stabilizer code exists if 
\begin{align}
  \frac{q^{n-k+2}-1}{q^{2}-1}>\sum_{j=1}^{d-1}(q^{2}-1)^{j-1}\binom{n}{j}~.
\end{align}
The bound gives rise to the *asymptotic quantum GV bound* (i.e., quantum GV bound in the $n\to\infty$ limit), expressed in terms of the maximum achievable rate $R$ and relative distance $\delta$,
\begin{align}
  R\geq 1-\delta\log_q(q+1) - h_{q}(\delta)~,
\end{align}
where $h_q$ is the $q$-ary entropy function.
\end{defterm}

## Transversal gates

- \begin{defterm}{Eastin-Knill theorem} \label{topic:eastin-knill} *Transversal gates* are logical gates on block codes that can be realized as tensor products of unitary operations acting on subsets of subsystems whose size is independent of $n$. For subsets of size one, gates are sometimes called *strongly transversal* if the single-subsystem unitaries are identical, and *weakly transversal* otherwise. A universal gate set for a finite-dimensional block quantum code cannot be transversal for any code that detects single-block errors due to the Eastin-Knill theorem  ([arXiv:0811.4262](https://arxiv.org/abs/0811.4262)). \end{defterm}
- A qudit code of length $n$ with permutation automorphism subgroups $N\triangleleft G\leq \mathrm{PAut}(Q)$ and simple non-Abelian quotient $G/N$ must satisfy $n\geq \mu(G/N)$  ([arXiv:2604.15111](https://arxiv.org/abs/2604.15111)).

## Relations

- _parent_: [[concepts/qec/qecc]]
- _cousin_: [[concepts/qec/single-subsystem]] — Block quantum codes for $n=1$ are monolithic codes.

## Notes

- Tables of linear-programming upper bounds on general block quantum codes for various $n$, $k$, and $q$, based on algorithms developed in Refs.  ([doi:10.1007/978-3-540-37634-7_13](https://doi.org/10.1007/978-3-540-37634-7_13), [arXiv:2405.15057](https://arxiv.org/abs/2405.15057)), are maintained by M. Grassl at this [website](https://www.codetables.de/). A Magma implementation exists at this [website](https://magma.maths.usyd.edu.au/magma/handbook/text/1976).
- States of block quantum codes can be classified in terms of the complexity of their underlying encoding circuit; see the Complexity Zoo Exhibit on Classes of Quantum States and Probability Distributions }.
