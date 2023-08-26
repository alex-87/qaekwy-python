"""ConstraintSin Module

This module defines the ConstraintSin class, which represents a
constraint to enforce a sine relationship between two variables.

Classes:
    ConstraintSin: Represents a constraint to enforce a sine relationship between two variables.

"""
from qaekwy.model.constraint.abstract_constraint import AbstractConstraint
from qaekwy.model.variable.variable import Variable


class ConstraintSin(AbstractConstraint):
    """
    Represents a constraint to enforce a sine relationship between two variables.

    This constraint enforces that the sine of var_1 is equal to var_2, or vice versa.

    Args:
        var_1 (Variable): The variable for which the sine relationship is enforced.
        var_2 (Variable): The result variable of the sine relationship.
        constraint_name (str, optional): A name for the constraint.

    Attributes:
        var_1 (Variable): The variable for which the sine relationship is enforced.
        var_2 (Variable): The result variable of the sine relationship.

    Methods:
        to_json(): Returns a JSON representation of the constraint.

    Example:
        sine_constraint =
            ConstraintSin(variable_to_sine, result_variable, "sine_constraint")
    """

    def __init__(self, var_1: Variable, var_2: Variable, constraint_name=None) -> None:
        """
        Initialize a new sine constraint instance.

        Args:
            var_1 (Variable): The variable for which the sine relationship is enforced.
            var_2 (Variable): The result variable of the sine relationship.
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
            "type": "sin",
        }
