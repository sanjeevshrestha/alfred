"""alfred bootstrapping."""

# All built-in application controllers should be imported, and registered
# in this file in the same way as alfredBaseController.

from alfred.cli.controllers.base import alfredBaseController

def load(app):
    app.handler.register(alfredBaseController)
