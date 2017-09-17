"""alfred exception classes."""

class alfredError(Exception):
    """Generic errors."""
    def __init__(self, msg):
        Exception.__init__(self)
        self.msg = msg

    def __str__(self):
        return self.msg

class alfredConfigError(alfredError):
    """Config related errors."""
    pass

class alfredRuntimeError(alfredError):
    """Generic runtime errors."""
    pass

class alfredArgumentError(alfredError):
    """Argument related errors."""
    pass
