---
type: concept
name: Classical-quantum (c-q) code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts: []
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/classical_into_quantum
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: classical_into_quantum
---

# Classical-quantum (c-q) code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/classical_into_quantum) (`code_id: classical_into_quantum`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Code designed specifically for transmission of classical information through non-classical channels, e.g., quantum channels, hybrid classical-quantum channels, or channels with classical inputs and quantum outputs. 
Such codes include maps from a classical alphabet into a quantum Hilbert space.

(source: raw/error-correction-zoo.md)

## Rate

The Holevo channel capacity,
\begin{align}
  C=\lim_{n\to\infty}\frac{1}{n}\chi\left({\cal N}^{\otimes n}\right)~,
\end{align}
where $\chi$ is the Holevo information, is the highest rate of classical information transmission through a quantum channel with arbitrarily small error rate  ([doi:10.1103/PhysRevA.56.131](https://doi.org/10.1103/PhysRevA.56.131), [doi:10.1109/18.651037](https://doi.org/10.1109/18.651037)).

For an ensemble $\{p_i,\rho_i\}$ of input states the single-letter Holevo quantity is
\begin{align}
  \chi(\{p_i,\rho_i\},\mathcal N)
  &= S\Bigl(\mathcal N\Bigl(\sum_i p_i\rho_i\Bigr)\Bigr)
   - \sum_i p_i S\bigl(\mathcal N(\rho_i)\bigr)
\end{align}
and maximization over ensembles defines $\chi(\mathcal N)$.  The capacity
above is the regularized version of this because $\chi$ can be superadditive;
Hastings' counterexample shows strict superadditivity for certain random channels  ([arXiv:0809.3972](https://arxiv.org/abs/0809.3972)).

Corrections to the Holevo capacity and tradeoff between decoding error, code rate and code length are determined in quantum generalizations of small  ([arXiv:1308.6503](https://arxiv.org/abs/1308.6503)), moderate  ([arXiv:1701.03114](https://arxiv.org/abs/1701.03114), [arXiv:1709.05258](https://arxiv.org/abs/1709.05258)), and large  ([arXiv:1409.3562](https://arxiv.org/abs/1409.3562)) deviation analysis.
Bounds exist on the one-shot capacity, i.e., the achievability of classical codes given only one use of the quantum channel.
The ideal decoding error is suppressed exponentially with the number of subsystems $n$ (for c-q block codes), and the achievable exponent has been studied in Refs.  ([arXiv:quant-ph/9703013](https://arxiv.org/abs/quant-ph/9703013), [arXiv:quant-ph/9907087](https://arxiv.org/abs/quant-ph/9907087), [arXiv:quant-ph/0206186](https://arxiv.org/abs/quant-ph/0206186), [arXiv:quant-ph/0611013](https://arxiv.org/abs/quant-ph/0611013), [arXiv:0805.4092](https://arxiv.org/abs/0805.4092), [arXiv:1007.5456](https://arxiv.org/abs/1007.5456), [arXiv:1312.3822](https://arxiv.org/abs/1312.3822), [arXiv:2208.02132](https://arxiv.org/abs/2208.02132), [arXiv:2303.04138](https://arxiv.org/abs/2303.04138), [arXiv:2310.09014](https://arxiv.org/abs/2310.09014)); see  ([arXiv:2208.02132](https://arxiv.org/abs/2208.02132)) for a summary.
Achievable error exponents for communication are related to those for privacy amplification  ([arXiv:2207.08899](https://arxiv.org/abs/2207.08899)).
In the high-rate case, a lower  ([arXiv:1201.5411](https://arxiv.org/abs/1201.5411)) and upper  ([arXiv:2407.12403](https://arxiv.org/abs/2407.12403)) bound on the error exponent for general channels matches a conjecture by Holevo  ([arXiv:quant-ph/9907087](https://arxiv.org/abs/quant-ph/9907087)).
A one-shot bound for random codes  ([arXiv:2507.06232](https://arxiv.org/abs/2507.06232)) resolves a conjecture by Burnashev and Holevo  ([arXiv:quant-ph/9703013](https://arxiv.org/abs/quant-ph/9703013)). 

Unambiguous state discrimination (USD) can be used to achieve Holevo capacity on a general pure-state c-q channel  ([doi:10.1109/ISIT.2013.6620209](https://doi.org/10.1109/ISIT.2013.6620209)).

## Decoders

- Unambiguous state discrimination (USD)  ([doi:10.1109/ISIT.2013.6620209](https://doi.org/10.1109/ISIT.2013.6620209)).

## Relations

- _parent_: [`oaecc`](https://errorcorrectionzoo.org/c/oaecc) — An OAQECC that retains its block structure for storing classical information but stores no quantum information and has no gauge degrees of freedom (e.g., gauge qubits) is a c-q code.
