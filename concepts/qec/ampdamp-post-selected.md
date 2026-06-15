---
type: concept
name: Post-selected PI code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/ampdamp
- concepts/qec/qubit-permutation-invariant
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/ampdamp_post_selected
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: ampdamp_post_selected
---

# Post-selected PI code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/ampdamp_post_selected) (`code_id: ampdamp_post_selected`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

PI qubit code whose recovery succeeds at protecting against AD errors with a success probability less than one.

The simplest code admits a codeword basis of
\begin{align}
\begin{split}
|\overline{0}\rangle&=\frac{1}{\sqrt{3}}\left(|100\rangle+|010\rangle+|001\rangle\right)\\
|\overline{1}\rangle&=|111\rangle~.
\end{split}
\end{align}
The code violates the diagonal part of the \term{Knill-Laflamme conditions}.
Nevertheless, the code admits a probabilistic recovery that protects against single losses and yields an infidelity of order $O(\gamma^2)$ in the noise rate $\gamma$.
The failure probability of the recovery is of the same order as the probability of the single loss errors, i.e., $O(\gamma)$.

(source: raw/error-correction-zoo.md)

## Realizations

- Superconducting circuits: IBM quantum hardware  ([arXiv:2603.04564](https://arxiv.org/abs/2603.04564)).

## Relations

- _parent_: [[concepts/qec/qubit-permutation-invariant]]
- _parent_: [[concepts/qec/ampdamp]]
