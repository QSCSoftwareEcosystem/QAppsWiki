---
type: concept
name: Hexagonal $CZ$ code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/cubic-theory
- concepts/qec/quantum-double-dihedral
- concepts/qec/spt
- concepts/qec/surface
- concepts/qec/tqd
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/hexagonal_cz
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: hexagonal_cz
---

# Hexagonal $CZ$ code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/hexagonal_cz) (`code_id: hexagonal_cz`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A hexagonal-lattice realization of the $2+1$D $l=m=n=1$ cubic theory / Type-III $\mathbb{Z}_2^3$ twisted quantum double phase.
Its stabilizers are products of Pauli-$Z$ operators and $CZ$ gates  ([arXiv:1508.03468](https://arxiv.org/abs/1508.03468)) ([arXiv:2503.15751](https://arxiv.org/abs/2503.15751)).
The ground-state subspace of the hexagonal $CZ$ code realizes the topological order of the Type-III $G=\mathbb{Z}^3_2$ Abelian TQD model  ([arXiv:1508.03468](https://arxiv.org/abs/1508.03468), [arXiv:2405.11719](https://arxiv.org/abs/2405.11719)), which is the same topological order as the $G=D_4$ non-Abelian quantum double  ([arXiv:hep-th/9511195](https://arxiv.org/abs/hep-th/9511195)).
The stabilizers include $CZ$ operators acting on hexagonal loops, but a reduced version exists where only two $CZ$ gates act on each loop  ([arXiv:2503.15751](https://arxiv.org/abs/2503.15751)).

(source: raw/error-correction-zoo.md)

## General gates

- The hexagonal $CZ$ code can be obtained from two surface codes by gauging  ([arXiv:1202.3120](https://arxiv.org/abs/1202.3120), [arXiv:1407.1025](https://arxiv.org/abs/1407.1025), [arXiv:1603.04442](https://arxiv.org/abs/1603.04442), [arXiv:1603.05182](https://arxiv.org/abs/1603.05182), [arXiv:1605.01640](https://arxiv.org/abs/1605.01640), [arXiv:1805.01836](https://arxiv.org/abs/1805.01836), [arXiv:1806.08679](https://arxiv.org/abs/1806.08679), [arXiv:2108.11402](https://arxiv.org/abs/2108.11402), [arXiv:2310.16032](https://arxiv.org/abs/2310.16032), [arXiv:2410.02213](https://arxiv.org/abs/2410.02213)) their logical $CZ$ gate  ([arXiv:2503.15751](https://arxiv.org/abs/2503.15751)). Gates on the two surface codes in the third level of the Clifford hierarchy, such as $CZ$ gates, can be realized fault-tolerantly by performing this procedure and reversing it  ([arXiv:2403.12119](https://arxiv.org/abs/2403.12119), [arXiv:2503.15751](https://arxiv.org/abs/2503.15751)).
- There is a constant-depth circuit implementing a transversal logical $T$ gate via an emergent automorphism symmetry of the underlying $\mathbb{D}_4$ topological order  ([arXiv:2511.02900](https://arxiv.org/abs/2511.02900)).

## Fault tolerance

- The hexagonal $CZ$ code can be obtained from two surface codes by gauging  ([arXiv:1202.3120](https://arxiv.org/abs/1202.3120), [arXiv:1407.1025](https://arxiv.org/abs/1407.1025), [arXiv:1603.04442](https://arxiv.org/abs/1603.04442), [arXiv:1603.05182](https://arxiv.org/abs/1603.05182), [arXiv:1605.01640](https://arxiv.org/abs/1605.01640), [arXiv:1805.01836](https://arxiv.org/abs/1805.01836), [arXiv:1806.08679](https://arxiv.org/abs/1806.08679), [arXiv:2108.11402](https://arxiv.org/abs/2108.11402), [arXiv:2310.16032](https://arxiv.org/abs/2310.16032), [arXiv:2410.02213](https://arxiv.org/abs/2410.02213)) their logical $CZ$ gate  ([arXiv:2503.15751](https://arxiv.org/abs/2503.15751)). Gates on the two surface codes in the third level of the Clifford hierarchy, such as $CZ$ gates, can be realized fault-tolerantly by performing this procedure and reversing it  ([arXiv:2403.12119](https://arxiv.org/abs/2403.12119), [arXiv:2503.15751](https://arxiv.org/abs/2503.15751)).

## Realizations

- Signatures of the phase detected in a 27-qubit trapped-ion device by Quantinuum  ([arXiv:2305.03766](https://arxiv.org/abs/2305.03766)). Preparation of ground states and braiding of anyons has also been performed.

## Relations

- _parent_: [[concepts/qec/cubic-theory]] — The $2+1$D cubic theory with $l=m=n=1$ realizes the same topological order as the Type-III $\mathbb{Z}_2^3$ twisted quantum double / $G=D_4$ quantum double, and the hexagonal $CZ$ code is a hexagonal-lattice realization of this phase  ([arXiv:1508.03468](https://arxiv.org/abs/1508.03468), [arXiv:2405.11719](https://arxiv.org/abs/2405.11719)).
- _parent_: [[concepts/qec/tqd]] — The ground-state subspace of the hexagonal $CZ$ code realizes the topological order of the Type-III $G=\mathbb{Z}^3_2$ Abelian TQD model  ([arXiv:1508.03468](https://arxiv.org/abs/1508.03468), [arXiv:2405.11719](https://arxiv.org/abs/2405.11719)), which is the same topological order as the $G=D_4$ quantum double  ([arXiv:hep-th/9511195](https://arxiv.org/abs/hep-th/9511195)). There is a constant-depth circuit implementing a transversal logical $T$ gate via an emergent automorphism symmetry of the underlying $\mathbb{D}_4$ topological order  ([arXiv:2511.02900](https://arxiv.org/abs/2511.02900)).
- _cousin_: [[concepts/qec/quantum-double-dihedral]] — The ground-state subspace of the hexagonal $CZ$ code realizes the topological order of the Type-III $G=\mathbb{Z}^3_2$ Abelian TQD model  ([arXiv:1508.03468](https://arxiv.org/abs/1508.03468), [arXiv:2405.11719](https://arxiv.org/abs/2405.11719)), which is the same topological order as the $G=D_4$ quantum double  ([arXiv:hep-th/9511195](https://arxiv.org/abs/hep-th/9511195)). There is a constant-depth circuit implementing a transversal logical $T$ gate via an emergent automorphism symmetry of the underlying $\mathbb{D}_4$ topological order  ([arXiv:2511.02900](https://arxiv.org/abs/2511.02900)).
- _cousin_: [[concepts/qec/surface]] — The hexagonal $CZ$ code can be obtained from two surface codes by gauging  ([arXiv:1202.3120](https://arxiv.org/abs/1202.3120), [arXiv:1407.1025](https://arxiv.org/abs/1407.1025), [arXiv:1603.04442](https://arxiv.org/abs/1603.04442), [arXiv:1603.05182](https://arxiv.org/abs/1603.05182), [arXiv:1605.01640](https://arxiv.org/abs/1605.01640), [arXiv:1805.01836](https://arxiv.org/abs/1805.01836), [arXiv:1806.08679](https://arxiv.org/abs/1806.08679), [arXiv:2108.11402](https://arxiv.org/abs/2108.11402), [arXiv:2310.16032](https://arxiv.org/abs/2310.16032), [arXiv:2410.02213](https://arxiv.org/abs/2410.02213)) their logical $CZ$ gate  ([arXiv:2503.15751](https://arxiv.org/abs/2503.15751)). Gates on the two surface codes in the third level of the Clifford hierarchy, such as $CZ$ gates, can be realized fault-tolerantly by performing this procedure and reversing it  ([arXiv:2403.12119](https://arxiv.org/abs/2403.12119), [arXiv:2503.15751](https://arxiv.org/abs/2503.15751)).
- _cousin_: [[concepts/qec/spt]] — The hexagonal $CZ$ code can be obtained by gauging  ([arXiv:1202.3120](https://arxiv.org/abs/1202.3120), [arXiv:1407.1025](https://arxiv.org/abs/1407.1025), [arXiv:1603.04442](https://arxiv.org/abs/1603.04442), [arXiv:1603.05182](https://arxiv.org/abs/1603.05182), [arXiv:1605.01640](https://arxiv.org/abs/1605.01640), [arXiv:1805.01836](https://arxiv.org/abs/1805.01836), [arXiv:1806.08679](https://arxiv.org/abs/1806.08679), [arXiv:2108.11402](https://arxiv.org/abs/2108.11402), [arXiv:2310.16032](https://arxiv.org/abs/2310.16032), [arXiv:2410.02213](https://arxiv.org/abs/2410.02213)) the symmetry of a particular SPT  ([arXiv:1508.03468](https://arxiv.org/abs/1508.03468)).

## Notes

- Popular summary of realization of non-Abelian topological order in [Quanta Magazine](https://www.quantamagazine.org/physicists-create-elusive-particles-that-remember-their-pasts-20230509/).
