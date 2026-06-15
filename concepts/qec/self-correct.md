---
type: concept
name: Self-correcting quantum code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Self-correcting quantum memory
- Thermally stable encoding
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/2d-stabilizer
- concepts/qec/3d-bacon-shor
- concepts/qec/3d-stabilizer
- concepts/qec/3d-subsystem-surface
- concepts/qec/3d-surface
- concepts/qec/4d-surface
- concepts/qec/color
- concepts/qec/general-qldpc
- concepts/qec/haah-cubic
- concepts/qec/hypergraph-product
- concepts/qec/quantum-concatenated
- concepts/qec/quantum-double
- concepts/qec/quantum-expander
- concepts/qec/quantum-repetition
- concepts/qec/surface
- concepts/qec/symmetry-protected-self-correct
- concepts/qec/translationally-invariant-stabilizer
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/self_correct
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: self_correct
---

# Self-correcting quantum code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/self_correct) (`code_id: self_correct`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A block quantum code that forms the ground-state subspace of an $n$-body geometrically local Hamiltonian whose logical information is recoverable for arbitrarily long times in the $n\to\infty$ limit after interaction with a sufficiently cold thermal environment.
Typically, one also requires a decoder whose decoding time scales polynomially with $n$ and a finite energy density.

The original criteria for a self-correcting quantum memory, informally known as the *Caltech rules*  ([arXiv:1411.7046](https://arxiv.org/abs/1411.7046), [arXiv:1501.04112](https://arxiv.org/abs/1501.04112)), also required finite-spin Hamiltonians.
A concatenated quantum code with self-simulating control elements based on work by Gacs  ([doi:10.1145/800061.808730](https://doi.org/10.1145/800061.808730), [doi:10.1016/0022-0000(86)90002-4](https://doi.org/10.1016/0022-0000(86)90002-4), [arXiv:math/0003117](https://arxiv.org/abs/math/0003117)) yields a self-correcting quantum memory in 2D  ([arXiv:2601.20818](https://arxiv.org/abs/2601.20818)).

The effect of a Markovian thermal environment consists of a Lindbladian in Davies form admitting a Gibbs steady state at some temperature $T$  ([arXiv:1411.6643](https://arxiv.org/abs/1411.6643)).
To test whether a system is self-correcting, an initial codeword $\rho(0)$ is evolved under the Davies Lindbladian and the code Hamiltonian (or, if we are to allow extra passive protection, the code Lindbladian) to the state $\rho(t)$ at time $t$, after which it is decoded via decoding map $\cal{D}$.
The memory time $\tau$ is defined to be
\begin{align}
  \tau=\sup\left\{ t>0\,|\left\Vert {\cal D}( \rho(t) )-\rho(0)\right\Vert _{1}<\epsilon\right\}
\end{align}
for some fixed $\epsilon$.
For a self-correcting memory, there exists a critical temperature $T_\star>0$ such that $\tau\to\infty$ (typically, exponentially with $n$) as $n\to\infty$ for any temperature $T<T_{\star}$ and any codeword $\rho(0)$.
A memory is *partially self-correcting* if $\tau$ scales polynomially with $n$ up to some cutoff $n_{max}$.
A self-correcting memory is typically associated with a (stable) phase of quantum matter.

(source: raw/error-correction-zoo.md)

## Protection

Self-correcting classical memories exist in two and higher dimensions, with the canonical example being the classical Ising model.
In that model, a classical bit is stored in the overall magnetization. The magnetization is thermally stable due to the fact that there is an $n$-dependent (i.e., *macroscopic*) energy cost of flipping a contiguous region of physical bits  ([doi:10.1017/S0305004100019174](https://doi.org/10.1017/S0305004100019174), [arXiv:1411.6643](https://arxiv.org/abs/1411.6643)).
This cost scales with the surface area of the region, and the surface area is $n$-dependent for dimensions greater than one.

Self-correcting quantum memories are known in four and higher dimensions, and a concatenated construction with self-simulating control elements yields one in 2D  ([arXiv:2601.20818](https://arxiv.org/abs/2601.20818)). Existence in one dimension is impossible (see, e.g., Ref.  ([arXiv:2510.08533](https://arxiv.org/abs/2510.08533))), and existence in three dimensions remains an open question.
For similar reasons as the classical 2D Ising model is a self-correcting classical memory, the 4D loop toric code is a self-correcting quantum memory due to an order $O(n)$ energy cost of creating a logical error  ([arXiv:quant-ph/0110143](https://arxiv.org/abs/quant-ph/0110143), [arXiv:0811.0033](https://arxiv.org/abs/0811.0033)).
On the other hand, the 2D surface code is not thermally stable  ([arXiv:quant-ph/0702102](https://arxiv.org/abs/quant-ph/0702102), [arXiv:0709.2717](https://arxiv.org/abs/0709.2717), [arXiv:0810.4584](https://arxiv.org/abs/0810.4584), [arXiv:0911.3843](https://arxiv.org/abs/0911.3843), [arXiv:2410.01206](https://arxiv.org/abs/2410.01206)) because its string-like logical operators anti-commute with stabilizer generators supported only at their ends, and thus have a constant energy cost of creation.
There is a general upper bound on the relaxation rate of a qubit stabilizer or qubit subsystem stabilizer quantum memory interacting with a Markovian environment  ([arXiv:0907.2807](https://arxiv.org/abs/0907.2807)).

An $n$-dependent energy barrier to creating all logical errors is likely necessary for a thermally stable memory, having been shown as such for a large class of 2D topological phases  ([arXiv:0810.3557](https://arxiv.org/abs/0810.3557), [arXiv:1412.2858](https://arxiv.org/abs/1412.2858)) including Abelian  ([arXiv:1601.01324](https://arxiv.org/abs/1601.01324)) and non-Abelian  ([arXiv:2107.01628](https://arxiv.org/abs/2107.01628)) quantum doubles.
Two-dimensional stabilizer codes  ([arXiv:0810.1983](https://arxiv.org/abs/0810.1983)) and encodings of frustration-free code Hamiltonians  ([arXiv:1209.5750](https://arxiv.org/abs/1209.5750)) admit only constant-energy excitations, and so do not admit such a barrier.
No-go theorems for 3D models are much more restrictive  ([arXiv:1105.4159](https://arxiv.org/abs/1105.4159)), e.g., a 3D lattice stabilizer code with a locality-preserving non-Clifford gate cannot have a microscopic energy barrier  ([arXiv:1408.1720](https://arxiv.org/abs/1408.1720)).
2D stabilizer codes  ([arXiv:0810.1983](https://arxiv.org/abs/0810.1983)) and encodings of frustration-free code Hamiltonians  ([arXiv:1209.5750](https://arxiv.org/abs/1209.5750)) admit only constant-energy excitations, and so do not have an energy barrier.
More generally, translationally invariant CSS codes are not self-correcting at high temperature  ([arXiv:2510.03090](https://arxiv.org/abs/2510.03090)).
There exist several candidates for self-correction as well as several partially self-correcting memories (see cousins below).

The lifetime of a ground-state memory protected by a Hamiltonian alone can increase at most logarithmically with $n$ under depolarizing noise  ([arXiv:0807.0287](https://arxiv.org/abs/0807.0287), [arXiv:0904.4861](https://arxiv.org/abs/0904.4861)), and a clock Hamiltonian can saturate this bound  ([arXiv:0904.4861](https://arxiv.org/abs/0904.4861)).

## Relations

- _parent_: [[concepts/qec/symmetry-protected-self-correct]] — Self-correcting quantum codes do no require a symmetry for protection, so in that sense they are protected by a trivial symmetry.
- _cousin_: [[concepts/qec/surface]] — The surface code is not thermally stable  ([arXiv:quant-ph/0702102](https://arxiv.org/abs/quant-ph/0702102), [arXiv:0709.2717](https://arxiv.org/abs/0709.2717), [arXiv:0810.4584](https://arxiv.org/abs/0810.4584), [arXiv:0911.3843](https://arxiv.org/abs/0911.3843), [arXiv:2410.01206](https://arxiv.org/abs/2410.01206)) because its string-like logical operators anti-commute with stabilizer generators supported only at their ends, and thus have a constant energy cost of creation. Various candidates for self-correcting quantum memories have been constructed by coupling neighboring anyons in the code so as to prevent them from spreading  ([arXiv:0812.4622](https://arxiv.org/abs/0812.4622), [arXiv:0908.4264](https://arxiv.org/abs/0908.4264), [arXiv:1101.6028](https://arxiv.org/abs/1101.6028)),arxiv:1406.2338,arxiv:1511.05579,arxiv:1512.04528,arxiv:2510.08056}.
- _cousin_: [[concepts/qec/2d-stabilizer]] — 2D stabilizer codes  ([arXiv:0810.1983](https://arxiv.org/abs/0810.1983)) and encodings of frustration-free code Hamiltonians  ([arXiv:1209.5750](https://arxiv.org/abs/1209.5750)) admit only constant-energy excitations, and so do not have an energy barrier.
- _cousin_: [[concepts/qec/quantum-double]] — An $n$-dependent energy barrier to creating all logical errors is likely necessary for a thermally stable memory, having been shown as such for a large class of 2D topological phases  ([arXiv:0810.3557](https://arxiv.org/abs/0810.3557), [arXiv:1412.2858](https://arxiv.org/abs/1412.2858)) including Abelian  ([arXiv:1601.01324](https://arxiv.org/abs/1601.01324)) and non-Abelian  ([arXiv:2107.01628](https://arxiv.org/abs/2107.01628)) quantum doubles.
- _cousin_: [[concepts/qec/3d-stabilizer]] — 3D translationally-invariant qubit stabilizer code families with constant $k$ support logical string operators and thus cannot be self-correcting  ([arXiv:1103.1885](https://arxiv.org/abs/1103.1885)). For non-constant $k$, such families can support at most a logarithmic energy barrier  ([arXiv:1101.1962](https://arxiv.org/abs/1101.1962)).
- _cousin_: [[concepts/qec/3d-surface]] — The 3D welded surface code is partially self-correcting with a power-law energy barrier  ([arXiv:1406.4227](https://arxiv.org/abs/1406.4227)). The 3D toric code is a classical self-correcting memory, whose protected bit admits a membrane-like logical operator  ([arXiv:1501.04112](https://arxiv.org/abs/1501.04112)), but it is not a quantum self-correcting memory because the star terms thermalize  ([arXiv:2510.03090](https://arxiv.org/abs/2510.03090)).
- _cousin_: [[concepts/qec/3d-subsystem-surface]] — The 3D subsystem surface code is not a self-correcting quantum memory despite being a single-shot code  ([arXiv:2305.06389](https://arxiv.org/abs/2305.06389)).
- _cousin_: [[concepts/qec/4d-surface]] — For similar reasons as the classical 2D Ising model is a self-correcting classical memory, the 4D loop toric code is a self-correcting quantum memory due to an order $O(n)$ energy cost of creating a logical error  ([arXiv:quant-ph/0110143](https://arxiv.org/abs/quant-ph/0110143), [arXiv:0811.0033](https://arxiv.org/abs/0811.0033)).
- _cousin_: [[concepts/qec/color]] — The 6D color code is a self-correcting quantum memory and admits a fault-tolerant universal gate set in 7D  ([arXiv:0907.5228](https://arxiv.org/abs/0907.5228)).
- _cousin_: [[concepts/qec/haah-cubic]] — Cubic code 1 is partially self-correcting with a logarithmic energy barrier  ([arXiv:1112.3252](https://arxiv.org/abs/1112.3252)).
- _cousin_: [[concepts/qec/translationally-invariant-stabilizer]] — Translationally invariant CSS codes are not self-correcting at high temperature  ([arXiv:2510.03090](https://arxiv.org/abs/2510.03090)).
- _cousin_: [[concepts/qec/quantum-repetition]] — The bit-flip repetition code associated with the 2D classical Ising model is a self-correcting classical memory  ([arXiv:1411.6643](https://arxiv.org/abs/1411.6643)).
- _cousin_: [`repetition`](https://errorcorrectionzoo.org/c/repetition) — The repetition code associated with the 2D classical Ising model is a self-correcting classical memory  ([doi:10.1007/BF02124328](https://doi.org/10.1007/BF02124328)) ([arXiv:1411.6643](https://arxiv.org/abs/1411.6643)).
- _cousin_: [[concepts/qec/3d-bacon-shor]] — 3D Bacon-Shor codes were conjectured to be self-correcting  ([arXiv:quant-ph/0506023](https://arxiv.org/abs/quant-ph/0506023)), but there remain issues to be resolved in order to validate this conjecture (see  ([arXiv:1411.6643](https://arxiv.org/abs/1411.6643))).
- _cousin_: [`expander`](https://errorcorrectionzoo.org/c/expander) — Constant-rate random (quantum) expander codes are self-correcting (quantum) memories, but have no thermodynamic phase transitions  ([arXiv:2403.10599](https://arxiv.org/abs/2403.10599)).
- _cousin_: [[concepts/qec/quantum-expander]] — Constant-rate random (quantum) expander codes are self-correcting (quantum) memories, but have no thermodynamic phase transitions  ([arXiv:2403.10599](https://arxiv.org/abs/2403.10599)).
- _cousin_: [[concepts/qec/hypergraph-product]] — There are bounds on the energy barrier of hypergraph product codes  ([arXiv:2407.20526](https://arxiv.org/abs/2407.20526)).
- _cousin_: [[concepts/qec/general-qldpc]] — Linear confinement of QLDPC (LDPC) codes implies (classical) self-correction  ([arXiv:2403.10599](https://arxiv.org/abs/2403.10599)).
- _cousin_: [`ldpc`](https://errorcorrectionzoo.org/c/ldpc) — Linear confinement of QLDPC (LDPC) codes implies (classical) self-correction  ([arXiv:2403.10599](https://arxiv.org/abs/2403.10599)).
- _cousin_: [[concepts/qec/quantum-concatenated]] — A concatenated quantum code with self-simulating control elements based on work by Gacs  ([doi:10.1145/800061.808730](https://doi.org/10.1145/800061.808730), [doi:10.1016/0022-0000(86)90002-4](https://doi.org/10.1016/0022-0000(86)90002-4), [arXiv:math/0003117](https://arxiv.org/abs/math/0003117)) yields a self-correcting quantum memory in 2D  ([arXiv:2601.20818](https://arxiv.org/abs/2601.20818)).

## Notes

- Reviews of self-correcting memories  ([arXiv:1210.3207](https://arxiv.org/abs/1210.3207), [arXiv:1411.6643](https://arxiv.org/abs/1411.6643)).
