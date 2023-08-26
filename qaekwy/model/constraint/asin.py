"""ConstraintASin Module

This module defines the ConstraintASin class, which represents an arcsine constraint
between two variables.

Classes:
    ConstraintASin: Represents an arcsine constraint between two variables.

"""

from qaekwy.model.constraint.abstract_constraint import AbstractConstraint
from qaekwy.model.variable.variable import Variable


class ConstraintASin(AbstractConstraint):
    """
    Represents an arcsine constraint between two variables.

    This constraint enforces the relationship between the arcsine of var_1 and var_2.
    It ensures that the arcsine of var_1 is equal to var_2,.

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
        asin_constraint = ConstraintASin(var_angle, var_value, "asin_constraint")
    """

    def __init__(self, var_1: Variable, var_2: Variable, constraint_name=None) -> None:
        """
        Initialize a new arcsine constraint instance.

        Args:
            var_1 (Variable): The first variable in the constraint.
            var_2 (Variable): The second variable in the constraint.
            constraint_name (str, optional): A name for the constraint.
        """
        super().__init__(constraint_name)
        self.var_1 = var_1
        self.var_2 = var_2

    def to_json(self) -> dict:
        """
        Convert the constraint to a JSON representation.

        Returns:
            dict: A dictionary containing constraint information in JSON format.
        """
        return {
            "name": self.constraint_name,
            "v1": self.var_1.var_name,
            "v2": self.var_2.var_name,
            "type": "asin",
        }
