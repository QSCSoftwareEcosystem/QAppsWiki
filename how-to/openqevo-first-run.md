---
type: how-to
status: draft
updated: 2026-06-02
task: Install OpenQEvo locally and run the first registry and adapter checks
packages: [OpenQEvo]
version_scope: local OpenQEvo source tree, pyproject version 0.1.0
prerequisites: [python>=3.10, git, pip]
commands_verified: false
sources:
  - ../OpenQEvo/README.md
  - ../OpenQEvo/pyproject.toml
  - ../OpenQEvo/tests/test_qiskit_adapter.py
provenance_status: source-backed
---

# OpenQEvo First Run

This page captures the first local usage path for OpenQEvo. It is source-backed
from the OpenQEvo README and `pyproject.toml`, but the commands have not yet
been re-run during this QAppsWiki ingest.

## Install From Source

```bash
git clone https://github.com/QSCSoftwareThrust/OpenQEvo.git
cd OpenQEvo
pip install -e ".[dev]"
```

Install adapter extras as needed:

```bash
pip install -e ".[qiskit]"
pip install -e ".[pennylane]"
pip install -e ".[adapters]"
```

## Registry Check

The README presents the registry API as the primary entry point:

```python
import openqevo

openqevo.list_methods()
method = openqevo.get("trotter_s2")
result = method.evolve(terms, t=1.0, steps=10)
```

Expected methods from the README:

- `exact`
- `pennylane_trotter`
- `qiskit_trotter`
- `trotter_s1`
- `trotter_s2`

## Qiskit Adapter Check

The Qiskit adapter is source-backed as working by the OpenQEvo README and by
local tests in `tests/test_qiskit_adapter.py`.

The tests cover:

- registration under `qiskit_trotter`;
- exact agreement for a single Pauli-Z term;
- convergence with more Trotter steps for a non-commuting two-qubit case;
- unitary output;
- order parameter behavior;
- expected errors for empty terms and invalid step counts.

## Known Caveats

- The package license is marked `TBD`.
- The README says the package is not yet released, while `pyproject.toml`
  declares version `0.1.0`; treat the version as package metadata and the
  release as pending until a release artifact or tag is verified.
- Commands on this page should be locally re-run before being marked active.

## Related

- [[packages/openqevo]]
- [[integrations/qiskit-to-openqevo]]
