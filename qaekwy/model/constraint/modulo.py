"""ConstraintModulo Module

This module defines the ConstraintModulo class, which represents a
constraint to enforce a modulo relationship between three variables.

Classes:
    ConstraintModulo: Represents a constraint to enforce a modulo
    relationship between three variables.

"""

from qaekwy.model.constraint.abstract_constraint import AbstractConstraint
from qaekwy.model.variable.variable import Variable


class ConstraintModulo(AbstractConstraint):
    """
    Represents a constraint to enforce a modulo relationship between three variables.

    This constraint enforces that the remainder of dividing var_1 by var_2 is equal to var_3.

    Args:
        var_1 (Variable): The dividend variable in the modulo relationship.
        var_2 (Variable): The divisor variable in the modulo relationship.
        var_3 (Variable): The result variable of the modulo relationship.
        constraint_name (str, optional): A name for the constraint.

    Attributes:
        var_1 (Variable): The dividend variable in the modulo relationship.
        var_2 (Variable): The divisor variable in the modulo relationship.
        var_3 (Variable): The result variable of the modulo relationship.

    Methods:
        to_json(): Returns a JSON representation of the constraint.

    Example:
        modulo_constraint =
            ConstraintModulo(
                dividend_variable,
                divisor_variable,
                result_variable,
                "modulo_constraint"
            )
    """

    def __init__(
        self, var_1: Variable, var_2: Variable, var_3: Variable, constraint_name=None
    ) -> None:
        """
        Initialize a new modulo constraint instance.

        Args:
            var_1 (Variable): The dividend variable in the modulo relationship.
            var_2 (Variable): The divisor variable in the modulo relationship.
            var_3 (Variable): The result variable of the modulo relationship.
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
            "v2": self.var_2.var_name,
            "v3": self.var_3.var_name,
            "type": "mod",
        }
