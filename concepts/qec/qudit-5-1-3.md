---
type: concept
name: $⟦5,1,3⟧_{\mathbb{Z}_q}$ modular-qudit code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/ame
- concepts/qec/graph-quantum
- concepts/qec/quantum-cyclic
- concepts/qec/qudit-stabilizer
- concepts/qec/small-distance-quantum
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/qudit_5_1_3
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: qudit_5_1_3
---

# $⟦5,1,3⟧_{\mathbb{Z}_q}$ modular-qudit code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/qudit_5_1_3) (`code_id: qudit_5_1_3`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Modular-qudit stabilizer code that generalizes the five-qubit perfect code using properties of the multiplicative group $\mathbb{Z}_q$  ([arXiv:quant-ph/9702033](https://arxiv.org/abs/quant-ph/9702033)); see also  ([arXiv:quant-ph/9703048](https://arxiv.org/abs/quant-ph/9703048)). It has four stabilizer generators consisting of $X Z Z^\dagger X^\dagger I$ and its cyclic permutations.

The components of the encoding isometry in the computational basis (with $a$ being the logical qudit index) are  ([arXiv:1902.07714](https://arxiv.org/abs/1902.07714))
\begin{align}
    T_{aklmnp}=\delta_{a,k+l+m+n+p}^{\mathbb{Z}_{q}}\frac{1}{q^{2}}\omega^{kl+lm+mn+np+pk}~,
\end{align}
where $\omega$ is a primitive $q$th root of unity, and where $\delta^{\mathbb{Z}_{q}}$ is the $\mathbb{Z_q$ Kronecker-delta function}.

(source: raw/error-correction-zoo.md)

## Protection

Protects against a single error on any one qudit. Detects two-qudit errors.

## Encoders

- Generalized CNOT, Toffoli, and quantum Fourier transform gates.
- Encoders for prime-dimensional qudits  ([arXiv:2502.05992](https://arxiv.org/abs/2502.05992), [arXiv:2509.25587](https://arxiv.org/abs/2509.25587)).

## Decoders

- Decoder for prime-dimensional qudits  ([arXiv:2502.05992](https://arxiv.org/abs/2502.05992)).

## General gates

- Magic-state distillation for the $q=3$ case  ([arXiv:1202.2326](https://arxiv.org/abs/1202.2326)).

## Relations

- _parent_: [[concepts/qec/qudit-stabilizer]]
- _parent_: [[concepts/qec/ame]] — The $⟦5,1,3⟧_{\mathbb{Z}_q}$ code is a perfect-tensor code because it stems from the $⟦6,0,4⟧_{\mathbb{Z}_q}$ AME state  ([arXiv:quant-ph/9703048](https://arxiv.org/abs/quant-ph/9703048)).
- _parent_: [[concepts/qec/quantum-cyclic]]
- _parent_: [[concepts/qec/small-distance-quantum]]
- _cousin_: [[concepts/qec/graph-quantum]] — The $⟦5,1,3⟧_{\mathbb{Z}_q}$ code admits a graph-quantum-code realization for $G=\mathbb{Z}_q$  ([arXiv:quant-ph/0012111](https://arxiv.org/abs/quant-ph/0012111)).
