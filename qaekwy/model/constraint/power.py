"""ConstraintPower Module

This module defines the ConstraintPower class, which represents a
constraint to enforce a power relationship between three variables.

Classes:
    ConstraintPower: Represents a constraint to enforce a
    power relationship between three variables.

"""

from qaekwy.model.constraint.abstract_constraint import AbstractConstraint
from qaekwy.model.variable.variable import Variable


class ConstraintPower(AbstractConstraint):
    """
    Represents a constraint to enforce a power relationship between three variables.

    This constraint enforces that the value of var_1 raised to the power of var_2 is equal to var_3.

    Args:
        var_1 (Variable): The base variable in the power relationship.
        var_2 (int): The exponent variable in the power relationship.
        var_3 (Variable): The result variable of the power relationship.
        constraint_name (str, optional): A name for the constraint.

    Attributes:
        var_1 (Variable): The base variable in the power relationship.
        var_2 (int): The exponent variable in the power relationship.
        var_3 (Variable): The result variable of the power relationship.

    Methods:
        to_json(): Returns a JSON representation of the constraint.

    Example:
        power_constraint =
            ConstraintPower(base_variable, exponent_value, result_variable, "power_constraint")
    """

    def __init__(
        self, var_1: Variable, var_2: int, var_3: Variable, constraint_name=None
    ) -> None:
        """
        Initialize a new power constraint instance.

        Args:
            var_1 (Variable): The base variable in the power relationship.
            var_2 (int): The exponent variable in the power relationship.
            var_3 (Variable): The result variable of the power relationship.
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
            "v2": self.var_2,
            "v3": self.var_3.var_name,
            "type": "pow",
        }
