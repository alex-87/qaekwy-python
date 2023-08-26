"""ConstraintDistinct Module

This module defines constraint classes for enforcing distinctness in arrays or
matrices.

Classes:
    ConstraintDistinctArray:
    Represents a constraint to ensure distinctness within an array.

    ConstraintDistinctRow:
    Represents a constraint to ensure distinctness within a specific row of an array.

    ConstraintDistinctCol:
    Represents a constraint to ensure distinctness within a specific column of an array.

    ConstraintDistinctSlice:
    Represents a constraint to ensure distinctness within a specific slice of an array.

"""

from qaekwy.model.constraint.abstract_constraint import AbstractConstraint
from qaekwy.model.variable.variable import ArrayVariable


class ConstraintDistinctArray(AbstractConstraint):
    """
    Represents a constraint to ensure distinctness within an array.

    This constraint enforces that all elements within the given array variable are distinct.

    Args:
        var_1 (ArrayVariable): The array variable to enforce distinctness for.
        constraint_name (str, optional): A name for the constraint.

    Attributes:
        var_1 (ArrayVariable): The array variable to enforce distinctness for.

    Methods:
        to_json(): Returns a JSON representation of the constraint.

    Example:
        distinct_constraint = ConstraintDistinctArray(array_var, "distinct_array_constraint")
    """

    def __init__(self, var_1: ArrayVariable, constraint_name=None) -> None:
        """
        Initialize a new distinct array constraint instance.

        Args:
            var_1 (ArrayVariable): The array variable to enforce distinctness for.
            constraint_name (str, optional): A name for the constraint.
        """
        super().__init__(constraint_name)
        self.var_1 = var_1

    def to_json(self):
        """
        Convert the constraint to a JSON representation.

        Returns:
            dict: A dictionary containing constraint information in JSON format.
        """
        return {
            "name": self.constraint_name,
            "type": "distinct",
            "v1": self.var_1.var_name,
            "selection": "standard",
        }


class ConstraintDistinctRow(AbstractConstraint):
    """
    Represents a constraint to ensure distinctness within a specific row of an array.

    This constraint enforces that all elements within a designated row of the given array variable
    are distinct from each other.

    Args:
        var_1 (ArrayVariable): The array variable to enforce distinctness within a row.
        size (int): The number of elements in the row to ensure distinctness for.
        idx (int): The index of the row to enforce distinctness for.
        constraint_name (str, optional): A name for the constraint.

    Attributes:
        var_1 (ArrayVariable): The array variable to enforce distinctness within a row.
        size (int): The number of elements in the row to ensure distinctness for.
        idx (int): The index of the row to enforce distinctness for.

    Methods:
        to_json(): Returns a JSON representation of the constraint.

    Example:
        distinct_row_constraint =
        ConstraintDistinctRow(array_var, size=3, idx=1, constraint_name="distinct_row_constraint")
    """

    def __init__(
        self, var_1: ArrayVariable, size: int, idx: int, constraint_name=None
    ) -> None:
        """
        Initialize a new distinct row constraint instance.

        Args:
            var_1 (ArrayVariable): The array variable to enforce distinctness within a row.
            size (int): The number of elements in the row to ensure distinctness for.
            idx (int): The index of the row to enforce distinctness for.
            constraint_name (str, optional): A name for the constraint.
        """
        super().__init__(constraint_name)
        self.var_1 = var_1
        self.size = size
        self.idx = idx

    def to_json(self):
        """
        Convert the constraint to a JSON representation.

        Returns:
            dict: A dictionary containing constraint information in JSON format.
        """
        return {
            "name": self.constraint_name,
            "type": "distinct",
            "v1": self.var_1.var_name,
            "selection": "row",
            "size": self.size,
            "index": self.idx,
        }


