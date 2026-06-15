---
type: concept
name: Subsystem modular-qudit stabilizer code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Gauge modular-qudit stabilizer code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/qudit-stabilizer
- concepts/qec/subsystem-qudits-into-qudits
- concepts/qec/subsystem-stabilizer
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/qudit_subsystem_stabilizer
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: qudit_subsystem_stabilizer
---

# Subsystem modular-qudit stabilizer code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/qudit_subsystem_stabilizer) (`code_id: qudit_subsystem_stabilizer`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Modular-qudit generalization of a subsystem qubit stabilizer code.
Can be obtained by taking a modular-qudit stabilizer code and assigning some of its logical qudits to be gauge qudits.
For composite qudit dimensions, such codes need not encode an integer number of qudits.

Subsystem stabilizer codes are defined by a gauge group $\mathsf{G}$ and a stabilizer group $\mathsf{S}$, both subgroups of the $n$-modular-qudit Pauli group $\mathsf{P}_n$ that satisfy $\mathsf{Z}(\mathsf{G})=\mathsf{S}$, where $\mathsf{Z}$ denotes taking the center of a group.

A code can be constructed by starting with either group.
Given an $\mathsf{S}$, one can pick any $\mathsf{G}$ satisfying $\mathsf{S}\subseteq\mathsf{G}\subseteq\mathsf{N(S)}$, where $\mathsf{N(S)}$ is the normalizer of the stabilizer group within $\mathsf{P}_n$.
Alternatively, given a $\mathsf{G}$, one defines $\mathsf{S}$ to be the center of the gauge group.

The logical Pauli group is $\mathsf{N}(\mathsf{G})/\mathsf{S}$.
As such, the case when $\mathsf{G}=\mathsf{S}$ reduces to an ordinary stabilizer code, while the case $\mathsf{G}=\mathsf{N(S)}$ reduces to a trivial code.

One can gauge fix  ([arXiv:quant-ph/0508131](https://arxiv.org/abs/quant-ph/0508131)) an Abelian subgroup of the gauge group by adding it to the stabilizer group.
\begin{defterm}{Gauge fixing}
\label{topic:gauge-fixing}
Gauge fixing is a map between subsystem codes that is done using an Abelian subgroup $\mathsf{F}\subseteq\mathsf{G}$,
\begin{align}
\begin{split}
  \mathsf{S}&\to\left\langle \mathsf{S},\mathsf{F}\right\rangle \\
  \mathsf{G}&\to\mathsf{N}_{\mathsf{G}}\left(\mathsf{F}\right)~,
\end{split}
\end{align}
where $\mathsf{N}_{\mathsf{G}}\left(\mathsf{F}\right)$ is the normalizer of $\mathsf{F}$ within $\mathsf{G}$.
\end{defterm}
Gauge fixing can be used to switch between different stabilizer codes that yield different gauge sets in a process known as *gauge switching*.
Gauge fixing also encompasses lattice surgery and code deformation  ([arXiv:1810.10037](https://arxiv.org/abs/1810.10037)).

One can also gauge out a subgroup $\mathsf{F}$ of the modular-qudit Pauli group by adding it to the gauge group.
\begin{defterm}{Gauging out}
\label{topic:gauging-out}
Gauging out is a map between subsystem codes that is done using a subgroup $\mathsf{F}\subseteq\mathsf{P}_n$,
\begin{align}
\begin{split}
  \mathsf{S}&\to\mathsf{Z}\left(\left\langle \mathsf{G},\mathsf{F}\right\rangle \right)\\
  \mathsf{G}&\to\left\langle \mathsf{G},\mathsf{F}\right\rangle ~.
\end{split}
\end{align}
The stabilizer group of the output subsystem code is a subgroup of that of the input code, $\mathsf{Z}\left(\left\langle \mathsf{G},\mathsf{F}\right\rangle \right)\subseteq\mathsf{Z}\left(\mathsf{G}\right)$.
When $\mathsf{F}$ is a subgroup of the logical Pauli group, this is also called *gauging*.
If $\mathsf{F}$ is itself a Pauli group of $m$ logical qudits of the original subsystem code, then gauging out those qudits is equivalent to treating them as gauge qubits.
Gauging out should not be confused with *gauging* (or ungauging) symmetries  ([arXiv:1202.3120](https://arxiv.org/abs/1202.3120), [arXiv:1605.01640](https://arxiv.org/abs/1605.01640), [arXiv:1805.01836](https://arxiv.org/abs/1805.01836), [arXiv:1806.08679](https://arxiv.org/abs/1806.08679)), a different process rooted in gauge theory which can be done to stabilizer or subsystem codes and which can change $n$.
\end{defterm}

(source: raw/error-correction-zoo.md)

## Decoders

- Syndrome measurements are obtained by first measuring gauge operators of the code and taking their products, which give the stabilizer measurement outcomes. The order in which gauge operators are measured is important since they do not commute. There is a necessary and sufficient condition for inferring the stabilizer syndrome from the measurements of the gauge generators  ([arXiv:1012.0425](https://arxiv.org/abs/1012.0425)).
- Decoder for certain geometrically local subsystem codes from hypergraphs  ([arXiv:1805.12542](https://arxiv.org/abs/1805.12542)).

## Relations

- _parent_: [[concepts/qec/subsystem-qudits-into-qudits]]
- _parent_: [[concepts/qec/subsystem-stabilizer]]
- _cousin_: [[concepts/qec/qudit-stabilizer]] — Subsystem modular-qudit stabilizer codes reduce to modular-qudit stabilizer codes when there are no gauge qudits.
