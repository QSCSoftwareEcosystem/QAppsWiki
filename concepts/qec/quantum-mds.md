---
type: concept
name: Quantum maximum-distance-separable (MDS) code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/block-quantum
- concepts/qec/galois-reed-muller
- concepts/qec/qecc-finite
- concepts/qec/skew-cyclic-galois-css
- concepts/qec/stabilizer-over-gfqsq
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/quantum_mds
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: quantum_mds
---

# Quantum maximum-distance-separable (MDS) code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/quantum_mds) (`code_id: quantum_mds`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A type of block quantum code whose parameters satisfy the quantum Singleton bound with equality.

An $((n,K,d))$ code constructed out of $q$-dimensional qudits is a quantum MDS code if parameters $n$, $K$, $d$, and $q$ are such that they saturate the quantum Singleton bound  ([arXiv:quant-ph/9604034](https://arxiv.org/abs/quant-ph/9604034), [arXiv:quant-ph/9702031](https://arxiv.org/abs/quant-ph/9702031), [arXiv:quant-ph/9703048](https://arxiv.org/abs/quant-ph/9703048)),
\begin{align}
K \leq q^{n-2(d-1)}
\end{align}
becomes an equality for such codes.
When $K = q^k$ for some integer $k$, the equality condition reduces to $2(d-1) = n-k$.
Such codes are pure  ([arXiv:quant-ph/9703048](https://arxiv.org/abs/quant-ph/9703048)); see also  mentioned in Ref.  ([arXiv:1907.07733](https://arxiv.org/abs/1907.07733)).
The length $n$ of a quantum MDS code with distance $d \geq 3$ is bounded by the qudit dimension, $n \leq q^2 + d - 2$  ([arXiv:1907.07733](https://arxiv.org/abs/1907.07733)).

(source: raw/error-correction-zoo.md)

## Protection

Given $n$ and $k$, MDS codes have the highest distance possible of all codes and so have the best possible error correction properties.

## Relations

- _parent_: [[concepts/qec/block-quantum]]
- _parent_: [[concepts/qec/qecc-finite]]
- _cousin_: [`mds`](https://errorcorrectionzoo.org/c/mds) — Quantum MDS codes are quantum analogues of MDS codes.
- _cousin_: [[concepts/qec/galois-reed-muller]] — Quantum GRM codes yield quantum MDS families $⟦q,q-2\nu-2,\nu+2⟧_q$ for $0 \leq \nu \leq (q-2)/2$, $⟦q^2,q^2-2\nu-2,\nu+2⟧_q$ for $0 \leq \nu \leq q-2$, and punctured descendants $⟦(\nu+1)q,(\nu+1)q-2\nu-2,\nu+2⟧_q$ for $0 \leq \nu \leq q-2$  ([arXiv:quant-ph/0502001](https://arxiv.org/abs/quant-ph/0502001)).
- _cousin_: [`q-ary_cyclic`](https://errorcorrectionzoo.org/c/q-ary_cyclic) — Quantum MDS codes can be constructed from $q$-ary cyclic codes using the Hermitian construction  ([doi:10.1109/TIT.2011.2159039](https://doi.org/10.1109/TIT.2011.2159039)).
- _cousin_: [[concepts/qec/stabilizer-over-gfqsq]] — Many quantum MDS codes are constructed from Hermitian self-orthogonal codes over $\mathbb{F}_{q^2}$ using the Hermitian construction  ([arXiv:quant-ph/0312164](https://arxiv.org/abs/quant-ph/0312164), [arXiv:0906.2509](https://arxiv.org/abs/0906.2509), [arXiv:1507.08355](https://arxiv.org/abs/1507.08355), [arXiv:1803.07927](https://arxiv.org/abs/1803.07927)), in particular from cyclic  ([doi:10.1109/TIT.2011.2159039](https://doi.org/10.1109/TIT.2011.2159039)), constacyclic  ([doi:10.1109/TIT.2014.2308180](https://doi.org/10.1109/TIT.2014.2308180), [doi:10.1109/TIT.2015.2388576](https://doi.org/10.1109/TIT.2015.2388576), [arXiv:1803.07927](https://arxiv.org/abs/1803.07927)) and negacyclic  ([doi:10.1109/TIT.2012.2220519](https://doi.org/10.1109/TIT.2012.2220519)) codes.
- _cousin_: [`constacyclic`](https://errorcorrectionzoo.org/c/constacyclic) — Many quantum MDS codes are constructed from Hermitian self-orthogonal codes over $\mathbb{F}_{q^2}$ using the Hermitian construction  ([arXiv:quant-ph/0312164](https://arxiv.org/abs/quant-ph/0312164), [arXiv:0906.2509](https://arxiv.org/abs/0906.2509), [arXiv:1507.08355](https://arxiv.org/abs/1507.08355), [arXiv:1803.07927](https://arxiv.org/abs/1803.07927)), in particular from cyclic  ([doi:10.1109/TIT.2011.2159039](https://doi.org/10.1109/TIT.2011.2159039)), constacyclic  ([doi:10.1109/TIT.2014.2308180](https://doi.org/10.1109/TIT.2014.2308180), [doi:10.1109/TIT.2015.2388576](https://doi.org/10.1109/TIT.2015.2388576), [arXiv:1803.07927](https://arxiv.org/abs/1803.07927)), and negacyclic  ([doi:10.1109/TIT.2012.2220519](https://doi.org/10.1109/TIT.2012.2220519)) codes.
- _cousin_: [`generalized_reed_solomon`](https://errorcorrectionzoo.org/c/generalized_reed_solomon) — Some quantum MDS codes are constructed from cyclic and constacyclic codes  ([arXiv:1502.05267](https://arxiv.org/abs/1502.05267)) which are GRS codes  ([doi:10.1007/s10623-022-01174-5](https://doi.org/10.1007/s10623-022-01174-5), [doi:10.1007/s10623-023-01294-6](https://doi.org/10.1007/s10623-023-01294-6)).
- _cousin_: [[concepts/qec/skew-cyclic-galois-css]] — Some quantum MDS codes are constructed from cyclic and constacyclic codes using the Galois-qudit CSS construction  ([doi:10.1016/j.disc.2020.112189](https://doi.org/10.1016/j.disc.2020.112189)).

## Notes

- See Ref.  ([doi:10.1017/CBO9781139034807.014](https://doi.org/10.1017/CBO9781139034807.014)) for an overview of quantum MDS codes.
- Tables of quantum MDS codes  ([arXiv:1907.07733](https://arxiv.org/abs/1907.07733)).
