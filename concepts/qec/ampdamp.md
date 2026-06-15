---
type: concept
name: Amplitude-damping (AD) code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/approximate-qecc
- concepts/qec/oscillators
- concepts/qec/qubit-concatenated
- concepts/qec/qubit-css
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/ampdamp
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: ampdamp
---

# Amplitude-damping (AD) code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/ampdamp) (`code_id: ampdamp`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Block quantum code on either qubits or bosonic modes that is designed to detect and correct qubit or bosonic AD errors, respectively.

(source: raw/error-correction-zoo.md)

## Protection

\begin{defterm}{Amplitude damping noise}
\label{topic:ad}
The amplitude damping (AD) channel is a bosonic channel that models loss of particles in a bosonic mode (a.k.a. photon loss, pure loss, or fiber attenuation).
Its Kraus operators are proportional to powers of a mode's annihilation operator $a$, with the power signifying the number of particles lost during the error,
\begin{align}
  E_{\ell}=\left(\frac{\gamma}{1-\gamma}\right)^{\ell/2}\frac{a^{\ell}}{\sqrt{\ell!}}\left(1-\gamma\right)^{\hat{n}/2}\,,
\end{align}
where $\gamma\in[0,1)$ is the noise rate  ([doi:10.1088/0954-8998/1/2/005](https://doi.org/10.1088/0954-8998/1/2/005), [arXiv:1708.05010](https://arxiv.org/abs/1708.05010)).
For multiple modes, error set elements are tensor products of elements of the single-mode error set. 
The fixed point of this channel for any truncation of Fock space is unique  ([arXiv:0909.1596](https://arxiv.org/abs/0909.1596)).

Restricting the channel to the first two Fock states $\{|0\rangle,|1\rangle\}$ yields the non-Pauli qubit AD channel, which requires protecting against the loss error $E_1\propto X+iY$ (instead of $X$ and $Y$ Pauli errors individually). Both channels are called AD since the context makes clear which one is being referred to.
In this restriction, the qubit AD channel has Kraus operators $A_0=\ket{0}\bra{0}+\sqrt{1-p}\ket{1}\bra{1}$ and $A_1=\sqrt{p}\ket{0}\bra{1}$; $A_1$ is the decay event and $A_0$ is the no-jump operator whose action still changes the relative amplitudes .
Other extensions to qudits are also known  ([arXiv:2008.00477](https://arxiv.org/abs/2008.00477)).
\end{defterm}

Protection against AD noise is typically approximate because the tensor product of Kraus operators with all $\ell=0$ is typically corrected only up to some order in $\gamma$  ([arXiv:quant-ph/9704002](https://arxiv.org/abs/quant-ph/9704002), [doi:10.1103/PhysRevA.56.1114](https://doi.org/10.1103/PhysRevA.56.1114)).
For example, a qubit code that corrects a single AD error is one for which all tensor products $E_{\ell_1}\otimes\cdots\otimes E_{\ell_n}$ with $\ell_1+\cdots + \ell_n \leq 1$ are correctable (per the \term{Knill-Laflamme conditions}) up to order $O(\gamma^2)$.
 
Certain codes also have intrinsic protection against AD, such as constant-excitation codes (CE), QSCs, or self-complementary codes.
Amplitude damping can be thought of as a quantum analogue to asymmetric noise  ([arXiv:1310.7536](https://arxiv.org/abs/1310.7536)).

## Rate

The quantum capacity of the AD channel is $\max\{0, \log \frac{1-\gamma}{\gamma}\} $  ([arXiv:quant-ph/0606132](https://arxiv.org/abs/quant-ph/0606132)). Quantum capacities of the qubit AD channel are also determined  ([arXiv:quant-ph/0405110](https://arxiv.org/abs/quant-ph/0405110), [arXiv:1309.2219](https://arxiv.org/abs/1309.2219)), including of channels with memory  ([arXiv:1207.5612](https://arxiv.org/abs/1207.5612), [arXiv:1510.05313](https://arxiv.org/abs/1510.05313)). Capacities of qudit extensions have also been studied  ([arXiv:2008.00477](https://arxiv.org/abs/2008.00477)).

## Relations

- _parent_: [[concepts/qec/oscillators]] — Restricting the AD channel to the first two Fock states $\{|0\rangle,|1\rangle\}$ yields the non-Pauli qubit AD channel, which requires protecting against the loss error $E_1\propto X+iY$ (instead of $X$ and $Y$ Pauli errors individually). Qubit AD codes are thus a special case of bosonic AD codes.
- _parent_: [[concepts/qec/approximate-qecc]] — Protection against AD noise is typically approximate because the tensor product of Kraus operators with all $\ell=0$ is typically corrected only up to some order in $\gamma$  ([arXiv:quant-ph/9704002](https://arxiv.org/abs/quant-ph/9704002), [doi:10.1103/PhysRevA.56.1114](https://doi.org/10.1103/PhysRevA.56.1114)).
- _cousin_: [[concepts/qec/qubit-css]] — An $⟦n,k,d_Z=t+1,d_X=2t+1⟧$ qubit CSS code protects against $t$ AD errors  ([arXiv:quant-ph/9705052](https://arxiv.org/abs/quant-ph/9705052)) ([arXiv:1001.2356](https://arxiv.org/abs/1001.2356)).
- _cousin_: [[concepts/qec/qubit-concatenated]] — Using the dual-rail code as an outer code with an inner $⟦n,k,d⟧$ qubit code yields an $⟦2n,k⟧$ code correcting $d-1$ qubit AD errors  ([arXiv:1001.2356](https://arxiv.org/abs/1001.2356)).
- _cousin_: [`hamming`](https://errorcorrectionzoo.org/c/hamming) — Ref.  ([arXiv:0710.1052](https://arxiv.org/abs/0710.1052)) presents a $⟦7,3⟧$ qubit stabilizer code for a single AD error based on the classical $[7,4,3]$ Hamming code.
