"""
This module defines the ConstraintMaximum class.
"""

from typing import List
from qaekwy.model.constraint.abstract_constraint import AbstractConstraint
from qaekwy.model.variable.variable import Variable


class ConstraintMaximum(AbstractConstraint):
    """Enforces that max(`var_1`, `var_2`) = `var_3`.

    Args:
        var_1: The first variable.
        var_2: The second variable.
        var_3: The variable to store the maximum.
        constraint_name: A name for the constraint.

    Example:
        >>> from qaekwy.model.variable.integer import IntegerVariable
        >>> from qaekwy.model.constraint.maximum import ConstraintMaximum
        >>> x = IntegerVariable("x", 0, 10)
        >>> y = IntegerVariable("y", 0, 10)
        >>> z = IntegerVariable("z", 0, 10)
        >>> constraint = ConstraintMaximum(x, y, z)
    """

    def __init__(
        self, var_1: Variable, var_2: Variable, var_3: Variable, constraint_name=None
    ) -> None:
        """Initializes a new maximum constraint.

        Args:
            var_1: The first variable.
            var_2: The second variable.
            var_3: The variable to store the maximum.
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
            "v2": self.var_2.var_name,
            "v3": self.var_3.var_name,
            "type": "max",
        }

    @staticmethod
    def from_json(json_data: dict, variables: List) -> "ConstraintMaximum":
        """Creates a ConstraintMaximum instance from a JSON object.

        Args:
            json_data: A dictionary representing the constraint.
            variables: The list of variables in the model.

        Returns:
            An instance of the ConstraintMaximum class.
        """
        var1_name = json_data["v1"]
        var2_name = json_data["v2"]
        var3_name = json_data["v3"]

        var1 = next((v for v in variables if v.var_name == var1_name), None)
        if var1 is None:
            raise ValueError(f"Variable '{var1_name}' not found in the model.")

        var2 = next((v for v in variables if v.var_name == var2_name), None)
        if var2 is None:
            raise ValueError(f"Variable '{var2_name}' not found in the model.")

        var3 = next((v for v in variables if v.var_name == var3_name), None)
        if var3 is None:
            raise ValueError(f"Variable '{var3_name}' not found in the model.")

        return ConstraintMaximum(var1, var2, var3, json_data.get("name"))
