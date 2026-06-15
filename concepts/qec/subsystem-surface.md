---
type: concept
name: Subsystem surface code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/subsystem-higher-dimensional-surface
- concepts/qec/surface
- concepts/qec/translationally-invariant-subsystem
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/subsystem_surface
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: subsystem_surface
---

# Subsystem surface code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/subsystem_surface) (`code_id: subsystem_surface`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Subsystem version of the surface code defined on a square lattice with qubits placed at every vertex and center of every edge.
Its gauge checks are weight-three triangle operators of type $XXX$ and $ZZZ$  ([arXiv:1207.1443](https://arxiv.org/abs/1207.1443)).

For example, a $⟦3L^2,2,L⟧$ family has weight-six $X,Z$-type stabilizers supported on two of the four triangles of each plaquette.

(source: raw/error-correction-zoo.md)

## Fault tolerance

- Gauge fixing and changing the order in which check operators are measured yields a fault-tolerant decoder  ([arXiv:2010.09626](https://arxiv.org/abs/2010.09626)).

## Code capacity threshold

- Independent $X,Z$ noise: the threshold under ML decoding corresponds to the value of a critical point of the two-dimensional hexagonal-lattice random-bond Ising model (RBIM) on the Nishimori line  ([doi:10.1143/JPSJ.55.3305](https://doi.org/10.1143/JPSJ.55.3305), [arXiv:1207.1443](https://arxiv.org/abs/1207.1443)), calculated to be around $7\%$ in Ref.  ([arXiv:cond-mat/0510816](https://arxiv.org/abs/cond-mat/0510816)).

## Threshold

- $0.81\%$ threshold for circuit-level depolarizing noise under a variant of MWPM and using gauge-fixing and specific measurement schedules  ([arXiv:2010.09626](https://arxiv.org/abs/2010.09626)), improving the $0.67\%$ threshold for standard measurement schedules  ([arXiv:1207.1443](https://arxiv.org/abs/1207.1443)).
- $2.22\%$ threshold for circuit-level infinitely biased noise under a variant of MWPM and using gauge-fixing and specific measurement schedules  ([arXiv:2010.09626](https://arxiv.org/abs/2010.09626)), improving the $0.52\%$ threshold with standard measurement schedules.

## Relations

- _parent_: [[concepts/qec/subsystem-higher-dimensional-surface]]
- _parent_: [[concepts/qec/translationally-invariant-subsystem]]
- _cousin_: [[concepts/qec/surface]] — Subsystem surface codes are subsystem versions of surface codes.

## Notes

- See  ([arXiv:1302.3428](https://arxiv.org/abs/1302.3428)) for an exposition.
