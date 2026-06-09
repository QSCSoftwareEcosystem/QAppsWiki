# qappswiki

**A markdown-native validator and knowledge-graph engine for QAppsWiki.**

`qappswiki` reads the wiki exactly as it is written — YAML frontmatter, Obsidian
`[[wikilinks]]`, and `(source: …)` citations — and turns the whole corpus into a
**typed, queryable knowledge graph** that it can validate, analyze, visualize, and
serve. No language parsing, no LLM: just the wiki's own conventions, made
machine-readable.

---

## Motivation

QAppsWiki was designed schema-first: a rich `frontmatter-v0` schema, controlled
vocabularies, two-level provenance, and an interlinked page graph. But a schema
written in a document is only a *promise* — nothing enforced it, nothing compiled
the links into a graph, and any agent answering a question had to re-read raw
markdown every time.

This tool closes that gap. It was built after studying
[Graphify](https://github.com/safishamsi/graphify), an open-source knowledge-graph
builder for code. Graphify already had the *engine* QAppsWiki had only planned
(a clean `detect → … → export` pipeline); QAppsWiki already had the *taxonomy*
Graphify lacked. `qappswiki` takes Graphify's pipeline philosophy and rebuilds it
**markdown-native**, so the existing schema becomes:

- **enforced** — every page is checked against `frontmatter-v0` on demand or in CI;
- **queryable** — links and provenance compile into a real graph you can traverse;
- **legible** — orphans, over-central pages, broken links, and provenance gaps are
  surfaced in a report instead of hiding in 16+ files.

The result is the substrate the Agentic-Software markdown-compilation workflow can
run on: validate before writing, answer from the graph instead of from raw chunks.

---

## What it produces

Running the pipeline writes four artifacts to `wiki-out/`:

| file | what it is |
|---|---|
| `VALIDATION_REPORT.md` | findings against `frontmatter-v0`, errors first |
| `GRAPH_REPORT.md` | god-nodes, orphans, under-linked pages, cross-domain & AMBIGUOUS edges, provenance gaps |
| `graph.json` | the full graph: nodes + typed/confidence-labeled edges + stats |
| `graph.html` | a self-contained interactive visualization (open in a browser) |

---

## Overall structure

The engine is a chain of small, single-purpose stages. Each is one module exposing
one function; stages pass plain dicts and a single `networkx.MultiDiGraph`, and
nothing is written outside `wiki-out/`.

```
collect → parse → links → edges → build → validate → analyze → report → export → serve
```

| stage | module | responsibility |
|---|---|---|
| collect | `collect.py` | find every `.md` page (skips `node_modules`, `raw/md`, …) |
| parse | `parse.py` | split frontmatter from body → a graph **node** |
| links | `links.py` | extract `[[wikilinks]]` and `(source:)` citations (ignoring code blocks) |
| edges | `edges.py` | derive **typed, confidence-labeled edges** from links, `related_*`, sources, and explicit `edges:` |
| build | `build.py` | assemble nodes + edges into a `networkx.MultiDiGraph` |
| validate | `validate.py` | check every page against `frontmatter-v0` → ERROR / WARNING findings |
| analyze | `analyze.py` | graph insight: god-nodes, orphans, cross-domain links, provenance gaps |
| report | `report.py` | render the two markdown reports |
| export | `export.py` | write `graph.json` + `graph.html` |
| serve | `serve.py` | expose the graph over an MCP stdio server |

Supporting modules: `schema.py` (the machine-readable mirror of `frontmatter-v0`:
vocabularies + required-field tables), `paths.py` (id normalization + link
classification), `cache.py` (per-page SHA256 parse cache), `cli.py` (orchestration).

### The graph model

**Nodes** are pages: `{id, type, title, domains, status, provenance_status}`. Link
targets with no backing page become `missing` nodes; sibling-repo / URL sources
become `external` nodes — so every edge resolves.

**Edges** are typed and confidence-labeled, derived from four origins:

| origin | example | confidence |
|---|---|---|
| body `[[wikilink]]` | `openqevo —has-how-to→ how-to/openqevo-first-run` | EXTRACTED |
| `related_*` / `packages:` | a named package with no page | EXTRACTED / INFERRED / AMBIGUOUS |
| `sources:` + inline `(source:)` | `openqevo —cites→ ../OpenQEvo/README.md` | EXTRACTED |
| explicit `edges:` frontmatter | pin a `supersedes` / `derived-from` link | as authored |

Confidence means: **EXTRACTED** (explicitly written), **INFERRED** (deduced), or
**AMBIGUOUS** (target unresolved — flagged for human review).

---

## Installation

Requires Python ≥ 3.10. From the wiki, install the package once (editable, so edits
to the tooling take effect immediately):

```bash
cd tools
pip install -e ".[dev]"      # add the MCP server with ".[all]"
```

This puts a `qappswiki` command on your PATH. Runtime dependencies: `pyyaml`,
`networkx` (plus `mcp` for the server).

For PDF ingest you also need a PDF→markdown converter. The default is
[`markitdown-lightpdf`](https://pypi.org/project/markitdown-lightpdf/) (no-OCR,
math/table heuristics for born-digital LaTeX papers), best installed standalone:

```bash
uv tool install markitdown-lightpdf      # provides the `lightpdf` command
```

`qappswiki` calls the converter as an external command, so it works whether the
converter is in this env or its own.

> Without installing, you can still run it as `python -m qappswiki …` from inside
> the `tools/` directory.

---

## Usage

After installing, `qappswiki` works from **any** directory. The simplest form needs
no arguments — the default root resolves to this `QAppsWiki` repo because that is
where the package lives:

```bash
qappswiki run                 # full pipeline: validate + build graph + report
```

> **On `--root`:** pass it only to target a different wiki, and prefer an absolute
> path. A relative `--root ..` works *only* from inside `tools/` (where `..` is the
> wiki root). Day-to-day, just omit it.

### Commands

```bash
qappswiki run [--strict] [--no-html] [--log]   # validate + build + report (one pass)
qappswiki validate [--strict] [--format json]  # lint only; what CI runs
qappswiki build                                # graph.json + graph.html only
qappswiki report                               # GRAPH_REPORT.md only
qappswiki ingest <pdf> [--type concept]        # convert a PDF + scaffold a stub page
qappswiki serve [--graph wiki-out/graph.json]  # MCP stdio server over the graph

# read-only graph queries
qappswiki query "trotter"                                  # find matching pages
qappswiki path packages/openqevo concepts/markdown-compilation
qappswiki explain packages/openqevo                        # a node + all its edges
```

Common flags: `--strict` promotes warnings to failures (non-zero exit); `--no-cache`
bypasses the parse cache; `--log` prints a ready-to-paste `log.md` entry line.

### What `validate` checks

Required-field-per-type, controlled-vocabulary membership (ERROR on closed enums,
WARNING on the extensible "initial" tag lists), broken `[[wikilinks]]`, orphan pages
(absent from `index.md`), dangling `related_*` / `packages:` references, missing
source files, inline citations not listed in `sources:`, and under-linked package
pages. `validate` exits non-zero when any ERROR is present (or any WARNING with
`--strict`).

### Ingesting PDFs

`ingest` is the one command that **writes into the wiki**. It converts a PDF with
your converter, archives the original to `raw/pdf/` (gitignored) for provenance,
and scaffolds a schema-valid stub page (the "template" — generated from the schema,
so it always validates) pre-filled with `sources:` / `source_markdown:` provenance:

```bash
qappswiki ingest paper.pdf --type concept --title "Trotterization"
# -> raw/md/paper.md  (converted)
#    raw/pdf/paper.pdf (archived)
#    concepts/paper.md (stub: status draft, provenance needs-verification)
```

It then prints a `raw/source-inventory.md` row to paste. The stub deliberately
reports `missing-domains`, `needs-verification`, and `orphan` warnings — your
to-do list for compiling it into real, linked, cited knowledge. Pick the converter
with `--converter`, `$QAPPSWIKI_CONVERTER`, or rely on the `lightpdf`/`mid` default.

---

## Integration & safety

The tooling is **read-only on the wiki** — it only ever writes to `wiki-out/`. The
Agentic-Software compilation workflow runs `qappswiki run --strict` before proposing
page edits and reads the reports to decide what to link or repair; `run --log` emits
a `log.md` entry for the workflow to paste rather than the tool editing the log
itself.

---

## Testing

```bash
pytest tools/tests -q
```

A synthetic wiki fixture (seeded with one of every defect) covers each module, plus
a read-only smoke test against the real corpus.
