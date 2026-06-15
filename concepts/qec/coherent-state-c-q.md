---
type: concept
name: Coherent-state c-q modulation format
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Coherent-state c-q modulation code
- Coherent-state c-q modulation scheme
- Coherent-state c-q signaling format
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/bosonic-classical-into-quantum
- concepts/qec/coherent-constellation
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/coherent_state_c-q
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: coherent_state_c-q
---

# Coherent-state c-q modulation format

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/coherent_state_c-q) (`code_id: coherent_state_c-q`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Bosonic c-q code whose codewords form a constellation of coherent states.
Encodes classical symbols into coherent states for transmission over a quantum channel and decoding with a quantum-enhanced *receiver*.

The code consists of $K$ coherent states on $n$ modes, where the $j$th state, or codeword, is uniquely defined through the amplitude vector $\boldsymbol{\alpha}^j=(\alpha_1^j, \alpha_2^j, \cdots, \alpha_n^j)$.
The *codebook*,
\begin{align}
C=\left(\begin{array}{c}
\boldsymbol{\alpha}^{1}\\
\vdots\\
\boldsymbol{\alpha}^{K}
\end{array}\right)=\left(\begin{array}{cccc}
\alpha_{1}^{1} & \alpha_{2}^{1} & \dots & \alpha_{n}^{1}\\
\vdots & \vdots & \ddots & \vdots\\
\alpha_{1}^{K} & \alpha_{2}^{K} & \dots & \alpha_{n}^{K}
\end{array}\right)~,
\end{align}
collects each codeword into the matrix $C$ that characterizes the system of states to discriminate.

From the properties of $C$, we can assess whether it is possible to discriminate the codebook unambiguously.
For a finite constellation, unambiguous state discrimination is possible only if the coherent states in the codebook are linearly independent.

(source: raw/error-correction-zoo.md)

## Rate

Random Gaussian-distributed coherent-state c-q codes achieve the capacity of the pure-loss bosonic channel  ([arXiv:quant-ph/0308012](https://arxiv.org/abs/quant-ph/0308012)).

## Decoders

- Optimal receiver performance in ambiguous state discrimination is determined using the *Yuen-Kennedy-Lax (YKL) conditions*  ([doi:10.1109/TIT.1975.1055351](https://doi.org/10.1109/TIT.1975.1055351)). See review  ([doi:10.1116/5.0036959](https://doi.org/10.1116/5.0036959)) for details on receivers used for coherent-state c-q codes.
- Joint-detection receiver that can attain channel capacity  ([arXiv:1101.1550](https://arxiv.org/abs/1101.1550)).
- Various near-optimal receiver designs that can handle arbitrary constellations of coherent states with possible degeneracies  ([arXiv:2109.00008](https://arxiv.org/abs/2109.00008)).
- The *square-root measurement* (a.k.a. pretty good measurement)  ([doi:10.1080/17442507508833114](https://doi.org/10.1080/17442507508833114), [doi:10.1137/1123048](https://doi.org/10.1137/1123048), [doi:10.1080/09500349414552221](https://doi.org/10.1080/09500349414552221)) is optimal for geometrically uniform  ([arXiv:quant-ph/0005132](https://arxiv.org/abs/quant-ph/0005132), [arXiv:quant-ph/0211111](https://arxiv.org/abs/quant-ph/0211111), [arXiv:2203.09822](https://arxiv.org/abs/2203.09822), [arXiv:2501.12376](https://arxiv.org/abs/2501.12376)), direct sums of geometrically uniform  ([arXiv:1504.04908](https://arxiv.org/abs/1504.04908)), and compound geometrically uniform  ([arXiv:1507.04737](https://arxiv.org/abs/1507.04737)) constellations.

## Realizations

- Continuous-variable quantum key distribution (CV-QKD)  ([arXiv:quant-ph/9907073](https://arxiv.org/abs/quant-ph/9907073), [arXiv:quant-ph/0109084](https://arxiv.org/abs/quant-ph/0109084), [arXiv:quant-ph/0312016](https://arxiv.org/abs/quant-ph/0312016)).

## Relations

- _parent_: [[concepts/qec/bosonic-classical-into-quantum]]
- _cousin_: [[concepts/qec/coherent-constellation]] — Coherent-state c-q codes encode classical alphabets into constellations of coherent states, while coherent-state constellation codes encode quantum information into superpositions of coherent states.

## Notes

- See book  ([doi:10.1002/9783527628285](https://doi.org/10.1002/9783527628285)).
