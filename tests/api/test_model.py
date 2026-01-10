# pylint: skip-file

import unittest
from unittest.mock import MagicMock, patch

from qaekwy import Model
from qaekwy import SolverError

from qaekwy.core.model.cutoff import Cutoff
from qaekwy.core.model.searcher import SearcherType
from qaekwy.core.response import SolutionResponse
from qaekwy.core.solution import Solution

from qaekwy.core.model.variable.integer import IntegerVariable
from qaekwy.core.model.variable.integer import IntegerVariableArray
from qaekwy.core.model.variable.variable import VectorExpression
from qaekwy.core.model.variable.variable import MatrixVariable




class TestModelVariables(unittest.TestCase):

    def setUp(self):
        self.model = Model()
        self.model._modeller = MagicMock()

    def test_integer_variable(self):
        var = self.model.integer_variable(
            name="x",
            domain=(0, 10)
        )

        self.assertIsInstance(var, IntegerVariable)
        self.model._modeller.add_variable.assert_called_once_with(var)

    def test_integer_array(self):
        arr = self.model.integer_array(
            name="x",
            length=5,
            domain=(0, 9)
        )

        self.assertIsInstance(arr, IntegerVariableArray)
        self.model._modeller.add_variable.assert_called_once_with(arr)

class TestConstraintDistinct(unittest.TestCase):

    def setUp(self):
        self.model = Model()
        self.model._modeller = MagicMock()

    def test_constraint_distinct_array(self):
        array = MagicMock(spec=IntegerVariableArray)

        self.model.constraint_distinct(array)

        self.model._modeller.add_constraint.assert_called_once()

    def test_constraint_distinct_row(self):
        matrix = MagicMock(spec=MatrixVariable)
        matrix.cols = 4

        vec = MagicMock(spec=VectorExpression)
        vec.matrix = matrix
        vec.kind = "row"
        vec.params = {"row": 1}

        self.model.constraint_distinct(vec)

        self.model._modeller.add_constraint.assert_called_once()

    def test_constraint_distinct_col(self):
        matrix = MagicMock(spec=MatrixVariable)
        matrix.rows = 3

        vec = MagicMock(spec=VectorExpression)
        vec.matrix = matrix
        vec.kind = "col"
        vec.params = {"col": 2}

        self.model.constraint_distinct(vec)

        self.model._modeller.add_constraint.assert_called_once()

    def test_constraint_distinct_slice(self):
        matrix = MagicMock(spec=MatrixVariable)
        matrix.cols = 5

        vec = MagicMock(spec=VectorExpression)
        vec.matrix = matrix
        vec.kind = "slice"
        vec.params = {
            "row_start": 0,
            "col_start": 0,
            "row_end": 2,
            "col_end": 2,
        }

        self.model.constraint_distinct(vec)

        self.model._modeller.add_constraint.assert_called_once()

    def test_constraint_distinct_invalid_type(self):
        with self.assertRaises(TypeError):
            self.model.constraint_distinct(object())


class TestSolve(unittest.TestCase):

    def setUp(self):
        self.model = Model()
        self.model._modeller = MagicMock()
        self.model._engine = MagicMock()

    def test_invalid_searcher(self):
        with self.assertRaises(ValueError):
            self.model.solve(searcher="invalid")

    def test_invalid_solution_limit(self):
        with self.assertRaises(ValueError):
            self.model.solve(solution_limit=0)

    def test_solver_error(self):
        response = MagicMock(spec=SolutionResponse)
        response.is_status_ok.return_value = False
        response.get_status.return_value = "ERROR"
        response.get_message.return_value = "Failure"
        response.get_content.return_value = {}

        self.model._engine.model.return_value = response

        with self.assertRaises(SolverError):
            self.model.solve()

    def test_solve_success(self):
        sol = MagicMock(spec=Solution)

        response = MagicMock(spec=SolutionResponse)
        response.is_status_ok.return_value = True
        response.get_solutions.return_value = [sol]

        self.model._engine.model.return_value = response

        solutions = self.model.solve()

        self.assertEqual(solutions, [sol])

    def test_solve_one(self):
        sol = MagicMock(spec=Solution)

        self.model.solve = MagicMock(return_value=[sol])

        result = self.model.solve_one()

        self.assertEqual(result, sol)

