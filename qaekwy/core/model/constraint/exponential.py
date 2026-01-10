"""
This module defines the ConstraintExponential class.
"""

from ..variable.variable import Variable
from .abstract_constraint import AbstractConstraint


class ConstraintExponential(AbstractConstraint):
    """Enforces that exp(`var_1`) = `var_2`.

    Args:
        var_1: The exponent.
        var_2: The result of the exponential.
        constraint_name: A name for the constraint.

    Example:
        >>> from qaekwy.core.model.variable.float import FloatVariable
        >>> from qaekwy.core.model.constraint.exponential import ConstraintExponential
        >>> x = FloatVariable("x", 0, 10)
        >>> y = FloatVariable("y", 1, 22027)
        >>> constraint = ConstraintExponential(x, y)
    """

    def __init__(self, var_1: Variable, var_2: Variable, constraint_name=None) -> None:
        """Initializes a new exponential constraint.

        Args:
            var_1: The exponent.
            var_2: The result of the exponential.
            constraint_name: A name for the constraint.
        """
        super().__init__(constraint_name)
        self.var_1 = var_1
        self.var_2 = var_2

    def to_json(self) -> dict:
        """Returns a JSON representation of the constraint."""
        return {
            "name": self.constraint_name,
            "v1": self.var_1.var_name,
            "v2": self.var_2.var_name,
            "type": "exp",
        }

    @staticmethod
    def from_json(json_data: dict, variables: list) -> "ConstraintExponential":
        """Creates a ConstraintExponential instance from a JSON object.

        Args:
            json_data: A dictionary representing the constraint.
            variables: The list of variables in the model.

        Returns:
            An instance of the ConstraintExponential class.
        """
        var1_name = json_data["v1"]
        var2_name = json_data["v2"]

        var1 = next((v for v in variables if v.var_name == var1_name), None)
        if var1 is None:
            raise ValueError(f"Variable '{var1_name}' not found in the model.")

        var2 = next((v for v in variables if v.var_name == var2_name), None)
        if var2 is None:
            raise ValueError(f"Variable '{var2_name}' not found in the model.")

        return ConstraintExponential(var1, var2, json_data.get("name"))
