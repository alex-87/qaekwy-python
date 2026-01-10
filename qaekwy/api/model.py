"""API Model Module

This module provides the `Model` class, which serves as a high-level API for constructing, managing,
and solving constraint programming models. It offers convenient methods for creating variables (integer,
float, boolean, arrays, and matrices), adding a wide range of constraints, and defining optimization
objectives. The `Model` class interfaces with a solver engine to find solutions according to the specified
search strategies and cutoffs.

Classes:
    Model:
        The main API class for building and interacting with constraint programming models.
        It encapsulates variable and constraint creation, objective specification, and communication with
        the underlying solver engine. The class provides methods for model serialization and deserialization,
        as well as for solving the model and retrieving solutions.
"""

from typing import Optional, Union

from ..core.engine import DirectEngine
from ..core.model import DIRECTENGINE_API_ENDPOINT
from ..core.model.constraint.abs import ConstraintAbs
from ..core.model.constraint.abstract_constraint import AbstractConstraint
from ..core.model.constraint.acos import ConstraintACos
from ..core.model.constraint.asin import ConstraintASin
from ..core.model.constraint.atan import ConstraintATan
from ..core.model.constraint.cos import ConstraintCos
from ..core.model.constraint.distinct import (
    ConstraintDistinctArray,
    ConstraintDistinctCol,
    ConstraintDistinctRow,
    ConstraintDistinctSlice,
)
from ..core.model.constraint.divide import ConstraintDivide
from ..core.model.constraint.element import ConstraintElement
from ..core.model.constraint.exponential import ConstraintExponential
from ..core.model.constraint.if_then_else import ConstraintIfThenElse
from ..core.model.constraint.logarithm import ConstraintLogarithm
from ..core.model.constraint.maximum import ConstraintMaximum
from ..core.model.constraint.member import ConstraintMember
from ..core.model.constraint.minimum import ConstraintMinimum
from ..core.model.constraint.modulo import ConstraintModulo
from ..core.model.constraint.multiply import ConstraintMultiply
from ..core.model.constraint.nroot import ConstraintNRoot
from ..core.model.constraint.power import ConstraintPower
from ..core.model.constraint.sin import ConstraintSin
from ..core.model.constraint.sort import ConstraintReverseSorted, ConstraintSorted
from ..core.model.constraint.tan import ConstraintTan
from ..core.model.cutoff import Cutoff
from ..core.model.modeller import Modeller
from ..core.model.searcher import SearcherType
from ..core.model.specific import SpecificMaximum, SpecificMinimum
from ..core.model.variable.boolean import (
    BooleanVariable,
    BooleanVariableArray,
    BooleanVariableMatrix,
)
from ..core.model.variable.branch import (
    BranchBooleanVal,
    BranchBooleanVar,
    BranchFloatVal,
    BranchFloatVar,
    BranchIntegerVal,
    BranchIntegerVar,
)
from ..core.model.variable.float import (
    FloatExpressionVariable,
    FloatVariable,
    FloatVariableArray,
    FloatVariableMatrix,
)
from ..core.model.variable.integer import (
    IntegerExpressionVariable,
    IntegerVariable,
    IntegerVariableArray,
    IntegerVariableMatrix,
)
from ..core.model.variable.variable import (
    ArrayVariable,
    Expression,
    Variable,
    VariableType,
    VectorExpression,
)
from ..core.response import SolutionResponse
from ..core.solution import Solution
from .exceptions import SolverError


