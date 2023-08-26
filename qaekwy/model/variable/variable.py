"""Variable Module

This module defines variable bases.

Enums:
    VariableType: Represents different types of variables.

Classes:

    ArrayVariable: Represents an array-type variable.
    Variable: Represents a variable.
    ExpressionVariable: Represents a variable defined by an expression.
"""
from enum import Enum
from typing import Optional

from qaekwy.model.variable.branch import (
    BranchIntegerVal,
    BranchIntegerVar,
    BranchVal,
    BranchVar,
)


class VariableType(Enum):
    """
    Represents different types of variables.

    The VariableType enum defines symbolic representations of various variable types
    used in constraint-based modeling and optimization, such as integer, integer array,
    float, float array, boolean, and boolean array.

    Enum Members:
        INTEGER (str): Represents an integer variable.
        INTEGER_ARRAY (str): Represents an array of integer variables.
        FLOAT (str): Represents a floating-point variable.
        FLOAT_ARRAY (str): Represents an array of floating-point variables.
        BOOLEAN (str): Represents a boolean variable.
        BOOLEAN_ARRAY (str): Represents an array of boolean variables.

    Example:
        var_type = VariableType.FLOAT  # Represents a floating-point variable
    """

    INTEGER = "integer"
    INTEGER_ARRAY = "integer_array"
    FLOAT = "float"
    FLOAT_ARRAY = "float_array"
    BOOLEAN = "boolean"
    BOOLEAN_ARRAY = "boolean_array"


class Expression:  # pylint: disable=missing-class-docstring
    def __init__(self, expr):
        self.expr = expr

    def __add__(self, expr):
        return Expression(f"({self.expr} + {expr})")

    def __radd__(self, expr):
        return Expression(f"({expr} + {self.expr})")

    def __sub__(self, expr):
        return Expression(f"({self.expr} - {expr})")

    def __rsub__(self, expr):
        return Expression(f"({expr} - {self.expr})")

    def __mul__(self, expr):
        return Expression(f"{self.expr} * {expr}")

    def __rmul__(self, expr):
        return Expression(f"{expr} * {self.expr}")

    def __truediv__(self, expr):
        return Expression(f"(({self.expr}) / ({expr}))")

    def __rtruediv__(self, expr):
        return Expression(f"(({expr}) / ({self.expr}))")

    def __mod__(self, expr):
        return Expression(f"(({self.expr}) % ({expr}))")

    def __rmod__(self, expr):
        return Expression(f"(({expr}) % ({self.expr}))")

    def __or__(self, expr):
        return Expression(f"({self.expr} | {expr})")

    def __ror__(self, expr):
        return Expression(f"({expr} | {self.expr})")

    def __and__(self, expr):
        return Expression(f"{self.expr} & {expr}")

    def __rand__(self, expr):
        return Expression(f"{expr} & {self.expr}")

    def __eq__(self, expr):
        return Expression(f"(({self.expr}) == ({expr}))")

    def __ne__(self, expr):
        return Expression(f"(({self.expr}) != ({expr}))")

    def __xor__(self, expr):
        return Expression(f"(({self.expr}) ^ ({expr}))")

    def __neg__(self):
        return Expression(f"!({self.expr})")

    def __lt__(self, expr):
        return Expression(f"(({self.expr}) < ({expr}))")

    def __le__(self, expr):
        return Expression(f"(({self.expr}) <= ({expr}))")

    def __gt__(self, expr):
        return Expression(f"(({self.expr}) > ({expr}))")

    def __ge__(self, expr):
        return Expression(f"(({self.expr}) >= ({expr}))")

    def __str__(self):
        return str(self.expr)