class TestModelExpressionVariables(unittest.TestCase):

    def setUp(self):
        self.model = Model()
        self.model._modeller = MagicMock()

    def test_integer_expression_variable(self):
        v = self.model.integer_variable(
            name="x",
            expression="y + 1"
        )

        self.model._modeller.add_variable.assert_called_once_with(v)
        self.assertEqual(v.var_name, "x")

    def test_float_expression_variable(self):
        v = self.model.float_variable(
            name="f",
            domain=None,
            expression="x * 0.5"
        )

        self.model._modeller.add_variable.assert_called_once_with(v)
        self.assertEqual(v.var_name, "f")

class TestModelBooleanVariables(unittest.TestCase):

    def setUp(self):
        self.model = Model()
        self.model._modeller = MagicMock()

    def test_boolean_variable(self):
        v = self.model.boolean_variable("b")

        self.model._modeller.add_variable.assert_called_once_with(v)

    def test_boolean_array(self):
        arr = self.model.boolean_array("b", length=3)

        self.model._modeller.add_variable.assert_called_once_with(arr)

class TestModelFloatCollections(unittest.TestCase):

    def setUp(self):
        self.model = Model()
        self.model._modeller = MagicMock()

    def test_float_array(self):
        arr = self.model.float_array("f", length=4, domain=(0.0, 1.0))
        self.model._modeller.add_variable.assert_called_once_with(arr)

    def test_float_matrix(self):
        mat = self.model.float_matrix("m", rows=2, cols=2, domain=(0.0, 10.0))
        self.model._modeller.add_variable.assert_called_once_with(mat)

class TestModelObjectives(unittest.TestCase):

    def setUp(self):
        self.model = Model()
        self.model._modeller = MagicMock()

    def test_minimize(self):
        var = MagicMock()
        self.model.minimize(var)

        self.model._modeller.add_objective.assert_called_once()

    def test_maximize(self):
        var = MagicMock()
        self.model.maximize(var)

        self.model._modeller.add_objective.assert_called_once()

class TestModelConstraints(unittest.TestCase):

    def setUp(self):
        self.model = Model()
        self.model._modeller = MagicMock()
        self.v1 = MagicMock()
        self.v2 = MagicMock()
        self.v3 = MagicMock()

    def test_constraint_abs(self):
        self.model.constraint_abs(self.v1, self.v2)
        self.model._modeller.add_constraint.assert_called_once()

    def test_constraint_multiply(self):
        self.model.constraint_multiply(self.v1, self.v2, self.v3)
        self.model._modeller.add_constraint.assert_called_once()

    def test_constraint_divide(self):
        self.model.constraint_divide(self.v1, self.v2, self.v3)
        self.model._modeller.add_constraint.assert_called_once()

    def test_constraint_power(self):
        self.model.constraint_power(self.v1, 2, self.v3)
        self.model._modeller.add_constraint.assert_called_once()

    def test_constraint_if_then_else(self):
        cond = MagicMock()
        then_c = MagicMock()

        self.model.constraint_if_then_else(cond, then_c)

        self.model._modeller.add_constraint.assert_called_once()

class TestModelSearcherConfiguration(unittest.TestCase):

    def setUp(self):
        self.model = Model()
        self.model._modeller = MagicMock()
        self.model._engine = MagicMock()

    def test_searcher_set_correctly(self):
        response = MagicMock()
        response.is_status_ok.return_value = True
        response.get_solutions.return_value = []

        self.model._engine.model.return_value = response

        self.model.solve(searcher="dfs")

        self.model._modeller.set_searcher.assert_called_once_with(
            searcher=SearcherType.DFS
        )

    def test_cutoff_passed(self):
        cutoff = MagicMock(spec=Cutoff)

        response = MagicMock()
        response.is_status_ok.return_value = True
        response.get_solutions.return_value = []

        self.model._engine.model.return_value = response

        self.model.solve(cutoff=cutoff)

        self.model._modeller.set_cutoff.assert_called_once_with(cutoff=cutoff)

class TestSolveOneEdgeCases(unittest.TestCase):

    def setUp(self):
        self.model = Model()

    def test_solve_one_no_solution(self):
        self.model.solve = MagicMock(return_value=[])

        result = self.model.solve_one()

        self.assertIsNone(result)

class TestModelJsonExtended(unittest.TestCase):

    def test_to_json_delegation(self):
        model = Model()
        model._modeller = MagicMock()
        model._modeller.to_json.return_value = {"k": "v"}

        self.assertEqual(model.to_json(), {"k": "v"})
