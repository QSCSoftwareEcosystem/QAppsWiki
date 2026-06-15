---
type: concept
name: Perfect quantum code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/qecc-finite
- concepts/qec/small-distance-quantum
- concepts/qec/stabilizer-over-gf4
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/quantum_perfect
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: quantum_perfect
---

# Perfect quantum code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/quantum_perfect) (`code_id: quantum_perfect`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A type of block quantum code whose parameters satisfy the quantum Hamming bound with equality.

A non-degenerate code constructed out of $q$-dimensional qudits and having parameters $((n,K,2t+1))$ is perfect if $n$, $K$, $t$, and $q$ are such that the quantum Hamming bound  ([arXiv:quant-ph/9602022](https://arxiv.org/abs/quant-ph/9602022)),
\begin{align}
\sum_{j=0}^{t}(q^2-1)^{j}{n \choose j}\leq q^{n}/K
\end{align}
becomes an equality for such codes.
For example, for a qubit $q=2$ code with one logical qubit ($K=2$) and $t=1$, the bound becomes $3n+1 \leq 2^{n-1}$.
The bound can be saturated only at certain $n$.

For qubit codes with $K=2^k$, one can work out an asymptotic Hamming bound in the large-$n,k,t$ limit,
\begin{align}
\frac{k}{n}\leq 1-\frac{t}{n}\log_{2}3-h(t/n),
\end{align}
where $h$ is the binary entropy function.

Degenerate codes can in principle violate the quantum Hamming bound.
It was shown that qubit stabilizer codes correcting up to two errors  ([arXiv:quant-ph/9705052](https://arxiv.org/abs/quant-ph/9705052)), qudit stabilizer codes up to distance two  ([arXiv:0711.4603](https://arxiv.org/abs/0711.4603)), qudit CSS codes of qudit dimension $q\geq 5$ along with certain other codes  ([arXiv:0811.1621](https://arxiv.org/abs/0811.1621)), and qubit codes up to distance $d\leq 127$  ([arXiv:2208.11800](https://arxiv.org/abs/2208.11800)) do not violate the bound.
A quantum Hamming-like bound exists for degenerate qubit stabilizer codes  ([arXiv:2306.00048](https://arxiv.org/abs/2306.00048)).

(source: raw/error-correction-zoo.md)

## Protection

Perfect codes have been classified.
For qubits ($q=2$), the only nontrivial perfect codes are the stabilizer code family $⟦(4^r-1)/3, (4^r-1)/3 - 2r, 3⟧$ for $r \geq 2$, obtained from Hamming codes over $\mathbb{F}_4$ via the Hermitian construction  ([arXiv:quant-ph/9607027](https://arxiv.org/abs/quant-ph/9607027), [arXiv:quant-ph/9608006](https://arxiv.org/abs/quant-ph/9608006)). These codes are related to partial spreads in projective geometry  ([doi:10.2140/iig.2008.6.53](https://doi.org/10.2140/iig.2008.6.53)).
For qudits, the corresponding family is the $⟦\frac{q^{2r}-1}{q^{2}-1},\frac{q^{2r}-1}{q^{2}-1}-2r,3⟧_q$ family of quantum twisted codes  ([arXiv:0907.0049](https://arxiv.org/abs/0907.0049), [doi:10.1002/(SICI)1520-6610(2000)8:3<174::AID-JCD3>3.0.CO;2-T](https://doi.org/10.1002/(SICI)1520-6610(2000)8:3<174::AID-JCD3>3.0.CO;2-T)).

## Rate

$k/n\to 1$ asymptotically with $n$.

## Relations

- _parent_: [[concepts/qec/small-distance-quantum]] — All non-trivial perfect codes have distance three.
- _parent_: [[concepts/qec/qecc-finite]]
- _cousin_: [`perfect`](https://errorcorrectionzoo.org/c/perfect) — A classical (quantum) perfect code saturates the classical (quantum) Hamming bound.
- _cousin_: [[concepts/qec/stabilizer-over-gf4]] — For qubits ($q=2$), the only nontrivial perfect codes are the stabilizer code family $⟦(4^r-1)/3, (4^r-1)/3 - 2r, 3⟧$ for $r \geq 2$, obtained from Hamming codes over $\mathbb{F}_4$ via the Hermitian construction  ([arXiv:quant-ph/9607027](https://arxiv.org/abs/quant-ph/9607027), [arXiv:quant-ph/9608006](https://arxiv.org/abs/quant-ph/9608006)). These codes are related to partial spreads in projective geometry  ([doi:10.2140/iig.2008.6.53](https://doi.org/10.2140/iig.2008.6.53)).
- _cousin_: [`q-ary_hamming`](https://errorcorrectionzoo.org/c/q-ary_hamming) — For qubits ($q=2$), the only nontrivial perfect codes are the stabilizer code family $⟦(4^r-1)/3, (4^r-1)/3 - 2r, 3⟧$ for $r \geq 2$, obtained from Hamming codes over $\mathbb{F}_4$ via the Hermitian construction  ([arXiv:quant-ph/9607027](https://arxiv.org/abs/quant-ph/9607027), [arXiv:quant-ph/9608006](https://arxiv.org/abs/quant-ph/9608006)). These codes are related to partial spreads in projective geometry  ([doi:10.2140/iig.2008.6.53](https://doi.org/10.2140/iig.2008.6.53)).

## Notes

- 
