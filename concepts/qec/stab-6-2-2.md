---
type: concept
name: $⟦6,2,2⟧$ $C_6$ code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/2d-color
- concepts/qec/css-6-1-2
- concepts/qec/goy
- concepts/qec/kls
- concepts/qec/quantum-h
- concepts/qec/qubit-concatenated
- concepts/qec/stabilizer-over-gf4
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/stab_6_2_2
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: stab_6_2_2
---

# $⟦6,2,2⟧$ $C_6$ code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/stab_6_2_2) (`code_id: stab_6_2_2`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Error-detecting normal self-dual CSS code on three qubit pairs that encodes a logical qubit pair and detects any error acting on one pair  ([arXiv:quant-ph/0410199](https://arxiv.org/abs/quant-ph/0410199)).
In Knill's $C_4/C_6$ architecture, this code is used at the second and higher concatenation levels.

A stabilizer tableau for the code is given by 
\begin{align}
\begin{array}{cccccc}
  Z & Z & Z & Z & I & I \\
  Z & Z & I & I & Z & Z \\
  X & X & X & X & I & I \\
  X & X & I & I & X & X
\end{array}~.
\end{align}
Its logical operators are $X_L = IIXXII$, $Z_L = ZIIZZI$, $X_S = IXIXXI$, and $Z_S = IIIIZZ$  ([arXiv:quant-ph/0410199](https://arxiv.org/abs/quant-ph/0410199)).

(source: raw/error-correction-zoo.md)

## Protection

As a distance-two code, the $C_6$ code detects any single-qubit error.
In the qubit-pair grouping used by Knill, it detects any error acting on one of the three pairs, and therefore can correct a pair error when its location is already known  ([arXiv:quant-ph/0410199](https://arxiv.org/abs/quant-ph/0410199)).

## Magic scaling exponent

Various magic-state distillation protocols exist for the $⟦4,2,2⟧$ qubit code and the $C_6$ code in what are known as Meier-Eastin-Knill (MEK) protocols  ([arXiv:1204.4221](https://arxiv.org/abs/1204.4221)). For example, the magic-state yield parameter is $\gamma = \log_2 5 \approx 2.322$ for a protocol using the $⟦10,2,2⟧$ code  ([arXiv:1612.07330](https://arxiv.org/abs/1612.07330)); see also  ([arXiv:1709.02789](https://arxiv.org/abs/1709.02789)).

## Transversal gates

- Transversal physical Hadamards preserve the codespace because the displayed $X$- and $Z$-check spaces coincide, making this a normal self-dual qubit CSS code  ([arXiv:2602.22211](https://arxiv.org/abs/2602.22211)).

## General gates

- Fault-tolerant magic-state preparation  ([arXiv:2506.14688](https://arxiv.org/abs/2506.14688)).

## Fault tolerance

- Knill's $C_4/C_6$ architecture uses the $⟦4,2,2⟧$ code at the first level and the $C_6$ code at higher levels, together with error-correcting teleportation  ([arXiv:quant-ph/0410199](https://arxiv.org/abs/quant-ph/0410199)). That paper gives evidence for postselected thresholds above $0.03$ and extrapolates to $0.06$, while the error-correcting architecture has evidence for a threshold above $0.01$. Later work refined the postselected-threshold analysis  ([arXiv:quant-ph/0608018](https://arxiv.org/abs/quant-ph/0608018), [arXiv:quant-ph/0703264](https://arxiv.org/abs/quant-ph/0703264)) (see also Ref.  ([arXiv:quant-ph/0612073](https://arxiv.org/abs/quant-ph/0612073))).
- Concatenating quantum Hamming codes on top of the $⟦4,2,2⟧$ and $C_6$ codes yields fault-tolerant quantum computation with constant space and quasi-polylogarithmic time overheads  ([arXiv:2402.09606](https://arxiv.org/abs/2402.09606)). In the optimized protocol of Ref.  ([arXiv:2402.09606](https://arxiv.org/abs/2402.09606)), a level-five $C_4/C_6$ code underlies concatenated quantum Hamming codes $\mathcal{Q}_5,\mathcal{Q}_6,\mathcal{Q}_7,\mathcal{Q}_7$, yielding a $2.5\%$ threshold and space overheads $162$ and $373$ physical qubits per logical qubit at physical error rate $0.1\%$ for logical CNOT error rates $10^{-10}$ and $10^{-24}$, respectively.
- Fault-tolerant magic-state preparation  ([arXiv:2506.14688](https://arxiv.org/abs/2506.14688)).
- One of the code's logical qubits can be relaxed to a gauge qubit to yield a $⟦6,1,1,2⟧$ subsystem qubit stabilizer code with a particular set of transversal gates. This code admits a fault-tolerant circuit relevant to magic-state preparation  ([arXiv:2501.17447](https://arxiv.org/abs/2501.17447)).

## Realizations

- Trapped ions: fault-tolerant magic-state preparation demonstrated on a 20-qubit H1-1 device by Quantinuum  ([arXiv:2506.14688](https://arxiv.org/abs/2506.14688)).

## Relations

- _parent_: [[concepts/qec/2d-color]] — The $C_6$ code is a color code on a ladder with three rungs and periodic boundary conditions, (a.k.a. a triangular prism with no top and bottom faces) . Purely $Z$- or $X$-type stabilizers lie on the three square faces of the ladder.
- _parent_: [[concepts/qec/quantum-h]] — The $⟦k+4,k,2⟧$ H code for $k=2$ is the $C_6$ code.
- _parent_: [[concepts/qec/goy]] — The Ganti-Onunkwo-Young code for $r=1$ is the $C_6$ code.
- _parent_: [[concepts/qec/kls]] — The Khesin-Lu-Shor code for $r=2$ and $m=2^r - 1 = 3$ is the $C_6$ code.
- _parent_: [[concepts/qec/stabilizer-over-gf4]] — The $C_6$ code is Hermitian  ([arXiv:2501.17447](https://arxiv.org/abs/2501.17447)).
- _cousin_: [[concepts/qec/css-6-1-2]] — Fixing one logical qubit of the $⟦6,2,2⟧$ $C_6$ code to $|Y^{-}\rangle_L$ yields this $⟦6,1,2⟧$ code  ([arXiv:2507.10519](https://arxiv.org/abs/2507.10519)).
- _cousin_: [[concepts/qec/qubit-concatenated]] — Concatenations of $⟦4,2,2⟧$ and $C_6$ codes yield fault-tolerant quantum computation schemes  ([arXiv:quant-ph/0410199](https://arxiv.org/abs/quant-ph/0410199)) admitting a post-selected threshold  ([arXiv:quant-ph/0608018](https://arxiv.org/abs/quant-ph/0608018), [arXiv:quant-ph/0703264](https://arxiv.org/abs/quant-ph/0703264)) (see also Ref.  ([arXiv:quant-ph/0612073](https://arxiv.org/abs/quant-ph/0612073))) and the Meier-Eastin-Knill (MEK) magic-state distillation protocols  ([arXiv:1204.4221](https://arxiv.org/abs/1204.4221)). Concatenating quantum Hamming codes on top of the $⟦4,2,2⟧$ and $C_6$ codes yields fault-tolerant quantum computation with constant space and quasi-polylogarithmic time overheads  ([arXiv:2402.09606](https://arxiv.org/abs/2402.09606)). In the optimized protocol of Ref.  ([arXiv:2402.09606](https://arxiv.org/abs/2402.09606)), a level-five $C_4/C_6$ code underlies concatenated quantum Hamming codes $\mathcal{Q}_5,\mathcal{Q}_6,\mathcal{Q}_7,\mathcal{Q}_7$, yielding a $2.5\%$ threshold and space overheads $162$ and $373$ physical qubits per logical qubit at physical error rate $0.1\%$ for logical CNOT error rates $10^{-10}$ and $10^{-24}$, respectively.
