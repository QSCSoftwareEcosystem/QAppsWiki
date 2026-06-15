---
type: concept
name: Two-component cat code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/asymmetric-qecc
- concepts/qec/cat
- concepts/qec/coherent-state-c-q
- concepts/qec/coherent-state-repetition
- concepts/qec/hamiltonian
- concepts/qec/quantum-repetition
- concepts/qec/squeezed-cat
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/two-legged-cat
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: two-legged-cat
---

# Two-component cat code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/two-legged-cat) (`code_id: two-legged-cat`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Code whose codespace is spanned by two coherent states $\left|\pm\alpha\right\rangle$ for nonzero complex $\alpha$.

An orthonormal basis for the codespace consists of the bosonic *cat states*  ([doi:10.1016/0031-8914(74)90215-8](https://doi.org/10.1016/0031-8914(74)90215-8))
\begin{align}
  |\overline{\pm}\rangle=\frac{\left|\alpha\right\rangle \pm\left|-\alpha\right\rangle }{\sqrt{2\left(1\pm e^{-2|\alpha|^{2}}\right)}}
\end{align}
for any complex $\alpha$.

A closely related approximate cat code is called *T4C code*  ([arXiv:2004.09322](https://arxiv.org/abs/2004.09322)).

(source: raw/error-correction-zoo.md)

## Protection

Two-component cat codes for large $\alpha$ provide protection against modal dephasing, i.e., diffusion of the angular degree of freedom of the mode. A single photon loss event maps the even and odd cat states approximately into each other and therefore acts as a logical bit flip rather than being corrected by the code. There exist modifications based on sign alternation  ([arXiv:1901.05358](https://arxiv.org/abs/1901.05358)), squeezing (yielding squeezed cat codes)  ([arXiv:2201.02570](https://arxiv.org/abs/2201.02570), [arXiv:2210.13406](https://arxiv.org/abs/2210.13406), [arXiv:2210.13359](https://arxiv.org/abs/2210.13359)), detuning  ([arXiv:2211.03689](https://arxiv.org/abs/2211.03689)), and addition of higher-order nonlinearities  ([arXiv:2503.11624](https://arxiv.org/abs/2503.11624)) that can add such protection.

## Encoders

- Lindbladian-based dissipative encoding and autonomous QEC  ([arXiv:1312.2017](https://arxiv.org/abs/1312.2017)) utilizing two-photon absorption  ([doi:10.1103/PhysRevLett.60.1836](https://doi.org/10.1103/PhysRevLett.60.1836), [doi:10.1103/PhysRevA.50.4330](https://doi.org/10.1103/PhysRevA.50.4330), [doi:10.1103/PhysRevA.49.490](https://doi.org/10.1103/PhysRevA.49.490), [doi:10.1103/PhysRevA.49.2785](https://doi.org/10.1103/PhysRevA.49.2785), [doi:10.1103/PhysRevLett.77.4728](https://doi.org/10.1103/PhysRevLett.77.4728)). Encoding passively protects against cavity dephasing, suppressing dephasing noise exponentially with $|\alpha|^2$  ([arXiv:1312.2017](https://arxiv.org/abs/1312.2017)). See Refs.  ([arXiv:2012.04108](https://arxiv.org/abs/2012.04108), [arXiv:2407.17299](https://arxiv.org/abs/2407.17299)) for analyses using displaced Fock states  ([doi:10.1088/0954-8998/3/6/005](https://doi.org/10.1088/0954-8998/3/6/005), [arXiv:1311.1920](https://arxiv.org/abs/1311.1920)). The Keldysh formalism yields non-perturbative bit-flip rates under various types of noise  ([arXiv:2507.18714](https://arxiv.org/abs/2507.18714)).
- Hamiltonian-based 'Kerr-cat' encoding utilizing the Kerr-effect Hamiltonian  ([arXiv:1605.09408](https://arxiv.org/abs/1605.09408)) (see also Ref.  ([arXiv:1510.02566](https://arxiv.org/abs/1510.02566))).
- Colored dissipation  ([arXiv:2107.09198](https://arxiv.org/abs/2107.09198)).
- Combined dissipative and Hamiltonian-based encoding utilizing two-photon exchange with an ancillary qubit  ([arXiv:2112.05545](https://arxiv.org/abs/2112.05545)).
- Critical encoding at nonzero detuning  ([arXiv:2208.04928](https://arxiv.org/abs/2208.04928)).

## General gates

- Universal gates in the quantum optical setting can be performed using teleportation, Bell measurements, displacements, and rotations  ([arXiv:quant-ph/0306004](https://arxiv.org/abs/quant-ph/0306004)). An earlier protocol requires a nonlinear interaction and uses state teleportation  ([arXiv:quant-ph/0109077](https://arxiv.org/abs/quant-ph/0109077)).
- Universal gates in the microwave setting can be performed using displacement operators and a rotation based on the Kerr nonlinearity  ([arXiv:1312.2017](https://arxiv.org/abs/1312.2017)). Kerr nonlinearity converts coherent states into Yurke-Stoler states  ([doi:10.1103/PhysRevLett.57.13](https://doi.org/10.1103/PhysRevLett.57.13)).
- Bias-preserving $X$, CNOT, and Toffoli gates  ([arXiv:1904.09474](https://arxiv.org/abs/1904.09474), [arXiv:1905.00450](https://arxiv.org/abs/1905.00450)). A bias-preserving SWAP gate has also been proposed  ([arXiv:2009.10756](https://arxiv.org/abs/2009.10756)).
- Cat-transmon entangling gate using an ancillary qubit  ([arXiv:2410.23363](https://arxiv.org/abs/2410.23363)).

## Decoders

- All-optical decoder  ([arXiv:2108.12225](https://arxiv.org/abs/2108.12225)) based on Knill error correction (a.k.a. telecorrection  ([arXiv:quant-ph/0601066](https://arxiv.org/abs/quant-ph/0601066))), which is based on teleportation  ([arXiv:quant-ph/0410199](https://arxiv.org/abs/quant-ph/0410199), [arXiv:quant-ph/0312190](https://arxiv.org/abs/quant-ph/0312190)).

## Fault tolerance

- Fault-tolerant error-correction procedure using small amplitude coherent states  ([arXiv:0707.0327](https://arxiv.org/abs/0707.0327)).
- Bias-preserving $X$, CNOT, and Toffoli gates  ([arXiv:1904.09474](https://arxiv.org/abs/1904.09474), [arXiv:1905.00450](https://arxiv.org/abs/1905.00450)). A bias-preserving SWAP gate has also been proposed  ([arXiv:2009.10756](https://arxiv.org/abs/2009.10756)).

## Realizations

- Lindbladian-based dissipative  ([arXiv:1412.4633](https://arxiv.org/abs/1412.4633), [arXiv:1705.02401](https://arxiv.org/abs/1705.02401)) and Hamiltonian-based 'Kerr-cat'  ([arXiv:1907.12131](https://arxiv.org/abs/1907.12131)) encodings have been achieved in superconducting circuit devices by the Devoret group; Ref.  ([arXiv:1705.02401](https://arxiv.org/abs/1705.02401)) also demonstrated a displacement-based gate. The Lindbladian-based scheme has further achieved a suppression of bit-flip errors that is exponential in the average photon number up to a bit-flip time of 1ms  ([arXiv:1907.11729](https://arxiv.org/abs/1907.11729)). A bit-flip time of up to 10s has been achieved for the two-component cat code in the classical-bit regime  ([arXiv:2204.09128](https://arxiv.org/abs/2204.09128), [arXiv:2307.06617](https://arxiv.org/abs/2307.06617), [arXiv:2307.06761](https://arxiv.org/abs/2307.06761)). A holonomic gate has been repurposed as a logical measurement  ([arXiv:1503.00194](https://arxiv.org/abs/1503.00194)). The 'Kerr-cat' encoding and a $\pi/2$ gate have been realized with the help of a band-block filter, yielding a bit-flip lifetime of 1 ms in the 10-photon regime  ([arXiv:2404.16697](https://arxiv.org/abs/2404.16697)) (see also Ref.  ([arXiv:2209.03934](https://arxiv.org/abs/2209.03934))). Lindblad-based encoding achieved in a 2D cavity by AWS  ([arXiv:2409.17556](https://arxiv.org/abs/2409.17556)).
- T4C code realized in a superconducting circuit device by the Wang group  ([arXiv:2004.09322](https://arxiv.org/abs/2004.09322)).

## Relations

- _parent_: [[concepts/qec/cat]] — The cat code reduces to its two-component version for $S=0$.
- _parent_: [[concepts/qec/coherent-state-repetition]] — The coherent-state repetition code for $n=1$ reduces to the two-component cat code.
- _parent_: [[concepts/qec/squeezed-cat]] — The squeezed cat code reduces to the two-component cat code when there is no squeezing.
- _cousin_: [[concepts/qec/hamiltonian]] — The two-component cat code forms the ground-state subspace of a Kerr Hamiltonian  ([arXiv:1605.09408](https://arxiv.org/abs/1605.09408)).
- _cousin_: [[concepts/qec/quantum-repetition]] — Two-component cat and quantum repetition codes can be thought of as classical codes because they protect against only one type of noise. Two-component cat codes (quantum repetition) codes suppress cavity dephasing (bit-flip) noise exponentially with $|\alpha|^2$ ($n$). The stability offered by cat codes has been linked to several favorable properties of phases of matter associated with the repetition-code Hamiltonian  ([arXiv:1804.11293](https://arxiv.org/abs/1804.11293), [arXiv:2008.02816](https://arxiv.org/abs/2008.02816)).
- _cousin_: [[concepts/qec/coherent-state-c-q]] — Two-component cat codes can be thought of as coherent-state c-q codes because they protect against only one type of noise and thus only reliably store classical information.
- _cousin_: [[concepts/qec/asymmetric-qecc]] — Cat qubits provide an asymmetric-noise platform admitting bias-preserving $X$, CNOT, and Toffoli gates  ([arXiv:1904.09474](https://arxiv.org/abs/1904.09474), [arXiv:1905.00450](https://arxiv.org/abs/1905.00450)). A bias-preserving SWAP gate has also been proposed  ([arXiv:2009.10756](https://arxiv.org/abs/2009.10756)).

## Notes

- Pedagogical introduction to cat codes in the context of microwave cavities can be found in Refs.  ([arXiv:2203.03222](https://arxiv.org/abs/2203.03222))}, and in the context of optical systems in books  ([doi:10.1093/acprof:oso/9780198509141.001.0001](https://doi.org/10.1093/acprof:oso/9780198509141.001.0001), [doi:10.1142/9781860948169_0009](https://doi.org/10.1142/9781860948169_0009), [doi:10.1002/9783527695805](https://doi.org/10.1002/9783527695805)).
- Ground states of the fluxonium superconducting qubit resemble two-component cat codewords  ([arXiv:2501.16425](https://arxiv.org/abs/2501.16425)).
