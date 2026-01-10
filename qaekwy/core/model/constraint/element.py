"""
This module defines the ConstraintElement class.
"""

from ..variable.variable import ArrayVariable, Variable
from .abstract_constraint import AbstractConstraint


class ConstraintElement(AbstractConstraint):
    """Enforces that `map_array`[`var_1`] = `var_2`.

    Args:
        map_array: The array of values.
        var_1: The index variable.
        var_2: The value at the index.
        constraint_name: A name for the constraint.

    Example:
        >>> from qaekwy.core.model.variable.integer import IntegerVariable, IntegerVariableArray
        >>> from qaekwy.core.model.constraint.element import ConstraintElement
        >>> map_array = IntegerVariableArray("map", 5, 0, 10)
        >>> index = IntegerVariable("index", 0, 4)
        >>> value = IntegerVariable("value", 0, 10)
        >>> constraint = ConstraintElement(map_array, index, value)
    """

    def __init__(
        self,
        map_array: ArrayVariable,
        var_1: Variable,
        var_2: Variable,
        constraint_name=None,
    ) -> None:
        """Initializes a new element constraint.

        Args:
            map_array: The array of values.
            var_1: The index variable.
            var_2: The value at the index.
            constraint_name: A name for the constraint.
        """
        super().__init__(constraint_name)
        self.map_array = map_array
        self.var_1 = var_1
        self.var_2 = var_2

    def to_json(self) -> dict:
        """Returns a JSON representation of the constraint."""
        return {
            "name": self.constraint_name,
            "map": self.map_array.var_name,
            "v1": self.var_1.var_name,
            "v2": self.var_2.var_name,
            "type": "element",
        }

    @staticmethod
    def from_json(json_data: dict, variables: list) -> "ConstraintElement":
        """Creates a ConstraintElement instance from a JSON object.

        Args:
            json_data: A dictionary representing the constraint.
            variables: The list of variables in the model.

        Returns:
            An instance of the ConstraintElement class.
        """
        map_array_name = json_data["map"]
        var1_name = json_data["v1"]
        var2_name = json_data["v2"]

        map_array = next((v for v in variables if v.var_name == map_array_name), None)
        if map_array is None:
            raise ValueError(f"Variable '{map_array_name}' not found in the model.")

        var1 = next((v for v in variables if v.var_name == var1_name), None)
        if var1 is None:
            raise ValueError(f"Variable '{var1_name}' not found in the model.")

        var2 = next((v for v in variables if v.var_name == var2_name), None)
        if var2 is None:
            raise ValueError(f"Variable '{var2_name}' not found in the model.")

        return ConstraintElement(map_array, var1, var2, json_data.get("name"))
