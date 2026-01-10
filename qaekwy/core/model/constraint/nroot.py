"""
This module defines the ConstraintNRoot class.
"""

from ..variable.variable import Variable
from .abstract_constraint import AbstractConstraint


class ConstraintNRoot(AbstractConstraint):
    """Enforces that the `var_2`-th root of `var_1` is equal to `var_3`.

    Args:
        var_1: The variable to take the n-th root of.
        var_2: The root degree.
        var_3: The variable to store the result.
        constraint_name: A name for the constraint.

    Example:
        >>> from qaekwy.core.model.variable.integer import IntegerVariable
        >>> from qaekwy.core.model.constraint.nroot import ConstraintNRoot
        >>> x = IntegerVariable("x", 0, 100)
        >>> y = 2
        >>> z = IntegerVariable("z", 0, 10)
        >>> constraint = ConstraintNRoot(x, y, z)
    """

    def __init__(
        self, var_1: Variable, var_2: int, var_3: Variable, constraint_name=None
    ) -> None:
        """Initializes a new n-th root constraint.

        Args:
            var_1: The variable to take the n-th root of.
            var_2: The root degree.
            var_3: The variable to store the result.
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
            "type": "nroot",
        }

    @staticmethod
    def from_json(json_data: dict, variables: list) -> "ConstraintNRoot":
        """Creates a ConstraintNRoot instance from a JSON object.

        Args:
            json_data: A dictionary representing the constraint.
            variables: The list of variables in the model.

        Returns:
            An instance of the ConstraintNRoot class.
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

        return ConstraintNRoot(var1, value, var3, json_data.get("name"))
