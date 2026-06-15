---
type: concept
name: On-off keyed (OOK) c-q modulation format
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- On-off keyed (OOK) c-q modulation code
- On-off keyed (OOK) c-q modulation scheme
- On-off keyed (OOK) c-q signaling format
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/coherent-state-c-q
- concepts/qec/quantum-bpsk
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/quantum_ook
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: quantum_ook
---

# On-off keyed (OOK) c-q modulation format

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/quantum_ook) (`code_id: quantum_ook`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Coherent-state c-q binary code whose encoding is either in the vacuum $|0\rangle$ or in a nonzero coherent state $|\alpha\rangle$.

(source: raw/error-correction-zoo.md)

## Protection

For equal priors on the binary alphabet $\{|0\rangle,|\alpha\rangle\}$, the minimum error probability is given by the Helstrom expression
\begin{align}
  P_{\mathrm{err}}^{\star}=\frac{1}{2}\left(1-\sqrt{1-e^{-|\alpha|^2}}\right)~,
\end{align}
since $|\langle 0|\alpha\rangle|^2=e^{-|\alpha|^2}$.
The mean photon number of the non-vacuum symbol is $|\alpha|^2$.

## Decoders

- Dolinar receiver , which attains the Helstrom limit in the ideal model and has been demonstrated in proof-of-principle experiments  ([doi:10.1038/nature05655](https://doi.org/10.1038/nature05655)).
- Superconducting transition edge sensor (TES) photon-number resolving detector  ([arXiv:1002.2819](https://arxiv.org/abs/1002.2819)).

## Realizations

- Proof-of-principle experiments using Dolinar  ([doi:10.1038/nature05655](https://doi.org/10.1038/nature05655)) and TES receivers  ([arXiv:1002.2819](https://arxiv.org/abs/1002.2819)).

## Relations

- _parent_: [[concepts/qec/coherent-state-c-q]]
- _cousin_: [[concepts/qec/quantum-bpsk]] — OOK c-q codewords are related to BPSK c-q codewords by a displacement in phase space.
