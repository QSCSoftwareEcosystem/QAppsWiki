---
type: concept
name: Gottesman-Kitaev-Preskill (GKP) code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/4d-stabilizer
- concepts/qec/holographic
- concepts/qec/quantum-lattice
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/multimodegkp
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: multimodegkp
---

# Gottesman-Kitaev-Preskill (GKP) code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/multimodegkp) (`code_id: multimodegkp`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Quantum lattice code for a non-degenerate lattice, thereby admitting a finite-dimensional logical subspace.
Codes on $n$ modes can be constructed from lattices with $2n$-dimensional full-rank Gram matrices $A$.
Any GKP code can be generated from a Gram matrix in standard form via a Gaussian unitary transformation  ([arXiv:2412.02442](https://arxiv.org/abs/2412.02442)).

The centralizer for the stabilizer group within the displacement operators case can be identified with the symplectic dual lattice ${\mathcal{L}}^{\perp}$ (i.e. all points in $\mathbb{R}^{2n}$ that have integer symplectic inner product with all points in ${\mathcal{L}}$ ), such that logical operations are identified with the dual quotients ${\mathcal{L}}^{\perp}/{\mathcal{L}}$. The size of this dual quotient is the determinant of the Gram matrix, yielding the logical dimension $d=\sqrt{\| \det{A}\|}$  ([arXiv:quant-ph/0008040](https://arxiv.org/abs/quant-ph/0008040)).
Stabilizer generator matrices equivalent under symplectic transformations are classified by distinct Hermite normal forms  ([arXiv:2109.14645](https://arxiv.org/abs/2109.14645)).

The space of all single-mode GKP codes is the moduli space of elliptic curves, i.e., the three sphere with a trefoil knot removed  ([arXiv:2407.03270](https://arxiv.org/abs/2407.03270)).

(source: raw/error-correction-zoo.md)

## Protection

The level of protection against displacement errors is quantified by the Euclidean code distance $\Delta=\min_{x\in {\mathcal{L}}^{\perp}\setminus {\mathcal{L}}} \|x\|_2$  ([arXiv:2109.14645](https://arxiv.org/abs/2109.14645)). There are upper bounds on this distance  ([arXiv:2109.14645](https://arxiv.org/abs/2109.14645), [doi:10.1109/ITW61385.2024.10806993](https://doi.org/10.1109/ITW61385.2024.10806993)).

## Rate

Transmission schemes with multimode GKP codes achieve a lower bound on displacement noise and a lower bound on the thermal-noise Gaussian channel capacities  ([arXiv:quant-ph/0105058](https://arxiv.org/abs/quant-ph/0105058), [arXiv:1708.07257](https://arxiv.org/abs/1708.07257), [arXiv:1801.04731](https://arxiv.org/abs/1801.04731), [arXiv:1801.07271](https://arxiv.org/abs/1801.07271)). 
Particular random lattice families of multimode GKP codes achieve the hashing bound of the displacement noise channel  ([arXiv:quant-ph/0105058](https://arxiv.org/abs/quant-ph/0105058)).
Particular families of GKP codes achieve the capacity of AD and amplification channels for some loss rates  ([arXiv:2412.06715](https://arxiv.org/abs/2412.06715)).

## Encoders

- GKP codes with fixed $n$ and prime-dimensional logical Hilbert space are symplectically related to a disjoint product of single-mode GKP codes on $n$ modes, such that encoding via Gaussian unitaries is possible.
- Dissipative stabilization of finite-energy GKP states using stabilizers conjugated by *cooling* ( ([arXiv:1310.7596](https://arxiv.org/abs/1310.7596)), Appx. B) or *damping* operator, i.e., a damped exponential of the total occupation number  ([arXiv:2009.07941](https://arxiv.org/abs/2009.07941), [arXiv:2201.12337](https://arxiv.org/abs/2201.12337)).
- Logical Bell state can be created from two canonical GKP states by applying a beamsplitter  ([arXiv:2008.12791](https://arxiv.org/abs/2008.12791)).

## General gates

- Gaussian operations and homodyne measurements on non-magic GKP states are classically simulable  ([arXiv:2406.06418](https://arxiv.org/abs/2406.06418)), and there is a sufficient condition for an additional element to achieve universal quantum computation  ([arXiv:2309.07820](https://arxiv.org/abs/2309.07820)). There is an algorithm for GKP circuit simulation whose runtime scales with the amount of negativity of the Zak-Gross Wigner function  ([arXiv:2412.13136](https://arxiv.org/abs/2412.13136)).
- There is a relation between magic (i.e., how far away a state is from being a stabilizer state) and non-Gaussianity for GKP codewords  ([arXiv:2109.13018](https://arxiv.org/abs/2109.13018), [arXiv:2406.06418](https://arxiv.org/abs/2406.06418)). In particular, implementing a non-Clifford logical gate requires a higher degree of non-Gaussianity than that expressed by ideal non-normalizable GKP states  ([arXiv:2406.06418](https://arxiv.org/abs/2406.06418)).
- By applying GKP error correction to Gaussian input states, computational universality can be achieved without additional non-Gaussian elements   ([arXiv:1903.00012](https://arxiv.org/abs/1903.00012)). This procedure can be alternatively described as performing heterodyne detection on one half of a GKP encoded Bell pair. The cubic phase gate is not a suitable gate  ([arXiv:2009.05309](https://arxiv.org/abs/2009.05309)).
- Logical shadow tomography protocol  ([arXiv:2411.00235](https://arxiv.org/abs/2411.00235)).
- Some gates have a constant logical gate error even in the limit of infinite squeezing  ([arXiv:2509.14658](https://arxiv.org/abs/2509.14658)).

## Fault tolerance

- Logical Clifford operations are given by Gaussian unitaries, which map bounded-size errors to bounded-size errors  ([arXiv:quant-ph/0008040](https://arxiv.org/abs/quant-ph/0008040)). For single-mode GKP codes, these operations correspond to non-trivial loops in the space of all single-mode GKP codes (the moduli space of elliptic curves, i.e., the three sphere with a trefoil knot removed)  ([arXiv:2407.03270](https://arxiv.org/abs/2407.03270)). Such gates provide another example of monodromy under the particular notion of parallel transport introduced in Ref.  ([arXiv:1309.7062](https://arxiv.org/abs/1309.7062)).
- The 4D square-lattice GKP code admits the isthmus property, which allows certain ancilla errors to be detectable  ([arXiv:2201.12337](https://arxiv.org/abs/2201.12337)).

## Decoders

- Syndrome extraction is performed by measuring stabilizers and correcting. Issues arising from the use of finite-energy approximate states can be mitigated  ([arXiv:2504.13383](https://arxiv.org/abs/2504.13383)).
- The MLD decoder for Gaussian displacement errors is realized by evaluating a lattice theta function, and in general the decision can be approximated by either solving (approximating) the closest vector problem (CVP)  ([doi:10.1109/TIT.2002.800499](https://doi.org/10.1109/TIT.2002.800499)) (a.k.a. closest lattice point problem) or by using other effective iterative schemes when, e.g., the lattice represents a concatenated GKP code  ([arXiv:1810.00047](https://arxiv.org/abs/1810.00047), [arXiv:1908.03579](https://arxiv.org/abs/1908.03579), [arXiv:2109.14645](https://arxiv.org/abs/2109.14645), [arXiv:2111.07029](https://arxiv.org/abs/2111.07029)). While the decoder time scales exponentially with number of modes $n$ generically, the time can be polynomial in $n$ for certain codes  ([arXiv:2303.04702](https://arxiv.org/abs/2303.04702)).
- Babai's nearest plane algorithm  ([doi:10.1007/bf02579403](https://doi.org/10.1007/bf02579403)) can be used for bounded-distance decoding  ([arXiv:2303.04702](https://arxiv.org/abs/2303.04702)).
- Combining AD noise with amplification yields displacement noise, the noise that GKP codes are designed to correct  ([arXiv:quant-ph/0008046](https://arxiv.org/abs/quant-ph/0008046), [arXiv:1801.07271](https://arxiv.org/abs/1801.07271)).
- ML decoder for correcting shift errors in GKP two-qubit gates  ([arXiv:2103.06994](https://arxiv.org/abs/2103.06994)).

## Relations

- _parent_: [[concepts/qec/quantum-lattice]] — GKP codes are $n$-mode quantum lattice codes with $2n$ stabilizers, i.e., constructed using a non-degenerate lattice.
- _cousin_: [`t-designs`](https://errorcorrectionzoo.org/c/t-designs) — GKP states on $n$ modes and their displaced versions for all possible lattices form a rigged 2-design for all $n$  ([arXiv:2412.17909](https://arxiv.org/abs/2412.17909)).
- _cousin_: [[concepts/qec/holographic]] — GKP codespaces exist in the CFT dual of a particular holographic framework  ([arXiv:2312.16298](https://arxiv.org/abs/2312.16298), [arXiv:2412.19653](https://arxiv.org/abs/2412.19653)).
- _cousin_: [[concepts/qec/4d-stabilizer]] — The 4D square-lattice GKP code admits the isthmus property, which allows certain ancilla errors to be detectable  ([arXiv:2201.12337](https://arxiv.org/abs/2201.12337)).

## Notes

- Reviews on GKP codes presented in Refs.  ([arXiv:2002.11008](https://arxiv.org/abs/2002.11008), [arXiv:2106.12989](https://arxiv.org/abs/2106.12989), [arXiv:2308.02913](https://arxiv.org/abs/2308.02913), [arXiv:2412.02442](https://arxiv.org/abs/2412.02442), [arXiv:2507.06943](https://arxiv.org/abs/2507.06943)).
