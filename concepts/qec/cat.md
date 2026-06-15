---
type: concept
name: Cat code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Superposition of coherent states (SCS)
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/bosonic-rotation
- concepts/qec/cat-repetition
- concepts/qec/group-representation
- concepts/qec/number-phase
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/cat
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: cat
---

# Cat code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/cat) (`code_id: cat`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Rotation-symmetric bosonic Fock-state code encoding a $q$-dimensional qudit into one oscillator which utilizes a constellation of $q(S+1)$ coherent states distributed equidistantly around a circle in phase space of radius $\alpha$.

Codewords for a qubit code ($q=2$) consist of a coherent state $|\alpha\rangle$ projected onto a subspace of Fock state number modulo $2(S+1)$. The logical state $|\overline{0}\rangle$ is in the $\{|0\rangle , |2(S+1)\rangle , |4(S+1)\rangle \cdots \}$ Fock-state subspace, while $|\overline{1}\rangle$ is in the $\{|(S+1)\rangle, |3(S+1)\rangle , |5(S+1)\rangle , |7(S+1)\rangle \cdots \}$ subspace.
These projected coherent states make up generalized cat states  ([doi:10.1016/0031-8914(74)90215-8](https://doi.org/10.1016/0031-8914(74)90215-8), [doi:10.1007/BF02581033](https://doi.org/10.1007/BF02581033)).

(source: raw/error-correction-zoo.md)

## Protection

Due to the spacing between sets of Fock states, the distance between two distinct logical states is $d=S+1$. Hence, this code is able to detect up to $S$ photon-loss errors.

## Encoders

- Lindbladian-based dissipative encoding and autonomous QEC utilizing multi-photon generalization of two-photon absorption  ([doi:10.1103/PhysRevLett.60.1836](https://doi.org/10.1103/PhysRevLett.60.1836), [doi:10.1103/PhysRevA.50.4330](https://doi.org/10.1103/PhysRevA.50.4330), [doi:10.1103/PhysRevA.49.490](https://doi.org/10.1103/PhysRevA.49.490), [doi:10.1103/PhysRevA.49.2785](https://doi.org/10.1103/PhysRevA.49.2785)). Encoding passively protects against modal dephasing, suppressing dephasing noise exponentially with $|\alpha|^2$  ([arXiv:1312.2017](https://arxiv.org/abs/1312.2017)).
- Approximate cat states can be prepared using Gaussian operations and photon detectors  ([arXiv:1902.02323](https://arxiv.org/abs/1902.02323)).

## General gates

- Holonomic gates utilizing the Berry phase of coherent states are universal  ([arXiv:1503.00194](https://arxiv.org/abs/1503.00194)).
- Universal gates for the $S=1$ code can be performed using squeezing operators and quantum Zeno effect and a rotation based on the Kerr nonlinearity  ([arXiv:1312.2017](https://arxiv.org/abs/1312.2017)).
- Error-detecting $CCZ$ and $cSWAP$ gates for four-component cat code using three-level ancilla  ([arXiv:2212.11196](https://arxiv.org/abs/2212.11196)).
- Universal set of error-corrected operations tolerating a single photon loss and an arbitrary ancilla fault  ([arXiv:2310.20578](https://arxiv.org/abs/2310.20578)).

## Decoders

- Measuring the Fock-state number modulo $S+1$ can be used to determine if photon-loss or excitation errors occurred. For $S=1$, this is the occupation number parity  ([arXiv:1901.08071](https://arxiv.org/abs/1901.08071)).

## Fault tolerance

- Universal set of error-corrected operations tolerating a single photon loss and an arbitrary ancilla fault  ([arXiv:2310.20578](https://arxiv.org/abs/2310.20578)).
- Linear-optical noise suppression and mitigation scheme  ([arXiv:2411.11313](https://arxiv.org/abs/2411.11313)).

## Realizations

- Parity-syndrome measurement tested  ([arXiv:1311.2534](https://arxiv.org/abs/1311.2534)) and implemented for the four-component ($S=1$) cat code  ([arXiv:1602.04768](https://arxiv.org/abs/1602.04768)) in a microwave cavity coupled to a superconducting circuit. The latter work  ([arXiv:1602.04768](https://arxiv.org/abs/1602.04768)) is the first to reach break-even error-correction, where the lifetime of a logical qubit is on par with the cavity lifetime, despite protection against dephasing not being implemented. A fault-tolerant version of parity measurement has also been realized  ([arXiv:1803.00102](https://arxiv.org/abs/1803.00102)).

## Relations

- _parent_: [[concepts/qec/bosonic-rotation]] — The cat code is a bosonic rotation code whose primitive state is the coherent state $|\alpha\rangle$  ([arXiv:1901.08071](https://arxiv.org/abs/1901.08071)).
- _parent_: [[concepts/qec/cat-repetition]] — The cat-repetition code for $n=1$ reduces to the cat code.
- _cousin_: [[concepts/qec/number-phase]] — In the limit as $N,S \to \infty$, phase measurement in the cat code has vanishing variance, just like in a number-phase code  ([arXiv:1901.08071](https://arxiv.org/abs/1901.08071)). Conversely, a cat code can be thought of as an appropriately regularized number-phase code.
- _cousin_: [[concepts/qec/group-representation]] — Cat codes are not group representation codes with $G$ being a cyclic group since their representation is reducible  ([arXiv:2306.11621](https://arxiv.org/abs/2306.11621)).
