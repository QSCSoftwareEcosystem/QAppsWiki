# qappswiki

Markdown-native validator + knowledge-graph engine for QAppsWiki. Turns the
existing `frontmatter-v0` schema and Obsidian `[[wikilinks]]` into an **enforced,
queryable** graph — without leaving markdown. Inspired by the pipeline shape of
[Graphify](https://github.com/safishamsi/graphify) but code-free (no tree-sitter,
no LLM): it reads only the corpus's own frontmatter, links, and provenance.

## Pipeline

```
collect -> parse -> links -> edges -> build -> validate -> analyze -> report -> export -> serve
```

Each stage is one module with one public function; stages pass plain dicts and a
single `networkx.MultiDiGraph`. Nothing is written outside `wiki-out/`.

## Install

```bash
cd tools
pip install -e ".[dev]"        # add the 'mcp' extra for the server: ".[all]"
```

Requires Python ≥ 3.10. Runtime deps: `pyyaml`, `networkx` (plus `mcp` for `serve`).

## Use

Run from anywhere with `--root <wiki>` (defaults to the parent of `tools/`):

```bash
qappswiki run --root ..              # validate + build + report (the canonical pass)
qappswiki validate --root .. --strict   # CI gate; exits non-zero on errors (or warnings with --strict)
qappswiki build --root ..            # graph.json + graph.html only
qappswiki report --root ..           # GRAPH_REPORT.md only
qappswiki serve --root ..            # MCP stdio server over graph.json
qappswiki query "trotter" --root ..  # find matching nodes
qappswiki path packages/openqevo concepts/markdown-compilation --root ..
qappswiki explain packages/openqevo --root ..
```

Outputs land in `<wiki>/wiki-out/`:

| file | what |
|---|---|
| `graph.json` | node-link graph (nodes + typed/confidence edges + stats) |
| `graph.html` | self-contained Cytoscape visualization (open in a browser) |
| `GRAPH_REPORT.md` | god-nodes, orphans, under-linked pages, cross-domain & AMBIGUOUS edges, provenance gaps |
| `VALIDATION_REPORT.md` | findings against `frontmatter-v0` (errors first) |
| `cache/` | per-page SHA256 parse cache |

## What it checks

Required-field-per-type, controlled-vocabulary membership (errors on closed
enums, warnings on the "initial" tag lists), broken `[[wikilinks]]`, orphan
pages (absent from `index.md`), dangling `related_*` / `packages:` references,
missing source files, inline citations not listed in `sources:`, and
under-linked package pages.

## Edges

Edges are typed and confidence-labeled, derived from four origins: body
`[[wikilinks]]`, `related_*` / `packages:` frontmatter, `sources:` + inline
`(source:)` citations (`cites`), and an optional explicit `edges:` block (see
the "Typed Edges" section in `schema/frontmatter-v0.md`).

## Integration

The AS markdown-compilation workflow runs `qappswiki run --strict` before
proposing page writes and reads `VALIDATION_REPORT.md` / `GRAPH_REPORT.md`. The
tooling is **read-only on the wiki** (writes only `wiki-out/`); `run --log`
prints a ready-to-paste `log.md` entry instead of editing the log itself.

## Test

```bash
pytest -q
```
