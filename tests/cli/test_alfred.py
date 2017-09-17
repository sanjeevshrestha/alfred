"""CLI tests for alfred."""

from alfred.utils import test

class CliTestCase(test.alfredTestCase):
    def test_alfred_cli(self):
        argv = ['--foo=bar']
        with self.make_app(argv=argv) as app:
            app.run()
            self.eq(app.pargs.foo, 'bar')