class Model:  # pylint: disable=too-many-public-methods
    """
    Model class for modelling and interacting with the solver engine.

    Args:
        endpoint (str): The API endpoint for the DirectEngine.
        timeout (int): The timeout for API requests.
        ssl_verify (bool): Whether to verify SSL certificates.
    """

    def __init__(
        self,
        endpoint: str = DIRECTENGINE_API_ENDPOINT,
        timeout: int = 30,
        ssl_verify: bool = True,
    ):
        self._modeller = Modeller()
        self._engine = DirectEngine(
            endpoint=endpoint, timeout=timeout, ssl_verify=ssl_verify
        )

    def integer_variable(
        self,
        name: str,
        domain: Optional[tuple[int, int]] = None,
        specific_domain: Optional[list[int]] = None,
        expression: Optional[str] = None,
        branch_val: BranchIntegerVal = BranchIntegerVal.VAL_RND,
        branch_order: Optional[int] = -1,
    ) -> Union[IntegerVariable, IntegerExpressionVariable]:
        """
        Creates an integer variable or an integer expression variable.

        Args:
            name (str): The name of the variable.
            domain (tuple[int, int]): A tuple representing the (low, high) domain of the variable.
            expression (str, optional): An expression defining the variable. If provided, an IntegerExpressionVariable is created.
            specific_domain (list[int], optional): A specific domain for the variable.
            branch_val (BranchIntegerVal, optional): The brancher value strategy.
            branch_order (int, optional): The branching order.

        Returns:
                IntegerVariable or IntegerExpressionVariable: The created variable.
        """
        if expression is not None:
            v: IntegerExpressionVariable = IntegerExpressionVariable(
                var_name=name,
                expression=expression,
                branch_val=branch_val,
                branch_order=branch_order,
            )

            self._modeller.add_variable(v)
            return v

        l, h = domain if domain is not None else (0, 0)
        w: IntegerVariable = IntegerVariable(
            var_name=name,
            domain_low=l,
            domain_high=h,
            specific_domain=specific_domain,
            branch_val=branch_val,
            branch_order=branch_order,
        )
        self._modeller.add_variable(w)
        return w

    def integer_array(
        self,
        name: str,
        length: int,
        domain: tuple[int, int],
        specific_domain: Optional[list[int]] = None,
        branch_var: BranchIntegerVar = BranchIntegerVar.VAR_RND,
        branch_val: BranchIntegerVal = BranchIntegerVal.VAL_RND,
        branch_order: Optional[int] = -1,
    ) -> IntegerVariableArray:
        """
        Creates an array of integer variables.

        Args:
            name (str): The name of the variable array.
            length (int): The length of the variable array.
            domain (tuple[int, int]): A tuple representing the (low, high) domain of the variables.
            specific_domain (list[int], optional): A specific domain for the variables.
            branch_var (BranchIntegerVar, optional): The brancher variable strategy.
            branch_val (BranchIntegerVal, optional): The brancher value strategy.
            branch_order (int, optional): The branching order.

        Returns:
                IntegerVariableArray: The created variable array.
        """
        v: IntegerVariableArray = IntegerVariableArray(
            var_name=name,
            length=length,
            domain_low=domain[0],
            domain_high=domain[1],
            specific_domain=specific_domain,
            branch_var=branch_var,
            branch_val=branch_val,
            branch_order=branch_order,
        )
        self._modeller.add_variable(v)
        return v

    def integer_matrix(
        self,
        name: str,
        rows: int,
        cols: int,
        domain: tuple[int, int],
        specific_domain: Optional[list[int]] = None,
        branch_var: BranchIntegerVar = BranchIntegerVar.VAR_RND,
        branch_val: BranchIntegerVal = BranchIntegerVal.VAL_RND,
        branch_order: Optional[int] = -1,
    ) -> IntegerVariableMatrix:
        """
        Creates a matrix of integer variables.

        Args:
            name (str): The name of the variable matrix.
            rows (int): The number of rows in the matrix.
            cols (int): The number of columns in the matrix.
            domain (tuple[int, int]): A tuple representing the (low, high) domain of the variables.
            specific_domain (list[int], optional): A specific domain for the variables.
            branch_var (BranchIntegerVar, optional): The brancher variable strategy.
            branch_val (BranchIntegerVal, optional): The brancher value strategy.
            branch_order (int, optional): The branching order.

        Returns:
                IntegerVariableMatrix: The created variable matrix.
        """
        l, h = domain
        v: IntegerVariableMatrix = IntegerVariableMatrix(
            var_name=name,
            rows=rows,
            cols=cols,
            domain_low=l,
            domain_high=h,
            specific_domain=specific_domain,
            branch_var=branch_var,
            branch_val=branch_val,
            branch_order=branch_order,
        )
        self._modeller.add_variable(v)
        return v

    def float_variable(
        self,
        name: str,
        domain: Optional[tuple[float, float]],
        expression: Optional[str] = None,
        branch_val: BranchFloatVal = BranchFloatVal.VAL_RND,
        branch_order: int = -1,
    ) -> Union[FloatVariable, FloatExpressionVariable]:
        """
        Creates a float variable or a float expression variable.

        Args:
            name (str): The name of the variable.
            domain (tuple[float, float], optional): A tuple representing the (low, high) domain of the variable.
            expression (str, optional): An expression defining the variable. If provided, a FloatExpressionVariable is created.
            branch_val (BranchFloatVal): The brancher value strategy.
            branch_order (int): The branching order.

        Returns:
            FloatVariable or FloatExpressionVariable: The created variable.
        """
        if expression is not None:
            v: FloatExpressionVariable = FloatExpressionVariable(
                var_name=name,
                expression=expression,
                branch_val=branch_val,
                branch_order=branch_order,
            )
            self._modeller.add_variable(v)
            return v

        l, h = domain if domain is not None else (0.0, 0.0)
        w: FloatVariable = FloatVariable(
            var_name=name,
            domain_low=l,
            domain_high=h,
            branch_val=branch_val,
            branch_order=branch_order,
        )
        self._modeller.add_variable(w)
        return w

    def float_array(
        self,
        name: str,
        length: int,
        domain: tuple[float, float],
        branch_var: BranchFloatVar = BranchFloatVar.VAR_RND,
        branch_val: BranchFloatVal = BranchFloatVal.VAL_RND,
        branch_order: int = -1,
    ) -> FloatVariableArray:
        """
        Creates an array of float variables.

        Args:
            name (str): The name of the variable array.
            length (int): The length of the variable array.
            domain (tuple[float, float]): A tuple representing the (low, high) domain of the variables.
            branch_var (BranchFloatVar, optional): The brancher variable strategy.
            branch_val (BranchFloatVal, optional): The brancher value strategy.
            branch_order (int, optional): The branching order.

        Returns:
            FloatVariableArray: The created variable array.
        """
        v: FloatVariableArray = FloatVariableArray(
            var_name=name,
            length=length,
            domain_low=domain[0],
            domain_high=domain[1],
            branch_var=branch_var,
            branch_val=branch_val,
            branch_order=branch_order,
        )
        self._modeller.add_variable(v)
        return v

    def float_matrix(
        self,
        name: str,
        rows: int,
        cols: int,
        domain: tuple[float, float],
        branch_var: BranchFloatVar = BranchFloatVar.VAR_RND,
        branch_val: BranchFloatVal = BranchFloatVal.VAL_RND,
        branch_order: Optional[int] = -1,
    ) -> FloatVariableMatrix:
        """
        Creates a matrix of float variables.

        Args:
            name (str): The name of the variable matrix.
            rows (int): The number of rows in the matrix.
            cols (int): The number of columns in the matrix.
            domain (tuple[float, float]): A tuple representing the (low, high) domain of the variables.
            branch_var (BranchFloatVar, optional): The brancher variable strategy.
            branch_val (BranchFloatVal, optional): The brancher value strategy.
            branch_order (int, optional): The branching order.

        Returns:
                FloatVariableMatrix: The created variable matrix.
        """
        l, h = domain
        v: FloatVariableMatrix = FloatVariableMatrix(
            var_name=name,
            rows=rows,
            cols=cols,
            domain_low=l,
            domain_high=h,
            branch_var=branch_var,
            branch_val=branch_val,
            branch_order=branch_order,
        )
        self._modeller.add_variable(v)
        return v

    def boolean_variable(
        self,
        name: str,
        branch_val: BranchBooleanVal = BranchBooleanVal.VAL_RND,
        branch_order: int = -1,
    ) -> BooleanVariable:
        """
        Creates a boolean variable.

        Args:
            name (str): The name of the variable.
            branch_val (BranchBooleanVal, optional): The brancher value strategy.
            branch_order (int, optional): The branching order.

        Returns:
            BooleanVariable: The created variable.
        """
        v: BooleanVariable = BooleanVariable(
            var_name=name, branch_val=branch_val, branch_order=branch_order
        )
        self._modeller.add_variable(v)
        return v

    def boolean_array(
        self,
        name: str,
        length: int,
        branch_var: BranchBooleanVar = BranchBooleanVar.VAR_RND,
        branch_val: BranchBooleanVal = BranchBooleanVal.VAL_RND,
        branch_order: int = -1,
    ) -> BooleanVariableArray:
        """
        Creates an array of boolean variables.

        Args:
            name (str): The name of the variable array.
            length (int): The length of the variable array.
            branch_var (BranchBooleanVar, optional): The brancher variable strategy.
            branch_val (BranchBooleanVal, optional): The brancher value strategy.
            branch_order (int, optional): The branching order.

        Returns:
            BooleanVariableArray: The created variable array.
        """
        v: BooleanVariableArray = BooleanVariableArray(
            var_name=name,
            length=length,
            branch_var=branch_var,
            branch_val=branch_val,
            branch_order=branch_order,
        )
        self._modeller.add_variable(v)
        return v

    def boolean_matrix(
        self,
        name: str,
        rows: int,
        cols: int,
        branch_var: BranchBooleanVar = BranchBooleanVar.VAR_RND,
        branch_val: BranchBooleanVal = BranchBooleanVal.VAL_RND,
        branch_order: Optional[int] = -1,
    ) -> BooleanVariableMatrix:
        """
        Creates a matrix of boolean variables.

        Args:
            name (str): The name of the variable matrix.
            rows (int): The number of rows in the matrix.
            cols (int): The number of columns in the matrix.
            branch_var (BranchBooleanVar, optional): The brancher variable strategy.
            branch_val (BranchBooleanVal, optional): The brancher value strategy.
            branch_order (int, optional): The branching order.

        Returns:
                BooleanVariableMatrix: The created variable matrix.
        """
        v: BooleanVariableMatrix = BooleanVariableMatrix(
            var_name=name,
            rows=rows,
            cols=cols,
            branch_var=branch_var,
            branch_val=branch_val,
            branch_order=branch_order,
        )
        self._modeller.add_variable(v)
        return v

    def constraint(self, constraint: Expression) -> None:
        """
        Add a custom constraint to the model.

        Args:
            constraint (Expression): The constraint expression to add.
        """
        self._modeller.add_constraint(constraint)

    def constraint_abs(self, var_1: Variable, var_2: Variable) -> None:
        """
        Add an absolute value constraint between two variables.

        Args:
            var_1 (Variable): The first variable.
            var_2 (Variable): The second variable.
        """

        constraint = ConstraintAbs(var_1, var_2)
        self._modeller.add_constraint(constraint)

    def constraint_acos(self, var_1: Variable, var_2: Variable) -> None:
        """
        Add an arc cosine constraint between two float variables.

        Args:
            var_1 (Variable): The first float variable.
            var_2 (Variable): The second float variable.
        """
        constraint = ConstraintACos(var_1, var_2)
        self._modeller.add_constraint(constraint)

    def constraint_asin(self, var_1: Variable, var_2: Variable) -> None:
        """
        Add an arc sine constraint between two float variables.

        Args:
            var_1 (Variable): The first float variable.
            var_2 (Variable): The second float variable.
        """
        constraint = ConstraintASin(var_1, var_2)
        self._modeller.add_constraint(constraint)

    def constraint_atan(self, var_1: Variable, var_2: Variable) -> None:
        """
        Add an arc tangent constraint between two float variables.

        Args:
            var_1 (Variable): The first float variable.
            var_2 (Variable): The second float variable.
        """
        constraint = ConstraintATan(var_1, var_2)
        self._modeller.add_constraint(constraint)

    def constraint_cos(self, var_1: Variable, var_2: Variable) -> None:
        """
        Add a cosine constraint between two float variables.

        Args:
            var_1 (Variable): The first float variable.
            var_2 (Variable): The second float variable.
        """
        constraint = ConstraintCos(var_1, var_2)
        self._modeller.add_constraint(constraint)

    def constraint_distinct(self, var: Union[ArrayVariable, VectorExpression]) -> None:
        """
        Add a distinct constraint.

        Supports:
        - ArrayVariable              → distinct on full array
        - VectorExpression (row)     → distinct on matrix row
        - VectorExpression (col)     → distinct on matrix column
        - VectorExpression (slice)   → distinct on matrix slice
        """

        constraint: AbstractConstraint

        if isinstance(var, ArrayVariable):
            constraint = ConstraintDistinctArray(var)
            self._modeller.add_constraint(constraint)
            return

        if isinstance(var, VectorExpression):
            matrix = var.matrix

            if var.kind == "row":
                idx = var.params["row"]
                size = matrix.cols

                constraint = ConstraintDistinctRow(
                    matrix,
                    size=size,
                    idx=idx,
                )

            elif var.kind == "col":
                idx = var.params["col"]
                size = matrix.rows

                constraint = ConstraintDistinctCol(
                    matrix,
                    size=size,
                    idx=idx,
                )

            elif var.kind == "slice":
                rs = var.params["col_start"]
                cs = var.params["row_start"]
                re = var.params["col_end"]
                ce = var.params["row_end"]
                size = matrix.cols

                constraint = ConstraintDistinctSlice(
                    matrix,
                    size=size,
                    offset_start_x=rs,
                    offset_start_y=cs,
                    offset_end_x=re - 1,
                    offset_end_y=ce - 1,
                )

            else:
                raise ValueError(f"Unknown VectorExpression kind: {var.kind}")

            self._modeller.add_constraint(constraint)
            return

        raise TypeError(
            "constraint_distinct expects an ArrayVariable or a Matrix vector "
            "(row / col / slice)"
        )

    def constraint_divide(
        self, var_1: Variable, var_2: Variable, var_3: Variable
    ) -> None:
        """
        Add a division constraint between three integer variables, such that var_3 = var_1 / var_2.

        Args:
            var_1 (Variable): The first integer variable.
            var_2 (Variable): The second integer variable.
            var_3 (Variable): The third integer variable.
        """
        constraint = ConstraintDivide(var_1, var_2, var_3)
        self._modeller.add_constraint(constraint)

    def constraint_element(
        self,
        mapping_table: ArrayVariable,
        var_1: Variable,
        var_2: Variable,
    ) -> None:
        """
        Add an element constraint between three integer variable arrays such that `mapping_table[var_1] = var_2`.

        Args:
            mapping_table (ArrayVariable): The mapping table.
            var_1 (Variable): The first variable.
            var_2 (Variable): The second variable.
        """
        constraint = ConstraintElement(mapping_table, var_1, var_2)
        self._modeller.add_constraint(constraint)

    def constraint_exponential(self, var_1: Variable, var_2: Variable) -> None:
        """
        Add an exponential constraint between two integer variables such that var_2 = e^(var_1).

        Args:
            var_1 (Variable): The first variable.
            var_2 (Variable): The second variable.
        """
        constraint = ConstraintExponential(var_1, var_2)
        self._modeller.add_constraint(constraint)

    def constraint_if_then_else(
        self,
        condition: Expression,
        then_constraint: Expression,
        else_constraint: Optional[Expression] = None,
        domain: str = "integer",
    ) -> None:
        """
        Add an if-then-else constraint.

        Args:
            condition (Expression): The condition expression.
            then_constraint (Expression): The constraint to apply if the condition is true.
            else_constraint (Optional[Expression]): The constraint to apply if the condition is false.
            domain (str): The domain of the constraint ("integer", "float" or "boolean").
        """
        constraint = ConstraintIfThenElse(
            condition=condition,
            then_constraint=then_constraint,
            else_constraint=else_constraint,
            domain=VariableType(domain.lower()),
        )
        self._modeller.add_constraint(constraint)

    def constraint_logarithm(self, var_1: Variable, var_2: Variable) -> None:
        """
        Add a logarithm constraint between two float variables such that var_2 = log(var_1).

        Args:
            var_1 (Variable): The first variable.
            var_2 (Variable): The second variable.
        """
        constraint = ConstraintLogarithm(var_1, var_2)
        self._modeller.add_constraint(constraint)

    def constraint_maximum(
        self, var_1: Variable, var_2: Variable, var_3: Variable
    ) -> None:
        """
        Add a maximum constraint between two variables such that var_3 = max(var_1, var_2).

        Args:
            var_1 (Variable): The first variable.
            var_2 (Variable): The second variable.
            var_3 (Variable): The variable to store the maximum.
        """
        constraint = ConstraintMaximum(var_1, var_2, var_3)
        self._modeller.add_constraint(constraint)

    def constraint_member(self, var_1: ArrayVariable, var_2: Variable) -> None:
        """
        Add a member constraint between an array variable and a variable.

        Args:
            var_1 (ArrayVariable): The array variable.
            var_2 (Variable): The variable to check for membership.
        """
        constraint = ConstraintMember(var_1, var_2)
        self._modeller.add_constraint(constraint)

    def constraint_minimum(
        self, var_1: Variable, var_2: Variable, var_3: Variable
    ) -> None:
        """
        Add a minimum constraint between two variables such that var_3 = min(var_1, var_2).

        Args:
            var_1 (Variable): The first variable.
            var_2 (Variable): The second variable.
            var_3 (Variable): The variable to store the minimum.
        """
        constraint = ConstraintMinimum(var_1, var_2, var_3)
        self._modeller.add_constraint(constraint)

    def constraint_modulo(
        self, var_1: Variable, var_2: Variable, var_3: Variable
    ) -> None:
        """
        Add a modulo constraint between integer variables such that var_3 = var_1 % var_2.

        Args:
            var_1 (Variable): The first integer variable.
            var_2 (Variable): The second integer variable.
            var_3 (Variable): The variable to store the modulo.
        """
        constraint = ConstraintModulo(var_1, var_2, var_3)
        self._modeller.add_constraint(constraint)

    def constraint_multiply(
        self, var_1: Variable, var_2: Variable, var_3: Variable
    ) -> None:
        """
        Add a multiply constraint between integer variables such that var_3 = var_1 * var_2.

        Args:
            var_1 (Variable): The first integer variable.
            var_2 (Variable): The second integer variable.
            var_3 (Variable): The variable to store the product.
        """
        constraint = ConstraintMultiply(var_1, var_2, var_3)
        self._modeller.add_constraint(constraint)

    def constraint_nroot(self, var_1: Variable, var_2: int, var_3: Variable) -> None:
        """
        Add a nroot constraint between integer variables such that var_3 = var_1 ** (1/var_2).

        Args:
            var_1 (Variable): The first integer variable.
            var_2 (Variable): The second integer variable.
            var_3 (Variable): The variable to store the nroot.
        """
        constraint = ConstraintNRoot(var_1, var_2, var_3)
        self._modeller.add_constraint(constraint)

    def constraint_power(self, var_1: Variable, var_2: int, var_3: Variable) -> None:
        """
        Add a power constraint between two integer variables.

        Args:
            var_1 (Variable): The first integer variable.
            var_2 (Variable): The second integer variable.
            var_3 (Variable): The variable to store the power.
        """
        constraint = ConstraintPower(var_1, var_2, var_3)
        self._modeller.add_constraint(constraint)

    def constraint_sin(self, var_1: FloatVariable, var_2: FloatVariable) -> None:
        """
        Add a sine constraint between two float variables.
        Args:
            var_1 (FloatVariable): The first float variable.
            var_2 (FloatVariable): The second float variable.
        """
        constraint = ConstraintSin(var_1, var_2)
        self._modeller.add_constraint(constraint)

    def constraint_sort(self, var_1: ArrayVariable) -> None:
        """
        Add a sort constraint between two integer variables.

        Args:
            var_1 (ArrayVariable): The array variable.
        """
        constraint = ConstraintSorted(var_1)
        self._modeller.add_constraint(constraint)

    def constraint_reversed_sort(self, var_1: ArrayVariable) -> None:
        """
        Add a reversed sort constraint between two integer variables.

        Args:
            var_1 (ArrayVariable): The array variable.
        """
        constraint = ConstraintReverseSorted(var_1)
        self._modeller.add_constraint(constraint)

    def constraint_tan(self, var_1: Variable, var_2: Variable) -> None:
        """
        Add a tangent constraint between two variables.

        Args:
            var_1 (Variable): The first variable.
            var_2 (Variable): The second variable.
        """
        constraint = ConstraintTan(var_1, var_2)
        self._modeller.add_constraint(constraint)

    def minimize(self, variable: Variable) -> None:
        """
        Adds an minimization objective to the model.

        Args:
            variable (Variable): The variable to minimize.
        """
        self._modeller.add_objective(objective=SpecificMinimum(variable=variable))

    def maximize(self, variable: Variable) -> None:
        """
        Adds an maximization objective to the model.

        Args:
            variable (Variable): The variable to maximize.
        """
        self._modeller.add_objective(objective=SpecificMaximum(variable=variable))

    def solve(
        self,
        searcher: str = "dfs",
        solution_limit: int = 1,
        cutoff: Union[Cutoff, None] = None,
    ) -> Union[list[Solution], None]:
        """
        Solves the model.

        This method configures the searcher strategy, solution limit, and cutoff strategy,
        then sends the model to the DirectEngine for solving. If the solver returns a successful
        status, the method returns the list of solutions found. If the solver encounters an error,
        a SolverError is raised with the relevant details.

        The different searcher strategies available are:
        - "dfs": Depth-First Search (default strategy)
        - "bab": Branch-and-Bound
        - "lds": Limited Discrepancy Search algorithm.
        - "pbs": Portfolio-Based Search algorithm.
        - "rbs": Restart-based Search algorithm.

        Args:
            searcher (str): The searcher strategy to use ("dfs", "bab", etc.).
            solution_limit (int): The maximum number of solutions to find.
            cutoff (Cutoff, optional): The cutoff strategy to use.
        """
        if searcher.upper() not in [st.value for st in SearcherType]:
            raise ValueError(
                f"Invalid searcher '{searcher}'. Available searchers: {[st.value for st in SearcherType]}"
            )
        self._modeller.set_searcher(searcher=SearcherType(searcher.upper()))

        if solution_limit <= 0:
            raise ValueError("solution_limit must be greater than 0.")
        self._modeller.set_solution_limit(solution_limit=solution_limit)

        self._modeller.set_cutoff(cutoff=cutoff)

        solution_response: SolutionResponse = self._engine.model(self._modeller)
        if not solution_response.is_status_ok():
            raise SolverError(
                status=solution_response.get_status(),
                message=solution_response.get_message(),
                content=solution_response.get_content(),
            )
        return solution_response.get_solutions()

    def solve_one(
        self, searcher: str = "dfs", cutoff: Union[Cutoff, None] = None
    ) -> Union[Solution, None]:
        """
        Solves the model and returns one solution.

        This method configures the searcher strategy and cutoff strategy,
        then sends the model to the DirectEngine for solving. If the solver returns a successful
        status, the method returns the first solution found. If the solver encounters an error,
        a SolverError is raised with the relevant details.

        The different searcher strategies available are:
        - "dfs": Depth-First Search (default strategy)
        - "bab": Branch-and-Bound
        - "lds": Limited Discrepancy Search algorithm.
        - "pbs": Portfolio-Based Search algorithm.
        - "rbs": Restart-based Search algorithm.

        Args:
            searcher (str): The searcher strategy to use ("dfs", "bab", etc.).
            cutoff (Cutoff, optional): The cutoff strategy to use.
        """
        solutions = self.solve(searcher=searcher, solution_limit=1, cutoff=cutoff)
        if solutions:
            return solutions[0]
        return None

    def to_json(self) -> dict:
        """
        Serializes the model into a JSON-compatible Python dictionary.

        Returns:
            dict: JSON representation of the optimization model.

        Raises:
            ModelFailure: If no searcher is defined before export.
        """
        return self._modeller.to_json(serialization=True)

    @staticmethod
    def from_json(json_data: dict) -> "Model":
        """
        Creates a Model instance from a JSON-compatible Python dictionary.

        Args:
            json_data (dict): A dictionary representing the model.

        Returns:
                Model: An instance of the Model class.
        """
        modeller = Modeller.from_json(json_data)
        model = Model()
        model._modeller = modeller  # pylint: disable=protected-access
        return model
