"""RelationalExpression Module

This module defines the RelationalExpression class, which represents a
constraint using a relational expression between variables and values.

Classes:
    RelationalExpression: Represents a constraint using a relational
    expression between variables or values.

"""
from qaekwy.model.constraint.abstract_constraint import AbstractConstraint
from qaekwy.model.variable.variable import Expression


class RelationalExpression(AbstractConstraint):
    """
    Represents a constraint using a relational expression between variables or values.

    This constraint enforces a relational expression that can be evaluated as True or False.
    The expression can involve variables, constants, and mathematical operators.

    Args:
        expr (Expression): The relational expression to be enforced.
        constraint_name (str, optional): A name for the constraint.

    Attributes:
        expr (Expression): The relational expression to be enforced.

    Methods:
        to_json(): Returns a JSON representation of the constraint.

    Example:
        expression = Expression(var_1 + var_2 >= var_3 + 1)
        relational_constraint =
            RelationalExpression(expression, "relational_constraint")
    """

    def __init__(self, expr: Expression, constraint_name=None) -> None:
        """
        Initialize a new relational expression constraint instance.

        Args:
            expr (Expression): The relational expression to be enforced.
            constraint_name (str, optional): A name for the constraint.
        """
        super().__init__(constraint_name)
        self.expr = expr

    def to_json(self) -> dict:
        """
        Convert the constraint to a JSON representation.

        Returns:
            dict: A dictionary containing constraint information in JSON format.
        """
        return {"name": self.constraint_name, "expr": str(self.expr), "type": "rel"}
