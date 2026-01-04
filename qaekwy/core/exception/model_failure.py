"""Model Failure Exception

This module defines the ModelFailure class, which represents an
exception that can be raised when a failure occurs in a model.

Classes:
    ModelFailure: Represents an exception raised when a model failure occurs.

"""


class ModelFailure(Exception):
    """
    The ModelFailure class extends the built-in Exception class to represent
    an exceptional situation where a failure occurs in a model.

    It can be raised to indicate unexpected or erroneous conditions in
    the building of a model.
    """

    def __init__(self, *args: object) -> None:
        super().__init__(*args)
