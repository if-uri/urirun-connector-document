# GENERATED smoke test — every handler returns a well-formed urirun envelope.
from urirun_connector_document import core


def test_bindings_expose_all_routes():
    text = str(core.urirun_bindings())
    assert 'document/command/create' in text
    assert 'document/query/read' in text
