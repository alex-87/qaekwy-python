"""ConstraintElement Module

This module defines the ConstraintElement class, which represents
a constraint to enforce an element-wise relationship between two
variables based on a mapping array.

Classes:
    ConstraintElement: Represents a constraint to enforce an element-wise
    relationship between two variables.

"""

from qaekwy.model.constraint.abstract_constraint import AbstractConstraint
from qaekwy.model.variable.variable import ArrayVariable, Variable


class ConstraintElement(AbstractConstraint):
    """
    Represents a constraint to enforce an element-wise relationship
    between two variables.

    This constraint enforces that the values of var_1 and var_2 are
    related element-wise based on a mapping array.

    Args:
        map_array (ArrayVariable): The mapping array that defines the element-wise relationship.
        var_1 (Variable): The first variable in the relationship.
        var_2 (Variable): The second variable in the relationship.
        constraint_name (str, optional): A name for the constraint.

    Attributes:
        map_array (ArrayVariable): The mapping array that defines the element-wise relationship.
        var_1 (Variable): The first variable in the relationship.
        var_2 (Variable): The second variable in the relationship.

    Methods:
        to_json(): Returns a JSON representation of the constraint.

    Example:
        element_constraint =
            ConstraintElement(mapping_array, variable_1, variable_2, "element_constraint")
    """

    def __init__(
        self,
        map_array: ArrayVariable,
        var_1: Variable,
        var_2: Variable,
        constraint_name=None,
    ) -> None:
        """
        Initialize a new element-wise constraint instance.

        Args:
            map_array (ArrayVariable): The mapping array that defines the element-wise relationship.
            var_1 (Variable): The first variable in the relationship.
            var_2 (Variable): The second variable in the relationship.
            constraint_name (str, optional): A name for the constraint.
        """
        super().__init__(constraint_name)
        self.map_array = map_array
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
            "map": self.map_array.var_name,
            "v1": self.var_1.var_name,
            "v2": self.var_2.var_name,
            "type": "element",
        }
