"""ConstraintTan Module

This module defines the ConstraintTan class, which represents a
constraint to enforce a tangent relationship between two variables.

Classes:
    ConstraintTan: Represents a constraint to enforce a tangent
    relationship between two variables.

"""
from qaekwy.model.constraint.abstract_constraint import AbstractConstraint
from qaekwy.model.variable.variable import Variable


class ConstraintTan(AbstractConstraint):
    """
    Represents a constraint to enforce a tangent relationship between two variables.

    This constraint enforces that the tangent of var_1 is equal to var_2, or vice versa.

    Args:
        var_1 (Variable): The variable for which the tangent relationship is enforced.
        var_2 (Variable): The result variable of the tangent relationship.
        constraint_name (str, optional): A name for the constraint.

    Attributes:
        var_1 (Variable): The variable for which the tangent relationship is enforced.
        var_2 (Variable): The result variable of the tangent relationship.

    Methods:
        to_json(): Returns a JSON representation of the constraint.

    Example:
        tangent_constraint =
            ConstraintTan(variable_to_tangent, result_variable, "tangent_constraint")
    """

    def __init__(self, var_1: Variable, var_2: Variable, constraint_name=None) -> None:
        """
        Initialize a new tangent constraint instance.

        Args:
            var_1 (Variable): The variable for which the tangent relationship is enforced.
            var_2 (Variable): The result variable of the tangent relationship.
            constraint_name (str, optional): A name for the constraint.
        """
        super().__init__(constraint_name)
        self.var_1 = var_1
        self.var_2 = var_2

    def to_json(self) -> dict:
        """
        Convert the constraint to a JSON representation.

        Returns:
            dict: A dictionary containing constraint information in JSON format.
        """
        return {
            "name": self.constraint_name,
            "v1": self.var_1.var_name,
            "v2": self.var_2.var_name,
            "type": "tan",
        }
