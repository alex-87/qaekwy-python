"""Variable Module

This module defines variable bases.

Enums:
    VariableType: Represents different types of variables.

Classes:

    ArrayVariable: Represents an array-type variable.
    Variable: Represents a variable.
    ExpressionVariable: Represents a variable defined by an expression.
    MatrixVariable: Represents a matrix-type variable.
    VectorExpression: Represents a vector expression for matrix row/col/slice access.
    Expression: Represents a symbolic expression involving variables.
    ExpressionArray: Represents an array of expressions.
"""

from enum import Enum
from typing import Optional, Union

from .branch import (
    BranchBooleanVal,
    BranchBooleanVar,
    BranchFloatVal,
    BranchFloatVar,
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

    @staticmethod
    def from_json(json_data: str) -> "VariableType":
        """
        Creates a VariableType instance from a JSON string.
        """
        return VariableType(json_data)


class Expression:
    """
    Expression class represents an expression used for constructing expressions
    that involve variables, arithmetic operations, and logical operations.
    """

    def __init__(self, expr):
        self.expr = expr

    def __abs__(self):
        return Expression(f"abs({self.expr})")

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

    def __rxor__(self, expr):
        return Expression(f"(({expr}) ^ ({self.expr}))")

    def __invert__(self):
        return Expression(f"!({self.expr})")

    def __neg__(self):
        return Expression(f"(-1) * ({self.expr})")

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


class ExpressionArray:
    """
    ExpressionArray class represents an array of expressions used for constructing expressions
    that involve arrays or table-like structures.

    Args:
        array_name (str): The name of the array.

    Methods:

        __getitem__(pos: int) -> Expression:
            Overloaded method to create an Expression for accessing a specific
            position in the array.
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

    def __getitem__(self, pos: int) -> Expression:
        """
        Create an Expression for accessing a specific position in the array.

        Args:
            pos (int): The position index to access.

        Returns:
            Expression: An Expression representing the position access.
        """
        return Expression(f"{self.array_name}[{pos}]")


class ArrayVariable(ExpressionArray):
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
        branch_order (int, optional): The branching order.

    Example:
        my_array =
            ArrayVariable("my_array", 10, var_type=VariableType.FLOAT_ARRAY,
                domain_low=0.0, domain_high=1.0)
    """

    def __init__(
        self,
        var_name: str,
        length: int,
        var_type: VariableType = VariableType.INTEGER_ARRAY,
        domain_low: Optional[Union[int, float]] = None,
        domain_high: Optional[Union[int, float]] = None,
        specific_domain: Optional[list] = None,
        branch_var: BranchVar = BranchIntegerVar.VAR_RND,
        branch_val: BranchVal = BranchIntegerVal.VAL_RND,
        branch_order: Optional[int] = -1,
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
        self.branching_order = branch_order

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
            "branching_order": self.branching_order,
        }

        if self.domain_low is not None:
            data_json["domlow"] = self.domain_low

        if self.domain_high is not None:
            data_json["domup"] = self.domain_high

        if self.specific_domain is not None:
            data_json["specific_domain"] = self.specific_domain

        return data_json

    @staticmethod
    def from_json(json_data: dict) -> "ArrayVariable":
        """
        Creates an ArrayVariable instance from a JSON object.

        Args:
            json_data (dict): A dictionary representing the array variable.

        Returns:
            ArrayVariable: An instance of the ArrayVariable class.
        """
        var_type = VariableType.from_json(json_data["type"])

        branch_var_enum: Union[
            type[BranchIntegerVar], type[BranchFloatVar], type[BranchBooleanVar]
        ] = BranchIntegerVar
        branch_val_enum: Union[
            type[BranchIntegerVal], type[BranchFloatVal], type[BranchBooleanVal]
        ] = BranchIntegerVal

        if var_type == VariableType.INTEGER_ARRAY:
            branch_var_enum = BranchIntegerVar
            branch_val_enum = BranchIntegerVal
        elif var_type == VariableType.FLOAT_ARRAY:
            branch_var_enum = BranchFloatVar
            branch_val_enum = BranchFloatVal
        elif var_type == VariableType.BOOLEAN_ARRAY:
            branch_var_enum = BranchBooleanVar
            branch_val_enum = BranchBooleanVal
        else:
            raise ValueError(f"Unsupported variable type for ArrayVariable: {var_type}")

        branch_var: BranchVar = branch_var_enum.from_json(
            json_data["brancher_variable"]
        )
        branch_val: BranchVal = branch_val_enum.from_json(json_data["brancher_value"])

        return ArrayVariable(
            var_name=json_data["name"],
            length=json_data["length"],
            var_type=var_type,
            domain_low=json_data.get("domlow"),
            domain_high=json_data.get("domup"),
            specific_domain=json_data.get("specific_domain"),
            branch_var=branch_var,
            branch_val=branch_val,
            branch_order=json_data.get("branching_order", -1),
        )


class VectorExpression(ExpressionArray):
    """
    Represents a vector expression for accessing rows, columns, or slices
    of a matrix variable.
    """

    def __init__(self, kind: str, matrix: "MatrixVariable", **kwargs):
        super().__init__(matrix.var_name)
        self.kind = kind
        self.matrix = matrix
        self.params = kwargs

    def __iter__(self):
        if self.kind == "row":
            r = self.params["row"]
            for c in range(self.matrix.cols):
                yield self.matrix[r][c]

        elif self.kind == "col":
            c = self.params["col"]
            for r in range(self.matrix.rows):
                yield self.matrix[r][c]

        elif self.kind == "slice":
            rs, cs, re, ce = (
                self.params["row_start"],
                self.params["col_start"],
                self.params["row_end"],
                self.params["col_end"],
            )
            for r in range(rs, re):
                for c in range(cs, ce):
                    yield self.matrix[r][c]

    def __radd__(self, other):
        if other == 0:
            return Expression(f"sum({self})")
        raise TypeError("Unsupported addition with VectorExpression")

    def sum(self) -> Expression:
        """
        Returns an expression representing the sum of the vector expression.
        """
        return Expression(f"sum({self})")

    def __str__(self):
        if self.kind == "row":
            return f"{self.matrix.var_name}[{self.matrix.rows}][{self.matrix.cols}][r][{self.params['row']}]"
        if self.kind == "col":
            return f"{self.matrix.var_name}[{self.matrix.rows}][{self.matrix.cols}][c][{self.params['col']}]"
        if self.kind == "slice":
            return f"{self.matrix.var_name}[{self.matrix.rows}][{self.matrix.cols}][s][{self.params['row_start']}][{self.params['col_start']}][{self.params['row_end']}][{self.params['col_end']}]"

        return "VectorExpression()"


class MatrixVariable:
    """
    Represents a matrix-type variable.

    The MatrixVariable class defines a variable that represents a matrix of values used in
    constraint-based modeling and optimization.

    Args:
        var_name (str): The name of the matrix variable.
        rows (int): The number of rows in the matrix.
        cols (int): The number of columns in the matrix.
        var_type (VariableType, optional): The type of the matrix variable.
        domain_low (int, optional): The lower bound of the domain for matrix values.
        domain_high (int, optional): The upper bound of the domain for matrix values.
        specific_domain (list, optional): A list of specific values that the matrix variable.
        branch_var (BranchVar, optional): The brancher variable strategy.
        branch_val (BranchVal, optional): The brancher value strategy.
        branch_order (int, optional): The branching order.

    Example:
        my_matrix =
            MatrixVariable("my_matrix", 3, 4, var_type=VariableType.FLOAT_ARRAY,
                domain_low=0.0, domain_high=1.0)
    """

    def __init__(
        self,
        var_name: str,
        rows: int,
        cols: int,
        var_type: VariableType = VariableType.INTEGER_ARRAY,
        domain_low: Optional[Union[int, float]] = None,
        domain_high: Optional[Union[int, float]] = None,
        specific_domain: Optional[list] = None,
        branch_var: BranchVar = BranchIntegerVar.VAR_RND,
        branch_val: BranchVal = BranchIntegerVal.VAL_RND,
        branch_order: Optional[int] = -1,
    ) -> None:

        typed_var_name: str = var_name
        if not var_name.startswith(f"MATRIX${rows}${cols}$"):
            if var_name.startswith("MATRIX$"):
                parts = var_name.split("$", 3)
                part_col, part_row = int(parts[1]), int(parts[2])
                if rows != part_row or cols != part_col:
                    raise ValueError(
                        f"var_name '{var_name}' should not start with 'MATRIX$'. Please provide a base variable name."
                    )
            else:
                typed_var_name = f"MATRIX${rows}${cols}${var_name}"

        self.var_name = typed_var_name
        self.var_type = var_type
        self.length = rows * cols
        self.domain_low = domain_low
        self.domain_high = domain_high
        self.specific_domain = specific_domain
        self.branch_var = branch_var
        self.branch_val = branch_val
        self.branching_order = branch_order
        self.rows = rows
        self.cols = cols

    class _MatrixRow:
        def __init__(self, matrix_var: "MatrixVariable", row: int):
            self.matrix_var = matrix_var
            self.row = row

        def __getitem__(self, col: int) -> Expression:
            return Expression(
                f"{self.matrix_var.var_name}[{self.row * (self.matrix_var.cols) + col}]"
            )

    def __getitem__(self, row: int) -> "_MatrixRow":
        return MatrixVariable._MatrixRow(self, row)

    def row(self, row: int) -> VectorExpression:
        """
        Returns a VectorExpression representing a specific row of the matrix.
        """
        return VectorExpression("row", self, row=row)

    def col(self, col: int) -> VectorExpression:
        """
        Returns a VectorExpression representing a specific column of the matrix.
        """
        return VectorExpression("col", self, col=col)

    def slice(
        self,
        row_start: int,
        col_start: int,
        row_end: int,
        col_end: int,
    ) -> VectorExpression:
        """
        Returns a VectorExpression representing a slice of the matrix.
        """
        return VectorExpression(
            "slice",
            self,
            row_start=row_start,
            col_start=col_start,
            row_end=row_end + 1,
            col_end=col_end + 1,
        )

    def to_json(self):
        """
        Converts the matrix variable to a JSON representation.

        Returns:
            dict: A JSON representation of the matrix variable.
        """
        data_json = {
            "name": self.var_name,
            "type": self.var_type.value,
            "length": self.length,
            "brancher_variable": self.branch_var.value,
            "brancher_value": self.branch_val.value,
            "branching_order": self.branching_order,
        }

        if self.domain_low is not None:
            data_json["domlow"] = self.domain_low

        if self.domain_high is not None:
            data_json["domup"] = self.domain_high

        if self.specific_domain is not None:
            data_json["specific_domain"] = self.specific_domain

        data_json["rows"] = self.rows
        data_json["cols"] = self.cols
        data_json["subtype"] = "matrix"
        return data_json

    @staticmethod
    def from_json(json_data) -> "MatrixVariable":
        """
        Creates a MatrixVariable instance from a JSON object.

        Args:
            json_data (dict): A dictionary representing the matrix variable.

        Returns:
            MatrixVariable: An instance of the MatrixVariable class.
        """
        var_type = VariableType.from_json(json_data["type"])

        branch_var_enum: Union[
            type[BranchIntegerVar], type[BranchFloatVar], type[BranchBooleanVar]
        ] = BranchIntegerVar
        branch_val_enum: Union[
            type[BranchIntegerVal], type[BranchFloatVal], type[BranchBooleanVal]
        ] = BranchIntegerVal

        if var_type == VariableType.INTEGER_ARRAY:
            branch_var_enum = BranchIntegerVar
            branch_val_enum = BranchIntegerVal
        elif var_type == VariableType.FLOAT_ARRAY:
            branch_var_enum = BranchFloatVar
            branch_val_enum = BranchFloatVal
        elif var_type == VariableType.BOOLEAN_ARRAY:
            branch_var_enum = BranchBooleanVar
            branch_val_enum = BranchBooleanVal
        else:
            raise ValueError(
                f"Unsupported variable type for MatrixVariable: {var_type}"
            )

        branch_var: BranchVar = branch_var_enum.from_json(
            json_data["brancher_variable"]
        )
        branch_val: BranchVal = branch_val_enum.from_json(json_data["brancher_value"])

        return MatrixVariable(
            var_name=json_data["name"],
            var_type=var_type,
            rows=json_data["rows"],
            cols=json_data["cols"],
            domain_low=json_data.get("domlow"),
            domain_high=json_data.get("domup"),
            specific_domain=json_data.get("specific_domain"),
            branch_var=branch_var,
            branch_val=branch_val,
            branch_order=json_data.get("branching_order", -1),
        )


class Variable(Expression):
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
        branch_order (int, optional): The branching order.

    Example:
        my_variable = Variable("x", domain_low=0, domain_high=10,
                               specific_domain=[2, 4, 6, 8], var_type=VariableType.INTEGER,
                               branch_val=BranchIntegerVal.VAL_RND)
    """

    def __init__(
        self,
        var_name: str,
        domain_low: Optional[Union[int, float]] = None,
        domain_high: Optional[Union[int, float]] = None,
        specific_domain: Optional[list] = None,
        var_type: VariableType = VariableType.INTEGER,
        branch_val: BranchVal = BranchIntegerVal.VAL_RND,
        branch_order: Optional[int] = -1,
    ) -> None:
        super().__init__(var_name)
        self.var_name = var_name
        self.var_type = var_type
        self.domain_low = domain_low
        self.domain_high = domain_high
        self.specific_domain = specific_domain
        self.branch_val = branch_val
        self.expression = None
        self.branching_order = branch_order

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
            "branching_order": self.branching_order,
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

    @staticmethod
    def from_json(json_data: dict) -> "Variable":
        """
        Creates a Variable instance from a JSON representation.
        """
        if "expr" in json_data:
            return ExpressionVariable.from_json(json_data)

        var_type = VariableType.from_json(json_data["type"])

        branch_val_enum: Union[
            type[BranchIntegerVal], type[BranchFloatVal], type[BranchBooleanVal]
        ] = BranchIntegerVal

        if var_type == VariableType.INTEGER:
            branch_val_enum = BranchIntegerVal
        elif var_type == VariableType.FLOAT:
            branch_val_enum = BranchFloatVal
        elif var_type == VariableType.BOOLEAN:
            branch_val_enum = BranchBooleanVal
        else:
            raise ValueError(f"Unsupported variable type for Variable: {var_type}")

        branch_val = branch_val_enum.from_json(json_data["brancher_value"])

        return Variable(
            var_name=json_data["name"],
            var_type=var_type,
            domain_low=json_data.get("domlow"),
            domain_high=json_data.get("domup"),
            specific_domain=json_data.get("specific_domain"),
            branch_val=branch_val,
            branch_order=json_data.get("branching_order", -1),
        )


class ExpressionVariable(Variable):
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
        branch_order (int, optional): The branching order.

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
        branch_order: Optional[int] = -1,
    ) -> None:
        super().__init__(var_name, None, None, None, var_type, branch_val, branch_order)
        self.expression = expression

    @staticmethod
    def from_json(json_data: dict) -> "ExpressionVariable":
        """
        Creates an ExpressionVariable instance from a JSON representation.
        """
        var_type = VariableType.from_json(json_data["type"])

        branch_val_enum: Union[
            type[BranchIntegerVal], type[BranchFloatVal], type[BranchBooleanVal]
        ] = BranchIntegerVal

        if var_type == VariableType.INTEGER:
            branch_val_enum = BranchIntegerVal
        elif var_type == VariableType.FLOAT:
            branch_val_enum = BranchFloatVal
        elif var_type == VariableType.BOOLEAN:
            branch_val_enum = BranchBooleanVal
        else:
            raise ValueError(
                f"Unsupported variable type for ExpressionVariable: {var_type}"
            )

        branch_val = branch_val_enum.from_json(json_data["brancher_value"])

        expression = Expression(json_data["expr"])

        return ExpressionVariable(
            var_name=json_data["name"],
            expression=expression,
            var_type=var_type,
            branch_val=branch_val,
            branch_order=json_data.get("branching_order", -1),
        )
