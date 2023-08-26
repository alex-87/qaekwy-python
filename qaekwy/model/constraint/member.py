"""ConstraintMember Module

This module defines the ConstraintMember class, which represents a
constraint to enforce a membership relationship between an array
variable and a variable.

Classes:
    ConstraintMember: Represents a constraint to enforce a membership
    relationship between an array variable and a variable.

"""

from qaekwy.model.constraint.abstract_constraint import AbstractConstraint
from qaekwy.model.variable.variable import ArrayVariable, Variable


class ConstraintMember(AbstractConstraint):
    """
    Represents a constraint to enforce a membership relationship between an
    array variable and a variable.

    This constraint enforces that the value of var_2 is a member of the array var_1.

    Args:
        var_1 (ArrayVariable): The array variable in the membership relationship.
        var_2 (Variable): The variable to be checked for membership.
        constraint_name (str, optional): A name for the constraint.

    Attributes:
        var_1 (ArrayVariable): The array variable in the membership relationship.
        var_2 (Variable): The variable to be checked for membership.

    Methods:
        to_json(): Returns a JSON representation of the constraint.

    Example:
        member_constraint =
            ConstraintMember(array_variable, variable_to_check, "member_constraint")
    """

    def __init__(
        self, var_1: ArrayVariable, var_2: Variable, constraint_name=None
    ) -> None:
        """
        Initialize a new membership constraint instance.

        Args:
            var_1 (ArrayVariable): The array variable in the membership relationship.
            var_2 (Variable): The variable to be checked for membership.
            constraint_name (str, optional): A name for the constraint.
        """
        super().__init__(constraint_name)
        self.var_1 = var_1
        self.var_2 = var_2

    def to_json(self):
        """
        Convert the constraint to a JSON representation.

        Returns:
            dict: A dictionary containing constraint information in JSON format.
        """
        return {
            "name": self.constraint_name,
            "v1": self.var_1.var_name,
            "v2": self.var_2.var_name,
            "type": "member",
        }
