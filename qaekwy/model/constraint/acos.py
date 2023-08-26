"""ConstraintACos Module

This module defines the ConstraintACos class, which represents an arccosine constraint
between two variables.

Classes:
    ConstraintACos: Represents an arccosine constraint between two variables.

"""

from qaekwy.model.constraint.abstract_constraint import AbstractConstraint
from qaekwy.model.variable.variable import Variable


class ConstraintACos(AbstractConstraint):
    """
    Represents an arccosine constraint between two variables.

    This constraint enforces the relationship between the arccosine of var_1 and var_2.
    It ensures that the arccosine of var_1 is equal to var_2.

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
        acos_constraint = ConstraintACos(var_angle, var_value, "acos_constraint")
    """

    def __init__(self, var_1: Variable, var_2: Variable, constraint_name=None) -> None:
        """
        Initialize a new arccosine constraint instance.

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
            "type": "acos",
        }
