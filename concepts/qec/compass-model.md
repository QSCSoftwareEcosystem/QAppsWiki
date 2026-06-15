---
type: concept
name: Compass code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/asymmetric-qecc
- concepts/qec/clifford-deformed-surface
- concepts/qec/quantum-parity
- concepts/qec/qubit-subsystem-css
- concepts/qec/random-stabilizer
- concepts/qec/rotated-surface
- concepts/qec/translationally-invariant-subsystem
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/compass_model
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: compass_model
---

# Compass code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/compass_model) (`code_id: compass_model`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Subspace or subsystem CSS code defined by gauge-fixing the Bacon-Shor code, i.e., the code whose gauge group consists of terms in the compass model Hamiltonian  ([doi:10.1070/PU1982v025n04ABEH004537](https://doi.org/10.1070/PU1982v025n04ABEH004537), [arXiv:cond-mat/0501708](https://arxiv.org/abs/cond-mat/0501708), [arXiv:1303.5922](https://arxiv.org/abs/1303.5922)) on a square lattice.
Families of random codes perform well against biased noise and spatially dependent (i.e., asymmetric) noise.

The gauge fixing proceeds by denoting plaquettes by $X$ or $Z$ type using two colors, and fixing or *cutting* the corresponding $X$ or $Z$-type gauge generators at the respective plaquettes.
A fully colored lattice yields a subspace code, but allowing for non-colored plaquettes yields a subsystem code.
A fully non-colored lattice reduces to the Bacon-Shor code.

The *surface-density* compass code family is obtained by randomly cutting $X$-type stabilizers at only plaquettes of one color in a checkerboard coloring; it interpolates between Bacon-Shor codes and rotated surface codes.
The *Shor-density* compass code family is obtained by randomly cutting $X$-type stabilizers at any plaquette; it interpolates between Bacon-Shor codes and QPCs.

(source: raw/error-correction-zoo.md)

## Protection

Provides some protection against coherent noise  ([arXiv:2405.09287](https://arxiv.org/abs/2405.09287)).

## Decoders

- Asymmetrically-weighted variant of the union-find decoder  ([arXiv:1809.01193](https://arxiv.org/abs/1809.01193)).

## Code capacity threshold

- See  ([arXiv:1809.01193](https://arxiv.org/abs/1809.01193)) for tables of code-capacity thresholds against spatially dependent and biased noise.

## Relations

- _parent_: [[concepts/qec/qubit-subsystem-css]]
- _parent_: [[concepts/qec/translationally-invariant-subsystem]]
- _cousin_: [[concepts/qec/rotated-surface]] — The surface-density compass code family interpolates between Bacon-Shor codes and rotated surface codes.
- _cousin_: [[concepts/qec/quantum-parity]] — The Shor-density compass code family interpolates between Bacon-Shor codes and QPCs.
- _cousin_: [[concepts/qec/random-stabilizer]] — Compass code families are constructed by randomly assigning stabilizers to plaquettes of a square lattice.
- _cousin_: [[concepts/qec/clifford-deformed-surface]] — Clifford deformation can enhance the performance of compass codes against biased noise  ([arXiv:2412.03808](https://arxiv.org/abs/2412.03808)).
- _cousin_: [[concepts/qec/asymmetric-qecc]] — Families of random compass codes perform well against biased noise and spatially dependent (i.e., asymmetric) noise  ([arXiv:1809.01193](https://arxiv.org/abs/1809.01193)).
Clifford deformation can enhance the performance of compass codes against biased noise  ([arXiv:2412.03808](https://arxiv.org/abs/2412.03808)).