class ConstraintDistinctCol(AbstractConstraint):
    """
    Represents a constraint to ensure distinctness within a specific column of an array.

    This constraint enforces that all elements within a designated column of
    the given array variable are distinct from each other.

    Args:
        var_1 (ArrayVariable): The array variable to enforce distinctness within a column.
        size (int): The number of elements in the column to ensure distinctness for.
        idx (int): The index of the column to enforce distinctness for.
        constraint_name (str, optional): A name for the constraint.

    Attributes:
        var_1 (ArrayVariable): The array variable to enforce distinctness within a column.
        size (int): The number of elements in the column to ensure distinctness for.
        idx (int): The index of the column to enforce distinctness for.

    Methods:
        to_json(): Returns a JSON representation of the constraint.

    Example:
        distinct_col_constraint =
        ConstraintDistinctCol(array_var, size=3, idx=0, constraint_name="distinct_col_constraint")
    """

    def __init__(
        self, var_1: ArrayVariable, size: int, idx: int, constraint_name=None
    ) -> None:
        """
        Initialize a new distinct column constraint instance.

        Args:
            var_1 (ArrayVariable): The array variable to enforce distinctness within a column.
            size (int): The number of elements in the column to ensure distinctness for.
            idx (int): The index of the column to enforce distinctness for.
            constraint_name (str, optional): A name for the constraint.
        """
        super().__init__(constraint_name)
        self.var_1 = var_1
        self.size = size
        self.idx = idx

    def to_json(self):
        """
        Convert the constraint to a JSON representation.

        Returns:
            dict: A dictionary containing constraint information in JSON format.
        """
        return {
            "name": self.constraint_name,
            "type": "distinct",
            "v1": self.var_1.var_name,
            "selection": "col",
            "size": self.size,
            "index": self.idx,
        }


class ConstraintDistinctSlice(AbstractConstraint):
    """
    Represents a constraint to ensure distinctness within a specific slice of an array.

    This constraint enforces that all elements within a designated rectangular
    slice of the given array variable are distinct from each other.

    Args:
        var_1 (ArrayVariable): The array variable to enforce distinctness within a slice.
        size (int): The number of elements in the slice to ensure distinctness for.
        offset_start_x (int): The starting offset along the x-axis for the slice.
        offset_start_y (int): The starting offset along the y-axis for the slice.
        offset_end_x (int): The ending offset along the x-axis for the slice.
        offset_end_y (int): The ending offset along the y-axis for the slice.
        constraint_name (str, optional): A name for the constraint.

    Attributes:
        var_1 (ArrayVariable): The array variable to enforce distinctness within a slice.
        size (int): The number of elements in the slice to ensure distinctness for.
        offset_start_x (int): The starting offset along the x-axis for the slice.
        offset_start_y (int): The starting offset along the y-axis for the slice.
        offset_end_x (int): The ending offset along the x-axis for the slice.
        offset_end_y (int): The ending offset along the y-axis for the slice.

    Methods:
        to_json(): Returns a JSON representation of the constraint.

    Example:
        distinct_slice_constraint =
            ConstraintDistinctSlice(
                array_var,
                size=6,
                offset_start_x=1,
                offset_start_y=1,
                offset_end_x=3,
                offset_end_y=2,
                constraint_name="distinct_slice_constraint")
    """

    def __init__(  # pylint: disable=too-many-arguments
        self,
        var_1: ArrayVariable,
        size: int,
        offset_start_x: int,
        offset_start_y: int,
        offset_end_x: int,
        offset_end_y: int,
        constraint_name=None,
    ) -> None:
        """
        Initialize a new distinct slice constraint instance.

        Args:
            var_1 (ArrayVariable): The array variable to enforce distinctness within a slice.
            size (int): The number of elements in the slice to ensure distinctness for.
            offset_start_x (int): The starting offset along the x-axis for the slice.
            offset_start_y (int): The starting offset along the y-axis for the slice.
            offset_end_x (int): The ending offset along the x-axis for the slice.
            offset_end_y (int): The ending offset along the y-axis for the slice.
            constraint_name (str, optional): A name for the constraint.
        """
        super().__init__(constraint_name)
        self.var_1 = var_1
        self.size = size
        self.offset_start_x = offset_start_x
        self.offset_start_y = offset_start_y
        self.offset_end_x = offset_end_x
        self.offset_end_y = offset_end_y

    def to_json(self):
        """
        Convert the constraint to a JSON representation.

        Returns:
            dict: A dictionary containing constraint information in JSON format.
        """
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
