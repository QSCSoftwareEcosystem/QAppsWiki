---
type: concept
name: Galois-qudit expander code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Galois-qudit Sipser-Spielman code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/balanced-product
- concepts/qec/galois-hypergraph-product
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/galois_expander
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: galois_expander
---

# Galois-qudit expander code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/galois_expander) (`code_id: galois_expander`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Galois-qudit CSS code obtained from tensor products of chain complexes associated with an explicit family of expander codes with Reed-Solomon local checks.

In the explicit construction of  ([arXiv:2410.14662](https://arxiv.org/abs/2410.14662)), these expander-code complexes contain planted GRM codewords, yielding a *multiplication property* that allows QLDPC Galois-qudit quantum expander codes with transversal $C^{r-1} Z$ gates while achieving $D\geq N^{1/r}/\operatorname{poly}(\log N)$ and $w\leq\operatorname{poly}(\log N)$.

(source: raw/error-correction-zoo.md)

## Magic scaling exponent

For every integer $r\geq 2$ and every $\epsilon>0$, the construction yields $⟦N,K\geq N^{1-\epsilon},D\geq N^{1/r}/\operatorname{poly}(\log N)⟧_q$ QLDPC Galois-qudit quantum expander codes with transversal $C^{r-1} Z$ gates and stabilizer weight $w\leq\operatorname{poly}(\log N)$  ([arXiv:2410.14662](https://arxiv.org/abs/2410.14662)). This construction allows for arbitrarily small magic-state yield parameter $\gamma$.

## Transversal gates

- For every integer $r\geq 2$, there are QLDPC Galois-qudit quantum expander codes with transversal $C^{r-1} Z$ gates and parameters $⟦N,K\geq N^{1-\epsilon},D\geq N^{1/r}/\operatorname{poly}(\log N)⟧_q$  ([arXiv:2410.14662](https://arxiv.org/abs/2410.14662)). By decomposing each Galois qudit into a Kronecker product of qubits, this yields an explicit qubit CSS QLDPC family with parameters $⟦N,K\geq N^{1-\epsilon},D\geq N^{1/r}/\operatorname{poly}(\log N)⟧$, stabilizer weight $\operatorname{poly}(\log N)$, and transversal $C^{r-1}Z$ gates acting on $N^{1-\epsilon}$ disjoint logical $r$-tuples.

## Relations

- _parent_: [[concepts/qec/galois-hypergraph-product]]
- _cousin_: [`reed_solomon`](https://errorcorrectionzoo.org/c/reed_solomon) — The explicit expander-code construction with Reed-Solomon local checks in  ([arXiv:2410.14662](https://arxiv.org/abs/2410.14662)) yields $⟦N,K\geq N^{1-\epsilon},D\geq N^{1/r}/\operatorname{poly}(\log N)⟧_q$ QLDPC Galois-qudit quantum expander codes with transversal $C^{r-1} Z$ gates. Balanced products of the same RS-based complexes also yield $[n,k\geq n^{1-\epsilon},d\geq n/\operatorname{poly}(\log n)]_q$ LTCs exhibiting the multiplication property.
- _cousin_: [`expander`](https://errorcorrectionzoo.org/c/expander) — The explicit expander-code construction of  ([arXiv:2410.14662](https://arxiv.org/abs/2410.14662)) yields $⟦N,K\geq N^{1-\epsilon},D\geq N^{1/r}/\operatorname{poly}(\log N)⟧_q$ QLDPC Galois-qudit quantum expander codes with transversal $C^{r-1} Z$ gates. Balanced products of the same expander-code complexes also yield $[n,k\geq n^{1-\epsilon},d\geq n/\operatorname{poly}(\log n)]_q$ LTCs exhibiting the multiplication property.
- _cousin_: [`generalized_reed_muller`](https://errorcorrectionzoo.org/c/generalized_reed_muller) — The explicit expander-code construction of  ([arXiv:2410.14662](https://arxiv.org/abs/2410.14662)) contains planted GRM codewords.
- _cousin_: [[concepts/qec/balanced-product]] — Balanced products of the RS-based expander-code complexes in  ([arXiv:2410.14662](https://arxiv.org/abs/2410.14662)) yield $[n,k\geq n^{1-\epsilon},d\geq n/\operatorname{poly}(\log n)]_q$ LTCs exhibiting the multiplication property.
- _cousin_: [`q-ary_ltc`](https://errorcorrectionzoo.org/c/q-ary_ltc) — Balanced products of the RS-based expander-code complexes in  ([arXiv:2410.14662](https://arxiv.org/abs/2410.14662)) yield $[n,k\geq n^{1-\epsilon},d\geq n/\operatorname{poly}(\log n)]_q$ LTCs exhibiting the multiplication property.
