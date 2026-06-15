---
type: concept
name: Topological code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/block-quantum
- concepts/qec/cluster-state
- concepts/qec/hamiltonian
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/topological
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: topological
---

# Topological code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/topological) (`code_id: topological`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A code whose codewords form the ground-state or low-energy subspace of a (typically geometrically local) code Hamiltonian realizing a topological phase.
A topological phase may be *bosonic* or *fermionic*, i.e., constructed out of underlying subsystems whose operators commute or anti-commute with each other, respectively.
Unless otherwise noted, the phases discussed are bosonic.

\subsection{2D topological codes}

The physical Hilbert space of 2D topological codes consists of $n$ subsystems which lie on edges, vertices, or faces of a tessellation of a 2D surface $\Sigma^2$.
2D topological order requires weight-four (four-body) Hamiltonian terms, i.e., it cannot be stabilized via weight-two (two-body) or weight-three (three-body) terms on nearly Euclidean geometries of qubits or qutrits  ([arXiv:quant-ph/0308021](https://arxiv.org/abs/quant-ph/0308021), [arXiv:1102.0770](https://arxiv.org/abs/1102.0770), [arXiv:1803.02213](https://arxiv.org/abs/1803.02213)).

For subsystems with finite local dimension, topological phases are defined by their *anyons*  ([doi:10.1007/BF02727953](https://doi.org/10.1007/BF02727953), [doi:10.1063/1.524510](https://doi.org/10.1063/1.524510), [doi:10.1103/PhysRevLett.49.957](https://doi.org/10.1103/PhysRevLett.49.957), [doi:10.1063/1.2810672](https://doi.org/10.1063/1.2810672)), which are local bulk excitations of the code Hamiltonian defined on a lattice; see Refs.  ([doi:10.1007/BF01877742](https://doi.org/10.1007/BF01877742), [doi:10.1007/BF01646454](https://doi.org/10.1007/BF01646454), [arXiv:1804.03203](https://arxiv.org/abs/1804.03203)) for more rigorous formulations.

Anyons are created in pairs by local operators, and two anyons lie in the same *superselection sector* if a  local operator can convert one anyon into the other.
Each superselection sector is assumed to be labeled by one anyon type, and local operators cannot change superselection sectors.

Anyons can braid with themselves, with their *exchange statistics* (a.k.a. *topological spin*) defined by phases $\theta(a)\in U(1)$ obtained by exchanging two anyons of each type $a$.
They can also braid with each other, a process defined by *braiding relations* $B(a,b)$ for an anyon pair $a,b$.
An anyon theory is called *non-modular* or *pre-modular* if there exists an anyon $a$ that braids trivially with all anyons.

Anyons $a$ and $b$ can also fuse with each other, meaning that one considers both anyons as one anyon $ab$ and decomposes $ab$ into the anyons representing each superselection sector according to the anyons' *fusion rules*.
For example, two anyons $a,b$ may fuse to the trivial (i.e., vacuum) anyon $1$, $ab=1$, meaning that the composite excitation $ab$ is indistinguishable from the case of no excitation.
Anyon fusion for many anyon theories is equivalent to a truncated Kronecker product of irreps of deformed Lie groups (i.e., "quantum groups"), which is a combination of the ordinary Kronecker product and a restriction to only decomposable representations  (Cambridge University Press, 1995)}}.

The exchange statistics and fusion rules of anyons cannot be arbitrary and have to satisfy certain consistency relations.
Admissible exchange and fusion data are characterized by a *unitary braided fusion category*.

Each anyon $a$ has a *quantum dimension* $d_a$ associated with it.
The quantum dimensions add up to the *total quantum dimension* $D$,
\begin{align}
  \sum_{a}d_{a}^{2}=D^{2}~.
\end{align}
Quantum dimensions do not correspond to dimensions of vector spaces and may not be integer-valued.

An anyon theory that does not admit gapped boundaries (when put on a manifold with boundaries) is called *chiral*; otherwise, it is *non-chiral* or *gapped*.
Chiral topological phases admit a nonzero value of the *chiral central charge* $c_{-}$.
A generalization  ([arXiv:quant-ph/9707021](https://arxiv.org/abs/quant-ph/9707021)) of the Gauss-Milgram sum rule for an anyon theory $A$ admitting $|A|$ anyon types,
\begin{align}
  \frac{1}{\sqrt{|A|}}\sum_{a\in A}d_{a}^{2}\theta_{a}=De^{i\frac{2\pi}{8}c_{-}}~,
\end{align}
relates the chiral central charge (modulo 8) to the exchange statistics and quantum dimensions.
Gapped anyon theories admit a Lagrangian subalgebra  ([arXiv:1009.2117](https://arxiv.org/abs/1009.2117), [arXiv:1203.4568](https://arxiv.org/abs/1203.4568), [arXiv:2107.13091](https://arxiv.org/abs/2107.13091)).

The *topological entanglement entropy*  ([arXiv:hep-th/0510092](https://arxiv.org/abs/hep-th/0510092), [arXiv:cond-mat/0510613](https://arxiv.org/abs/cond-mat/0510613)) of a 2D topological code is a measure of the entanglement between a region and its complement; this measure extracts the total quantum dimension $D$ of the phase.
ZX calculus can be used to detect 2D topological order  ([arXiv:2509.12355](https://arxiv.org/abs/2509.12355)).
Other functions of code states extract the topological $S$-matrix  ([arXiv:1111.2342](https://arxiv.org/abs/1111.2342), [arXiv:1407.2926](https://arxiv.org/abs/1407.2926)) and the chiral central charge $c_-$  ([arXiv:2110.06932](https://arxiv.org/abs/2110.06932)).
No observable can distinguish topological order from product states  ([arXiv:2106.12627](https://arxiv.org/abs/2106.12627)).

There is no 1D bosonic topological order at nonzero temperature  ([arXiv:1804.05457](https://arxiv.org/abs/1804.05457), [arXiv:2511.14699](https://arxiv.org/abs/2511.14699)), and no commuting-projector model with nontrivial 2D topological order at nonzero temperature  ([arXiv:1106.6026](https://arxiv.org/abs/1106.6026)) (see also Ref.  ([arXiv:0904.4492](https://arxiv.org/abs/0904.4492))). 
General thermal states are separable above a sufficiently high temperature  ([arXiv:2403.16850](https://arxiv.org/abs/2403.16850)).

\subsection{3D and higher-dimensional topological codes}

The physical Hilbert space of 3D topological codes consists of $n$ subsystems which lie on edges, vertices, or faces of a tessellation of a 3D surface.
3D topological phases can have point-like and loop-like excitations, with the latter being created in pairs by 2D operators acting on subsystems supported on a plane or, more generally, a "membrane".

In the case when all point-like excitations satisfy bosonic braiding statistics, the topological phase can be realized by a Dijkgraaf-Witten gauge theory.
Such cases are thus characterized by the gauge theory's underlying data, a finite group and a cohomological cycle (i.e., cocycle)  ([arXiv:1704.04221](https://arxiv.org/abs/1704.04221), [arXiv:1808.09394](https://arxiv.org/abs/1808.09394)).
This data is in one-to-one correspondence with pointed fusion two-categories  ([arXiv:1704.04221](https://arxiv.org/abs/1704.04221)).

Phases with fermionic point-like excitations are examples of *beyond-group-cohomology phases*  ([arXiv:1403.1467](https://arxiv.org/abs/1403.1467)).
They have been classified  ([arXiv:1801.08530](https://arxiv.org/abs/1801.08530)), and some of them can be described by a two-gauge theory  ([arXiv:2110.14644](https://arxiv.org/abs/2110.14644)).

The classification of 4D  ([arXiv:2104.04534](https://arxiv.org/abs/2104.04534)) and higher-dimensional  ([arXiv:1405.5858](https://arxiv.org/abs/1405.5858), [arXiv:1702.00673](https://arxiv.org/abs/1702.00673), [arXiv:2003.06663](https://arxiv.org/abs/2003.06663)) topological phases is ongoing.

(source: raw/error-correction-zoo.md)

## Protection

Geometrically local 2D commuting-projector topological code Hamiltonians satisfy the two topological quantum order (TQO) conditions, TQO-1 and TQO-2  ([arXiv:1001.4363](https://arxiv.org/abs/1001.4363), [arXiv:1001.0344](https://arxiv.org/abs/1001.0344), [arXiv:1810.02428](https://arxiv.org/abs/1810.02428), [arXiv:2010.15337](https://arxiv.org/abs/2010.15337)).
For geometrically local frustration-free Hamiltonians, LTQO generalizes the TQO conditions, and LTQO together with the Local-Gap condition yields stability of the spectral gap under sufficiently weak quasi-local perturbations  ([arXiv:1109.1588](https://arxiv.org/abs/1109.1588), [arXiv:2110.11194](https://arxiv.org/abs/2110.11194)).

\begin{defterm}{TQO conditions}
\label{topic:tqo}
The TQO-1 condition states that the distance of the ground-state-subspace code is macroscopic, i.e., grows as a positive power of the lattice size  ([arXiv:1001.0344](https://arxiv.org/abs/1001.0344)).
The TQO-2 condition relates the ground states of restrictions of the Hamiltonian to some geometrically local region to those of the full Hamiltonian.
Let $\Pi_{N(X)}$ be the ground-state subspace projector of the Hamiltonian that includes all terms with at least some support on a geometrically local region $X$, with $N(X)$ consisting of the smallest region containing the support of all included terms.
TQO-2 states that any operator $O_X$ that annihilates the codespace projector $\Pi$ also has to annihilate the local projector $\Pi_{N(X)}$,
\begin{align}
  O_{X}\Pi=0\quad\Rightarrow\quad O_{X}\Pi_{N(X)}=0~.
\end{align}
This condition implies that any operator supported solely on $X$ cannot distinguish the global projector from the local one  ([arXiv:1001.4363](https://arxiv.org/abs/1001.4363), [arXiv:2405.19412](https://arxiv.org/abs/2405.19412)).
\end{defterm}

A notion of topological order generalizing both the cleaning lemma and the TQO conditions is *homogeneous topological order*  ([arXiv:2009.13551](https://arxiv.org/abs/2009.13551)).
Related topological order definitions include equivalence under course-graining (i.e., renormalization group)  ([arXiv:1406.5090](https://arxiv.org/abs/1406.5090), [arXiv:1407.8203](https://arxiv.org/abs/1407.8203)).
See  ([arXiv:2009.13551](https://arxiv.org/abs/2009.13551)) for a discussion.

Certain topological codes have nontrivial codespace complexity  ([arXiv:2310.04710](https://arxiv.org/abs/2310.04710)).

## Rate

The logical dimension $K$ of 2D topological codes described by unitary modular fusion categories depends on the type of manifold $\Sigma^2$ that is tessellated to form the many-body system.
For closed orientable manifolds  ([doi:10.1007/bf01217730](https://doi.org/10.1007/bf01217730), [doi:10.1007/BF01238857](https://doi.org/10.1007/BF01238857)),
\begin{align}
  K=\sum_{a\in A}\left(d_{a}/D\right)^{\chi(\Sigma^{2})}~,
\end{align}
and a generalization of the formula to the non-orientable case can be found in Ref.  ([arXiv:1612.07792](https://arxiv.org/abs/1612.07792)).

## Threshold

- Topological-code families can be used to obtain a fault-tolerance threshold, although the numerical threshold value and overhead depend strongly on the syndrome-extraction and decoding protocol .

## Encoders

- A depth of order $\Omega(L)$ is necessary for a unitary circuit to initialize in a 2D topologically ordered state using geometrically local gates on an $L\times L$ lattice  ([arXiv:quant-ph/0603121](https://arxiv.org/abs/quant-ph/0603121), [arXiv:quant-ph/0603114](https://arxiv.org/abs/quant-ph/0603114)), irrespective of whether the ground state admits Abelian or non-Abelian anyonic excitations.
However, only a finite-depth circuit and one round of measurements is required for non-Abelian topological orders with a Lagrangian subgroup  ([arXiv:2209.03964](https://arxiv.org/abs/2209.03964)).
- Algorithm that takes in reduced density matrices and outputs a circuit preparing the global state in polynomial time  ([arXiv:2410.23544](https://arxiv.org/abs/2410.23544)).

## General gates

- Ising anyon braiding and fusion were studied in a phenomenological model that was the first to study error correction with non-Abelian anyons  ([arXiv:1311.0019](https://arxiv.org/abs/1311.0019)).
- Codes with non-Abelian anyons present two complications. First, their anyons are not always represented as tensor-product unitary operators and thus cannot be corrected by such operations. Second, fusing such anyons can yield more than one outcome, complicating decoding algorithms  ([arXiv:hep-th/0110205](https://arxiv.org/abs/hep-th/0110205)).

## Relations

- _parent_: [[concepts/qec/block-quantum]] — Topological codes are block codes because an infinite family of tensor-product Hilbert spaces is required to formally define a phase of matter.
- _parent_: [[concepts/qec/hamiltonian]] — Codespace of a topological code is typically the ground-state or low-energy subspace of a geometrically local Hamiltonian admitting a topological phase.
Logical qubits can also be created via lattice defects or by appropriately scheduling measurements of gauge generators (see Floquet codes).
Geometrically local frustration-free code Hamiltonians on Euclidean manifolds are stable with respect to sufficiently weak quasi-local perturbations when they satisfy local topological quantum order together with the Local-Gap condition  ([arXiv:1109.1588](https://arxiv.org/abs/1109.1588), [arXiv:2110.11194](https://arxiv.org/abs/2110.11194)).
- _cousin_: [[concepts/qec/cluster-state]] — There exist necessary and sufficient conditions for a family of cluster states to exhibit the TQO-1 property  ([arXiv:2112.02502](https://arxiv.org/abs/2112.02502)).

## Notes

- Ref.  ([arXiv:cond-mat/0506438](https://arxiv.org/abs/cond-mat/0506438)) ([doi:10.7907/5NDZ-W890](https://doi.org/10.7907/5NDZ-W890), [arXiv:0707.1889](https://arxiv.org/abs/0707.1889), [arXiv:1508.02595](https://arxiv.org/abs/1508.02595), [arXiv:1610.03911](https://arxiv.org/abs/1610.03911), [doi:10.1017/9781316226308](https://doi.org/10.1017/9781316226308), [arXiv:2205.05565](https://arxiv.org/abs/2205.05565)) for introductions to topological phases.
- See [AnyonWiki](https://anyonwiki.github.io/) for lists of categories relevant to anyons.
- See  ([arXiv:2605.29137](https://arxiv.org/abs/2605.29137)) for a pedagogical introduction to topological codes.
