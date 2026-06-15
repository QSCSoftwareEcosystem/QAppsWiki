---
type: concept
name: Quantum quadratic-residue (QR) code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/galois-css
- concepts/qec/galois-duadic
- concepts/qec/quantum-divisible
- concepts/qec/quantum-mds
- concepts/qec/quantum-triorthogonal
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/galois_quad_residue
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: galois_quad_residue
---

# Quantum quadratic-residue (QR) code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/galois_quad_residue) (`code_id: galois_quad_residue`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Galois-qudit $⟦n,1⟧_q$ pure self-dual Galois-qudit CSS code constructed from a dual-containing QR code via the Galois-qudit CSS construction.
For $q$ not divisible by $n$, its distance satisfies $d^2-d+1 \geq n$ when $n \equiv 3$ modulo 4  ([arXiv:quant-ph/0508070](https://arxiv.org/abs/quant-ph/0508070)) and $d \geq \sqrt{n}$ when $n\equiv 1$ modulo 4  ([arXiv:quant-ph/0508070](https://arxiv.org/abs/quant-ph/0508070)).

(source: raw/error-correction-zoo.md)

## Protection

For qubit quantum QR codes obtained from extended binary QR codes, explicit examples satisfy $n \leq d^2-d+1$ and $d \leq 4\lfloor (n+1)/24 \rfloor + 3$  ([arXiv:2408.12752](https://arxiv.org/abs/2408.12752)).

## Transversal gates

- Qubit quantum QR codes admit transversal implementations of the single-qubit Clifford group  ([arXiv:2408.12752](https://arxiv.org/abs/2408.12752)). They yield a family of high-distance triorthogonal codes  ([arXiv:2408.12752](https://arxiv.org/abs/2408.12752)) via the doubling transformation  ([arXiv:1509.03239](https://arxiv.org/abs/1509.03239)); such codes admit transversal implementations of the $T$ gate.

## Relations

- _parent_: [[concepts/qec/galois-css]]
- _parent_: [[concepts/qec/galois-duadic]] — Quantum QR codes are quantum duadic codes since QR codes are duadic codes.
- _cousin_: [`q-ary_quad_residue`](https://errorcorrectionzoo.org/c/q-ary_quad_residue) — Quantum quadratic-residue codes are quantum analogues of $q$-ary quadratic-residue codes.
- _cousin_: [[concepts/qec/quantum-mds]] — Almost all quantum QR codes for prime-dimensional qudits are quantum MDS  ([arXiv:quant-ph/9703048](https://arxiv.org/abs/quant-ph/9703048)).
- _cousin_: [[concepts/qec/quantum-triorthogonal]] — Qubit quantum QR codes are doubly even and admit transversal implementations of the single-qubit Clifford group  ([arXiv:2408.12752](https://arxiv.org/abs/2408.12752)). They yield a family of high-distance triorthogonal and weak triply even codes via the doubling transformation  ([arXiv:2408.12752](https://arxiv.org/abs/2408.12752)); such codes admit transversal implementations of the $T$ gate.
- _cousin_: [[concepts/qec/quantum-divisible]] — Qubit quantum QR codes are doubly even and admit transversal implementations of the single-qubit Clifford group  ([arXiv:2408.12752](https://arxiv.org/abs/2408.12752)). They yield a family of high-distance triorthogonal and weak triply even codes via the doubling transformation  ([arXiv:2408.12752](https://arxiv.org/abs/2408.12752)); such codes admit transversal implementations of the $T$ gate.
