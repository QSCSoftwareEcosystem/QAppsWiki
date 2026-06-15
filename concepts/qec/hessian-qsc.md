---
type: concept
name: Hessian QSC
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/qsc
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/hessian_qsc
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: hessian_qsc
---

# Hessian QSC

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/hessian_qsc) (`code_id: hessian_qsc`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Quantum spherical code encoding a logical qubit, with each codeword an equal superposition of vertices of a Hessian complex polyhedron.

For the unit sphere, the codewords are
\begin{align}
  |\overline{0}\rangle &= \frac{1}{\sqrt{27}}\left( \sum_{\mu,\nu=0}^{2} |0,\omega^{\mu},-\omega^{\nu}\rangle + |-\omega^{\nu},0,\omega^{\mu}\rangle + |\omega^{\mu},-\omega^{\nu},0\rangle   \right) \\
  |\overline{1}\rangle &= \frac{1}{\sqrt{27}}\left( \sum_{\mu,\nu=0}^{2} |0,-\omega^{\mu},\omega^{\nu}\rangle + |\omega^{\nu},0,-\omega^{\mu}\rangle + |-\omega^{\mu},\omega^{\nu},0\rangle   \right)~,
\end{align}
where $\omega = e^{\frac{2\pi i}{3}}$.

(source: raw/error-correction-zoo.md)

## Protection

The Hessian QSC is a $\langle 4, 5, 9 \rangle$ code, i.e. it detects 8 photon losses and protects against 3. The code also detects up to 4 ladder errors (losses or gains). The code resolution $ d_E = 1.0$.

## Relations

- _parent_: [[concepts/qec/qsc]] — The Hessian QSC is an example of a QSC with logical constellation built from the Hessian complex polyhedron.
- _cousin_: [`hessian_polyhedron`](https://errorcorrectionzoo.org/c/hessian_polyhedron) — Each codeword of the Hessian QSC is a quantum superposition of vertices of a Hessian complex polyhedron.
