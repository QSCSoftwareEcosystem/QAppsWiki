---
type: concept
name: $⟦4,2,2⟧_{G}$ four group-qudit code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/covariant
- concepts/qec/group-quantum-parity
- concepts/qec/iceberg
- concepts/qec/quantum-concatenated
- concepts/qec/quantum-double
- concepts/qec/small-distance-quantum
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/group_4_2_2
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: group_4_2_2
---

# $⟦4,2,2⟧_{G}$ four group-qudit code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/group_4_2_2) (`code_id: group_4_2_2`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

$⟦4,2,2⟧_{G}$ group quantum code that is an extension of the four-qubit code to group-valued qudits.

For elements $g_1, g_2$ of any finite group $G$, a set of codewords is
\begin{align}
  |\overline{g_{1},g_{2}}\rangle=\frac{1}{\sqrt{|G|}}\sum_{g\in G}|g,gg_{1},gg_{2},gg_{1}g_{2}\rangle~.
\end{align}

See Ref.  ([arXiv:2406.02444](https://arxiv.org/abs/2406.02444)) for a $⟦4,1,2⟧_{\mathbb{Z}_q}$ subcode.

(source: raw/error-correction-zoo.md)

## Relations

- _parent_: [[concepts/qec/quantum-double]] — The four group-qudit code is the smallest quantum double code.
- _parent_: [[concepts/qec/covariant]] — The four group-qudit code is $(G\times G)$-covariant, with transversal logical left and right multiplication gates  ([arXiv:1902.07714](https://arxiv.org/abs/1902.07714)).
- _parent_: [[concepts/qec/small-distance-quantum]]
- _cousin_: [[concepts/qec/iceberg]] — The four group-qudit code can be extended to the $⟦2m,2m-2,2⟧_{G}$ group-qudit code  ([arXiv:1902.07714](https://arxiv.org/abs/1902.07714)). The latter reduces to the $⟦2m,2m-2,2⟧$ error-detecting code for $G=\mathbb{Z}_2$.
- _cousin_: [[concepts/qec/group-quantum-parity]] — The $|\overline{g_1=1,g_2}\rangle$ $⟦4,1,2⟧_{G}$ subcode is the smallest group-based QPC, i.e., a concatenation of a bit-flip with a phase-flip group-based repetition code for that group.
- _cousin_: [[concepts/qec/quantum-concatenated]] — The $|\overline{g_1=1,g_2}\rangle$ $⟦4,1,2⟧_{G}$ subcode is the smallest group-based QPC, i.e., a concatenation of a bit-flip with a phase-flip group-based repetition code for that group.
