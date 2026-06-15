---
type: concept
name: Modular-qudit USt code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/qudits-into-qudits
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/qudit_non_stabilizer
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: qudit_non_stabilizer
---

# Modular-qudit USt code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/qudit_non_stabilizer) (`code_id: qudit_non_stabilizer`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A modular-qudit code whose codespace consists of a direct sum of a modular-qudit stabilizer codespace and one or more of that stabilizer code's error spaces.

Given a subset $T$ of coset representatives of $\mathsf{N}(\mathsf{S})/\mathsf{S}$ of a modular-qudit stabilizer code $((n,K))$ with codespace $\mathsf{C}$ and stabilizer group $\mathsf{S}$, one can construct the modular-qudit USt with codespace
\begin{align}
  \mathsf{C}_{\text{USt}}=\bigoplus_{t\in T}t\mathsf{C}~.
\end{align}
The parameters of the USt are $((n,K|T|,d))$, where $|T|$ is the number of chosen coset representatives.
A modular-qudit USt is *CSS-like* when the underlying stabilizer code is CSS.

(source: raw/error-correction-zoo.md)

## Relations

- _parent_: [[concepts/qec/qudits-into-qudits]]
