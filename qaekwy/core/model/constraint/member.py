"""
This module defines the ConstraintMember class.
"""

from ..variable.variable import ArrayVariable, Variable
from .abstract_constraint import AbstractConstraint


class ConstraintMember(AbstractConstraint):
    """Enforces that `var_2` is a member of the array `var_1`.

    Args:
        var_1: The array of values.
        var_2: The variable to check for membership.
        constraint_name: A name for the constraint.

    Example:
        >>> from qaekwy.core.model.variable.integer import IntegerVariable, IntegerVariableArray
        >>> from qaekwy.core.model.constraint.member import ConstraintMember
        >>> x = IntegerVariableArray("x", 5, 0, 10)
        >>> y = IntegerVariable("y", 0, 10)
        >>> constraint = ConstraintMember(x, y)
    """

    def __init__(
        self, var_1: ArrayVariable, var_2: Variable, constraint_name=None
    ) -> None:
        """Initializes a new member constraint.

        Args:
            var_1: The array of values.
            var_2: The variable to check for membership.
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
            "type": "member",
        }

    @staticmethod
    def from_json(json_data: dict, variables: list) -> "ConstraintMember":
        """Creates a ConstraintMember instance from a JSON object.

        Args:
            json_data: A dictionary representing the constraint.
            variables: The list of variables in the model.

        Returns:
            An instance of the ConstraintMember class.
        """
        var1_name = json_data["v1"]
        var2_name = json_data["v2"]

        var1 = next((v for v in variables if v.var_name == var1_name), None)
        if var1 is None:
            raise ValueError(f"Variable '{var1_name}' not found in the model.")

        var2 = next((v for v in variables if v.var_name == var2_name), None)
        if var2 is None:
            raise ValueError(f"Variable '{var2_name}' not found in the model.")

        return ConstraintMember(var1, var2, json_data.get("name"))
