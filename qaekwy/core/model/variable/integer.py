"""IntegerVariable Module

This module defines classes related to integer variables.

Classes:
    IntegerVariable: Represents an integer variable.
    IntegerExpressionVariable: Represents an integer variable defined by an expression.
    IntegerVariableArray: Represents an array of integer variables.
    IntegerVariableMatrix: Represents a matrix of integer variables.

"""

from typing import Optional

from .branch import BranchIntegerVal, BranchIntegerVar, BranchVal, BranchVar
from .variable import (
    ArrayVariable,
    Expression,
    ExpressionVariable,
    MatrixVariable,
    Variable,
    VariableType,
)


class IntegerVariable(Variable):
    """
    Represents an integer variable.

    The IntegerVariable class represents an integer variable.

    Args:
        var_name (str): The name of the variable.
        domain_low (int, optional): The lower bound of the variable's domain.
        domain_high (int, optional): The upper bound of the variable's domain.
        specific_domain (list[int], optional): A specific domain for the variable.
        branch_val (BranchVal, optional): The brancher value strategy.
        branch_order (int, optional): The branching order.

    Example:
        my_integer_var =
            IntegerVariable("x", domain_low=1, domain_high=10, branch_val=BranchIntegerVal.VAL_RND)
    """

    def __init__(
        self,
        var_name: str,
        domain_low: Optional[int] = None,
        domain_high: Optional[int] = None,
        specific_domain: Optional[list[int]] = None,
        branch_val: BranchVal = BranchIntegerVal.VAL_RND,
        branch_order: Optional[int] = -1,
    ) -> None:
        super().__init__(
            var_name=var_name,
            domain_low=domain_low,
            domain_high=domain_high,
            specific_domain=specific_domain,
            var_type=VariableType.INTEGER,
            branch_val=branch_val,
            branch_order=branch_order,
        )

    @staticmethod
    def from_json(json_data: dict) -> "IntegerVariable":
        branch_val = BranchIntegerVal.from_json(json_data["brancher_value"])
        return IntegerVariable(
            var_name=json_data["name"],
            domain_low=json_data.get("domlow"),
            domain_high=json_data.get("domup"),
            specific_domain=json_data.get("specific_domain"),
            branch_val=branch_val,
            branch_order=json_data.get("branching_order", -1),
        )


class IntegerExpressionVariable(ExpressionVariable):
    """
    Represents an integer variable defined by an expression.

    The IntegerExpressionVariable class extends the functionality of the
    ExpressionVariable class to represent integer variables that are defined by an expression.

    Args:
        var_name (str): The name of the variable.
        expression: The expression defining the variable.
        branch_val (BranchVal, optional): The brancher value strategy.
        branch_order (int, optional): The branching order.

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
        branch_order: Optional[int] = -1,
    ) -> None:
        super().__init__(
            var_name, expression, VariableType.INTEGER, branch_val, branch_order
        )

    @staticmethod
    def from_json(json_data: dict) -> "IntegerExpressionVariable":
        branch_val = BranchIntegerVal.from_json(json_data["brancher_value"])
        expression = Expression(json_data["expr"])
        return IntegerExpressionVariable(
            var_name=json_data["name"],
            expression=expression.expr,
            branch_val=branch_val,
            branch_order=json_data.get("branching_order", -1),
        )


class IntegerVariableArray(ArrayVariable):
    """
    Represents an array of integer variables.

    The IntegerVariableArray class represents an array of integer variables.

    Args:
        var_name (str): The name of the variable.
        length (int): The length of the array.
        domain_low (int, optional): The lower bound of the variables' domain.
        domain_high (int, optional): The upper bound of the variables' domain.
        specific_domain (list[int], optional): A specific domain for the variables.
        branch_var (BranchVar, optional): The brancher variable strategy.
        branch_val (BranchVal, optional): The brancher value strategy.
        branch_order (int, optional): The branching order.

    Example:
        my_integer_array = IntegerVariableArray("arr", length=5, domain_low=0, domain_high=100,
                                                branch_var=BranchIntegerVar.VAR_MAX)
    """

    def __init__(
        self,
        var_name: str,
        length: int,
        domain_low: Optional[int] = None,
        domain_high: Optional[int] = None,
        specific_domain: Optional[list[int]] = None,
        branch_var: BranchVar = BranchIntegerVar.VAR_RND,
        branch_val: BranchVal = BranchIntegerVal.VAL_RND,
        branch_order: Optional[int] = -1,
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
            branch_order=branch_order,
        )

    @staticmethod
    def from_json(json_data: dict) -> "IntegerVariableArray":
        branch_var = BranchIntegerVar.from_json(json_data["brancher_variable"])
        branch_val = BranchIntegerVal.from_json(json_data["brancher_value"])
        return IntegerVariableArray(
            var_name=json_data["name"],
            length=json_data["length"],
            domain_low=json_data.get("domlow"),
            domain_high=json_data.get("domup"),
            specific_domain=json_data.get("specific_domain"),
            branch_var=branch_var,
            branch_val=branch_val,
            branch_order=json_data.get("branching_order", -1),
        )


class IntegerVariableMatrix(MatrixVariable):
    """
    Represents an integer matrix variable.

    The IntegerVariableMatrix class represents an integer matrix variable.
    Args:
        var_name (str): The name of the variable.
        rows (int): The number of rows in the matrix.
        cols (int): The number of columns in the matrix.
        domain_low (int, optional): The lower bound of the variables' domain.
        domain_high (int, optional): The upper bound of the variables' domain.
        specific_domain (list[int], optional): A specific domain for the variables.
        branch_var (BranchVar, optional): The brancher variable strategy.
        branch_val (BranchVal, optional): The brancher value strategy.
        branch_order (int, optional): The branching order.

    Example:
        my_integer_matrix = IntegerMatrixVariable("matrix", rows=3, cols=3,
                                                 domain_low=0, domain_high=100,
                                                 branch_var=BranchIntegerVar.VAR_MAX)
    """

    def __init__(
        self,
        var_name: str,
        rows: int,
        cols: int,
        domain_low: Optional[int] = None,
        domain_high: Optional[int] = None,
        specific_domain: Optional[list[int]] = None,
        branch_var: BranchVar = BranchIntegerVar.VAR_RND,
        branch_val: BranchVal = BranchIntegerVal.VAL_RND,
        branch_order: Optional[int] = -1,
    ) -> None:
        super().__init__(
            var_name=var_name,
            var_type=VariableType.INTEGER_ARRAY,
            rows=rows,
            cols=cols,
            domain_low=domain_low,
            domain_high=domain_high,
            specific_domain=specific_domain,
            branch_var=branch_var,
            branch_val=branch_val,
            branch_order=branch_order,
        )

    @staticmethod
    def from_json(json_data: dict) -> "IntegerVariableMatrix":
        return IntegerVariableMatrix(
            var_name=json_data["name"],
            rows=json_data["rows"],
            cols=json_data["cols"],
            domain_low=json_data.get("domlow"),
            domain_high=json_data.get("domup"),
            specific_domain=json_data.get("specific_domain"),
            branch_var=BranchIntegerVar.from_json(json_data["brancher_variable"]),
            branch_val=BranchIntegerVal.from_json(json_data["brancher_value"]),
            branch_order=json_data.get("branching_order", -1),
        )
