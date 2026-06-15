---
type: concept
name: Squeezed Fock-state code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/ampdamp
- concepts/qec/single-mode
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/squeezed_fock_state
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: squeezed_fock_state
---

# Squeezed Fock-state code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/squeezed_fock_state) (`code_id: squeezed_fock_state`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Approximate bosonic code that encodes a qubit into a superposition of one or a few squeezed Fock states, some of which are the result of a photon-number resolving measurement  ([arXiv:2509.16993](https://arxiv.org/abs/2509.16993)).

The simplest code encodes a qubit into the same Fock state, but one which is squeezed in opposite directions  ([arXiv:2312.16000](https://arxiv.org/abs/2312.16000)).
Taking the Fock state $|1\rangle$, the codewords are
\begin{align}
\begin{split}
|\overline{0}\rangle&=S(r)|1\rangle \\
|\overline{1}\rangle&=S(-r)|1\rangle~,
\end{split}
\end{align}
where $S(\pm r)$ is the squeezing operator with squeezing parameter $\pm r$.

(source: raw/error-correction-zoo.md)

## Protection

The code approximately protects against loss and dephasing errors, becoming exact in the $r\to\infty$ limit.

## Relations

- _parent_: [[concepts/qec/single-mode]]
- _parent_: [[concepts/qec/ampdamp]] — The squeezed Fock-state code approximately protects against loss and dephasing errors, becoming exact in the $r\to\infty$ limit.
