---
type: reference
status: canonical
updated: 2026-04-24
source: shared by Vicente Leyton, 2026-04-24
---

# The LLM Wiki pattern

> This page is a reference. It captures the design pattern QAppsWiki is built on, in the form it was originally shared. Iterate on the *application* of the pattern (our `CONTEXT.md`, our schema, our workflow) rather than on this file. When the pattern itself needs updating, update this page and date the change.

## The core idea

Most people's experience with LLMs and documents looks like RAG: you upload a collection of files, the LLM retrieves relevant chunks at query time, and generates an answer. This works, but the LLM is rediscovering knowledge from scratch on every question. There's no accumulation. Ask a subtle question that requires synthesizing five documents, and the LLM has to find and piece together the relevant fragments every time. Nothing is built up. NotebookLM, ChatGPT file uploads, and most RAG systems work this way.

The idea here is different. Instead of just retrieving from raw documents at query time, the LLM incrementally builds and maintains a persistent wiki — a structured, interlinked collection of markdown files that sits between you and the raw sources. When you add a new source, the LLM doesn't just index it for later retrieval. It reads it, extracts the key information, and integrates it into the existing wiki — updating entity pages, revising topic summaries, noting where new data contradicts old claims, strengthening or challenging the evolving synthesis. The knowledge is compiled once and then kept current, not re-derived on every query.

This is the key difference: the wiki is a persistent, compounding artifact. The cross-references are already there. The contradictions have already been flagged. The synthesis already reflects everything you've read. The wiki keeps getting richer with every source you add and every question you ask.

You never (or rarely) write the wiki yourself — the LLM writes and maintains all of it. You're in charge of sourcing, exploration, and asking the right questions. The LLM does all the grunt work — the summarizing, cross-referencing, filing, and bookkeeping that makes a knowledge base actually useful over time. In practice: the LLM agent open on one side, Obsidian (or equivalent) on the other. The LLM makes edits based on conversation; you browse the results in real time — following links, checking the graph view, reading the updated pages. Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase.

This applies broadly:
- **Personal:** goals, health, psychology — journal entries, articles, podcast notes.
- **Research:** deep dives on a topic over weeks or months with an evolving thesis.
- **Reading a book:** filing each chapter, building pages for characters, themes, plot threads — a personal fan-wiki.
- **Business / team:** internal wiki maintained by LLMs, fed by Slack threads, transcripts, project docs, customer calls.
- Competitive analysis, due diligence, trip planning, course notes, hobby deep-dives.

## Architecture — three layers

1. **Raw sources** — curated source documents. Articles, papers, images, data files. Immutable: the LLM reads from them, never modifies them. Source of truth.

2. **The wiki** — a directory of LLM-generated markdown files. Summaries, entity pages, concept pages, comparisons, overview, synthesis. The LLM owns this layer entirely. It creates pages, updates them when new sources arrive, maintains cross-references, and keeps everything consistent. You read it; the LLM writes it.

3. **The context file** — a document such as `CONTEXT.md` that tells the LLM how the wiki is structured, what the conventions are, and what workflows to follow when ingesting sources, answering questions, or maintaining the wiki. **This is the key configuration file** — what makes the LLM a disciplined wiki maintainer rather than a generic chatbot. You and the LLM co-evolve this over time.

## Operations

### Ingest
You drop a new source into the raw collection and tell the LLM to process it. Example flow: LLM reads the source, discusses key takeaways with you, writes a summary page in the wiki, updates the index, updates relevant entity/concept pages across the wiki, appends an entry to the log. A single source might touch 10-15 wiki pages.

One-at-a-time ingest with supervision vs. batch-ingest with less oversight — both valid. Choose a workflow, document it in the schema.

### Query
You ask questions against the wiki. The LLM searches for relevant pages, reads them, and synthesizes an answer with citations.

Answers can take different forms: a markdown page, a comparison table, a slide deck (Marp), a chart, a canvas.

**Key insight:** good answers can be filed back into the wiki as new pages. A comparison you asked for, an analysis, a connection you discovered — these are valuable and shouldn't disappear into chat history. Explorations compound in the knowledge base just like ingested sources do.

### Lint
Periodic health-check. Look for:
- Contradictions between pages.
- Stale claims that newer sources have superseded.
- Orphan pages with no inbound links.
- Important concepts mentioned but lacking their own page.
- Missing cross-references.
- Data gaps that could be filled with a web search.

The LLM is good at suggesting new questions to investigate and new sources to look for.

## Indexing and logging

Two special files help navigate the wiki as it grows.

### `index.md` — content-oriented
Catalog of everything in the wiki — each page listed with link, one-line summary, optional metadata (date, source count). Organized by category (entities, concepts, sources, etc.). LLM updates it on every ingest. Query flow: LLM reads the index first, then drills into relevant pages. Works surprisingly well at moderate scale (~100 sources, hundreds of pages) — avoids the need for embedding-based RAG infrastructure.

### `log.md` — chronological
Append-only record of what happened and when — ingests, queries, lint passes. Consistent entry prefix (e.g. `## [2026-04-02] ingest | Article Title`) makes the log parseable with unix tools: `grep "^## \[" log.md | tail -5`. Timeline of the wiki's evolution; helps the LLM understand what's been done recently.

## Optional: CLI tools

As the wiki grows, small tools help the LLM operate efficiently.

**Search** is the most obvious. At small scale the index file is enough; at larger scale you want proper search. `qmd` is a good option — local search engine for markdown files with hybrid BM25/vector search and LLM re-ranking, fully on-device. CLI + MCP server. Or vibe-code a naive search script.

## Tips and tricks

- **Obsidian Web Clipper** — browser extension that converts web articles to markdown. Fast way to get sources into raw.
- **Download images locally.** Obsidian Settings → Files and links → "Attachment folder path" set to a fixed dir (e.g. `raw/assets/`). Bind "Download attachments for current file" to a hotkey. After clipping, hit the hotkey; images land locally. LLMs can't natively read markdown with inline images in one pass — read text first, then view images separately as needed.
- **Obsidian's graph view** — best way to see the wiki's shape: what's connected, which pages are hubs, which are orphans.
- **Marp** — markdown-based slide decks; Obsidian plugin. Generate presentations directly from wiki content.
- **Dataview** — Obsidian plugin that queries page frontmatter. If pages have YAML frontmatter (tags, dates, counts), Dataview generates dynamic tables and lists.
- **The wiki is a git repo of markdown.** Version history, branching, collaboration for free.

## Why this works

The tedious part of maintaining a knowledge base is not the reading or the thinking — it's the bookkeeping. Updating cross-references, keeping summaries current, noting when new data contradicts old claims, maintaining consistency across dozens of pages. Humans abandon wikis because the maintenance burden grows faster than the value. LLMs don't get bored, don't forget to update a cross-reference, and can touch 15 files in one pass. The wiki stays maintained because the cost of maintenance is near zero.

The human's job is to curate sources, direct the analysis, ask good questions, and think about what it all means. The LLM's job is everything else.

Related in spirit to **Vannevar Bush's Memex (1945)** — a personal, curated knowledge store with associative trails between documents. Bush's vision was closer to this than to what the web became: private, actively curated, with the connections between documents as valuable as the documents themselves. The part he couldn't solve was who does the maintenance. The LLM handles that.
