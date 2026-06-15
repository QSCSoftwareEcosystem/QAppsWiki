---
type: concept
name: Chuang-Leung-Yamamoto (CLY) code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/constant-excitation
- concepts/qec/fock-state
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/chuang-leung-yamamoto
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: chuang-leung-yamamoto
---

# Chuang-Leung-Yamamoto (CLY) code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/chuang-leung-yamamoto) (`code_id: chuang-leung-yamamoto`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Bosonic Fock-state code that encodes $k$ qubits into $n$ oscillators, with each oscillator restricted to having at most $N$ excitations. Codewords are superpositions of oscillator Fock states which have exactly $N$ total excitations, and are either uniform (i.e., balanced) superpositions or unbalanced superpositions.

Codes can be denoted as $⟦N,n,2^k,d⟧$, which conflicts with stabilizer code notation.

(source: raw/error-correction-zoo.md)

## Protection

Protects against AD for up to $t = d-1$ excitation losses. Defining the *spacing* between two Fock states $|u_1\cdots u_n\rangle$ and $|v_1\cdots v_n\rangle$,
\begin{align}
\text{Spacing}(u,v) = \frac{1}{2}\sum_{i=1}^n |u_i - v_i|,
\end{align}
the code distance $d$ can be defined as the minimal spacing between Fock states making up the codewords.

## Rate

Code rate is $\frac{k}{n \log_2(N+1)}$. To correct the loss of up to $t$ excitations with $K+1$ codewords, a code exists with scaling $N \sim t^3 K/2$.

## Encoders

- Photon Fock state input into a network of beamsplitters, phase shifters, and Kerr media. These operations all preserve total photon number. Beamsplitters and phase shifters take annihilation operators to linear combinations of annihilation operators, and the transformation matrix is unitary. The operations corresponding to Kerr nonlinear media are diagonal in the Fock basis, but they implement phases that in general depend nonlinearly on the number of photons in each mode. State preparation may require ancillary modes and be conditioned on photon-number measurement results.

## Decoders

- Destructive decoding with a photon number measurement on each mode.
- State can be decoded with a network of beamsplitters, phase shifters, and Kerr media.

## Relations

- _parent_: [[concepts/qec/fock-state]] — Chuang-Leung-Yamamoto codes are multi-mode Fock-state codes.
- _parent_: [[concepts/qec/constant-excitation]] — Chuang-Leung-Yamamoto codewords are constructed out of Fock states with the same total excitation number.