class ExpressionArray:  # pylint: disable=missing-class-docstring
    """
    ExpressionArray class represents an array of expressions used for constructing expressions
    that involve arrays or table-like structures.

    Args:
        array_name (str): The name of the array.

    Methods:
        col(table_width: int, column: int) -> Expression:
            Creates an Expression for accessing a column in the array-like structure.

        row(table_width: int, row: int) -> Expression:
            Creates an Expression for accessing a row in the array-like structure.

        slice() -> Expression:
            Creates an Expression for accessing a slice in the array-like structure.

        __getitem__(pos: int) -> Expression:
            Overloaded method to create an Expression for accessing a specific
            position in the array.

    Example:
        col_expression =
            my_array.col(table_width=4, column=2)  # Creates an expression for column access.

    """

    def __init__(self, array_name: str) -> None:
        """
        Initialize an ExpressionArray instance.

        Args:
            array_name (str): The name of the array.

        Returns:
            None
        """
        self.array_name = array_name

    def col(self, table_width: int, table_height: int, column: int) -> Expression:
        """
        Create an Expression for accessing a column in the array-like structure.

        Args:
            table_width (int): The width of the table or array-like structure.
            table_height (int): The height of the table or array-like structure.
            column (int): The index of the column to access.

        Returns:
            Expression: An Expression representing the column access.
        """
        return Expression(
            f"{self.array_name}[{table_width}][{table_height}][c][{column}]"
        )

    def row(self, table_width: int, table_height: int, row: int) -> Expression:
        """
        Create an Expression for accessing a row in the array-like structure.

        Args:
            table_width (int): The width of the table or array-like structure.
            table_height (int): The height of the table or array-like structure.
            row (int): The index of the row to access.

        Returns:
            Expression: An Expression representing the row access.
        """
        return Expression(f"{self.array_name}[{table_width}][{table_height}][r][{row}]")

    def slice(
        self,
        table_width: int,
        table_height: int,
        offset_x_start: int,
        offset_x_end: int,
        offset_y_start: int,
        offset_y_end: int,
    ) -> Expression:
        """
        Create an Expression for accessing a slice in the array-like structure.

        This method generates an Expression that represents a slice operation on an array-like
        structure. The slice operation extracts a rectangular subregion from the given array-like
        structure, specified by the provided parameters.

        Args:
            table_width (int): The width of the array-like structure.
            table_height (int): The height of the array-like structure.
            offset_x_start (int): The starting index along the x-axis (horizontal) for the slice.
            offset_x_end (int): The ending index along the x-axis (horizontal) for the slice.
            offset_y_start (int): The starting index along the y-axis (vertical) for the slice.
            offset_y_end (int): The ending index along the y-axis (vertical) for the slice.

        Returns:
            Expression: An Expression object representing the slice access.
        """
        return Expression(
            f"{self.array_name}[{table_width}][{table_height}][s][{offset_x_start}][{offset_x_end}][{offset_y_start}][{offset_y_end}]"  # pylint: disable=line-too-long
        )

    def __getitem__(self, pos: int) -> Expression:
        """
        Create an Expression for accessing a specific position in the array.

        Args:
            pos (int): The position index to access.

        Returns:
            Expression: An Expression representing the position access.
        """
        return Expression(f"{self.array_name}[{pos}]")


class ArrayVariable(ExpressionArray):  # pylint: disable=too-many-instance-attributes
    """
    Represents an array-type variable.

    The ArrayVariable class defines a variable that represents an array of values used in
    constraint-based modeling and optimization.

    Args:
        var_name (str): The name of the array variable.
        length (int): The length of the array.
        var_type (VariableType, optional): The type of the array variable.
        domain_low (int, optional): The lower bound of the domain for array values.
        domain_high (int, optional): The upper bound of the domain for array values.
        specific_domain (list, optional): A list of specific values that the array variable.
        branch_var (BranchVar, optional): The brancher variable strategy.
        branch_val (BranchVal, optional): The brancher value strategy.

    Example:
        my_array =
            ArrayVariable("my_array", 10, var_type=VariableType.FLOAT_ARRAY,
                domain_low=0.0, domain_high=1.0)
    """

    def __init__(  # pylint: disable=too-many-arguments
        self,
        var_name: str,
        length: int,
        var_type: VariableType = VariableType.INTEGER_ARRAY,
        domain_low: Optional[int] = None,
        domain_high: Optional[int] = None,
        specific_domain: Optional[list] = None,
        branch_var: BranchVar = BranchIntegerVar.VAR_RND,
        branch_val: BranchVal = BranchIntegerVal.VAL_RND,
    ) -> None:
        super().__init__(var_name)
        self.var_name = var_name
        self.var_type = var_type
        self.length = length
        self.domain_low = domain_low
        self.domain_high = domain_high
        self.specific_domain = specific_domain
        self.branch_var = branch_var
        self.branch_val = branch_val
        self.branching_order = None

    def set_branching_order(self, branching_order: int):
        """
        Sets the branching order.

        Args:
            branching_order (int): The branching order value.

        Returns:
            None
        """

        self.branching_order = branching_order

    def __len__(self) -> int:
        return self.length

    def to_json(self):
        """
        Converts the array variable to a JSON representation.

        Returns:
            dict: A JSON representation of the array variable.
        """
        data_json = {
            "name": self.var_name,
            "type": self.var_type.value,
            "length": self.length,
            "brancher_variable": self.branch_var.value,
            "brancher_value": self.branch_val.value,
        }

        if self.domain_low is not None:
            data_json["domlow"] = self.domain_low

        if self.domain_high is not None:
            data_json["domup"] = self.domain_high

        if self.specific_domain is not None:
            data_json["specific_domain"] = self.specific_domain

        return data_json


