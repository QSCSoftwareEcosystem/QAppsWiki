from qappswiki import collect, links
from qappswiki.cache import Cache
from qappswiki.parse import parse_page, split_frontmatter


def test_collect_skips_raw_md_and_node_modules(tmp_wiki):
    refs = collect.collect_pages(tmp_wiki)
    ids = {r["node_id"] for r in refs}
    assert "packages/widget" in ids
    assert "raw/source-inventory" in ids
    assert not any(i.startswith("raw/md/") for i in ids)


def test_collect_dirs_filter(tmp_wiki):
    # --dirs restricts to those top-level dirs plus root-level files (e.g. index).
    refs = collect.collect_pages(tmp_wiki, dirs=["packages"])
    ids = {r["node_id"] for r in refs}
    assert {"packages/widget", "packages/lonely-pkg"} <= ids
    assert not any(i.startswith(("concepts/", "how-to/", "integrations/")) for i in ids)


def test_split_frontmatter():
    fm, body = split_frontmatter("---\na: 1\n---\nhello\n")
    assert fm.strip() == "a: 1" and body.strip() == "hello"
    fm2, body2 = split_frontmatter("no frontmatter here")
    assert fm2 is None and body2 == "no frontmatter here"


def test_parse_page_node_and_meta(tmp_wiki):
    ref = {"path": str(tmp_wiki / "packages/widget.md"),
           "rel_path": "packages/widget.md", "node_id": "packages/widget"}
    node, meta = parse_page(ref, tmp_wiki, cache=None)
    assert node["type"] == "package"
    assert node["title"] == "Widget"
    assert "quantum-software" in node["domains"]
    assert "concepts/idea" in meta["body_links"]
    assert meta["parse_error"] is None


def test_links_ignore_code_blocks():
    body = "Real (source: a.md).\n`example (source: <path>)`\n```\n(source: b.md)\n```"
    cites = links.extract_citations(body)
    paths = [p for c in cites for p in c["paths"]]
    assert "a.md" in paths
    assert "<path>" not in paths and "b.md" not in paths


def test_cache_hit(tmp_wiki):
    out = tmp_wiki / "wiki-out"
    cache = Cache(out, enabled=True)
    ref = {"path": str(tmp_wiki / "concepts/idea.md"),
           "rel_path": "concepts/idea.md", "node_id": "concepts/idea"}
    n1, _ = parse_page(ref, tmp_wiki, cache)
    digest = Cache.file_hash(tmp_wiki / "concepts/idea.md")
    assert cache.load(digest) is not None
    n2, _ = parse_page(ref, tmp_wiki, cache)
    assert n1 == n2
