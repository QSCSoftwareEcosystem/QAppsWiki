---
type: concept
name: $⟦23, 1, 7⟧$ Quantum Golay code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Qubit Golay code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/data-syndrome
- concepts/qec/galois-quad-residue
- concepts/qec/quantum-triorthogonal
- concepts/qec/qutrit-golay
- concepts/qec/self-dual-css
- concepts/qec/small-distance-qubit-stabilizer
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/qubit_golay
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: qubit_golay
---

# $⟦23, 1, 7⟧$ Quantum Golay code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/qubit_golay) (`code_id: qubit_golay`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A $⟦23, 1, 7⟧$ self-dual CSS code with eleven stabilizer generators of each type, and with each generator being weight eight.

The code's 11-by-23 stabilizer generator matrix blocks $H_{X}$ and $H_{Z}$ are both parity-check matrices of the classical Golay code.
Equivalently, it can be obtained from the $[24,12,8]$ extended Golay code by shortening on one bit to a self-orthogonal $[23,11,7]$ code  ([arXiv:1703.07847](https://arxiv.org/abs/1703.07847)).
It can be punctured twice to obtain a $⟦21,3,5⟧$ code  ([arXiv:1703.07847](https://arxiv.org/abs/1703.07847)).

The automorphism group of the code is $M_{23}$  ([arXiv:2109.12735](https://arxiv.org/abs/2109.12735)).

(source: raw/error-correction-zoo.md)

## Protection

Detects up to 6-qubit errors and corrects up to 3-qubit errors.

## Encoders

- Fault-tolerant depth-7 circuit consisting of 57 CNOT gates and preparing a logical-zero state  ([arXiv:1106.2190](https://arxiv.org/abs/1106.2190)).
- Circuit with 56 entangling gates using reinforcement learning  ([arXiv:2503.14660](https://arxiv.org/abs/2503.14660)).

## Magic scaling exponent

Magic-state distillation scaling exponent $\gamma=\log_2 23 \approx 4.52$ ([arXiv:2003.02717](https://arxiv.org/abs/2003.02717)).

## Transversal gates

- Single-qubit Clifford group by choosing $\overline{U}=U^{\otimes 23}$ for every Clifford unitary $U$  ([arXiv:1106.2190](https://arxiv.org/abs/1106.2190)).

## General gates

- The Golay code can be used to perform magic-state distillation for the magic state defined as $|T\rangle\langle T|=\frac{1}{2}(I+\frac{1}{\sqrt{3}}(X+Y+Z) )$, where $|T\rangle$ is an eigenstate of the Clifford "facet" gate $SH$  ([arXiv:quant-ph/0411036](https://arxiv.org/abs/quant-ph/0411036)).
- Pipelining the $⟦23,1,7⟧$ code after $⟦7,1,3⟧$ and $⟦17,1,5⟧$ inner-code stages yields a 95-to-1 seventh-order magic-state distillation protocol  ([arXiv:1703.07847](https://arxiv.org/abs/1703.07847)).

## Decoders

- Meggitt decoding for the cyclic CSS structure was used in comparative logical-CNOT simulations  ([arXiv:0711.1556](https://arxiv.org/abs/0711.1556)).

## Fault tolerance

- Fault-tolerant depth-7 circuit consisting of 57 CNOT gates and preparing a logical-zero state  ([arXiv:1106.2190](https://arxiv.org/abs/1106.2190)).

## Threshold

- $1.32\times 10^{-3}$-per gate error rate for depolarizing noise upon recursive concatenation  ([arXiv:1106.2190](https://arxiv.org/abs/1106.2190)), improving previous lower bounds  ([arXiv:quant-ph/0207119](https://arxiv.org/abs/quant-ph/0207119), [arXiv:0711.1556](https://arxiv.org/abs/0711.1556)). A numerical study  ([arXiv:quant-ph/0207119](https://arxiv.org/abs/quant-ph/0207119)) found that the Golay code achieved the highest threshold among a dozen well-known codes at the time  ([arXiv:0711.1556](https://arxiv.org/abs/0711.1556)).

## Relations

- _parent_: [[concepts/qec/self-dual-css]]
- _parent_: [[concepts/qec/galois-quad-residue]] — The Golay code is a qubit quantum QR code  ([arXiv:0712.0103](https://arxiv.org/abs/0712.0103), [arXiv:1907.01393](https://arxiv.org/abs/1907.01393)).
- _parent_: [[concepts/qec/data-syndrome]] — There exists a $⟦23,1,7:18⟧$ QDS code based on the qubit Golay code, requiring 18 additional stabilizer measurements instead of 24 from the general cyclic construction  ([arXiv:1907.01393](https://arxiv.org/abs/1907.01393)).
- _cousin_: [`golay`](https://errorcorrectionzoo.org/c/golay) — The qubit Golay code is a CSS code constructed with the Golay code.
- _cousin_: [[concepts/qec/qutrit-golay]] — The qubit Golay code is the qubit counterpart of the qutrit Golay code.
- _cousin_: [[concepts/qec/quantum-triorthogonal]] — A $⟦95,1,7⟧$ triorthogonal code with a transversal $T$ gate can be obtained from the qubit Golay code via the doubling transformation  ([arXiv:2307.14425](https://arxiv.org/abs/2307.14425)).
- _cousin_: [[concepts/qec/small-distance-qubit-stabilizer]] — The quantum Golay code can be punctured twice to obtain a $⟦21,3,5⟧$ code.

## Notes

- See Ref.  ([arXiv:quant-ph/0612004](https://arxiv.org/abs/quant-ph/0612004)) for more details.
- Two levels of concatenation of the qubit Golay code can tolerate high teleportation errors  ([arXiv:quant-ph/0607065](https://arxiv.org/abs/quant-ph/0607065), [arXiv:quant-ph/0701043](https://arxiv.org/abs/quant-ph/0701043)).
