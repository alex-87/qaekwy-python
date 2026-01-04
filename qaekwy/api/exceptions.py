"""Custom exceptions for the QAekwy API module."""


class SolverError(Exception):
    """Custom exception for solver-related errors."""

    def __init__(self, status: str = "", message: str = "", content: str = ""):
        super().__init__(message)
        self.status = status
        self.content = content
