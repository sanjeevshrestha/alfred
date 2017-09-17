"""Testing utilities for alfred."""

from alfred.cli.main import alfredTestApp
from cement.utils.test import *

class alfredTestCase(CementTestCase):
    app_class = alfredTestApp

    def setUp(self):
        """Override setup actions (for every test)."""
        super(alfredTestCase, self).setUp()

    def tearDown(self):
        """Override teardown actions (for every test)."""
        super(alfredTestCase, self).tearDown()

