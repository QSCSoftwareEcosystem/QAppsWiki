---
type: concept
name: Hyperbolic Floquet code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/floquet
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/hyperbolic_floquet
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: hyperbolic_floquet
---

# Hyperbolic Floquet code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/hyperbolic_floquet) (`code_id: hyperbolic_floquet`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Floquet code whose check-operators correspond to edges of a hyperbolic lattice of degree 3.

(source: raw/error-correction-zoo.md)

## Protection

Code distance is at most $O(\log n)$ due to the hyperbolic qubit geometry  ([arXiv:2110.05348](https://arxiv.org/abs/2110.05348)), but semi-hyperbolic lattices yield $O(\sqrt{n})$ distance  ([arXiv:2308.03750](https://arxiv.org/abs/2308.03750)).

A useful concept is the *embedded distance*  ([arXiv:2308.03750](https://arxiv.org/abs/2308.03750)), which is the distance of the stabilizer code lying inside the subspace defined by measurement outcomes of the weight-two parity checks of the code.

## Rate

Finite encoding rate whose value depends on the hyperbolic lattice. The asymptotic rate is 1/8 for a lattice of octagons  ([arXiv:2309.10033](https://arxiv.org/abs/2309.10033)).

## Decoders

- Syndrome structure allows for MWPM decoding.

## Threshold

- $0.1\%$ under standard circuit-level depolarizing noise  ([arXiv:2308.03750](https://arxiv.org/abs/2308.03750)).
- $0.1\%$ under phenomenological error model including depolarizing and measurement errors for the octagonal codes  ([arXiv:2309.10033](https://arxiv.org/abs/2309.10033)).

## Relations

- _parent_: [[concepts/qec/floquet]]

## Notes

- The code may be suitable for distributed storage  ([arXiv:2501.14029](https://arxiv.org/abs/2501.14029)).
