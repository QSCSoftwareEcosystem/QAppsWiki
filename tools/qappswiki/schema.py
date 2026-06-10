"""Controlled vocabularies and required-field tables.

This module is the machine-readable mirror of ``schema/frontmatter-v0.md``. When
the schema doc changes, update the sets and tables here. Nothing in this module
does I/O — it is pure data plus small lookup helpers consumed by ``validate.py``.

Vocabularies come in two flavours:

* **closed enums** — governed taxonomies (``type``, ``status``, ``domains`` …).
  A value outside the set is an ERROR.
* **open "initial" lists** — the schema explicitly labels ``capabilities``,
  ``hardware_targets`` and ``interfaces`` as "initial" and extensible. A value
  outside the set is a WARNING (likely a typo or a tag worth adding).
"""

from __future__ import annotations

# --------------------------------------------------------------------------- #
# Page types
# --------------------------------------------------------------------------- #

# Content pages carry provenance and participate in graph metrics.
CONTENT_TYPES = {
    "package",
    "concept",
    "how-to",
    "integration",
    "workflow",
    "qec-artifact",
    "benchmark",
    "source",
}

# Provisional types: defined ahead of evidence. Missing required fields are
# softened to WARNING and pages should carry ``status: provisional``.
PROVISIONAL_TYPES = {"workflow", "qec-artifact", "benchmark"}

# Navigation / governance pages. Minimal validation; excluded from centrality
# and orphan metrics. Includes the project-doc types actually used by
# README/PLAN/CONTEXT, which are not in the frontmatter-v0 ``type`` enum.
NAV_TYPES = {
    "schema",
    "index",
    "activity-log",
    "note",
    "project-charter",
    "project-plan",
    "operating-manual",
}

KNOWN_TYPES = CONTENT_TYPES | NAV_TYPES

# --------------------------------------------------------------------------- #
# Closed enums
# --------------------------------------------------------------------------- #

STATUS = {"draft", "provisional", "active", "deprecated", "blocked"}
PROVENANCE_STATUS = {"source-backed", "partially-source-backed", "needs-verification"}
PROVENANCE_GRANULARITY = {"page", "section", "claim"}

DOMAINS = {
    "quantum-information",
    "quantum-algorithms",
    "quantum-simulation",
    "quantum-software",
    "quantum-languages",
    "quantum-implementation",
    "quantum-error-correction",
    "quantum-hpc",
    "compilation",
    "benchmarking-validation",
    "wiki-infrastructure",
}

PACKAGE_ROLE = {
    "library",
    "framework",
    "simulator",
    "compiler",
    "workflow",
    "backend",
    "dataset",
    "other",
}

CONCEPT_KIND = {
    "algorithm",
    "application",
    "capability",
    "interface",
    "language",
    "hardware",
    "simulation",
    "information",
    "workflow-pattern",
    "schema",
    "provenance",
    "failure-mode",
    "qec",
    "qhpc",
    "validation",
    "other",
}

ARTIFACT_KIND = {
    "protocol-package",
    "circuit-family",
    "compiler-output",
    "ir",
    "metadata-bundle",
    "benchmark-input",
    "other",
}

BENCHMARK_KIND = {
    "validation-case",
    "performance-dataset",
    "simulator-comparison",
    "workflow-metric",
    "other",
}

SOURCE_TYPE = {
    "documentation",
    "repository",
    "paper",
    "issue",
    "release-note",
    "report",
    "dataset",
    "other",
}

PREFERRED_INGEST_PATH = {"raw/md", "raw/pdf", "external"}

MATURITY = {"prototype", "pre-alpha", "alpha", "beta", "production", "unknown"}

# Union of the validation_status enums used across integration/workflow/qec/benchmark.
VALIDATION_STATUS = {
    "unverified",
    "locally-tested",
    "source-tested",
    "benchmarked",
    "production",
}

# --------------------------------------------------------------------------- #
# Open "initial" lists (out-of-vocab => WARNING)
# --------------------------------------------------------------------------- #

CAPABILITIES = {
    "time-evolution",
    "trotterization",
    "circuit-framework",
    "differentiable-programming",
    "simulation",
    "stabilizer-simulation",
    "adapter",
    "workflow-composition",
    "schema",
    "agentic-query",
    "markdown-compilation",
    "knowledge-graph",
    "provenance",
    "qec",
    "qhpc",
    "resource-estimation",
    "benchmarking",
}

HARDWARE_TARGETS = {
    "local-cpu",
    "local-gpu",
    "hpc",
    "quantum-hardware",
    "simulator",
    "unknown",
}

