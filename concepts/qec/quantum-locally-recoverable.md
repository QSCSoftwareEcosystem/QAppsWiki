---
type: concept
name: Quantum locally recoverable code (QLRC)
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/block-quantum
- concepts/qec/galois-css
- concepts/qec/hypergraph-product
- concepts/qec/quantum-random
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/quantum_locally_recoverable
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: quantum_locally_recoverable
---

# Quantum locally recoverable code (QLRC)

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/quantum_locally_recoverable) (`code_id: quantum_locally_recoverable`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A QLRC of locality $r$ is a block quantum code whose code states can be recovered after a single erasure by accessing at most $r-1$ other subsystems and applying a recovery map.

(source: raw/error-correction-zoo.md)

## Protection

A Singleton-like QLRC bound states that an $((n,K,d))_q$ QLRC of locality $r$ and rate $R = \frac{\log_q K}{n}$ must have relative distance  ([arXiv:2311.08653](https://arxiv.org/abs/2311.08653))
\begin{align}
  \delta = \frac{d}{n} \leq \frac{1-R}{2} - \Omega\left(\frac{1}{r}\right)~,
\end{align}
implying that locality restricts the distance of the code.
Random QLRCs with qudit dimension $q = 2^{O(r)}$ achieve a relative distance that is order $O(1/r)$ below the bound  ([arXiv:2311.08653](https://arxiv.org/abs/2311.08653)).
Codes constructed with the help of AEL distance amplification  ([doi:10.1109/SFCS.1995.492581](https://doi.org/10.1109/SFCS.1995.492581), [doi:10.1109/18.556669](https://doi.org/10.1109/18.556669)) admit a gap of order $O(1/r^{1/4})$  ([arXiv:2311.08653](https://arxiv.org/abs/2311.08653)).
Folded quantum Tamo-Barg codes yield explicit QLRCs of arbitrary prime locality $r$, rate at least $R$, relative distance $\delta \geq (1-R)/2 - O(1/\sqrt{r})$, and qudit dimension $q = n^{O(r^2)}$  ([arXiv:2311.08653](https://arxiv.org/abs/2311.08653)).

QLRCs have been extended to codes with intersecting recovery sets, and a Singleton-like bound has been derived for such codes  ([arXiv:2501.10354](https://arxiv.org/abs/2501.10354)).

## Decoders

- Codes constructed with the help of AEL distance amplification  ([doi:10.1109/SFCS.1995.492581](https://doi.org/10.1109/SFCS.1995.492581), [doi:10.1109/18.556669](https://doi.org/10.1109/18.556669)) admit efficient decoders  ([arXiv:2311.08653](https://arxiv.org/abs/2311.08653)).

## Relations

- _parent_: [[concepts/qec/block-quantum]]
- _cousin_: [`locally_recoverable`](https://errorcorrectionzoo.org/c/locally_recoverable) — QLRCs are quantum analogues of LRCs.
- _cousin_: [[concepts/qec/galois-css]] — A Galois-qudit CSS code is a QLRC of locality $r$ if each qudit participates in at least one $X$-type and one $Z$-type stabilizer whose union of supports has weight $\leq r$  ([arXiv:2311.08653](https://arxiv.org/abs/2311.08653)).
- _cousin_: [[concepts/qec/quantum-random]] — Random QLRCs with qudit dimension $q = 2^{O(r)}$ achieve a relative distance that is order $O(1/r)$ below the Singleton-like QLRC bound  ([arXiv:2311.08653](https://arxiv.org/abs/2311.08653)).
- _cousin_: [[concepts/qec/hypergraph-product]] — A variant of the hypergraph product can be used to define QLRCs with intersecting recovery sets  ([arXiv:2501.10354](https://arxiv.org/abs/2501.10354)).
