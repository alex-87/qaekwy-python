"""
This module defines the RelationalExpression class.
"""

from ..variable.variable import Expression, VariableType
from .abstract_constraint import AbstractConstraint


class RelationalExpression(AbstractConstraint):
    """Enforces a relational expression.

    The expression can involve variables, constants, and mathematical operators.

    Args:
        expr: The relational expression to enforce.
        domain: The variable type domain.
        constraint_name: A name for the constraint.

    Example:
        >>> from qaekwy.core.model.variable.integer import IntegerVariable
        >>> from qaekwy.core.model.constraint.relational import RelationalExpression
        >>> x = IntegerVariable("x", 0, 10)
        >>> y = IntegerVariable("y", 0, 10)
        >>> constraint = RelationalExpression(x + y <= 10)
    """

    def __init__(
        self,
        expr: Expression,
        domain: VariableType = VariableType.INTEGER,
        constraint_name=None,
    ) -> None:
        """Initializes a new relational expression constraint.

        Args:
            expr: The relational expression to enforce.
            domain: The variable type domain.
            constraint_name: A name for the constraint.
        """
        super().__init__(constraint_name)
        self.expr = expr
        self.domain = domain

    def to_json(self) -> dict:
        """Returns a JSON representation of the constraint."""
        if self.domain == VariableType.BOOLEAN:
            return {
                "name": self.constraint_name,
                "expr": str(self.expr),
                "type": "rel",
                "varset": "boolean",
            }
        if self.domain == VariableType.FLOAT:
            return {
                "name": self.constraint_name,
                "expr": str(self.expr),
                "type": "rel",
                "varset": "float",
            }

        return {"name": self.constraint_name, "expr": str(self.expr), "type": "rel"}

    @staticmethod
    def from_json(json_data: dict) -> "RelationalExpression":
        """Creates a RelationalExpression instance from a JSON object.

        Args:
            json_data: A dictionary containing constraint information.

        Returns:
            A RelationalExpression instance.
        """
        expr = Expression(json_data["expr"])
        domain = VariableType[json_data.get("varset", "INTEGER").upper()]
        return RelationalExpression(expr, domain, json_data.get("name"))
