"""BooleanVariable Module

This module defines classes related to boolean variables.

Classes:
    BooleanVariable: Represents a boolean variable.
    BooleanExpressionVariable: Represents a boolean variable defined by an expression.
    BooleanVariableArray: Represents an array of boolean variables.
    BooleanVariableMatrix: Represents a matrix of boolean variables.
"""

from typing import Optional

from .branch import BranchBooleanVal, BranchBooleanVar, BranchVal, BranchVar
from .variable import (
    ArrayVariable,
    Expression,
    ExpressionVariable,
    MatrixVariable,
    Variable,
    VariableType,
)


class BooleanVariable(Variable):
    """
    Represents a boolean variable.

    The BooleanVariable class represents a boolean variable.

    Args:
        var_name (str): The name of the variable.
        branch_val (BranchVal): The brancher value strategy.
        branch_order (int, optional): The branching order.

    Example:
        my_bool_var = BooleanVariable("b1", branch_val=BranchVal.VAL_MIN)
    """

    def __init__(
        self,
        var_name: str,
        branch_val: BranchVal = BranchBooleanVal.VAL_RND,
        branch_order: Optional[int] = -1,
    ) -> None:
        super().__init__(
            var_name=var_name,
            domain_low=0,
            domain_high=1,
            var_type=VariableType.BOOLEAN,
            branch_val=branch_val,
            branch_order=branch_order,
        )

    @staticmethod
    def from_json(json_data: dict) -> "BooleanVariable":
        branch_val = BranchBooleanVal.from_json(json_data["brancher_value"])
        return BooleanVariable(
            var_name=json_data["name"],
            branch_val=branch_val,
            branch_order=json_data.get("branching_order", -1),
        )


class BooleanExpressionVariable(ExpressionVariable):
    """
    Represents a boolean variable defined by an expression.

    The BooleanExpressionVariable class extends the functionality of the
    ExpressionVariable class to represent boolean variables that are defined
    by an expression.

    Args:
        var_name (str): The name of the variable.
        expression: The expression defining the variable.
        branch_val (BranchVal): The brancher value strategy.
        branch_order (int, optional): The branching order.

    Example:
        expr = Expression(x[3] > 5)
        my_expr_bool_var =
            BooleanExpressionVariable("b2", expression=expr, branch_val=BranchVal.VAL_MID)
    """

    def __init__(
        self,
        var_name: str,
        expression: str,
        branch_val: BranchVal = BranchBooleanVal.VAL_RND,
        branch_order: Optional[int] = -1,
    ) -> None:
        super().__init__(
            var_name, expression, VariableType.BOOLEAN, branch_val, branch_order
        )

    @staticmethod
    def from_json(json_data: dict) -> "BooleanExpressionVariable":
        branch_val = BranchBooleanVal.from_json(json_data["brancher_value"])
        expression = Expression(json_data["expr"])
        return BooleanExpressionVariable(
            var_name=json_data["name"],
            expression=expression.expr,
            branch_val=branch_val,
            branch_order=json_data.get("branching_order", -1),
        )


class BooleanVariableArray(ArrayVariable):
    """
    Represents an array of boolean variables.

    The BooleanVariableArray class represents an array of boolean variables.

    Args:
        var_name (str): The name of the variable.
        length (int): The length of the array.
        branch_var (BranchVar): The brancher variable strategy.
        branch_val (BranchVal): The brancher value strategy.
        branch_order (int, optional): The branching order.

    Example:
        my_bool_array = BooleanVariableArray("bool_arr", length=3, branch_var=BranchVar.VAR_MIN,
                                             branch_val=BranchVal.VAL_RND)
    """

    def __init__(
        self,
        var_name: str,
        length: int,
        branch_var: BranchVar = BranchBooleanVar.VAR_RND,
        branch_val: BranchVal = BranchBooleanVal.VAL_RND,
        branch_order: Optional[int] = -1,
    ) -> None:
        super().__init__(
            var_name=var_name,
            var_type=VariableType.BOOLEAN_ARRAY,
            length=length,
            domain_low=0,
            domain_high=1,
            branch_var=branch_var,
            branch_val=branch_val,
            branch_order=branch_order,
        )

    @staticmethod
    def from_json(json_data: dict) -> "BooleanVariableArray":
        branch_var = BranchBooleanVar.from_json(json_data["brancher_variable"])
        branch_val = BranchBooleanVal.from_json(json_data["brancher_value"])
        return BooleanVariableArray(
            var_name=json_data["name"],
            length=json_data["length"],
            branch_var=branch_var,
            branch_val=branch_val,
            branch_order=json_data.get("branching_order", -1),
        )


class BooleanVariableMatrix(MatrixVariable):
    """
    Represents a matrix of boolean variables.

    The BooleanVariableMatrix class represents a matrix of boolean variables.

    Args:
        var_name (str): The name of the variable.
        rows (int): The number of rows in the matrix.
        cols (int): The number of columns in the matrix.
        branch_var (BranchVar): The brancher variable strategy.
        branch_val (BranchVal): The brancher value strategy.
        branch_order (int, optional): The branching order.

    Example:
        my_bool_matrix = BooleanVariableMatrix("bool_mat", rows=3, cols=3,
                                              branch_var=BranchVar.VAR_MIN,
                                              branch_val=BranchVal.VAL_RND)
    """

    def __init__(
        self,
        var_name: str,
        rows: int,
        cols: int,
        branch_var: BranchVar = BranchBooleanVar.VAR_RND,
        branch_val: BranchVal = BranchBooleanVal.VAL_RND,
        branch_order: Optional[int] = -1,
    ) -> None:
        super().__init__(
            var_name=var_name,
            var_type=VariableType.BOOLEAN_ARRAY,
            rows=rows,
            cols=cols,
            domain_low=0,
            domain_high=1,
            branch_var=branch_var,
            branch_val=branch_val,
            branch_order=branch_order,
        )

    @staticmethod
    def from_json(json_data: dict) -> "BooleanVariableMatrix":
        branch_var = BranchBooleanVar.from_json(json_data["brancher_variable"])
        branch_val = BranchBooleanVal.from_json(json_data["brancher_value"])
        return BooleanVariableMatrix(
            var_name=json_data["name"],
            rows=json_data["rows"],
            cols=json_data["cols"],
            branch_var=branch_var,
            branch_val=branch_val,
            branch_order=json_data.get("branching_order", -1),
        )
