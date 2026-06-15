---
type: concept
name: Toric code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/surface
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/toric
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: toric
---

# Toric code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/toric) (`code_id: toric`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Version of the Kitaev surface code on a square lattice with periodic boundary conditions, encoding two logical qubits.
Being the first manifestation of the surface code, "toric code" is often an alternative name for the general construction.
*Twisted toric code*  ([arXiv:2012.09271](https://arxiv.org/abs/2012.09271)) refers to the construction on a torus with twisted (a.k.a. shifted) boundary conditions.
In the original Hamiltonian construction, open Pauli-$Z$ and Pauli-$X$ strings create pairs of electric charges and magnetic vortices, and braiding one type around the other yields the nontrivial Abelian anyonic phase  ([arXiv:quant-ph/9707021](https://arxiv.org/abs/quant-ph/9707021)).

The stabilizers of the toric code are generated
by star operators $A_v$ and plaquette operators $B_p$.
Each star operator is a product of four Pauli-$X$ operators on the edges adjacent to a vertex   $v$ of the lattice; each plaquette operator is a product of four Pauli-$Z$ operators applied to the edges adjacent to a face, or plaquette, $p$ of the
lattice (\ref{figure:toric-code-operators}).



We denote by
$\overline{X}_i,\overline{Z}_i$ the logical Pauli-$X$ and Pauli-$Z$
operator of the $i$-th logical qubit (with $i\in\{1,2\}$).  They are represented by strings of Pauli-$X$ operators or Pauli-$Z$ operators that wrap around the torus, as shown in \ref{figure:toric-code-operators}.

(source: raw/error-correction-zoo.md)

## Protection

Toric code on an $L\times L$ torus is a $⟦2L^2,2,L⟧$ CSS code.
The number of error patterns can be used to bound the ground-state energy of a $\pm J$ Ising model  ([arXiv:cond-mat/0405313](https://arxiv.org/abs/cond-mat/0405313)).
Coherent physical errors in the toric code are expected to become incoherent logical errors under syndrome measurement; see corroborating numerical studies performed by embedding each physical qubit into two fermions via the tetron code  ([arXiv:1710.02270](https://arxiv.org/abs/1710.02270)) as well as deriving analytical bounds  ([arXiv:1912.04319](https://arxiv.org/abs/1912.04319)).
More generally, there is a tensor-network routine that calculates the effective logical channel  ([arXiv:2403.08706](https://arxiv.org/abs/2403.08706))

## Encoders

- Lindbladian-based dissipative encoding for the toric code  ([arXiv:1310.1036](https://arxiv.org/abs/1310.1036)) that does not give a speedup relative to circuit-based encoders  ([arXiv:1310.1037](https://arxiv.org/abs/1310.1037)).

## Transversal gates

- Transversal logical Pauli gates correspond to Pauli strings on non-trivial loops of the torus.

## General gates

- Logical $CX$ gate for the $⟦12,2,3⟧$ twisted toric code  ([arXiv:2505.20261](https://arxiv.org/abs/2505.20261)).

## Code capacity threshold

- Independent $X,Z$ noise: $p_X = 10.31\%$ under MWPM decoding  ([arXiv:quant-ph/0207088](https://arxiv.org/abs/quant-ph/0207088)) (see also Ref.  ([arXiv:1405.4883](https://arxiv.org/abs/1405.4883))), $9.9\%$ under BP-OSD decoding  ([arXiv:2005.07016](https://arxiv.org/abs/2005.07016)), and $8.9\%$ under GBP decoding  ([arXiv:2212.03214](https://arxiv.org/abs/2212.03214)). 
The threshold under ML decoding corresponds to the value of a critical point of a two-dimensional random-bond Ising model (RBIM) on the Nishimori line  ([doi:10.1143/JPSJ.55.3305](https://doi.org/10.1143/JPSJ.55.3305), [arXiv:quant-ph/0110143](https://arxiv.org/abs/quant-ph/0110143)), calculated to be $10.94 \pm 0.02\%$ in Ref.  ([arXiv:cond-mat/0010143](https://arxiv.org/abs/cond-mat/0010143)), $10.93(2)\%$ in Ref.  ([arXiv:cond-mat/0106023](https://arxiv.org/abs/cond-mat/0106023)), $10.9187\%$ in Ref.  ([arXiv:0811.0464](https://arxiv.org/abs/0811.0464)), $10.917(3)\%$ in Ref.  ([arXiv:0811.2101](https://arxiv.org/abs/0811.2101)), $10.939(6)\%$ in Ref.  ([arXiv:0902.4153](https://arxiv.org/abs/0902.4153)), and estimated to be between $10.9\%$ and $11\%$ in Ref.  ([arXiv:1405.4883](https://arxiv.org/abs/1405.4883)).
The model for the case of the toric code has been thoroughly investigated  ([arXiv:2402.16937](https://arxiv.org/abs/2402.16937), [arXiv:2512.10399](https://arxiv.org/abs/2512.10399)).
The Bravyi-Suchara-Vargo (BSV) tensor network decoder  ([arXiv:1405.4883](https://arxiv.org/abs/1405.4883)) exactly solves the ML decoding problem under independent $X,Z$ noise for the surface code and has complexity of order $O(n^2)$; the decoder provides an efficient tensor-network contraction for the partition function resulting from the statistical mechanical mapping, which is known to be solvable for an Ising model on a planar graph  ([doi:10.1103/PhysRev.88.1332](https://doi.org/10.1103/PhysRev.88.1332)).
ML decoding  ([arXiv:quant-ph/0110143](https://arxiv.org/abs/quant-ph/0110143)) is $\#P$-hard in general for the surface code  ([arXiv:2309.10331](https://arxiv.org/abs/2309.10331)).
Above values are for one type of noise only, and the ML threshold for combined $X$ and $Z$ noise is $2p_X - p_X^2 \approx 20.6\%$  ([arXiv:2212.03214](https://arxiv.org/abs/2212.03214)). 
Thresholds for various lattices have been obtained in Refs.  ([arXiv:1112.1613](https://arxiv.org/abs/1112.1613), [arXiv:1202.2743](https://arxiv.org/abs/1202.2743)).
- Depolarizing noise: between $17\%$ and $18.5\%$ under BSV tensor-network decoding  ([arXiv:1405.4883](https://arxiv.org/abs/1405.4883)), $14\%$ under GBP decoding  ([arXiv:2212.03214](https://arxiv.org/abs/2212.03214)), $16.5\%$ under recursive MWPM  ([arXiv:2212.11632](https://arxiv.org/abs/2212.11632)), between $16\%$ and $17.5\%$ under AMBP4 (depending on whether surface or toric code is considered)  ([arXiv:2104.13659](https://arxiv.org/abs/2104.13659)), and between $15\%$ and $16\%$ under RG  ([arXiv:0911.0581](https://arxiv.org/abs/0911.0581)), Markov-chain  ([arXiv:1302.2669](https://arxiv.org/abs/1302.2669)), or MWPM  ([arXiv:0905.0531](https://arxiv.org/abs/0905.0531)) decoding. The threshold under ML decoding corresponds to the value of a critical point of the disordered eight-vertex Ising model, calculated to be $18.9(3)\%$  ([arXiv:1202.1852](https://arxiv.org/abs/1202.1852)) (see also APS Physics viewpoint  ([doi:10.1103/Physics.5.50](https://doi.org/10.1103/Physics.5.50))).
- Erasure noise: $50\%$ for square tiling  ([arXiv:0904.3556](https://arxiv.org/abs/0904.3556), [arXiv:0912.1159](https://arxiv.org/abs/0912.1159)). There is an inverse relationship between coordination number of the syndrome graph, with the threshold corresponding to a percolation transition  ([arXiv:1810.09621](https://arxiv.org/abs/1810.09621)).
- AD noise: $39\%$  ([arXiv:1607.06460](https://arxiv.org/abs/1607.06460)).
- Correlated noise: the threshold under ML decoding corresponds to the value of a critical point of a particular random-bond Ising model (RBIM)  ([arXiv:1209.2157](https://arxiv.org/abs/1209.2157), [arXiv:1304.2975](https://arxiv.org/abs/1304.2975)). A threshold of $10.04(6)\%$ under mildly correlated bit-flip noise is obtained in Ref.  ([arXiv:1809.10704](https://arxiv.org/abs/1809.10704)).
- The toric code has a measurement threshold of one  ([arXiv:2402.00145](https://arxiv.org/abs/2402.00145)).
- Coherent noise: the threshold under ML decoding corresponds to the value of a critical point of a particular random-bond Ising model (RBIM) called the complex-coupled Ashkin-Teller model  ([arXiv:2410.22436](https://arxiv.org/abs/2410.22436), [arXiv:2411.05785](https://arxiv.org/abs/2411.05785)). Another statistical mechanical mapping has been studied for $X$-type noise channels interpolating between coherent and incoherent noise  ([arXiv:2412.21055](https://arxiv.org/abs/2412.21055)).
- Threshold of $1.5\%$ under real-time geometrically local decoder based on introducing an ancillary buffer and confining spacetime interactions between anyons   ([arXiv:2510.08056](https://arxiv.org/abs/2510.08056)).

## Threshold

- The threshold under ML decoding with measurement errors corresponds to the value of a critical point of a three-dimensional random plaquette model  ([arXiv:quant-ph/0110143](https://arxiv.org/abs/quant-ph/0110143), [arXiv:quant-ph/0207088](https://arxiv.org/abs/quant-ph/0207088)).
- $0.133\%$ for independent $X,Z$ noise and faulty syndrome measurements using a local automaton decoder  ([arXiv:1609.00510](https://arxiv.org/abs/1609.00510)).
- Toric-code thresholds for post-selected QEC can be studied with statistical mechanical models  ([arXiv:2410.07598](https://arxiv.org/abs/2410.07598)).

## Realizations

- Neutral atom arrays: One cycle of syndrome readout on 19-qubit planar and 24-qubit toric codes  ([arXiv:2112.03923](https://arxiv.org/abs/2112.03923)).

## Relations

- _parent_: [[concepts/qec/surface]] — The toric code is the surface code on a 2D torus.
- _parent_: [`higher_dimensional_toric`](https://errorcorrectionzoo.org/c/higher_dimensional_toric) — The $D$-dimensional twisted toric code reduces to the toric code for $D=2$ and a square lattice.
- _parent_: [`cyclic_hgp`](https://errorcorrectionzoo.org/c/cyclic_hgp) — The toric code can be obtained from a hypergraph product of two repetition codes  ([arXiv:1202.0928](https://arxiv.org/abs/1202.0928)). Other hypergraph products of two repetition codes yield the related $⟦2d^2-2d+1,1,d⟧$ CSS code family  ([arXiv:1202.0928](https://arxiv.org/abs/1202.0928)).
- _cousin_: [`string_net`](https://errorcorrectionzoo.org/c/string_net) — The toric code is the Turaev-Viro/Levin-Wen string-net code for the $\mathbb{Z}_2$ input category; equivalently, the construction of Ref.  ([arXiv:1002.2816](https://arxiv.org/abs/1002.2816)) on a genus-one handlebody yields the toric code.
- _cousin_: [`lifted_product`](https://errorcorrectionzoo.org/c/lifted_product) — A lifted-product code for the ring $R=\mathbb{F}_2[x,y]/(x^L-1,y^L-1)$ is the toric code  ([arXiv:2111.03654](https://arxiv.org/abs/2111.03654)).
- _cousin_: [`balanced_product`](https://errorcorrectionzoo.org/c/balanced_product) — Twisted toric codes can be obtained from balanced products of cyclic graphs over a cyclic group  ([arXiv:2012.09271](https://arxiv.org/abs/2012.09271)).
- _cousin_: [`repetition`](https://errorcorrectionzoo.org/c/repetition) — The toric code can be obtained from a hypergraph product of two repetition codes  ([arXiv:1202.0928](https://arxiv.org/abs/1202.0928)). Other hypergraph products of two repetition codes yield the related $⟦2d^2-2d+1,1,d⟧$ CSS code family  ([arXiv:1202.0928](https://arxiv.org/abs/1202.0928)).
- _cousin_: [`tetron`](https://errorcorrectionzoo.org/c/tetron) — Coherent physical errors in the toric code are expected to become incoherent logical errors under syndrome measurement; see corroborating numerical studies performed by embedding each physical qubit into two fermions via the tetron code  ([arXiv:1710.02270](https://arxiv.org/abs/1710.02270)) as well as deriving analytical bounds  ([arXiv:1912.04319](https://arxiv.org/abs/1912.04319)).
- _cousin_: [`rotated_surface`](https://errorcorrectionzoo.org/c/rotated_surface) — Rotating the square lattice by $\pi/4$ and choosing periodicity vectors on the rotated checkerboard lattice yields periodic checkerboard or rotated-toric variants with the same $⟦L^2,2,L⟧$ scaling, as well as non-bipartite odd-distance families with parameters $⟦t^2+(t+1)^2,1,2t+1⟧$  ([arXiv:1202.0928](https://arxiv.org/abs/1202.0928)).
- _cousin_: [`quantum_lego`](https://errorcorrectionzoo.org/c/quantum_lego) — The toric code can be constructed by arranging $⟦4,2,2⟧$ tensors on a square lattice and recovering the star and plaquette operators by operator pushing  ([arXiv:2109.08158](https://arxiv.org/abs/2109.08158)).
