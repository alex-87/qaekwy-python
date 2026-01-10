"""
This module defines constraints for sorting arrays.
"""

from ..variable.variable import ArrayVariable
from .abstract_constraint import AbstractConstraint


class ConstraintSorted(AbstractConstraint):
    """Enforces that the elements of an array are sorted in ascending order.

    Args:
        var_1: The array variable to sort.
        constraint_name: A name for the constraint.

    Example:
        >>> from qaekwy.core.model.variable.integer import IntegerVariableArray
        >>> from qaekwy.core.model.constraint.sort import ConstraintSorted
        >>> x = IntegerVariableArray("x", 5, 0, 10)
        >>> constraint = ConstraintSorted(x)
    """

    def __init__(self, var_1: ArrayVariable, constraint_name=None) -> None:
        """Initializes a new sorted constraint.

        Args:
            var_1: The array variable to sort.
            constraint_name: A name for the constraint.
        """
        super().__init__(constraint_name)
        self.var_1 = var_1

    def to_json(self) -> dict:
        """Returns a JSON representation of the constraint."""
        return {
            "name": self.constraint_name,
            "v1": self.var_1.var_name,
            "type": "sorted",
        }

    @staticmethod
    def from_json(json_data: dict, variables: list) -> "ConstraintSorted":
        """Creates a ConstraintSorted instance from a JSON object.

        Args:
            json_data: A dictionary representing the constraint.
            variables: The list of variables in the model.

        Returns:
            An instance of the ConstraintSorted class.
        """
        var1_name = json_data["v1"]

        var1 = next((v for v in variables if v.var_name == var1_name), None)
        if var1 is None:
            raise ValueError(f"Variable '{var1_name}' not found in the model.")

        return ConstraintSorted(var1, json_data.get("name"))


class ConstraintReverseSorted(AbstractConstraint):
    """Enforces that the elements of an array are sorted in descending order.

    Args:
        var_1: The array variable to sort.
        constraint_name: A name for the constraint.

    Example:
        >>> from qaekwy.core.model.variable.integer import IntegerVariableArray
        >>> from qaekwy.core.model.constraint.sort import ConstraintReverseSorted
        >>> x = IntegerVariableArray("x", 5, 0, 10)
        >>> constraint = ConstraintReverseSorted(x)
    """

    def __init__(self, var_1: ArrayVariable, constraint_name=None) -> None:
        """Initializes a new reverse sorted constraint.

        Args:
            var_1: The array variable to sort.
            constraint_name: A name for the constraint.
        """
        super().__init__(constraint_name)
        self.var_1 = var_1

    def to_json(self) -> dict:
        """Returns a JSON representation of the constraint."""
        return {
            "name": self.constraint_name,
            "v1": self.var_1.var_name,
            "type": "rsorted",
        }

    @staticmethod
    def from_json(json_data: dict, variables: list) -> "ConstraintReverseSorted":
        """Creates a ConstraintReverseSorted instance from a JSON object.

        Args:
            json_data: A dictionary representing the constraint.
            variables: The list of variables in the model.

        Returns:
            An instance of the ConstraintReverseSorted class.
        """
        var1_name = json_data["v1"]

        var1 = next((v for v in variables if v.var_name == var1_name), None)
        if var1 is None:
            raise ValueError(f"Variable '{var1_name}' not found in the model.")

        return ConstraintReverseSorted(var1, json_data.get("name"))
