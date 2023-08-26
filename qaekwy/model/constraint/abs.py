"""ConstraintAbs Module

This module defines the ConstraintAbs class, which represents an absolute value constraint
between two variables.

Classes:
    ConstraintAbs: Represents an absolute value constraint between two variables.

"""

from qaekwy.model.constraint.abstract_constraint import AbstractConstraint
from qaekwy.model.variable.variable import Variable


class ConstraintAbs(AbstractConstraint):
    """
    Represents an absolute value constraint between two variables.

    This constraint ensures that the absolute value of var_1 is equal to var_2

    Args:
        var_1 (Variable): The first variable in the constraint.
        var_2 (Variable): The second variable in the constraint.
        constraint_name (str, optional): A name for the constraint.

    Attributes:
        var_1 (Variable): The first variable in the constraint.
        var_2 (Variable): The second variable in the constraint.

    Methods:
        to_json(): Returns a JSON representation of the constraint.

    Example:

    """

    def __init__(self, var_1: Variable, var_2: Variable, constraint_name=None) -> None:
        """
        Initialize a new absolute value constraint instance.

        Args:
            var_1 (Variable): The first variable in the constraint.
            var_2 (Variable): The second variable in the constraint.
            constraint_name (str, optional): A name for the constraint.
        """
        super().__init__(constraint_name)
        self.var_1 = var_1
        self.var_2 = var_2

    def to_json(self) -> dict:
        return {
            "name": self.constraint_name,
            "v1": self.var_1.var_name,
            "v2": self.var_2.var_name,
            "type": "abs",
        }
