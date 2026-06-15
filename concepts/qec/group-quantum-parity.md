---
type: concept
name: Group-based QPC
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/group-quantum
- concepts/qec/quantum-concatenated
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/group_quantum_parity
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: group_quantum_parity
---

# Group-based QPC

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/group_quantum_parity) (`code_id: group_quantum_parity`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

An $⟦m r,1,\min(m,r)⟧_G$ generalization of the QPC.

Logical codewords for each group element $g$ are
\begin{align}
  |\overline{g}\rangle=\left({\textstyle \frac{1}{\sqrt{|G|^{m-1}}}}\sum_{h_{1},h_{2},\cdots,h_{m}\in G}\delta^{G}_{g,h_{1}h_{2}\cdots h_{m}}|h_{1},h_{2},\cdots,h_{m}\rangle\right)^{\otimes r}~.
\end{align}
where $\delta^{G}_{g,h}$ is the group Kronecker-delta function.
For non-compact groups, the sum becomes an integral, and ideal codewords are no longer normalizable.

(source: raw/error-correction-zoo.md)

## Relations

- _parent_: [[concepts/qec/group-quantum]]
- _parent_: [[concepts/qec/quantum-concatenated]] — A group-based QPC is a concatenation of a phase-flip group-based repetition code with a bit-flip group-based repetition code.
