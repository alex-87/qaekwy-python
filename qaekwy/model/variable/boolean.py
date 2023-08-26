"""BooleanVariable Module

This module defines classes related to boolean variables.

Classes:
    BooleanVariable: Represents a boolean variable.
    BooleanExpressionVariable: Represents a boolean variable defined by an expression.
    BooleanVariableArray: Represents an array of boolean variables.

"""
from qaekwy.model.variable.branch import BranchVal, BranchVar
from qaekwy.model.variable.variable import (
    ArrayVariable,
    ExpressionVariable,
    Variable,
    VariableType,
)


class BooleanVariable(Variable):  # pylint: disable=too-few-public-methods
    """
    Represents a boolean variable.

    The BooleanVariable class represents a boolean variable.

    Args:
        var_name (str): The name of the variable.
        branch_val (BranchVal): The brancher value strategy.

    Example:
        my_bool_var = BooleanVariable("b1", branch_val=BranchVal.VAL_MIN)
    """

    def __init__(self, var_name: str, branch_val: BranchVal) -> None:
        super().__init__(var_name, 0, 1, VariableType.BOOLEAN, branch_val)


class BooleanExpressionVariable(
    ExpressionVariable
):  # pylint: disable=too-few-public-methods
    """
    Represents a boolean variable defined by an expression.

    The BooleanExpressionVariable class extends the functionality of the
    ExpressionVariable class to represent boolean variables that are defined
    by an expression.

    Args:
        var_name (str): The name of the variable.
        expression: The expression defining the variable.
        branch_val (BranchVal): The brancher value strategy.

    Example:
        expr = Expression(x[3] > 5)
        my_expr_bool_var =
            BooleanExpressionVariable("b2", expression=expr, branch_val=BranchVal.VAL_MID)
    """

    def __init__(self, var_name: str, expression: str, branch_val: BranchVal) -> None:
        super().__init__(var_name, expression, VariableType.BOOLEAN, branch_val)


class BooleanVariableArray(ArrayVariable):  # pylint: disable=too-few-public-methods
    """
    Represents an array of boolean variables.

    The BooleanVariableArray class represents an array of boolean variables.

    Args:
        var_name (str): The name of the variable.
        length (int): The length of the array.
        branch_var (BranchVar): The brancher variable strategy.
        branch_val (BranchVal): The brancher value strategy.

    Example:
        my_bool_array = BooleanVariableArray("bool_arr", length=3, branch_var=BranchVar.VAR_MIN,
                                             branch_val=BranchVal.VAL_RND)
    """

    def __init__(
        self, var_name: str, length: int, branch_var: BranchVar, branch_val: BranchVal
    ) -> None:
        super().__init__(
            var_name, VariableType.BOOLEAN_ARRAY, length, 0, 1, branch_var, branch_val
        )
