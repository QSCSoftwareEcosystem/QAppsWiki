---
type: concept
name: Good QLDPC code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/general-qldpc
- concepts/qec/quantum-mds
- concepts/qec/quantum-singleton
- concepts/qec/translationally-invariant-stabilizer
- concepts/qec/translationally-invariant-subsystem
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/good_qldpc
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: good_qldpc
---

# Good QLDPC code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/good_qldpc) (`code_id: good_qldpc`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Also called *asymptotically good QLDPC codes*. A family of QLDPC codes $⟦n_i,k_i,d_i⟧$ whose asymptotic rate $\lim_{i\to\infty} k_i/n_i$ and asymptotic distance $\lim_{i\to\infty} d_i/n_i$ are both positive.

Known constructions of good QLDPC codes can be understood as closely related balanced-product-type constructions on left-right Cayley complexes  ([arXiv:2402.16831](https://arxiv.org/abs/2402.16831)).
Three prominent constructions assign qubits and check operators to vertices, edges, and faces of the left-right Cayley complex in different ways:
  \begin{table}
    \begin{cells}
    \celldata<c H, c H, c H, c H>{Code & vertices & edges & faces}
    \celldata<c, c, c, c>{
    expander lifted-product & qubits & $X,Z$ checks & qubits
        \\
    quantum Tanner & $X,Z$ checks &  & qubits
        \\
    Dinur-Hsieh-Lin-Vidick & $X$ checks & qubits & $Z$ checks
    }
    \end{cells}
    \caption{Assignment of qubits and checks for three asymptotically good QLDPC codes.}
    \label{table:good-qldpc-codes}
  \end{table}
  The left-right Cayley complex can itself be understood as a balanced product of two Cayley graphs, and this viewpoint organizes its relation to balanced-product and quantum Tanner constructions  ([arXiv:2402.16831](https://arxiv.org/abs/2402.16831)).
  See  ([arXiv:2402.16831](https://arxiv.org/abs/2402.16831)) for more relationships between the constructions.

(source: raw/error-correction-zoo.md)

## Rate

The codes' rate and distance are both separated from zero as block length goes to infinity. 
Rains shadow enumerators can be used to show that the distance of an asymptotically good QLDPC code should be bounded as $d\leq n/3$  ([arXiv:quant-ph/9611001](https://arxiv.org/abs/quant-ph/9611001)); see Ref.  ([arXiv:2408.16914](https://arxiv.org/abs/2408.16914)).
AEL distance amplification  ([doi:10.1109/SFCS.1995.492581](https://doi.org/10.1109/SFCS.1995.492581), [doi:10.1109/18.556669](https://doi.org/10.1109/18.556669)) can be used to construct constant-alphabet QLDPC CSS codes of any target rate $R$ and relative distance $(1-R-\gamma)/2$ that are decodable in linear time up to half that distance  ([arXiv:2212.09935](https://arxiv.org/abs/2212.09935)).

## Relations

- _parent_: [[concepts/qec/general-qldpc]]
- _cousin_: [[concepts/qec/translationally-invariant-stabilizer]] — Chain complexes describing some QLDPC codes  ([arXiv:2012.02249](https://arxiv.org/abs/2012.02249), [arXiv:2309.16104](https://arxiv.org/abs/2309.16104)), and, more generally, CSS codes  ([arXiv:2404.16736](https://arxiv.org/abs/2404.16736)) can be 'lifted' into higher-dimensional manifolds admitting some notion of geometric locality. Applying this procedure to good QLDPC codes yields $⟦n,n^{1-2/D},n^{1-1/D}⟧$ lattice stabilizer codes in $D$ spatial dimensions that saturate the BPT bound  ([arXiv:2303.06755](https://arxiv.org/abs/2303.06755), [arXiv:2309.16104](https://arxiv.org/abs/2309.16104), [arXiv:2408.01769](https://arxiv.org/abs/2408.01769)).
- _cousin_: [[concepts/qec/translationally-invariant-subsystem]] — An $⟦n,k,d⟧$ qubit stabilizer code can be converted into an order $⟦O(\ell \delta n),k,\Omega(d/w)⟧$ subsystem qubit stabilizer code with weight-three gauge operators via the wire-code mapping  ([arXiv:2410.10194](https://arxiv.org/abs/2410.10194)), which uses weight reduction. 
Here, $w$ and $\delta$ are the weight and degree of the input code's Tanner graph, while $\ell$ is the length of the longest edge of a particular embedding of that graph.
Applying this procedure to good QLDPC codes and using an embedding into $D$-dimensional Euclidean space yields lattice subsystem codes whose logical-qubit number and distance both scale as $\Theta(n^{1-1/D})$ as functions of block length $n$, saturating the subsystem BT bound  ([arXiv:2410.10194](https://arxiv.org/abs/2410.10194)).
- _cousin_: [[concepts/qec/quantum-mds]] — AEL distance amplification  ([doi:10.1109/SFCS.1995.492581](https://doi.org/10.1109/SFCS.1995.492581), [doi:10.1109/18.556669](https://doi.org/10.1109/18.556669)) can be used to construct asymptotically good QLDPC codes that approach the quantum Singleton bound  ([arXiv:2212.09935](https://arxiv.org/abs/2212.09935)).
- _cousin_: [[concepts/qec/quantum-singleton]] — AEL distance amplification  ([doi:10.1109/SFCS.1995.492581](https://doi.org/10.1109/SFCS.1995.492581), [doi:10.1109/18.556669](https://doi.org/10.1109/18.556669)) can be used to construct constant-alphabet QLDPC CSS codes of any target rate $R$ and relative distance $(1-R-\gamma)/2$ that are decodable in linear time up to half that distance  ([arXiv:2212.09935](https://arxiv.org/abs/2212.09935)). The AEL distance-amplification framework also yields constant-alphabet approximate quantum codes that decode nearly up to the quantum Singleton bound  ([arXiv:2212.09935](https://arxiv.org/abs/2212.09935)).
