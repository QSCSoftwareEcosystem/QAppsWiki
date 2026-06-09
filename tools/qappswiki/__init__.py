"""qappswiki — markdown-native validator + knowledge-graph engine for QAppsWiki.

A stateless single-function-per-stage pipeline over the QAppsWiki markdown corpus:

    collect -> parse -> links -> edges -> build -> validate -> analyze -> report -> export -> serve

Each stage is one module exposing one public entry function. Stages communicate
through plain dicts and a single ``networkx.MultiDiGraph``; nothing is written
outside the output directory (``wiki-out/`` by default).
"""

__version__ = "0.1.0"

__all__ = [
    "collect_pages",
    "parse_page",
    "derive_edges",
    "build_graph",
    "validate",
    "analyze",
    "to_json",
    "to_html",
]


def __getattr__(name):  # lazy re-exports so importing the package stays cheap
    if name in ("collect_pages",):
        from .collect import collect_pages

        return collect_pages
    if name in ("parse_page",):
        from .parse import parse_page

        return parse_page
    if name in ("derive_edges",):
        from .edges import derive_edges

        return derive_edges
    if name in ("build_graph",):
        from .build import build_graph

        return build_graph
    if name in ("validate",):
        from .validate import validate

        return validate
    if name in ("analyze",):
        from .analyze import analyze

        return analyze
    if name in ("to_json", "to_html"):
        from . import export

        return getattr(export, name)
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
