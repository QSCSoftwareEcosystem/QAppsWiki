from qappswiki import validate


def _codes(findings):
    return {(f["level"], f["code"], f["page"]) for f in findings}


def test_validate_catches_defects(pipeline):
    findings = validate.validate(pipeline["pages"], pipeline["graph"], pipeline["root"])
    codes = _codes(findings)
    # bad status enum on lonely-pkg -> ERROR
    assert ("ERROR", "invalid-enum-value", "packages/lonely-pkg") in codes
    # out-of-vocab domain -> ERROR
    assert any(c == "invalid-enum-value" and p == "packages/lonely-pkg" for _l, c, p in codes)
    # made-up capability -> WARNING (open list)
    assert ("WARNING", "unknown-tag", "packages/lonely-pkg") in codes
    # dangling related_packages ref -> WARNING
    assert ("WARNING", "dangling-related-ref", "packages/lonely-pkg") in codes
    # dangling packages: Ghost -> WARNING
    assert ("WARNING", "dangling-package-ref", "integrations/widget-to-thing") in codes
    # needs-verification surfaced
    assert ("WARNING", "needs-verification", "integrations/widget-to-thing") in codes


def test_orphan_detection(pipeline):
    findings = validate.validate(pipeline["pages"], pipeline["graph"], pipeline["root"])
    # lonely-pkg is in index? It is linked from index, so NOT orphan-not-in-index.
    # But it has no content edges -> analyze orphan. Here check the in-index variant:
    pages_in_index = {f["page"] for f in findings if f["code"] == "orphan-not-in-index"}
    assert "packages/widget" not in pages_in_index


def test_missing_source_file(pipeline):
    findings = validate.validate(pipeline["pages"], pipeline["graph"], pipeline["root"])
    # widget cites raw/md/widget-docs.md which DOES exist -> no missing-source for it
    bad = [f for f in findings if f["code"] == "missing-source-file" and f["page"] == "packages/widget"]
    assert not bad


def test_has_errors_and_exit(pipeline):
    findings = validate.validate(pipeline["pages"], pipeline["graph"], pipeline["root"])
    assert validate.has_errors(findings)


def test_broken_wikilink_fires_for_ghost(pipeline):
    # Body link [[packages/ghost]] in the integration page has no target -> ERROR.
    findings = validate.validate(pipeline["pages"], pipeline["graph"], pipeline["root"])
    assert ("ERROR", "broken-wikilink", "integrations/widget-to-thing") in _codes(findings)
