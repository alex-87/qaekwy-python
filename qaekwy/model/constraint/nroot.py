"""ConstraintNRoot Module

This module defines the ConstraintNRoot class, which represents a
constraint to enforce an n-th root relationship between three variables.

Classes:
    ConstraintNRoot: Represents a constraint to enforce an n-th root
    relationship between three variables.

"""

from qaekwy.model.constraint.abstract_constraint import AbstractConstraint
from qaekwy.model.variable.variable import Variable


class ConstraintNRoot(AbstractConstraint):
    """
    Represents a constraint to enforce an n-th root relationship between three variables.

    This constraint enforces that the n-th root of var_1 is equal to var_3, or vice versa.

    Args:
        var_1 (Variable): The variable for which the n-th root is enforced.
        var_2 (int): The value of n for the n-th root.
        var_3 (Variable): The result variable of the n-th root relationship.
        constraint_name (str, optional): A name for the constraint.

    Attributes:
        var_1 (Variable): The variable for which the n-th root is enforced.
        var_2 (int): The value of n for the n-th root.
        var_3 (Variable): The result variable of the n-th root relationship.

    Methods:
        to_json(): Returns a JSON representation of the constraint.

    Example:
        nroot_constraint =
            ConstraintNRoot(variable_to_root, n_value, result_variable, "nroot_constraint")
    """

    def __init__(
        self, var_1: Variable, var_2: int, var_3: Variable, constraint_name=None
    ) -> None:
        """
        Initialize a new n-th root constraint instance.

        Args:
            var_1 (Variable): The variable for which the n-th root is enforced.
            var_2 (int): The value of n for the n-th root.
            var_3 (Variable): The result variable of the n-th root relationship.
            constraint_name (str, optional): A name for the constraint.
        """
        super().__init__(constraint_name)
        self.var_1 = var_1
        self.var_2 = var_2
        self.var_3 = var_3

    def to_json(self) -> dict:
        """
        Convert the constraint to a JSON representation.

        Returns:
            dict: A dictionary containing constraint information in JSON format.
        """
        return {
            "name": self.constraint_name,
            "v1": self.var_1.var_name,
            "v2": self.var_2,
            "v3": self.var_3.var_name,
            "type": "nroot",
        }
