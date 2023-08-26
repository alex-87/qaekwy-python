"""ConstraintMaximum Module

This module defines the ConstraintMaximum class, which represents a
constraint to enforce a maximum value relationship between three variables.

Classes:
    ConstraintMaximum: Represents a constraint to enforce a maximum
    value relationship between three variables.

"""

from qaekwy.model.constraint.abstract_constraint import AbstractConstraint
from qaekwy.model.variable.variable import Variable


class ConstraintMaximum(AbstractConstraint):
    """
    Represents a constraint to enforce a maximum value relationship between two variables.

    This constraint enforces max{var_1, var_2} == var_3

    Args:
        var_1 (Variable): The first variable in the maximum value relationship.
        var_2 (Variable): The second variable in the maximum value relationship.
        var_3 (Variable): The third variable in the maximum value relationship.
        constraint_name (str, optional): A name for the constraint.

    Attributes:
        var_1 (Variable): The first variable in the maximum value relationship.
        var_2 (Variable): The second variable in the maximum value relationship.
        var_3 (Variable): The third variable in the maximum value relationship.

    Methods:
        to_json(): Returns a JSON representation of the constraint.

    Example:
        max_constraint = ConstraintMaximum(variable_1, variable_2, variable_3, "max_constraint")
    """

    def __init__(
        self, var_1: Variable, var_2: Variable, var_3: Variable, constraint_name=None
    ) -> None:
        """
        Initialize a new maximum value constraint instance.

        Args:
            var_1 (Variable): The first variable in the maximum value relationship.
            var_2 (Variable): The second variable in the maximum value relationship.
            var_3 (Variable): The third variable in the maximum value relationship.
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
            "type": "max",
        }
