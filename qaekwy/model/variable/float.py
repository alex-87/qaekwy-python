"""FloatVariable Module

This module defines classes related to float variables.

Classes:
    FloatVariable: Represents a float variable.
    FloatExpressionVariable: Represents a float variable defined by an expression.
    FloatVariableArray: Represents an array of float variables.

"""

from typing import Optional
from qaekwy.model.variable.branch import (
    BranchFloatVal,
    BranchFloatVar,
    BranchVal,
)
from qaekwy.model.variable.variable import (
    ArrayVariable,
    ExpressionVariable,
    Variable,
    VariableType,
)


class FloatVariable(Variable):  # pylint: disable=too-few-public-methods
    """
    Represents a float variable.

    The FloatVariable class represents a float variable.

    Args:
        var_name (str): The name of the variable.
        domain_low (float, optional): The lower bound of the variable's domain.
        domain_high (float, optional): The upper bound of the variable's domain.
        specific_domain (list, optional): A specific domain for the variable.
        branch_val (BranchVal, optional): The brancher value strategy.

    Example:
        my_float_var =
            FloatVariable("x", domain_low=0.0, domain_high=1.0, branch_val=BranchFloatVal.VAL_RND)
    """

    def __init__(  # pylint: disable=too-many-arguments
        self,
        var_name: str,
        domain_low: Optional[float] = None,
        domain_high: Optional[float] = None,
        specific_domain: Optional[list] = None,
        branch_val: BranchVal = BranchFloatVal.VAL_RND,
    ) -> None:
        super().__init__(
            var_name,
            domain_low,
            domain_high,
            specific_domain,
            VariableType.FLOAT,
            branch_val,
        )


class FloatExpressionVariable(
    ExpressionVariable
):  # pylint: disable=too-few-public-methods
    """
    Represents a float variable defined by an expression.

    The FloatExpressionVariable class extends the functionality of the ExpressionVariable
    class to represent float variables that are defined by an expression.

    Args:
        var_name (str): The name of the variable.
        expression: The expression defining the variable.
        branch_val (BranchVal, optional): The brancher value strategy.

    Example:
        expr = Expression(0.5 * x + 0.2)
        my_expr_float_var = FloatExpressionVariable("y", expression=expr,
                                                    branch_val=BranchFloatVal.VAL_MID)
    """

    def __init__(
        self,
        var_name: str,
        expression: str,
        branch_val: BranchVal = BranchFloatVal.VAL_RND,
    ) -> None:
        super().__init__(var_name, expression, VariableType.FLOAT, branch_val)


class FloatVariableArray(ArrayVariable):
    """
    Represents an array of float variables.

    The FloatVariableArray class represents an array of float variables.

    Args:
        var_name (str): The name of the variable.
        length (int): The length of the array.
        domain_low (float, optional): The lower bound of the variables' domain.
        domain_high (float, optional): The upper bound of the variables' domain.
        branch_var (BranchFloatVar, optional): The brancher variable strategy.
        branch_val (BranchVal, optional): The brancher value strategy.

    Example:
        my_float_array = FloatVariableArray("arr", length=5, domain_low=0.0, domain_high=10.0,
                                            branch_var=BranchFloatVar.VAR_RND)
    """

    def __init__(  # pylint: disable=too-many-arguments
        self,
        var_name: str,
        length: int,
        domain_low: Optional[float] = None,
        domain_high: Optional[float] = None,
        branch_var: BranchFloatVar = BranchFloatVar.VAR_RND,
        branch_val: BranchVal = BranchFloatVal.VAL_RND,
    ) -> None:
        super().__init__(
            var_name,
            VariableType.FLOAT_ARRAY,
            length,
            domain_low,
            domain_high,
            branch_var,
            branch_val,
        )
