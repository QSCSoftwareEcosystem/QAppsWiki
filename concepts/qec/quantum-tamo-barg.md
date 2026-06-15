---
type: concept
name: Quantum Tamo-Barg (QTB) code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/galois-css
- concepts/qec/quantum-locally-recoverable
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/quantum_tamo_barg
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: quantum_tamo_barg
---

# Quantum Tamo-Barg (QTB) code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/quantum_tamo_barg) (`code_id: quantum_tamo_barg`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A member of a family of Galois-qudit CSS codes whose underlying classical codes consist of Tamo-Barg codes together with specific low-weight codewords.
Folded versions of QTB codes, or *FQTB codes*, defined on qudits whose dimension depends on $n$, yield explicit examples of QLRCs of arbitrary locality $r$  ([arXiv:2311.08653](https://arxiv.org/abs/2311.08653)).

(source: raw/error-correction-zoo.md)

## Protection

A family of QTBs can be defined for every prime $r$, rate $R\in(0,1)$, and qudit dimension $q = n+1$ such that their relative distance is $\delta \geq 1 - \sqrt{(1+R)/2} - O(1/r)$  ([arXiv:2311.08653](https://arxiv.org/abs/2311.08653)).

*Folding* these codes by combining qudits into larger qudits yields FQTB codes with relative distance $\delta \geq (1-R)/2 - O(1/\sqrt{r})$  ([arXiv:2311.08653](https://arxiv.org/abs/2311.08653)) and qudit dimension $q = n^{O(r^2)}$.
This relative distance is of order $O(1/\sqrt{r})$ below the Singleton-like QLRC bound.

## Decoders

- Polynomially efficient decoder for QTB codes against errors acting on a number of subsystems that can go up to half of the distance bound proved for the family  ([arXiv:2311.08653](https://arxiv.org/abs/2311.08653)). The decoder is based on decoding RS codes, and its runtime is independent of the locality $r$.
- Polynomially efficient decoder for FQTB codes against errors acting on a number of subsystems that can go up to half of the distance bound proved for the family  ([arXiv:2311.08653](https://arxiv.org/abs/2311.08653)). The runtime depends on the locality $r$.

## Relations

- _parent_: [[concepts/qec/galois-css]]
- _parent_: [[concepts/qec/quantum-locally-recoverable]] — Folded quantum Tamo-Barg codes yield explicit QLRCs of arbitrary prime locality $r$, rate at least $R$, relative distance $\delta \geq (1-R)/2 - O(1/\sqrt{r})$, and qudit dimension $q = n^{O(r^2)}$  ([arXiv:2311.08653](https://arxiv.org/abs/2311.08653)).
- _cousin_: [`tamo_barg`](https://errorcorrectionzoo.org/c/tamo_barg) — QTB codes are CSS codes constructed from Tamo-Barg codes.
