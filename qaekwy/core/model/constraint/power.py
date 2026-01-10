"""
This module defines the ConstraintPower class.
"""

from ..variable.variable import Variable
from .abstract_constraint import AbstractConstraint


class ConstraintPower(AbstractConstraint):
    """Enforces that `var_1` ^ `var_2` = `var_3`.

    Args:
        var_1: The base.
        var_2: The exponent.
        var_3: The result of the power operation.
        constraint_name: A name for the constraint.

    Example:
        >>> from qaekwy.core.model.variable.integer import IntegerVariable
        >>> from qaekwy.core.model.constraint.power import ConstraintPower
        >>> x = IntegerVariable("x", 0, 10)
        >>> y = 2
        >>> z = IntegerVariable("z", 0, 100)
        >>> constraint = ConstraintPower(x, y, z)
    """

    def __init__(
        self, var_1: Variable, var_2: int, var_3: Variable, constraint_name=None
    ) -> None:
        """Initializes a new power constraint.

        Args:
            var_1: The base.
            var_2: The exponent.
            var_3: The result of the power operation.
            constraint_name: A name for the constraint.
        """
        super().__init__(constraint_name)
        self.var_1 = var_1
        self.var_2 = var_2
        self.var_3 = var_3

    def to_json(self) -> dict:
        """Returns a JSON representation of the constraint."""
        return {
            "name": self.constraint_name,
            "v1": self.var_1.var_name,
            "v2": self.var_2,
            "v3": self.var_3.var_name,
            "type": "pow",
        }

    @staticmethod
    def from_json(json_data: dict, variables: list) -> "ConstraintPower":
        """Creates a ConstraintPower instance from a JSON object.

        Args:
            json_data: A dictionary representing the constraint.
            variables: The list of variables in the model.

        Returns:
            An instance of the ConstraintPower class.
        """
        var1_name = json_data["v1"]
        value = json_data["v2"]
        var3_name = json_data["v3"]

        var1 = next((v for v in variables if v.var_name == var1_name), None)
        if var1 is None:
            raise ValueError(f"Variable '{var1_name}' not found in the model.")

        var3 = next((v for v in variables if v.var_name == var3_name), None)
        if var3 is None:
            raise ValueError(f"Variable '{var3_name}' not found in the model.")

        return ConstraintPower(var1, value, var3, json_data.get("name"))
