from qappswiki import paths


def test_to_node_id():
    assert paths.to_node_id("packages/openqevo.md") == "packages/openqevo"
    assert paths.to_node_id("README.md") == "README"


def test_strip_link_variants():
    assert paths.strip_link("packages/x|Display") == "packages/x"
    assert paths.strip_link("packages/x#heading") == "packages/x"
    assert paths.strip_link("./packages/x.md") == "packages/x"


def test_classify_wikilink():
    known = {"packages/x", "README"}
    assert paths.classify_wikilink("packages/x", known)["kind"] == "page"
    assert paths.classify_wikilink("packages/ghost", known)["kind"] == "missing"
    assert paths.classify_wikilink("../OtherRepo/y", known)["kind"] == "external"
    assert paths.classify_wikilink("https://a.b/c", known)["kind"] == "external"


def test_is_ignored():
    assert paths.is_ignored("node_modules/foo/bar.md")
    assert paths.is_ignored("raw/md/paper.md")
    assert paths.is_ignored("raw/pdf/paper.pdf")
    assert not paths.is_ignored("packages/openqevo.md")
    assert not paths.is_ignored("raw/source-inventory.md")


def test_resolve_source_external_vs_internal(tmp_path):
    (tmp_path / "raw").mkdir()
    (tmp_path / "raw" / "doc.md").write_text("x")
    (tmp_path / "packages").mkdir()
    info = paths.resolve_source("../raw/doc.md", "packages/p.md", tmp_path, {"raw/doc"})
    assert info["kind"] == "internal" and info["exists"]
    ext = paths.resolve_source("../../Sibling/readme.md", "packages/p.md", tmp_path, set())
    assert ext["kind"] == "external"
    url = paths.resolve_source("https://x.y/z", "packages/p.md", tmp_path, set())
    assert url["kind"] == "url"