class Variable(Expression):  # pylint: disable=too-few-public-methods
    """
    Represents a variable.

    The Variable class defines a variable used in constraint-based modeling and optimization.
    It inherits from the Expression class and provides methods to convert the variable to a JSON
    representation suitable for serialization.

    Args:
        var_name (str): The name of the variable.
        domain_low (int, optional): The lower bound of the domain for variable values.
        domain_high (int, optional): The upper bound of the domain for variable values.
        specific_domain (list, optional): A list of specific values that the variable can take.
        var_type (VariableType, optional): The type of the variable.
        branch_val (BranchVal, optional): The brancher value strategy.

    Example:
        my_variable = Variable("x", domain_low=0, domain_high=10,
                               specific_domain=[2, 4, 6, 8], var_type=VariableType.INTEGER,
                               branch_val=BranchIntegerVal.VAL_RND)
    """

    def __init__(  # pylint: disable=too-many-arguments
        self,
        var_name: str,
        domain_low: Optional[int] = None,
        domain_high: Optional[int] = None,
        specific_domain: Optional[list] = None,
        var_type: VariableType = VariableType.INTEGER,
        branch_val: BranchVal = BranchIntegerVal.VAL_RND,
    ) -> None:
        super().__init__(var_name)
        self.var_name = var_name
        self.var_type = var_type
        self.domain_low = domain_low
        self.domain_high = domain_high
        self.specific_domain = specific_domain
        self.branch_val = branch_val
        self.expression = None
        self.branching_order = None

    def set_branching_order(self, branching_order: int):
        """
        Sets the branching order.

        Args:
            branching_order (int): The branching order value.

        Returns:
            None
        """

        self.branching_order = branching_order

    def to_json(self):
        """
        Converts the variable to a JSON representation.

        Returns:
            dict: A JSON representation of the variable.
        """

        data_json = {
            "name": self.var_name,
            "type": self.var_type.value,
            "brancher_value": self.branch_val.value,
        }

        if self.expression is not None:
            data_json["expr"] = str(self.expression)

        else:
            if self.domain_low is not None:
                data_json["domlow"] = self.domain_low

            if self.domain_high is not None:
                data_json["domup"] = self.domain_high

            if self.specific_domain is not None:
                data_json["specific_domain"] = self.specific_domain

        return data_json


class ExpressionVariable(Variable):  # pylint: disable=too-few-public-methods
    """
    Represents a variable defined by an expression.

    The ExpressionVariable class extends the functionality of the Variable class
    to represent variables that are defined by an expression. It inherits from
    the Variable class.

    Args:
        var_name (str): The name of the variable.
        expression: The expression defining the variable.
        var_type (VariableType, optional): The type of the variable.
        branch_val (BranchVal, optional): The brancher value strategy.

    Example:
        expr = Expression(3 * x + 2)
        my_expr_variable = ExpressionVariable("y", expression=expr,
                                              var_type=VariableType.FLOAT,
                                              branch_val=BranchIntegerVal.VAL_RND)
    """

    def __init__(
        self,
        var_name: str,
        expression,
        var_type: VariableType = VariableType.INTEGER,
        branch_val: BranchVal = BranchIntegerVal.VAL_RND,
    ) -> None:
        super().__init__(var_name, None, None, None, var_type, branch_val)
        self.expression = expression
