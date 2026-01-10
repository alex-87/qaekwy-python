"""FloatVariable Module

This module defines classes related to float variables.

Classes:
    FloatVariable: Represents a float variable.
    FloatExpressionVariable: Represents a float variable defined by an expression.
    FloatVariableArray: Represents an array of float variables.
    FloatVariableMatrix: Represents a matrix of float variables.
"""

from typing import Optional

from .branch import BranchFloatVal, BranchFloatVar, BranchVal
from .variable import (
    ArrayVariable,
    Expression,
    ExpressionVariable,
    MatrixVariable,
    Variable,
    VariableType,
)


class FloatVariable(Variable):
    """
    Represents a float variable.

    The FloatVariable class represents a float variable.

    Args:
        var_name (str): The name of the variable.
        domain_low (float, optional): The lower bound of the variable's domain.
        domain_high (float, optional): The upper bound of the variable's domain.
        branch_val (BranchVal, optional): The brancher value strategy.
        branch_order (int, optional): The branching order.

    Example:
        my_float_var =
            FloatVariable("x", domain_low=0.0, domain_high=1.0, branch_val=BranchFloatVal.VAL_RND)
    """

    def __init__(
        self,
        var_name: str,
        domain_low: Optional[float] = None,
        domain_high: Optional[float] = None,
        branch_val: BranchVal = BranchFloatVal.VAL_RND,
        branch_order: Optional[int] = -1,
    ) -> None:
        super().__init__(
            var_name=var_name,
            var_type=VariableType.FLOAT,
            domain_low=domain_low,
            domain_high=domain_high,
            branch_val=branch_val,
            branch_order=branch_order,
        )

    @staticmethod
    def from_json(json_data: dict) -> "FloatVariable":
        branch_val = BranchFloatVal.from_json(json_data["brancher_value"])
        return FloatVariable(
            var_name=json_data["name"],
            domain_low=json_data.get("domlow"),
            domain_high=json_data.get("domup"),
            branch_val=branch_val,
            branch_order=json_data.get("branching_order", -1),
        )


class FloatExpressionVariable(ExpressionVariable):
    """
    Represents a float variable defined by an expression.

    The FloatExpressionVariable class extends the functionality of the ExpressionVariable
    class to represent float variables that are defined by an expression.

    Args:
        var_name (str): The name of the variable.
        expression: The expression defining the variable.
        branch_val (BranchVal, optional): The brancher value strategy.
        branch_order (int, optional): The branching order.

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
        branch_order: Optional[int] = -1,
    ) -> None:
        super().__init__(
            var_name=var_name,
            expression=expression,
            var_type=VariableType.FLOAT,
            branch_val=branch_val,
            branch_order=branch_order,
        )

    @staticmethod
    def from_json(json_data: dict) -> "FloatExpressionVariable":
        branch_val = BranchFloatVal.from_json(json_data["brancher_value"])
        expression = Expression(json_data["expr"])
        return FloatExpressionVariable(
            var_name=json_data["name"],
            expression=expression.expr,
            branch_val=branch_val,
            branch_order=json_data.get("branching_order", -1),
        )


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
        branch_order (int, optional): The branching order.

    Example:
        my_float_array = FloatVariableArray("arr", length=5, domain_low=0.0, domain_high=10.0,
                                            branch_var=BranchFloatVar.VAR_RND)
    """

    def __init__(
        self,
        var_name: str,
        length: int,
        domain_low: Optional[float] = None,
        domain_high: Optional[float] = None,
        branch_var: BranchFloatVar = BranchFloatVar.VAR_RND,
        branch_val: BranchVal = BranchFloatVal.VAL_RND,
        branch_order: Optional[int] = -1,
    ) -> None:
        super().__init__(
            var_name=var_name,
            var_type=VariableType.FLOAT_ARRAY,
            length=length,
            domain_low=domain_low,
            domain_high=domain_high,
            branch_var=branch_var,
            branch_val=branch_val,
            branch_order=branch_order,
        )

    @staticmethod
    def from_json(json_data: dict) -> "FloatVariableArray":
        branch_var = BranchFloatVar.from_json(json_data["brancher_variable"])
        branch_val = BranchFloatVal.from_json(json_data["brancher_value"])
        return FloatVariableArray(
            var_name=json_data["name"],
            length=json_data["length"],
            domain_low=json_data.get("domlow"),
            domain_high=json_data.get("domup"),
            branch_var=branch_var,
            branch_val=branch_val,
            branch_order=json_data.get("branching_order", -1),
        )


class FloatVariableMatrix(MatrixVariable):
    """
    Represents a matrix of float variables.

    The FloatVariableMatrix class represents a matrix of float variables.
    Args:
        var_name (str): The name of the variable.
        rows (int): The number of rows in the matrix.
        cols (int): The number of columns in the matrix.
        domain_low (float, optional): The lower bound of the variables' domain.
        domain_high (float, optional): The upper bound of the variables' domain.
        branch_var (BranchFloatVar, optional): The brancher variable strategy.
        branch_val (BranchVal, optional): The brancher value strategy.
        branch_order (int, optional): The branching order.

    Example:
        my_float_matrix = FloatMatrixVariable("mat", rows=3, cols=3,
                                              domain_low=0.0, domain_high=1.0,
                                              branch_var=BranchFloatVar.VAR_RND)
    """

    def __init__(
        self,
        var_name: str,
        rows: int,
        cols: int,
        domain_low: Optional[float] = None,
        domain_high: Optional[float] = None,
        branch_var: BranchFloatVar = BranchFloatVar.VAR_RND,
        branch_val: BranchVal = BranchFloatVal.VAL_RND,
        branch_order: Optional[int] = -1,
    ) -> None:
        super().__init__(
            var_name=var_name,
            var_type=VariableType.FLOAT_ARRAY,
            rows=rows,
            cols=cols,
            domain_low=domain_low,
            domain_high=domain_high,
            branch_var=branch_var,
            branch_val=branch_val,
            branch_order=branch_order,
        )

    @staticmethod
    def from_json(json_data: dict) -> "FloatVariableMatrix":
        branch_var = BranchFloatVar.from_json(json_data["brancher_variable"])
        branch_val = BranchFloatVal.from_json(json_data["brancher_value"])
        return FloatVariableMatrix(
            var_name=json_data["name"],
            rows=json_data["rows"],
            cols=json_data["cols"],
            domain_low=json_data.get("domlow"),
            domain_high=json_data.get("domup"),
            branch_var=branch_var,
            branch_val=branch_val,
            branch_order=json_data.get("branching_order", -1),
        )
