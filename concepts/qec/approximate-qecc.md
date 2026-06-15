---
type: concept
name: Approximate quantum error-correcting code (AQECC)
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/spt
- concepts/qec/topological
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/approximate_qecc
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: approximate_qecc
---

# Approximate quantum error-correcting code (AQECC)

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/approximate_qecc) (`code_id: approximate_qecc`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Encodes quantum information so that it is possible to approximately recover that information from noise up to an error bound in recovery.

Many families of approximate block quantum codes become exact in the $n\to\infty$ limit (see children).
More generally, codes that become exact for some parameter values are called *quasi-exact*  ([arXiv:2105.14777](https://arxiv.org/abs/2105.14777)).

(source: raw/error-correction-zoo.md)

## Protection

Many of the state fidelity conditions that hold exactly for (exact) QECCs can be shown to hold up to some error $\epsilon$ for approximate QECCs.
Approximate correction has been formulated for certain types of correlated noise  ([arXiv:0909.1466](https://arxiv.org/abs/0909.1466)).

\subsection{Input-output fidelity}

This is the primary notion of closeness between states before and after error correction. 
It is defined as
\begin{align}
  \langle\psi|\mathcal{N}(|\psi\rangle\langle\psi|)|\psi\rangle~,
\end{align}
where $\mathcal{N}$ is the combination of encoding, noise, and recovery channels.
This quantity is difficult to compute, and there exist other quantities that are easier to work with and that also become 1 in the limit of perfect error correction.

\subsection{Entanglement fidelity}

Let $f(\rho_1,\rho_2)$ be the fidelity between quantum states.
Let the entanglement fidelity between channels $\mathcal{N}$ and $\mathcal{M}$ be defined as
\begin{align}
  F_{\rho}(\mathcal{N},\mathcal{M})
  = f( (\mathcal{N}\otimes\mathrm{id})\ket{\psi}\bra{\psi}, (\mathcal{M}\otimes\mathrm{id})\ket{\psi}\bra{\psi} )~,
\end{align}
where $\ket{\psi}$ is a purification of the mixed state $\rho$.
The worst-case entanglement fidelity is then defined as
\begin{align}
  F(\mathcal{N},\mathcal{M})=\min_{\rho} F_{\rho}(\mathcal{N},\mathcal{M})~.
\end{align}

Now, based on the Bures distance and worst-case entanglement fidelity, we define
\begin{align}
  d(\mathcal{N},\mathcal{M})=\sqrt{1-F(\mathcal{N},\mathcal{M})}
\end{align}
as a measure of distance between quantum channels~ ([arXiv:0907.5391](https://arxiv.org/abs/0907.5391)).

Given some encoding map $\mathcal{U}$ and some noise channel $\mathcal{E}$,
the code described by $\mathcal{U}$ is *$\epsilon$-correctable* if there exists
some quantum channel $\mathcal{D}$ such that
\begin{align}
  d(\mathcal{D}\mathcal{E}\mathcal{U}(\rho),\rho)\leq \epsilon
\end{align}
for all logical states $\rho$~ ([arXiv:0907.5391](https://arxiv.org/abs/0907.5391)).
When $\epsilon=0$ we can derive the standard \term{Knill-Laflamme conditions}  ([arXiv:1102.3809](https://arxiv.org/abs/1102.3809)).

Upper and lower bounds based on the average entanglement fidelity can be derived  ([arXiv:0907.5391](https://arxiv.org/abs/0907.5391)) ([arXiv:0907.3386](https://arxiv.org/abs/0907.3386)) ([arXiv:1103.0649](https://arxiv.org/abs/1103.0649)).
Riemannian optimization techniques can be applied to design approximate QECCs since the set of unitary encoding maps $U$ forms a Stiefel manifold  ([arXiv:2407.08423](https://arxiv.org/abs/2407.08423)).

\subsection{Complementary channel formulation}

Given a noise channel $\mathcal{E}$, there exists a recovery channel $\mathcal{D}$ such that
$F(\mathcal{D}\mathcal{E},\mathrm{id})=1-\epsilon$ iff there exists some $\mathcal{D}'$ such that
for complementary channel $\mathcal{E}^C$, $F(\mathcal{E}^C,\mathcal{D}')=1-\epsilon$
and $\mathcal{D}'(\rho)=\rho_0$ for some fixed $\rho_0$.
Note that $F$ denotes worst case entanglement fidelity between channels.

We can generalize this by replacing $\mathrm{id}$ with some channel $M$. Given noise channel $\mathcal{E}$,
there exists a recovery channel $\mathcal{D}$ such that
$F(\mathcal{D}\mathcal{E},\mathcal{M})=1-\epsilon$ iff there exists some $\mathcal{D}'$ such that
for complementary channel $\mathcal{E}^C$, $F(\mathcal{E}^C,\mathcal{D}'\mathcal{M}^C)=1-\epsilon$  ([arXiv:0907.5391](https://arxiv.org/abs/0907.5391)).
If $\mathcal{M}^C$ is a projection, this dual formulation yields the near-optimal estimate
\begin{align}
  \frac{1}{2}d(\mathcal{E}^C,\mathcal{E}^C\mathcal{M}^C)
  \leq \min_{\mathcal{D}}d(\mathcal{D}\mathcal{E},\mathcal{M})
  \leq d(\mathcal{E}^C,\mathcal{E}^C\mathcal{M}^C)~,
\end{align}
reducing the recovery problem to estimating the information leaked to the environment  ([arXiv:0907.5391](https://arxiv.org/abs/0907.5391)).

\subsection{Approximate error-correction conditions}
Analogously to the \term{Knill-Laflamme conditions} for (exact) QECCs, there exist various formulations of necessary and sufficient conditions for approximate error correction to determine if some code is $\epsilon$-correctable under a noise channel.

Necessary and sufficient conditions for approximate error correction can also be expressed in terms of
complementary channels.
Given some code defined by projector $\Pi = U U^\dagger$, $\Pi$ is *$\epsilon$-correctable*
with respect to some noise channel $\mathcal{E}$ if
\begin{align}
  \Pi E_i^{\dagger}E_j \Pi =\lambda_{ij}\Pi +\Pi B_{ij}\Pi ~,
\end{align}
where $\Lambda(\rho)=\mathrm{Tr}(\rho)\sum_{ij} \lambda_{ij}|i\rangle\langle j|$
is a density operator,
\begin{align}
  (\Lambda+B)(\rho)=\Lambda(\rho)+\sum_{ij}\mathrm{Tr}(\rho B_{ij})|i\rangle\langle j|
\end{align}
is the output state of the complementary noise channel $\mathcal{E}^C = \Lambda+B$, and the Bures distance $d(\Lambda+B,\Lambda)\le\epsilon$~ ([arXiv:0907.5391](https://arxiv.org/abs/0907.5391)).
An alternative measure, the *AQEC relative entropy*, measures the relative entropy between $\Lambda + B$ and $\Lambda$  ([arXiv:2312.16991](https://arxiv.org/abs/2312.16991)).
The non-correctable contributions $B_{ij}$ can be arranged in a signature vector that is amenable to numerical optimization in the space of Stiefel manifolds  ([arXiv:2410.07983](https://arxiv.org/abs/2410.07983), [arXiv:2504.20847](https://arxiv.org/abs/2504.20847)). 
The Frobenius norm of the matrix $B_{ij}$ bounds the difference between the two quantum weight enumerators  ([arXiv:2108.04434](https://arxiv.org/abs/2108.04434)).

In addition to the necessary and sufficient error correction conditions,
there exist sufficient conditions for AQECCs.
Given a noise channel $\mathcal{U}(\rho)=\sum_{n} A_n \rho A_n^{\dagger}$ where $\forall{n}$, $A_n$ is a Kraus operator, and code projector $\Pi $, express the following using polar decomposition, $A_n \Pi =U_n \sqrt{\Pi A_n^{\dagger}A_n \Pi }$, and let $p_n$ and $p_n\lambda_n$ be the largest and smallest eigenvalues for $\Pi A_n^{\dagger}A_n \Pi $.
Then, we are guaranteed that if
\begin{align}\Pi U_m^{\dagger}U_n \Pi =\delta_{mn} \Pi  \land p_n(1-\lambda_n)\le O( f(\epsilon) )\end{align}
we have a fidelity $F \geq 1-O( f(\epsilon) )$ after recovery~ ([arXiv:quant-ph/9704002](https://arxiv.org/abs/quant-ph/9704002)).

\subsection{Universal subspace AQECCs and alpha-bits}

Universal subspace approximate error correction is a type of approximate error correction that quantifies protection of information stored in (strict) subspaces of a logical space.
See also formulations of error correction for subsets that are not necessarily subspaces  ([arXiv:2112.01858](https://arxiv.org/abs/2112.01858)).

Given a subspace of a Hilbert space $\mathsf{S}$ of dimension $d$, noise channel $\mathcal{E}$, and encoding $\mathcal{U}$, we define the subspace as an *$\alpha$-dit* with error $\epsilon$ if, for all subspaces $\tilde{\mathsf{S}}$ of dimension less than or equal to $d^{\alpha}+1$,
there exists some channel $\tilde{\mathcal{D}}$ such that
\begin{align}||(\tilde{\mathcal{D}}\circ \mathcal{E}\circ \mathcal{U})|\psi\rangle-|\psi\rangle||_1\leq \epsilon\end{align}
for all $|\psi\rangle\in \tilde{\mathsf{S}}$~ ([arXiv:1706.09434](https://arxiv.org/abs/1706.09434)).

Generalizing the notion of quantum information transmission and capacity of (exact) QECCs, one can achieve an $\alpha$-bit transmission rate $r$ for quantum channel $\mathcal{E}$ iff,
for sufficiently large $d$ and $n$, and for all $\epsilon>0$, the channel $\mathcal{E}^{\otimes n}$
is able to transmit
\begin{align}\left\lceil \frac{n r}{\log(d)} \right\rceil\quad \textup{$\alpha$-dits}\end{align}
with total error $\epsilon$ across those $\alpha$-dits.
The $\alpha$-bit capacity $Q$ of $\mathcal{E}$
is defined as the supremum of achievable transmission rates~ ([arXiv:1706.09434](https://arxiv.org/abs/1706.09434)).

\subsection{Other metrics of approximate error correction}

\begin{enumerate}[(1)]
\item \begin{defterm}{Code space complexity}
\label{topic:codespace-complexity}
One can relate robustness of an approximate quantum code to the quantum *circuit complexity*  ([arXiv:1210.1281](https://arxiv.org/abs/1210.1281), [arXiv:1402.5674](https://arxiv.org/abs/1402.5674), [arXiv:1301.1363](https://arxiv.org/abs/1301.1363), [arXiv:1607.05256](https://arxiv.org/abs/1607.05256)) of creating states in the codespace.
For a family of block codes, scaling as order $O(k/n)$ of a code parameter called the *subsystem variance* characterizes the transition between code subspaces with low and high circuit complexity  ([arXiv:2310.04710](https://arxiv.org/abs/2310.04710)).
The Lovasz local lemma yields a trade-off between circuit complexity and local indistinguishability  ([arXiv:2510.04453](https://arxiv.org/abs/2510.04453)).
\end{defterm}
\item *Integrity* measures how well a code state $\psi$ and an orthogonal state can be distinguished in trace distance after noise and recovery are applied  ([arXiv:1707.09951](https://arxiv.org/abs/1707.09951)).
\end{enumerate}

## Rate

An extension of the BPT bound to approximate codes is done in Ref.  ([arXiv:1610.06169](https://arxiv.org/abs/1610.06169)).

## Encoders

- Given a decoder, an encoding that yields the optimal entanglement fidelity can be obtained by solving a semi-definite program  ([arXiv:quant-ph/0109155](https://arxiv.org/abs/quant-ph/0109155), [arXiv:quant-ph/0307138](https://arxiv.org/abs/quant-ph/0307138), [arXiv:0706.3400](https://arxiv.org/abs/0706.3400), [arXiv:0708.3658](https://arxiv.org/abs/0708.3658))).
- Variational quantum circuit encoder  ([arXiv:2204.03560](https://arxiv.org/abs/2204.03560)).

## Decoders

- Given an encoding and a noise channel, a decoder that yields the optimal entanglement fidelity can be obtained by solving a semi-definite program  ([arXiv:quant-ph/0109155](https://arxiv.org/abs/quant-ph/0109155), [arXiv:quant-ph/0307138](https://arxiv.org/abs/quant-ph/0307138), [arXiv:quant-ph/0606105](https://arxiv.org/abs/quant-ph/0606105), [arXiv:0706.3400](https://arxiv.org/abs/0706.3400), [arXiv:0708.3658](https://arxiv.org/abs/0708.3658)). This optimal decoder is robust to unexpected variations in the noise channel  ([arXiv:0905.3838](https://arxiv.org/abs/0905.3838)).
- The *decoupling approach* a.k.a. the *Uhlmann decoder*  ([arXiv:quant-ph/0702005](https://arxiv.org/abs/quant-ph/0702005), [arXiv:1004.1641](https://arxiv.org/abs/1004.1641), [arXiv:1012.6044](https://arxiv.org/abs/1012.6044)).
- Quantum machine-learning based decoders such as quantum convolutional neural networks  ([arXiv:1810.03787](https://arxiv.org/abs/1810.03787)) and quantum autoencoders  ([arXiv:2202.00555](https://arxiv.org/abs/2202.00555)).
- The *Leung recovery map*  ([arXiv:quant-ph/9704002](https://arxiv.org/abs/quant-ph/9704002)) for a noise channel whose Kraus operators $E_j$ yield a diagonal QEC matrix, $c_{ij}\propto\delta_{ij}$, has Kraus operators $\Pi V_j^{\dagger}$, where $\Pi$ is the codespace projection, and where $V_j$ is the unitary from the polar decomposition of $E_j \Pi$. This is the recovery used in the proof of the Knill-Laflamme conditions  ([doi:10.1017/CBO9780511976667](https://doi.org/10.1017/CBO9780511976667)).
- A near-optimal recovery channel can be constructed from a saddle point in the complementary-channel optimization, achieving recovery error $d(\widetilde{\mathcal{D}}\mathcal{E},\mathcal{M})\leq d(\mathcal{E}^C,\mathcal{E}^C\mathcal{M}^C)$ whenever $\mathcal{M}^C$ is a projection  ([arXiv:0907.5391](https://arxiv.org/abs/0907.5391)).
- The *Cafaro recovery map*  ([arXiv:1308.4582](https://arxiv.org/abs/1308.4582)) can be obtained for noise Kraus operators if there exists a basis of error words with respect to which the uncorrectable piece in the Knill-Laflamme conditions is diagonal; see Ref.  ([arXiv:2406.02444](https://arxiv.org/abs/2406.02444)). The map recovers information perfectly for strictly correctable noise.
- The *Petz recovery map* a.k.a. the *transpose map*  ([doi:10.1007/BF01212345](https://doi.org/10.1007/BF01212345), [doi:10.1093/qmath/39.1.97](https://doi.org/10.1093/qmath/39.1.97), [arXiv:1810.03150](https://arxiv.org/abs/1810.03150)), a quantum channel determined by the codespace and noise channel, yields an infidelity of recovery that is at most twice away from the infidelity of the best possible recovery  ([arXiv:quant-ph/0004088](https://arxiv.org/abs/quant-ph/0004088)). The fidelity can be expressed exactly as a function of the \term{Knill-Laflamme conditions}  ([arXiv:2401.02022](https://arxiv.org/abs/2401.02022)), and it can be used to derive a generalization of the \term{Knill-Laflamme conditions} for approximate QECCs  ([arXiv:0909.0931](https://arxiv.org/abs/0909.0931), [arXiv:1202.5139](https://arxiv.org/abs/1202.5139)). Satisfaction of the \term{Knill-Laflamme conditions} is sufficient but not necessary for the Petz recovery map to be the optimal recovery, and a necessary and sufficient condition has been derived  ([arXiv:2410.23622](https://arxiv.org/abs/2410.23622)). The infidelity of a modified Petz recovery map under erasure can be bounded using the conditional mutual information via the *approximate Petz theorem*  ([arXiv:1410.0664](https://arxiv.org/abs/1410.0664), [arXiv:1509.07127](https://arxiv.org/abs/1509.07127), [arXiv:1610.06169](https://arxiv.org/abs/1610.06169)). In the case of topological codes, the Petz infidelity is related to the topological entanglement entropy  ([arXiv:2408.00857](https://arxiv.org/abs/2408.00857)). Modifications include the Petz-like decoder  ([arXiv:2405.06051](https://arxiv.org/abs/2405.06051)), the temporal Petz recovery map for dynamical codes  ([arXiv:2502.09177](https://arxiv.org/abs/2502.09177)), and a syndrome-based Petz recovery  ([arXiv:2510.08719](https://arxiv.org/abs/2510.08719)). The Petz map is related to quantum Bayes' rule  ([arXiv:2410.00319](https://arxiv.org/abs/2410.00319)).
- The Yoshida-Kitaev decoder for the Hayden-Preskill protocol  ([arXiv:1710.03363](https://arxiv.org/abs/1710.03363)) can be extended to general QECCs  ([arXiv:2405.06051](https://arxiv.org/abs/2405.06051)).
- If parts of the \term{Knill-Laflamme conditions} are violated, a deterministic recovery operation is not possible. However, a probabilistic recovery and a modified version of the conditions can still be constructed  ([arXiv:2410.00155](https://arxiv.org/abs/2410.00155)).

## Relations

- _parent_: [`approximate_oaecc`](https://errorcorrectionzoo.org/c/approximate_oaecc)
- _cousin_: [[concepts/qec/topological]] — In the case of topological codes, the Petz infidelity is related to the topological entanglement entropy  ([arXiv:2408.00857](https://arxiv.org/abs/2408.00857)).
- _cousin_: [[concepts/qec/spt]] — Certain phases with continuous symmetries cannot be prepared using a constant-depth circuit, a consequence of the Lieb-Schult-Mattis theorem  ([doi:10.1016/0003-4916(61)90115-4](https://doi.org/10.1016/0003-4916(61)90115-4), [arXiv:cond-mat/9911137](https://arxiv.org/abs/cond-mat/9911137), [arXiv:2112.06946](https://arxiv.org/abs/2112.06946), [arXiv:2405.14929](https://arxiv.org/abs/2405.14929)). The theorem, in turn, can be linked to the circuit complexity of the underlying approximate error-correcting code  ([arXiv:2510.04453](https://arxiv.org/abs/2510.04453)).
- _cousin_: [`stiefel`](https://errorcorrectionzoo.org/c/stiefel) — Riemannian optimization techniques can be applied to design approximate QECCs since the set of unitary encoding maps $U$ forms a Stiefel manifold  ([arXiv:2407.08423](https://arxiv.org/abs/2407.08423)).

## Notes

- See review  ([arXiv:2208.00365](https://arxiv.org/abs/2208.00365)).
