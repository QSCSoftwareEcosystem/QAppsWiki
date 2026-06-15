---
type: concept
name: Coherent-state constellation code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/oscillators
- concepts/qec/oscillators-concatenated
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/coherent_constellation
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: coherent_constellation
---

# Coherent-state constellation code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/coherent_constellation) (`code_id: coherent_constellation`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Qudit-into-oscillator code whose codewords can succinctly be expressed as superpositions of a countable set of coherent states that is called a *constellation*. Some useful constellations form a group (see gkp, cat or $2T$-qutrit codes) while others make up a Gaussian quadrature rule  ([arXiv:1603.05970](https://arxiv.org/abs/1603.05970), [doi:10.1109/ISIT.2016.7541749](https://doi.org/10.1109/ISIT.2016.7541749)).

(source: raw/error-correction-zoo.md)

## Rate

Coherent-state constellation codes consisting of points from a Gaussian quadrature rule can be concatenated with quantum polar codes to achieve the Gaussian coherent information of the thermal noise channel  ([arXiv:1603.05970](https://arxiv.org/abs/1603.05970), [doi:10.1109/ISIT.2016.7541749](https://doi.org/10.1109/ISIT.2016.7541749)).

## Relations

- _parent_: [[concepts/qec/oscillators]]
- _cousin_: [[concepts/qec/oscillators-concatenated]] — Coherent-state constellation codes consisting of points from a Gaussian quadrature rule can be concatenated with quantum polar codes to achieve the Gaussian coherent information of the thermal noise channel  ([arXiv:1603.05970](https://arxiv.org/abs/1603.05970), [doi:10.1109/ISIT.2016.7541749](https://doi.org/10.1109/ISIT.2016.7541749)).
- _cousin_: [`t-designs`](https://errorcorrectionzoo.org/c/t-designs) — Coherent-state constellation codes consisting of points from a Gaussian quadrature rule can be concatenated with quantum polar codes to achieve the Gaussian coherent information of the thermal noise channel  ([arXiv:1603.05970](https://arxiv.org/abs/1603.05970), [doi:10.1109/ISIT.2016.7541749](https://doi.org/10.1109/ISIT.2016.7541749)).
- _cousin_: [`modulation`](https://errorcorrectionzoo.org/c/modulation) — Coherent-state constellation codes are quantum counterparts of modulation schemes in that their codewords are superpositions of points in a constellation. Additionally, analog codes that achieve AWGN capacity  ([doi:10.1109/ALLERTON.2010.5706965](https://doi.org/10.1109/ALLERTON.2010.5706965)) can be used to develop capacity-achieving concatenations of coherent-state constellation codes with quantum polar codes  ([arXiv:1603.05970](https://arxiv.org/abs/1603.05970), [doi:10.1109/ISIT.2016.7541749](https://doi.org/10.1109/ISIT.2016.7541749)).
