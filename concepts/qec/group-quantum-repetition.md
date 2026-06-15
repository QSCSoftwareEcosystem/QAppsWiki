---
type: concept
name: Group-based quantum repetition code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/group-quantum-parity
- concepts/qec/quantum-cyclic
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/group_quantum_repetition
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: group_quantum_repetition
---

# Group-based quantum repetition code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/group_quantum_repetition) (`code_id: group_quantum_repetition`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

An $⟦n,1⟧_G$ generalization of the quantum repetition code.

The code encodes one group-valued qudit into $n$.
There are two variants, a bit- and a phase-flip code, whose codewords for any $g\in G$ and for $n=3$ are
\begin{align}
  |\overline{g}_{\text{bit}}\rangle&\rightarrow|g,g,g\rangle\\
  |\overline{g}_{\text{phase}}\rangle&\rightarrow\frac{1}{|G|}\sum_{h_{1},h_{2},h_{3}\in G}\delta^{G}_{g,h_{1}h_{2}h_{3}}|h_{1},h_{2},h_{3}\rangle~,
\end{align}
where $\delta^{G}_{g,h}$ is the group Kronecker-delta function.
For non-compact groups, the sum becomes an integral, and ideal codewords are no longer normalizable.

(source: raw/error-correction-zoo.md)

## Relations

- _parent_: [[concepts/qec/group-quantum-parity]] — A $⟦m_1 m_2,1,\min(m_1,m_2)⟧_G$ group-based QPC reduces to a group-based quantum repetition code when $m_1$ or $m_2$ is one.
- _parent_: [[concepts/qec/quantum-cyclic]]
