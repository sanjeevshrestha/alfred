"""Tests for Example Plugin."""

from alfred.utils import test

class ExamplePluginTestCase(test.alfredTestCase):
    def test_load_example_plugin(self):
        self.app.setup()
        self.app.plugin.load_plugin('example')
