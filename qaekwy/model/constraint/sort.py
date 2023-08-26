"""ConstraintSorted and ConstraintReverseSorted Module

This module defines the ConstraintSorted and ConstraintReverseSorted classes,
which represent constraints to enforce sorted and reverse-sorted relationships
among elements of an array variable.

Classes:
    ConstraintSorted: Represents a constraint to enforce a sorted relationship
    among elements of an array variable.

    ConstraintReverseSorted: Represents a constraint to enforce a reverse-sorted
    relationship among elements of an array variable.

"""

from qaekwy.model.constraint.abstract_constraint import AbstractConstraint
from qaekwy.model.variable.variable import ArrayVariable


class ConstraintSorted(AbstractConstraint):
    """
    Represents a constraint to enforce a sorted relationship among elements
    of an array variable.

    This constraint enforces that the elements of the array variable var_1
    are in ascending sorted order.

    Args:
        var_1 (ArrayVariable): The array variable for which the sorted relationship is enforced.
        constraint_name (str, optional): A name for the constraint.

    Attributes:
        var_1 (ArrayVariable): The array variable for which the sorted relationship is enforced.

    Methods:
        to_json(): Returns a JSON representation of the constraint.

    Example:
        array_to_sort = ArrayVariable("array_to_sort")
        sorted_constraint = ConstraintSorted(array_to_sort, "sorted_constraint")
        constraint_json = sorted_constraint.to_json()
    """

    def __init__(self, var_1: ArrayVariable, constraint_name=None) -> None:
        """
        Initialize a new sorted constraint instance.

        Args:
            var_1 (ArrayVariable): The array variable for which the sorted
            relationship is enforced.
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
            "v1": self.var_1.var_name,
            "type": "sorted",
        }


class ConstraintReverseSorted(AbstractConstraint):
    """
    Represents a constraint to enforce a reverse-sorted relationship
    among elements of an array variable.

    This constraint enforces that the elements of the array variable var_1
    are in descending sorted order.

    Args:
        var_1 (ArrayVariable): The array variable for which the reverse-sorted
        relationship is enforced.
        constraint_name (str, optional): A name for the constraint.

    Attributes:
        var_1 (ArrayVariable): The array variable for which the reverse-sorted
        relationship is enforced.

    Methods:
        to_json(): Returns a JSON representation of the constraint.

    Example:
        reverse_sorted_constraint =
            ConstraintReverseSorted(array_to_reverse_sort, "reverse_sorted_constraint")
    """

    def __init__(self, var_1: ArrayVariable, constraint_name=None) -> None:
        """
        Initialize a new reverse-sorted constraint instance.

        Args:
            var_1 (ArrayVariable): The array variable for which the reverse-sorted
            relationship is enforced.
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
            "v1": self.var_1.var_name,
            "type": "rsorted",
        }
