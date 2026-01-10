"""
This module defines the ConstraintATan class.
"""

from ..variable.variable import Variable
from .abstract_constraint import AbstractConstraint


class ConstraintATan(AbstractConstraint):
    """Enforces that the arctangent of `var_1` is equal to `var_2`.

    Args:
        var_1: The variable to take the arctangent of.
        var_2: The variable to store the result.
        constraint_name: A name for the constraint.

    Example:
        >>> from qaekwy.core.model.variable.float import FloatVariable
        >>> from qaekwy.core.model.constraint.atan import ConstraintATan
        >>> x = FloatVariable("x", -10, 10)
        >>> y = FloatVariable("y", -1.5708, 1.5708)
        >>> constraint = ConstraintATan(x, y)
    """

    def __init__(self, var_1: Variable, var_2: Variable, constraint_name=None) -> None:
        """Initializes a new arctangent constraint.

        Args:
            var_1: The variable to take the arctangent of.
            var_2: The variable to store the result.
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
            "type": "atan",
        }

    @staticmethod
    def from_json(json_data: dict, variables: list) -> "ConstraintATan":
        """Creates a ConstraintATan instance from a JSON object.

        Args:
            json_data: A dictionary representing the constraint.
            variables: The list of variables in the model.

        Returns:
            An instance of the ConstraintATan class.
        """
        var1_name = json_data["v1"]
        var2_name = json_data["v2"]

        var1 = next((v for v in variables if v.var_name == var1_name), None)
        if var1 is None:
            raise ValueError(f"Variable '{var1_name}' not found in the model.")

        var2 = next((v for v in variables if v.var_name == var2_name), None)
        if var2 is None:
            raise ValueError(f"Variable '{var2_name}' not found in the model.")

        return ConstraintATan(var1, var2, json_data.get("name"))
