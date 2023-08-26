"""ConstraintLogarithme Module

This module defines the ConstraintLogarithme class, which represents a constraint to enforce
a logarithmic relationship between two variables.

Classes:
    ConstraintLogarithme: Represents a constraint to enforce a logarithmic
    relationship between two variables.

"""

from qaekwy.model.constraint.abstract_constraint import AbstractConstraint
from qaekwy.model.variable.variable import Variable


class ConstraintLogarithme(AbstractConstraint):
    """
    Represents a constraint to enforce a logarithmic relationship between two variables.

    This constraint enforces that the logarithm of var_1 is equal to var_2, or vice versa.

    Args:
        var_1 (Variable): The variable for which the logarithm is enforced.
        var_2 (Variable): The result variable of the logarithmic relationship.
        constraint_name (str, optional): A name for the constraint.

    Attributes:
        var_1 (Variable): The variable for which the logarithm is enforced.
        var_2 (Variable): The result variable of the logarithmic relationship.

    Methods:
        to_json(): Returns a JSON representation of the constraint.

    Example:
        logarithmic_constraint =
            ConstraintLogarithme(variable_to_log, result_variable, "logarithmic_constraint")
    """

    def __init__(self, var_1: Variable, var_2: Variable, constraint_name=None) -> None:
        """
        Initialize a new logarithmic constraint instance.

        Args:
            var_1 (Variable): The variable for which the logarithm is enforced.
            var_2 (Variable): The result variable of the logarithmic relationship.
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
            "type": "log",
        }
