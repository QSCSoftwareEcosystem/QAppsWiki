---
type: concept
name: Twisted XZZX toric code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- XZZX cyclic code
- Cyclic toric code
- Generalized toric code (GTC)
- Genus-one genon code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/quantum-cyclic
- concepts/qec/stab-5-1-2-convolutional
- concepts/qec/xzzx
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/twisted_xzzx
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: twisted_xzzx
---

# Twisted XZZX toric code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/twisted_xzzx) (`code_id: twisted_xzzx`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A cyclic code that can be thought of as the XZZX toric code with shifted (a.k.a twisted) boundary conditions.
Admits a set of stabilizer generators that are equivalent to cyclic shifts of a particular weight-four $XZZX$ Pauli string.

Codes encode either one or two logical qubits, depending on qubit geometry, and perform well against biased noise  ([arXiv:2203.16486](https://arxiv.org/abs/2203.16486)).
See Ref.  ([arXiv:2406.09951](https://arxiv.org/abs/2406.09951)) for a table of some of these for small instances, where they are called genus-one genon codes.

(source: raw/error-correction-zoo.md)

## Protection

A family of $⟦a^2+b^2,k,d⟧$ cyclic codes exists for all $b > a \geq 1$ such that $\text{gcd}(a,b)=1$  ([arXiv:2101.09349](https://arxiv.org/abs/2101.09349)).
Here, $k=1$ ($k=2$) and $d=a+b$ ($d=\max(a,b)$) for odd $n$ (even $n$).
The subfamily $⟦d^2+1,2,d⟧$ (i.e., $a=1,b=d$ for odd $d$) includes $⟦10,2,3⟧$, $⟦26,2,5⟧$, $⟦50,2,7⟧$, $\ldots$  ([arXiv:1202.0928](https://arxiv.org/abs/1202.0928)).
The subfamily $⟦t^2+(t+1)^2,1,2t+1⟧$ (i.e., $a=t,b=t+1$) includes $⟦5,1,3⟧$, $⟦13,1,5⟧$, $⟦25,1,7⟧$, $\ldots$  ([arXiv:1202.0928](https://arxiv.org/abs/1202.0928)).
Small instances are tabulated in Ref.  ([arXiv:2406.09951](https://arxiv.org/abs/2406.09951)) as genus-one genon codes.
Other types of distances have been considered for this code  ([arXiv:2203.16486](https://arxiv.org/abs/2203.16486)).

## Decoders

- Fault-tolerant syndrome extraction circuits using flag qubits  ([arXiv:2203.16486](https://arxiv.org/abs/2203.16486)).
- AMBP4, a quaternary version  ([arXiv:2202.06612](https://arxiv.org/abs/2202.06612)) of the MBP decoder  ([arXiv:2104.13659](https://arxiv.org/abs/2104.13659)).
- Fault-tolerant BP (FTBP) decoder  ([arXiv:2409.18689](https://arxiv.org/abs/2409.18689)).

## Code capacity threshold

- Depolarizing noise: $17.5\%$ under AMBP4 decoding for the $⟦(m^2+1)/2,1,m⟧$ family  ([arXiv:2202.06612](https://arxiv.org/abs/2202.06612)).
- Biased noise: between $20\%$ and $45\%$ at noise bias ranging from 1 to 10 under MWPM  ([arXiv:2203.16486](https://arxiv.org/abs/2203.16486)).

## Threshold

- Phenomenological noise: between $3\%$ and $10\%$ at noise bias ranging from 1 to 4 under MWPM  ([arXiv:2203.16486](https://arxiv.org/abs/2203.16486)).

## Fault tolerance

- Fault-tolerant syndrome extraction circuits using flag qubits  ([arXiv:2203.16486](https://arxiv.org/abs/2203.16486)).

## Relations

- _parent_: [[concepts/qec/xzzx]] — Imposing twisted (a.k.a. shifted) boundary conditions on the toric XZZX code yields the twisted XZZX code  ([arXiv:1108.5490](https://arxiv.org/abs/1108.5490)) ([arXiv:2101.09349](https://arxiv.org/abs/2101.09349)).
- _parent_: [[concepts/qec/quantum-cyclic]]
- _cousin_: [[concepts/qec/stab-5-1-2-convolutional]] — $(5,1,2)$-convolutional codes (twisted XZZX toric codes) are 1D (2D) lattice extensions of the five-qubit perfect code.
