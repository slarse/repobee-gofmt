from repobee import plugin

from repobee_gofmt import gofmt


def test_register():
    """Just test that there is no crash"""
    plugin.register_plugins([gofmt])
