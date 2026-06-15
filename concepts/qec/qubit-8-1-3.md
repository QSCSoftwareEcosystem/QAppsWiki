---
type: concept
name: $((8,2,3))$ Plenio-Vedral-Knight CE code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/constant-excitation
- concepts/qec/qubits-into-qubits
- concepts/qec/small-distance-quantum
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/qubit_8_1_3
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: qubit_8_1_3
---

# $((8,2,3))$ Plenio-Vedral-Knight CE code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/qubit_8_1_3) (`code_id: qubit_8_1_3`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

An eight-qubit single-error-correcting code that is the first CE code.
Each logical state is a superposition of computational basis states with four excitations.

Admits codewords of the form
\begin{align}
\begin{split}
  |\overline{0}\rangle&=(|00001111\rangle+|11101000\rangle−|10010110\rangle−|01110001\rangle\\&+|11010100\rangle+|00110011\rangle+|01001101\rangle+|10101010\rangle)/\sqrt{8}\\
  |\overline{1}\rangle&=X^{\otimes8}|\overline{0}\rangle~.
\end{split}
\end{align}

(source: raw/error-correction-zoo.md)

## Relations

- _parent_: [[concepts/qec/qubits-into-qubits]]
- _parent_: [[concepts/qec/constant-excitation]]
- _parent_: [[concepts/qec/small-distance-quantum]]
