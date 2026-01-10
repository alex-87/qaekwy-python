"""
This module defines the ConstraintModulo class.
"""

from ..variable.variable import Variable
from .abstract_constraint import AbstractConstraint


class ConstraintModulo(AbstractConstraint):
    """Enforces that `var_1` % `var_2` = `var_3`.

    Args:
        var_1: The dividend.
        var_2: The divisor.
        var_3: The remainder.
        constraint_name: A name for the constraint.

    Example:
        >>> from qaekwy.core.model.variable.integer import IntegerVariable
        >>> from qaekwy.core.model.constraint.modulo import ConstraintModulo
        >>> x = IntegerVariable("x", 0, 10)
        >>> y = IntegerVariable("y", 1, 10)
        >>> z = IntegerVariable("z", 0, 9)
        >>> constraint = ConstraintModulo(x, y, z)
    """

    def __init__(
        self, var_1: Variable, var_2: Variable, var_3: Variable, constraint_name=None
    ) -> None:
        """Initializes a new modulo constraint.

        Args:
            var_1: The dividend.
            var_2: The divisor.
            var_3: The remainder.
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
            "type": "mod",
        }

    @staticmethod
    def from_json(json_data: dict, variables: list) -> "ConstraintModulo":
        """Creates a ConstraintModulo instance from a JSON object.

        Args:
            json_data: A dictionary representing the constraint.
            variables: The list of variables in the model.

        Returns:
            An instance of the ConstraintModulo class.
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

        return ConstraintModulo(var1, var2, var3, json_data.get("name"))
