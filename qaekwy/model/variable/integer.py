"""IntegerVariable Module

This module defines classes related to integer variables.

Classes:
    IntegerVariable: Represents an integer variable.
    IntegerExpressionVariable: Represents an integer variable defined by an expression.
    IntegerVariableArray: Represents an array of integer variables.

"""

from typing import Optional
from qaekwy.model.variable.branch import (
    BranchIntegerVal,
    BranchIntegerVar,
    BranchVal,
    BranchVar,
)
from qaekwy.model.variable.variable import (
    ArrayVariable,
    ExpressionVariable,
    Variable,
    VariableType,
)


class IntegerVariable(Variable):  # pylint: disable=too-few-public-methods
    """
    Represents an integer variable.

    The IntegerVariable class represents an integer variable.

    Args:
        var_name (str): The name of the variable.
        domain_low (int, optional): The lower bound of the variable's domain.
        domain_high (int, optional): The upper bound of the variable's domain.
        specific_domain (list, optional): A specific domain for the variable.
        branch_val (BranchVal, optional): The brancher value strategy.

    Example:
        my_integer_var =
            IntegerVariable("x", domain_low=1, domain_high=10, branch_val=BranchIntegerVal.VAL_RND)
    """

    def __init__(  # pylint: disable=too-many-arguments
        self,
        var_name: str,
        domain_low: Optional[int] = None,
        domain_high: Optional[int] = None,
        specific_domain: Optional[list] = None,
        branch_val: BranchVal = BranchIntegerVal.VAL_RND,
    ) -> None:
        super().__init__(
            var_name=var_name,
            domain_low=domain_low,
            domain_high=domain_high,
            specific_domain=specific_domain,
            var_type=VariableType.INTEGER,
            branch_val=branch_val,
        )


class IntegerExpressionVariable(
    ExpressionVariable
):  # pylint: disable=too-few-public-methods
    """
    Represents an integer variable defined by an expression.

    The IntegerExpressionVariable class extends the functionality of the
    ExpressionVariable class to represent integer variables that are defined by an expression.

    Args:
        var_name (str): The name of the variable.
        expression: The expression defining the variable.
        branch_val (BranchVal, optional): The brancher value strategy.

    Example:
        expr = Expression("3 * x + 2")
        my_expr_integer_var = IntegerExpressionVariable("y", expression=expr,
                                                        branch_val=BranchIntegerVal.VAL_MID)
    """

    def __init__(
        self,
        var_name: str,
        expression: str,
        branch_val: BranchVal = BranchIntegerVal.VAL_RND,
    ) -> None:
        super().__init__(var_name, expression, VariableType.INTEGER, branch_val)


class IntegerVariableArray(ArrayVariable):
    """
    Represents an array of integer variables.

    The IntegerVariableArray class represents an array of integer variables.

    Args:
        var_name (str): The name of the variable.
        length (int): The length of the array.
        domain_low (int, optional): The lower bound of the variables' domain.
        domain_high (int, optional): The upper bound of the variables' domain.
        specific_domain (list, optional): A specific domain for the variables.
        branch_var (BranchVar, optional): The brancher variable strategy.
        branch_val (BranchVal, optional): The brancher value strategy.

    Example:
        my_integer_array = IntegerVariableArray("arr", length=5, domain_low=0, domain_high=100,
                                                branch_var=BranchIntegerVar.VAR_MAX)
    """

    def __init__(  # pylint: disable=too-many-arguments
        self,
        var_name: str,
        length: int,
        domain_low: Optional[int] = None,
        domain_high: Optional[int] = None,
        specific_domain: Optional[list] = None,
        branch_var: BranchVar = BranchIntegerVar.VAR_RND,
        branch_val: BranchVal = BranchIntegerVal.VAL_RND,
    ) -> None:
        super().__init__(
            var_name=var_name,
            var_type=VariableType.INTEGER_ARRAY,
            length=length,
            domain_low=domain_low,
            domain_high=domain_high,
            specific_domain=specific_domain,
            branch_var=branch_var,
            branch_val=branch_val,
        )
