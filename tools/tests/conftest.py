"""Shared fixtures: a synthetic wiki with deliberate breakage."""

from __future__ import annotations

from pathlib import Path

import pytest

from qappswiki import cli

# A small wiki seeded with both valid pages and one of every defect the
# validator is supposed to catch.
_FILES = {
    "index.md": """---
type: index
status: active
updated: 2026-01-01
---
# Index
- [[packages/widget]]
- [[concepts/idea]]
- [[how-to/use-widget]]
- [[integrations/widget-to-thing]]
- [[packages/lonely-pkg]]
""",
    "packages/widget.md": """---
type: package
name: Widget
status: active
updated: 2026-01-01
package_role: library
capabilities: [simulation]
hardware_targets: [local-cpu]
interfaces: [python-api]
domains: [quantum-software]
sources: [raw/md/widget-docs.md]
provenance_status: source-backed
related_concepts: [idea]
---
# Widget
Implements [[concepts/idea]] and has a [[how-to/use-widget]].
Cited from `code (source: not-a-real-citation)` should be ignored.
A real claim (source: raw/md/widget-docs.md).
""",
    "concepts/idea.md": """---
type: concept
name: Idea
status: active
updated: 2026-01-01
concept_kind: capability
domains: [quantum-software]
sources: [raw/md/widget-docs.md]
provenance_status: source-backed
---
# Idea
Linked by widget.
""",
    "how-to/use-widget.md": """---
type: how-to
status: draft
updated: 2026-01-01
task: Use the widget
packages: [Widget]
version_scope: v1
domains: [quantum-software]
sources: [raw/md/widget-docs.md]
provenance_status: source-backed
---
# Use Widget
See [[packages/widget]].
""",
    "integrations/widget-to-thing.md": """---
type: integration
status: draft
updated: 2026-01-01
packages: [Widget, Ghost]
interfaces: [python-api]
inputs: [a]
outputs: [b]
domains: [quantum-software]
sources: [raw/md/widget-docs.md]
provenance_status: needs-verification
---
# Widget to Thing
Connects [[packages/widget]] to a [[packages/ghost]] page that does not exist.
""",
    # Orphan: a package not reachable from index, missing required fields,
    # out-of-vocab domain, dangling related ref, bad status enum.
    "packages/lonely-pkg.md": """---
type: package
name: Lonely
status: bogus-status
updated: 2026-01-01
package_role: library
capabilities: [made-up-capability]
hardware_targets: [local-cpu]
interfaces: [python-api]
domains: [not-a-domain]
provenance_status: source-backed
related_packages: [does-not-exist]
---
# Lonely
No inbound or outbound content links.
""",
    # Raw source markdown: must be ignored by collect (no frontmatter).
    "raw/md/widget-docs.md": "# Widget docs\nPlain converted source, no frontmatter.\n",
    "raw/source-inventory.md": """---
type: source
status: active
updated: 2026-01-01
title: Inventory
source_type: documentation
location: local
preferred_ingest_path: raw/md
provenance_status: source-backed
---
# Inventory
""",
}


@pytest.fixture
def tmp_wiki(tmp_path: Path) -> Path:
    for rel, content in _FILES.items():
        p = tmp_path / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content, encoding="utf-8")
    return tmp_path


@pytest.fixture
def pipeline(tmp_wiki: Path):
    out = tmp_wiki / "wiki-out"
    pages, graph = cli.run_pipeline(tmp_wiki, out, use_cache=False)
    return {"root": tmp_wiki, "out": out, "pages": pages, "graph": graph}
