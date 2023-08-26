"""ConstraintDivide Module

This module defines the ConstraintDivide class, which represents a
constraint to enforce a division relationship between three variables.

Classes:
    ConstraintDivide: Represents a constraint to enforce a division
    relationship between three variables.

"""

from qaekwy.model.constraint.abstract_constraint import AbstractConstraint
from qaekwy.model.variable.variable import Variable


class ConstraintDivide(AbstractConstraint):
    """
    Represents a constraint to enforce a division relationship between three variables.

    This constraint enforces that the division of var_1 by var_2 is equal to var_3.

    Args:
        var_1 (Variable): The numerator variable in the division.
        var_2 (Variable): The denominator variable in the division.
        var_3 (Variable): The result variable of the division.
        constraint_name (str, optional): A name for the constraint.

    Attributes:
        var_1 (Variable): The numerator variable in the division.
        var_2 (Variable): The denominator variable in the division.
        var_3 (Variable): The result variable of the division.

    Methods:
        to_json(): Returns a JSON representation of the constraint.

    Example:
        divide_constraint =
            ConstraintDivide(numerator, denominator, result, "divide_constraint")
    """

    def __init__(
        self, var_1: Variable, var_2: Variable, var_3: Variable, constraint_name=None
    ) -> None:
        """
        Initialize a new division constraint instance.

        Args:
            var_1 (Variable): The numerator variable in the division.
            var_2 (Variable): The denominator variable in the division.
            var_3 (Variable): The result variable of the division.
            constraint_name (str, optional): A name for the constraint.
        """
        super().__init__(constraint_name)
        self.var_1 = var_1
        self.var_2 = var_2
        self.var_3 = var_3

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
            "v3": self.var_3.var_name,
            "type": "div",
        }
