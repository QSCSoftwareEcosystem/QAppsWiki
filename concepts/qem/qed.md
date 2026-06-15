---
type: concept
name: Quantum Error Detection
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- QED
- post-selective error detection
- stabilizer post-selection
- error-detecting codes
domains:
- quantum-error-correction
related_concepts:
- concepts/qem/accreditation
- concepts/qem/ide
- concepts/qem/partial-pauli-twirling
- concepts/qem/subspace-expansion
- concepts/qem/symmetry-verification
sources:
- raw/qem-zoo.md
- https://qemzoo.com/technique.html?id=qed
provenance_status: needs-verification
imported_from: qem-zoo
imported_id: qed
---

# Quantum Error Detection

> **Imported by `qappswiki import-zoo qemzoo`** from the [QEM Zoo](https://qemzoo.com/technique.html?id=qed) (`id: qed`, category: mitigation). Public domain (The Unlicense); cited as the QEM Zoo (qemzoo.com), public domain (The Unlicense). This is a `needs-verification` page — confirm against the references below.

## Summary

Encodes logical qubits into a quantum error-detecting code (e.g., a $[\![ n, k, d ]\!]$ stabilizer code with $d \geq 2$) and measures stabilizer generators at the end of (or during) the computation. Outcomes that flag a stabilizer violation are discarded via post-selection. Unlike full quantum error correction, QED does not attempt to correct errors — it only detects them, trading acceptance rate for output fidelity.

(source: raw/qem-zoo.md)

## Properties

| Property | Value |
|---|---|
| Bias | Removed for detectable errors; undetectable errors remain |
| Sampling overhead | Inversely proportional to acceptance rate; depends on noise and code distance |
| Noise model required | None; code structure determines detectable errors |
| Applicability | Any circuit that can be embedded in an error-detecting code; most effective for low to moderate noise |

## Related techniques

- [[concepts/qem/symmetry-verification]] — SV is a special case using symmetry as the detecting code
- [[concepts/qem/accreditation]] — both use post-selection to improve output quality
- [[concepts/qem/partial-pauli-twirling]] — PPT aligns errors with QED's detectable error space for synergistic mitigation
- [[concepts/qem/subspace-expansion]] — QSE can function as a quantum error decoder
- [[concepts/qem/ide]] — IDE uses error-correcting code distance as an extrapolation parameter within the QEM framework

## References

- E. Knill. *Quantum Computing with Realistically Noisy Devices*. Nature, 2005 [arXiv:quant-ph/0410199](https://arxiv.org/abs/quant-ph/0410199) [doi](https://doi.org/10.1038/nature03350)
- A. D. Córcoles, E. Magesan, S. J. Srinivasan, A. W. Cross, M. Steffen, J. M. Gambetta, J. M. Chow. *Demonstration of a Quantum Error Detection Code Using a Square Lattice of Four Superconducting Qubits*. Nature Communications, 2015 [doi](https://doi.org/10.1038/ncomms7979)
- N. M. Linke, M. Gutierrez, K. A. Landsman, C. Figgatt, S. Debnath, K. R. Brown, C. Monroe. *Fault-Tolerant Quantum Error Detection*. Science Advances, 2017 [arXiv:1611.06946](https://arxiv.org/abs/1611.06946) [doi](https://doi.org/10.1126/sciadv.1701074)
- J. R. McClean, Z. Jiang, N. C. Rubin, R. Babbush, H. Neven. *Decoding Quantum Errors with Subspace Expansions*. Nature Communications, 2020 [arXiv:1903.05786](https://arxiv.org/abs/1903.05786) [doi](https://doi.org/10.1038/s41467-020-14341-w)
- M. Urbanek, B. Nachman, W. A. de Jong. *Error Detection on Quantum Computers Improves Accuracy of Chemical Calculations*. Physical Review A, 2020 [arXiv:1910.00129](https://arxiv.org/abs/1910.00129) [doi](https://doi.org/10.1103/PhysRevA.102.022427)
- M. Gong, X. Yuan, S. Wang, Y. Wu, Y. Zhao, C. Zha, S. Li, Z. Zhang, Q. Zhao, Y. Liu, F. Liang, J. Lin, Y. Xu, H. Deng, H. Rong, H. Lu, S. C. Benjamin, C.-Z. Peng, X. Ma, Y.-A. Chen, X. Zhu, J.-W. Pan. *Experimental Exploration of Five-Qubit Quantum Error Correcting Code with Superconducting Qubits*. National Science Review, 2022 [arXiv:1907.04507](https://arxiv.org/abs/1907.04507) [doi](https://doi.org/10.1093/nsr/nwab011)
- C. N. Self, M. Benedetti, D. Amaro. *Protecting Expressive Circuits with a Quantum Error Detection Code*. Nature Physics, 2024 [arXiv:2211.06703](https://arxiv.org/abs/2211.06703) [doi](https://doi.org/10.1038/s41567-023-02282-2)
- E. Chertkov, A. C. Potter, D. Hayes, M. Foss-Feig. *Error Detection Without Post-Selection in Adaptive Quantum Circuits*. arXiv preprint, 2025 [arXiv:2509.25326](https://arxiv.org/abs/2509.25326)
- S. Martiel, A. Javadi-Abhari. *Low-Overhead Error Detection with Spacetime Codes*. arXiv preprint, 2025 [arXiv:2504.15725](https://arxiv.org/abs/2504.15725)
- A. Javadi-Abhari, S. Martiel, A. Seif, M. Takita, K. X. Wei. *Big Cats: Entanglement in 120 Qubits and Beyond*. arXiv preprint, 2025 [arXiv:2510.09520](https://arxiv.org/abs/2510.09520)
- A. Vezvaee, V. Tripathi, M. Morford-Oberst, F. Butt, V. Kasatkin, D. A. Lidar. *Demonstration of High-Fidelity Entangled Logical Qubits Using Transmons*. arXiv preprint, 2025 [arXiv:2503.14472](https://arxiv.org/abs/2503.14472)
- C. Zhang, C. Li, Z. Tian, Y. Jiang, F. Xu, S. Zhang, H. Wang, Y.-N. Zhang, X. Bai, B. Zhao, Y.-F. Zhang, H. Shu, J. Liu, K. Wu, C. Huang, K. Shi, M. Duan, T. Xin, P. Huang, T. Pan, S. Liu, G. Wang, G. Hu, Y. He, D. Yu. *Quantum Error Detection in a Silicon Quantum Processor*. Nature Electronics, 2026 [doi](https://doi.org/10.1038/s41928-025-01557-1)
