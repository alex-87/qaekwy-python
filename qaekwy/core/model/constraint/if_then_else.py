"""
This module defines the ConstraintIfThenElse class.
"""

from typing import Optional

from ..variable.variable import Expression, VariableType
from .abstract_constraint import AbstractConstraint


class ConstraintIfThenElse(AbstractConstraint):
    """Represents a conditional constraint.

    This constraint has the form:
    IF condition THEN then_constraint ELSE else_constraint.

    This is a high-level constraint that models conditional logic. It is
    decomposed into simpler constraints.

    Args:
        condition: The condition to evaluate.
        then_constraint: The constraint to enforce if the condition is true.
        else_constraint: The constraint to enforce if the condition is false.
        domain: The variable type domain for the constraint.
        constraint_name: A name for the constraint.

    Example:
        >>> from qaekwy.core.model.variable.integer import IntegerVariable
        >>> from qaekwy.core.model.constraint.if_then_else import ConstraintIfThenElse
        >>> x = IntegerVariable("x", 0, 10)
        >>> y = IntegerVariable("y", 0, 10)
        >>> condition = x > 5
        >>> then_constraint = y == 10
        >>> else_constraint = y == 0
        >>> constraint = ConstraintIfThenElse(condition, then_constraint, else_constraint)
    """

    def __init__(
        self,
        condition: Expression,
        then_constraint: Expression,
        else_constraint: Optional[Expression] = None,
        domain: VariableType = VariableType.INTEGER,
        constraint_name=None,
    ) -> None:
        """Initializes a new if-then-else constraint."""
        super().__init__(constraint_name)
        self.condition = condition
        self.then_constraint = then_constraint
        self.else_constraint = else_constraint
        self.domain = domain

    def to_json(self) -> dict:
        """Serializes the constraint into a JSON-compatible dictionary.

        Returns:
            A dictionary containing the constraint's name, expression, type,
            subtype, and variable set (if applicable). The dictionary
            structure adapts based on the constraint's domain (BOOLEAN,
            FLOAT, or other). The 'expr' field represents the logical
            expression of the constraint, constructed as an if-then-else
            (ITE) expression if an else_constraint is present, or as a
            simple conjunction otherwise.
        """

        expr: Expression
        if self.else_constraint is not None:
            expr = (Expression(self.condition) & Expression(self.then_constraint)) | (
                ~Expression(self.condition) & Expression(self.else_constraint)
            )
        else:
            expr = Expression(self.condition) & Expression(self.then_constraint)

        if self.domain == VariableType.BOOLEAN:
            return {
                "name": self.constraint_name,
                "expr": str(expr),
                "type": "rel",
                "subtype": "ite",
                "ite_condition": str(self.condition),
                "ite_then": str(self.then_constraint),
                "ite_else": (
                    str(self.else_constraint) if self.else_constraint else "None"
                ),
                "varset": "boolean",
            }
        if self.domain == VariableType.FLOAT:
            return {
                "name": self.constraint_name,
                "expr": str(expr),
                "type": "rel",
                "subtype": "ite",
                "ite_condition": str(self.condition),
                "ite_then": str(self.then_constraint),
                "ite_else": (
                    str(self.else_constraint) if self.else_constraint else "None"
                ),
                "varset": "float",
            }

        return {
            "name": self.constraint_name,
            "expr": str(expr),
            "type": "rel",
            "subtype": "ite",
            "ite_condition": str(self.condition),
            "ite_then": str(self.then_constraint),
            "ite_else": str(self.else_constraint) if self.else_constraint else "None",
            "varset": "integer",
        }

    @staticmethod
    def from_json(json_data: dict) -> "ConstraintIfThenElse":
        """Creates a ConstraintIfThenElse instance from a JSON object.

        Args:
            json_data: A dictionary containing constraint information.

        Returns:
            A reconstructed ConstraintIfThenElse instance.
        """
        condition = Expression(json_data["ite_condition"])
        then_constraint = Expression(json_data["ite_then"])
        else_constraint = (
            Expression(json_data["ite_else"])
            if json_data.get("ite_else") and json_data["ite_else"] != "None"
            else None
        )

        varset = json_data.get("varset", "integer").lower()
        if varset == "boolean":
            domain = VariableType.BOOLEAN
        elif varset == "float":
            domain = VariableType.FLOAT
        else:
            domain = VariableType.INTEGER

        return ConstraintIfThenElse(
            condition=condition,
            then_constraint=then_constraint,
            else_constraint=else_constraint,
            domain=domain,
            constraint_name=json_data.get("name"),
        )
