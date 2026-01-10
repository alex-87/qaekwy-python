"""
This module defines constraints for enforcing distinctness in arrays.
"""

from ..variable.variable import ArrayVariable, MatrixVariable
from .abstract_constraint import AbstractConstraint


class ConstraintDistinctArray(AbstractConstraint):
    """Enforces that all elements in an array are distinct."""

    def __init__(self, var_1: ArrayVariable, constraint_name=None) -> None:
        """Initializes a new distinct array constraint.

        Args:
            var_1: The array variable.
            constraint_name: A name for the constraint.

        Example:
            >>> from qaekwy.core.model.variable.integer import IntegerVariableArray
            >>> from qaekwy.core.model.constraint.distinct import ConstraintDistinctArray
            >>> x = IntegerVariableArray("x", 5, 0, 10)
            >>> constraint = ConstraintDistinctArray(x)
        """
        super().__init__(constraint_name)
        self.var_1 = var_1

    def to_json(self) -> dict:
        """Returns a JSON representation of the constraint."""
        return {
            "name": self.constraint_name,
            "type": "distinct",
            "v1": self.var_1.var_name,
            "selection": "standard",
        }

    @staticmethod
    def from_json(json_data: dict, variables: list) -> "ConstraintDistinctArray":
        """Creates a ConstraintDistinctArray instance from a JSON object.

        Args:
            json_data: A dictionary representing the constraint.
            variables: The list of variables in the model.

        Returns:
            An instance of the ConstraintDistinctArray class.
        """
        var1_name = json_data["v1"]

        var1 = next((v for v in variables if v.var_name == var1_name), None)
        if var1 is None:
            raise ValueError(f"Variable '{var1_name}' not found in the model.")

        return ConstraintDistinctArray(var1, json_data.get("name"))


class ConstraintDistinctRow(AbstractConstraint):
    """Enforces that all elements in a specific row of an matrix are distinct.

    Args:
        var_1: The matrix variable.
        size: The number of elements in the row.
        idx: The index of the row.
        constraint_name: A name for the constraint.
    """

    def __init__(
        self, var_1: MatrixVariable, size: int, idx: int, constraint_name=None
    ) -> None:
        """Initializes a new distinct row constraint.

        Args:
            var_1: The matrix variable.
            size: The number of elements in the row.
            idx: The index of the row.
            constraint_name: A name for the constraint.
        """
        super().__init__(constraint_name)
        self.var_1 = var_1
        self.size = size
        self.idx = idx

    def to_json(self) -> dict:
        """Returns a JSON representation of the constraint."""
        return {
            "name": self.constraint_name,
            "type": "distinct",
            "v1": self.var_1.var_name,
            "selection": "row",
            "size": self.size,
            "index": self.idx,
        }

    @staticmethod
    def from_json(json_data: dict, variables: list) -> "ConstraintDistinctRow":
        """Creates a ConstraintDistinctRow instance from a JSON object.

        Args:
            json_data: A dictionary representing the constraint.
            variables: The list of variables in the model.

        Returns:
            An instance of the ConstraintDistinctRow class.
        """
        var1_name = json_data["v1"]

        var1 = next((v for v in variables if v.var_name == var1_name), None)
        if var1 is None:
            raise ValueError(f"Variable '{var1_name}' not found in the model.")

        return ConstraintDistinctRow(
            var1, json_data["size"], json_data["index"], json_data.get("name")
        )


class ConstraintDistinctCol(AbstractConstraint):
    """Enforces that all elements in a specific column of an matrix are distinct.

    Args:
        var_1: The matrix variable.
        size: The number of elements in the column.
        idx: The index of the column.
        constraint_name: A name for the constraint.
    """

    def __init__(
        self, var_1: MatrixVariable, size: int, idx: int, constraint_name=None
    ) -> None:
        """Initializes a new distinct column constraint.

        Args:
            var_1: The matrix variable.
            size: The number of elements in the column.
            idx: The index of the column.
            constraint_name: A name for the constraint.
        """
        super().__init__(constraint_name)
        self.var_1 = var_1
        self.size = size
        self.idx = idx

    def to_json(self) -> dict:
        """Returns a JSON representation of the constraint."""
        return {
            "name": self.constraint_name,
            "type": "distinct",
            "v1": self.var_1.var_name,
            "selection": "col",
            "size": self.size,
            "index": self.idx,
        }

    @staticmethod
    def from_json(json_data: dict, variables: list) -> "ConstraintDistinctCol":
        """Creates a ConstraintDistinctCol instance from a JSON object.

        Args:
            json_data: A dictionary representing the constraint.
            variables: The list of variables in the model.

        Returns:
            An instance of the ConstraintDistinctCol class.
        """
        var1_name = json_data["v1"]

        var1 = next((v for v in variables if v.var_name == var1_name), None)
        if var1 is None:
            raise ValueError(f"Variable '{var1_name}' not found in the model.")

        return ConstraintDistinctCol(
            var1, json_data["size"], json_data["index"], json_data.get("name")
        )


class ConstraintDistinctSlice(AbstractConstraint):
    """Enforces that all elements in a specific slice of an matrix are distinct.

    Args:
        var_1: The matrix variable.
        size: The number of elements in the slice.
        offset_start_x: The starting x-offset of the slice.
        offset_start_y: The starting y-offset of the slice.
        offset_end_x: The ending x-offset of the slice.
        offset_end_y: The ending y-offset of the slice.
        constraint_name: A name for the constraint.
    """

    def __init__(
        self,
        var_1: MatrixVariable,
        size: int,
        offset_start_x: int,
        offset_start_y: int,
        offset_end_x: int,
        offset_end_y: int,
        constraint_name=None,
    ) -> None:
        """Initializes a new distinct slice constraint.

        Args:
            var_1: The matrix variable.
            size: The number of elements in the slice.
            offset_start_x: The starting x-offset of the slice.
            offset_start_y: The starting y-offset of the slice.
            offset_end_x: The ending x-offset of the slice.
            offset_end_y: The ending y-offset of the slice.
            constraint_name: A name for the constraint.
        """
        super().__init__(constraint_name)
        self.var_1 = var_1
        self.size = size
        self.offset_start_x = offset_start_x
        self.offset_start_y = offset_start_y
        self.offset_end_x = offset_end_x
        self.offset_end_y = offset_end_y

    def to_json(self) -> dict:
        """Returns a JSON representation of the constraint."""
        return {
            "name": self.constraint_name,
            "type": "distinct",
            "v1": self.var_1.var_name,
            "selection": "slice",
            "size": self.size,
            "offset_start_x": self.offset_start_x,
            "offset_start_y": self.offset_start_y,
            "offset_end_x": self.offset_end_x,
            "offset_end_y": self.offset_end_y,
        }

    @staticmethod
    def from_json(json_data: dict, variables: list) -> "ConstraintDistinctSlice":
        """Creates a ConstraintDistinctSlice instance from a JSON object.

        Args:
            json_data: A dictionary representing the constraint.
            variables: The list of variables in the model.

        Returns:
            An instance of the ConstraintDistinctSlice class.
        """
        var1_name = json_data["v1"]

        var1 = next((v for v in variables if v.var_name == var1_name), None)
        if var1 is None:
            raise ValueError(f"Variable '{var1_name}' not found in the model.")

        return ConstraintDistinctSlice(
            var1,
            json_data["size"],
            json_data["offset_start_x"],
            json_data["offset_start_y"],
            json_data["offset_end_x"],
            json_data["offset_end_y"],
            json_data.get("name"),
        )
