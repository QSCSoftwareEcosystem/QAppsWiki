---
type: concept
name: Binomial code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/bosonic-rotation
- concepts/qec/cat
- concepts/qec/number-phase
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/binomial
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: binomial
---

# Binomial code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/binomial) (`code_id: binomial`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Bosonic rotation codes designed to approximately protect against errors consisting of powers of raising and lowering operators up to some maximum power. Binomial codes can be thought of as spin-coherent states embedded into an oscillator  ([arXiv:1708.05010](https://arxiv.org/abs/1708.05010)).

A simple example of a binomial code is the *"0-2-4"* qubit code with codewords
\begin{align}
\begin{split}
  |\overline{0}\rangle&=\frac{1}{\sqrt{2}}\left(|0\rangle+|4\rangle\right)\\
  |\overline{1}\rangle&=|2\rangle~,
\end{split}
\end{align}
constructed out of binomial states  ([doi:10.1080/713821735](https://doi.org/10.1080/713821735)).

General $q$-dimensional qudit $(N, S)$ binomial codeword states are $\{|\overline{i}\rangle\mid i\in \mathbb Z_q \}$, where
  \begin{align}
    |\overline{i}\rangle = \frac{1}{\sqrt{q^N}} \sum_{\substack{p=0\\p\equiv i \pmod{q}}}^{(q-1)(N+1)} \sqrt{\binom{N+1}{p}_q} \ket{p(S+1)}.
  \end{align}
  The set $\{\ket{i}\mid i \in \mathbb{N}\}$ is the set of Fock states. Also, $\binom{N+1}{p}_q$ are extended binomial coefficients, or polynomial coefficients, defined recursively as
  \begin{align}
    \binom{n}{m}_1 \equiv 1,\quad \binom{n}{m}_q \equiv \sum_{k=0}^n \binom{n}{k}\binom{k}{m-k}_{q-1}.
  \end{align}
  The extended binomial coefficients $ \binom{n}{m}_q $ are also the coefficients of $ x^m $ in the polynomial $ (1 + x + \cdots + x^{q-1})^n $.

(source: raw/error-correction-zoo.md)

## Protection

An $(N, S)$ binomial code protects against $L$ boson losses, $G$ boson gains, and dephasing up to $\hat{n}^{D}$, where $S=L+G$ and $N = \mathrm{max}(L,G,2D)$.  Binomial codes approximately protect against continuous-time AD, boson loss and gain, and dephasing.

## Encoders

- State preparation using spin-boson interactions  ([arXiv:2507.08585](https://arxiv.org/abs/2507.08585)).

## General gates

- Error-detecting $CCZ$ and $cSWAP$ gates for "0-2-4" code using three-level ancilla  ([arXiv:2212.11196](https://arxiv.org/abs/2212.11196)).
- Single logical-qubit rotations  ([arXiv:2408.12968](https://arxiv.org/abs/2408.12968)).
- Amplitude-mixing error-transparent gates  ([arXiv:2412.08870](https://arxiv.org/abs/2412.08870)).

## Decoders

- Photon loss and dephasing errors can be detected by measuring the phase-space rotation $\exp\left(2\pi\mathrm{i} \hat{n} / (S+1)\right)$ and the check operator $(J_x/J)^2$ in the spin-coherent state language, where $J$ is the total angular momentum and $J_x$ is the angular momentum in the $x$ direction  ([arXiv:1708.05010](https://arxiv.org/abs/1708.05010)). This type of error correction fails for errors that are products of photon loss/gain and dephasing errors. However, for certain $(N,S)$ instances of the binomial code, detection of these types of errors can be done.
- Recovery can be done via projective measurements and unitary operations in a version of the Cafaro recovery map  ([arXiv:1602.00008](https://arxiv.org/abs/1602.00008), [arXiv:1708.05010](https://arxiv.org/abs/1708.05010)).
- Fault-tolerant scheme that converts the required POVM into binary measurements whose redundancy is guaranteed by a classical code  ([arXiv:2402.04093](https://arxiv.org/abs/2402.04093)).

## Realizations

- Microwave cavities coupled to superconducting circuits: state transfer between a binomial codeword to another system  ([arXiv:1712.05832](https://arxiv.org/abs/1712.05832)), error-correction protocol nearly reaching break-even  ([arXiv:1805.09072](https://arxiv.org/abs/1805.09072)), a teleported CNOT gate  ([arXiv:1810.04690](https://arxiv.org/abs/1810.04690)), and fault-tolerant logical operations utilizing three-level ancillas  ([arXiv:1907.12327](https://arxiv.org/abs/1907.12327)). A realization of the "0-2-4" encoding is the first to go beyond break-even error-correction and yields a logical lifetime that exceeds the cavity lifetime by $16\%$  ([arXiv:2211.09319](https://arxiv.org/abs/2211.09319)) (see also  ([arXiv:2211.09116](https://arxiv.org/abs/2211.09116))). See Ref.  ([arXiv:2111.07965](https://arxiv.org/abs/2111.07965)) for another experiment. The 0-2-4 binomial code has been used to store entangled states  ([arXiv:2501.04460](https://arxiv.org/abs/2501.04460)).
- Motional degree of freedom of a trapped ion: binomial state preparation for $S=2$ realized by Tan group  ([arXiv:2310.15546](https://arxiv.org/abs/2310.15546)).

## Relations

- _parent_: [[concepts/qec/bosonic-rotation]] — One can verify by direct calculation that the logical states are eigenstates of the discrete rotation operator. One has freedom in the exact form of the primitive state to choose; see  ([arXiv:1901.08071](https://arxiv.org/abs/1901.08071)).
- _cousin_: [[concepts/qec/cat]] — For a fixed $S$, binomial codes with $N \to \infty$ coincide with cat codes as $\alpha \to \infty$  ([arXiv:1602.00008](https://arxiv.org/abs/1602.00008)).
- _cousin_: [[concepts/qec/number-phase]] — In the limit as $N,S \to \infty$, phase measurement in the binomial code has vanishing variance, just like in a number-phase code  ([arXiv:1901.08071](https://arxiv.org/abs/1901.08071)).

## Notes

- The mean occupation number, or average Fock-state number in maximally-mixed state of the code, is $(N+1)(S+1)(q-1)/2 $, where $q$ is the qudit dimension.
