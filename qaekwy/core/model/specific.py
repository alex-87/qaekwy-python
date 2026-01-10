"""Specific Constraints Module

This module defines specific constraint classes that represent constraints for minimizing
and maximizing specific variables.

Classes:
    SpecificMinimum: Represents a constraint to minimize a specific variable.
    SpecificMaximum: Represents a constraint to maximize a specific variable.

"""

from .constraint.abstract_constraint import AbstractConstraint
from .variable.variable import Variable


class SpecificMinimum(AbstractConstraint):
    """
    Represents a constraint to minimize a specific variable.

    The SpecificMinimum class defines a constraint that aims to minimize the value
    of a specific variable.

    It inherits from the AbstractConstraint class and provides a method to convert the constraint
    to a JSON representation suitable for serialization.

    Args:
        variable (Variable): The variable to be minimized.
        constraint_name (str, optional): The name of the constraint.

    Example:
        specific_min = SpecificMinimum(my_variable, "minimize_constraint")
    """

    def __init__(self, variable: Variable, constraint_name=None) -> None:
        super().__init__(constraint_name)
        self.variable = variable

    def to_json(self):
        """
        Converts the constraint to a JSON representation.

        Returns:
            dict: A JSON representation of the constraint.
        """
        return {"var": self.variable.var_name, "type": "minimize"}

    @staticmethod
    def from_json(json_data: dict, variables: list) -> "SpecificMinimum":
        """
        Creates a SpecificMinimum instance from a JSON object.

        Args:
            json_data (dict): A dictionary with a "var" key.
            variables (list): The list of variables in the model.

        Returns:
            SpecificMinimum: An instance of the SpecificMinimum class.
        """
        var_name = json_data["var"]
        variable = next((v for v in variables if v.var_name == var_name), None)
        if variable is None:
            raise ValueError(f"Variable '{var_name}' not found in the model.")
        return SpecificMinimum(variable)


class SpecificMaximum(AbstractConstraint):
    """
    Represents a constraint to maximize a specific variable.

    The SpecificMaximum class defines a constraint that aims to maximize the value
    of a specific variable.

    It inherits from the AbstractConstraint class and provides a method to convert the constraint
    to a JSON representation suitable for serialization.

    Args:
        variable (Variable): The variable to be maximized.
        constraint_name (str, optional): The name of the constraint.

    Example:
        specific_max = SpecificMaximum(my_variable, "maximize_constraint")
    """

    def __init__(self, variable: Variable, constraint_name=None) -> None:
        super().__init__(constraint_name)
        self.variable = variable

    def to_json(self):
        """
        Converts the constraint to a JSON representation.

        Returns:
            dict: A JSON representation of the constraint.
        """
        return {"var": self.variable.var_name, "type": "maximize"}

    @staticmethod
    def from_json(json_data: dict, variables: list) -> "SpecificMaximum":
        """
        Creates a SpecificMaximum instance from a JSON object.

        Args:
            json_data (dict): A dictionary with a "var" key.
            variables (list): The list of variables in the model.

        Returns:
            SpecificMaximum: An instance of the SpecificMaximum class.
        """
        var_name = json_data["var"]
        variable = next((v for v in variables if v.var_name == var_name), None)
        if variable is None:
            raise ValueError(f"Variable '{var_name}' not found in the model.")
        return SpecificMaximum(variable)