INTERFACES = {
    "python-api",
    "registry",
    "adapter",
    "json-context",
    "markdown-source",
    "qasm",
    "qir",
    "stim",
    "mlir",
    "metadata-bundle",
    "mcp",
    "cli",
    "hybrid-agent-interface",
}

# --------------------------------------------------------------------------- #
# Required fields per type
# --------------------------------------------------------------------------- #

# Fields every content page must declare. ``provenance_status`` is required for
# content types only (nav/doc pages legitimately omit it).
COMMON_REQUIRED = ("type", "status", "updated")

REQUIRED_BY_TYPE = {
    "package": (
        "type",
        "name",
        "status",
        "updated",
        "package_role",
        "capabilities",
        "hardware_targets",
        "interfaces",
        "sources",
        "provenance_status",
    ),
    "concept": (
        "type",
        "name",
        "status",
        "updated",
        "concept_kind",
        "sources",
        "provenance_status",
    ),
    "how-to": (
        "type",
        "status",
        "updated",
        "task",
        "packages",
        "version_scope",
        "sources",
        "provenance_status",
    ),
    "integration": (
        "type",
        "status",
        "updated",
        "packages",
        "interfaces",
        "inputs",
        "outputs",
        "sources",
        "provenance_status",
    ),
    "workflow": (
        "type",
        "status",
        "updated",
        "packages",
        "interfaces",
        "inputs",
        "outputs",
        "artifacts",
        "hardware_targets",
        "validation_status",
        "sources",
        "provenance_status",
    ),
    "qec-artifact": (
        "type",
        "status",
        "updated",
        "artifact_kind",
        "formats",
        "producers",
        "consumers",
        "interfaces",
        "hardware_targets",
        "sources",
        "provenance_status",
    ),
    "benchmark": (
        "type",
        "status",
        "updated",
        "benchmark_kind",
        "packages",
        "workflows",
        "metrics",
        "hardware_targets",
        "sources",
        "provenance_status",
    ),
    "source": (
        "type",
        "status",
        "updated",
        "title",
        "source_type",
        "location",
        "preferred_ingest_path",
        "provenance_status",
    ),
}

# Map a frontmatter scalar/list field to the closed enum it must draw from.
# Used by validate.py for membership checks (ERROR on miss).
CLOSED_ENUM_FIELDS = {
    "status": STATUS,
    "provenance_status": PROVENANCE_STATUS,
    "provenance_granularity": PROVENANCE_GRANULARITY,
    "domains": DOMAINS,
    "package_role": PACKAGE_ROLE,
    "concept_kind": CONCEPT_KIND,
    "artifact_kind": ARTIFACT_KIND,
    "benchmark_kind": BENCHMARK_KIND,
    "source_type": SOURCE_TYPE,
    "preferred_ingest_path": PREFERRED_INGEST_PATH,
    "maturity": MATURITY,
    "validation_status": VALIDATION_STATUS,
}

# Fields whose membership miss is only a WARNING (open/extensible lists).
OPEN_LIST_FIELDS = {
    "capabilities": CAPABILITIES,
    "hardware_targets": HARDWARE_TARGETS,
    "interfaces": INTERFACES,
}

# The related_* frontmatter fields and the edge relation each implies.
RELATED_FIELDS = {
    "related_packages": "related",
    "related_concepts": "related",
    "related_integrations": "integrates",
    "related_how_to": "has-how-to",
    "related_workflows": "composes-with",
    "related_artifacts": "uses",
}

# Closed vocabulary for typed edges (schema extension + tooling-derived).
EDGE_RELATIONS = {
    "integrates",
    "depends-on",
    "supersedes",
    "uses",
    "implements",
    "derived-from",
    "cites",
    "related",
    "has-how-to",
    "composes-with",
    "uses-interface",
}

EDGE_CONFIDENCE = {"EXTRACTED", "INFERRED", "AMBIGUOUS"}

# Authoritative source kinds for the optional `version_source` field on package
# pages. `deterministic` kinds have a version endpoint; `docs`/`git` are fuzzy.
VERSION_SOURCE_KIND = {
    "pypi",
    "github-releases",
    "github-tags",
    "conda",
    "npm",
    "crates",
    "git",
    "docs",
}


def required_fields(page_type: str) -> tuple[str, ...]:
    """Required frontmatter keys for ``page_type`` (common set as a fallback)."""
    return REQUIRED_BY_TYPE.get(page_type, COMMON_REQUIRED)


def is_content_type(page_type: str | None) -> bool:
    return page_type in CONTENT_TYPES
