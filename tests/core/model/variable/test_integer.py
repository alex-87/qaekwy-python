# pylint: skip-file

import unittest

from qaekwy.core.model.variable.branch import BranchIntegerVal, BranchIntegerVar
from qaekwy.core.model.variable.integer import IntegerVariable, IntegerVariableMatrix
from qaekwy.core.model.variable.variable import Expression, VariableType, VectorExpression


class TestExpression(unittest.TestCase):
    def test_arithmetic_operations(self):
        expr = Expression("x")
        expr_add = expr + 2
        self.assertEqual(str(expr_add), "(x + 2)")

        expr_sub = expr - 3
        self.assertEqual(str(expr_sub), "(x - 3)")

        expr_mul = expr * 4
        self.assertEqual(str(expr_mul), "x * 4")

        expr_div = expr / 5
        self.assertEqual(str(expr_div), "((x) / (5))")

        expr_mod = expr % 6
        self.assertEqual(str(expr_mod), "((x) % (6))")


class TestVariable(unittest.TestCase):
    def test_variable_to_json(self):
        var = IntegerVariable("x", domain_low=0, domain_high=10)

        var_json = var.to_json()
        self.assertEqual(var_json["name"], "x")
        self.assertEqual(var_json["type"], "integer")
        self.assertEqual(var_json["brancher_value"], "VAL_RND")
        self.assertEqual(var_json["domlow"], 0)
        self.assertEqual(var_json["domup"], 10)


class TestSpecificDomainVariable(unittest.TestCase):
    def test_variable_to_json(self):
        var = IntegerVariable("x", specific_domain=[2, 4, 6])

        var_json = var.to_json()
        self.assertEqual(var_json["name"], "x")
        self.assertEqual(var_json["type"], "integer")
        self.assertEqual(var_json["brancher_value"], "VAL_RND")
        self.assertEqual(var_json["specific_domain"], [2, 4, 6])


class TestExprVariable(unittest.TestCase):
    def test_variable_to_json(self):
        var = IntegerVariable("x")
        var_expr = var + 2
        var.expression = var_expr

        var_json = var.to_json()
        self.assertEqual(var_json["name"], "x")
        self.assertEqual(var_json["type"], "integer")
        self.assertEqual(var_json["brancher_value"], "VAL_RND")
        self.assertEqual(var_json["expr"], "(x + 2)")


class TestIntegerVariable(unittest.TestCase):
    def test_integer_variable_to_json(self):
        int_var = IntegerVariable("y", domain_low=1, domain_high=5)
        int_var_json = int_var.to_json()
        self.assertEqual(int_var_json["name"], "y")
        self.assertEqual(int_var_json["type"], "integer")
        self.assertEqual(int_var_json["brancher_value"], "VAL_RND")
        self.assertEqual(int_var_json["domlow"], 1)
        self.assertEqual(int_var_json["domup"], 5)

    def test_from_json(self):
        json_data = {
            "name": "i",
            "type": "integer",
            "brancher_value": "VAL_MAX",
            "specific_domain": [1, 2, 3],
        }
        i = IntegerVariable.from_json(json_data)
        self.assertEqual(i.var_name, "i")
        self.assertEqual(i.specific_domain, [1, 2, 3])
        self.assertEqual(i.branch_val, BranchIntegerVal.VAL_MAX)

        json_data = {
            "name": "j",
            "type": "integer",
            "brancher_value": "VAL_MAX",
            "domlow": 0,
            "domup": 100,
        }
        i = IntegerVariable.from_json(json_data)
        self.assertEqual(i.var_name, "j")
        self.assertEqual(i.domain_low, 0)
        self.assertEqual(i.domain_high, 100)
        self.assertEqual(i.branch_val, BranchIntegerVal.VAL_MAX)


class TestIntegerMatrix(unittest.TestCase):

    def test_matrix_variable_basic_init(self):
        m = IntegerVariableMatrix("A", rows=2, cols=3)

        assert m.rows == 2
        assert m.cols == 3
        assert m.length == 6
        assert m.var_type == VariableType.INTEGER_ARRAY
        assert m.var_name == "MATRIX$2$3$A"

    def test_matrix_variable_domain_fields(self):
        m = IntegerVariableMatrix(
            "B",
            rows=2,
            cols=2,
            domain_low=0,
            domain_high=10,
            specific_domain=[1, 3, 5],
        )

        assert m.domain_low == 0
        assert m.domain_high == 10
        assert m.specific_domain == [1, 3, 5]

    def test_matrix_item_access_returns_expression(self):
        m = IntegerVariableMatrix("A", rows=2, cols=3)

        expr = m[1][2]
        assert isinstance(expr, Expression)
        assert str(expr) == "MATRIX$2$3$A[5]"  # 1 * 3 + 2


    def test_row_vector_expression_creation(self):
        m = IntegerVariableMatrix("A", rows=2, cols=3)

        v = m.row(1)
        assert isinstance(v, VectorExpression)
        assert v.kind == "row"
        assert v.params["row"] == 1


    def test_col_vector_expression_creation(self):
        m = IntegerVariableMatrix("A", rows=2, cols=3)

        v = m.col(2)
        assert isinstance(v, VectorExpression)
        assert v.kind == "col"
        assert v.params["col"] == 2


    def test_slice_vector_expression_creation(self):
        m = IntegerVariableMatrix("A", rows=3, cols=3)

        v = m.slice(0, 1, 1, 2)

        assert v.kind == "slice"
        assert v.params["row_start"] == 0
        assert v.params["col_start"] == 1
        # slice() adds +1 internally
        assert v.params["row_end"] == 2
        assert v.params["col_end"] == 3

    def test_iter_row_vector_expression(self):
        m = IntegerVariableMatrix("A", rows=2, cols=3)

        v = m.row(0)
        items = list(v)

        assert len(items) == 3
        assert [str(e) for e in items] == [
            "MATRIX$2$3$A[0]",
            "MATRIX$2$3$A[1]",
            "MATRIX$2$3$A[2]",
        ]


    def test_iter_col_vector_expression(self):
        m = IntegerVariableMatrix("A", rows=3, cols=2)

        v = m.col(1)
        items = list(v)

        assert len(items) == 3
        assert [str(e) for e in items] == [
            "MATRIX$3$2$A[1]",
            "MATRIX$3$2$A[3]",
            "MATRIX$3$2$A[5]",
        ]


    def test_iter_slice_vector_expression(self):
        m = IntegerVariableMatrix("A", rows=3, cols=3)

        v = m.slice(0, 0, 1, 1)
        items = list(v)

        assert len(items) == 4
        assert [str(e) for e in items] == [
            "MATRIX$3$3$A[0]",
            "MATRIX$3$3$A[1]",
            "MATRIX$3$3$A[3]",
            "MATRIX$3$3$A[4]",
        ]


    def test_vector_expression_str_row(self):
        m = IntegerVariableMatrix("A", rows=2, cols=3)

        v = m.row(1)
        assert str(v) == "MATRIX$2$3$A[2][3][r][1]"


    def test_vector_expression_str_col(self):
        m = IntegerVariableMatrix("A", rows=2, cols=3)

        v = m.col(0)
        assert str(v) == "MATRIX$2$3$A[2][3][c][0]"


    def test_vector_expression_str_slice(self):
        m = IntegerVariableMatrix("A", rows=3, cols=3)

        v = m.slice(0, 1, 1, 2)
        assert str(v) == "MATRIX$3$3$A[3][3][s][0][1][2][3]"


    def test_vector_expression_sum_method(self):
        m = IntegerVariableMatrix("A", rows=2, cols=2)

        v = m.row(0)
        s = v.sum()

        assert isinstance(s, Expression)
        assert str(s) == f"sum({v})"


    def test_vector_expression_radd_with_zero(self):
        m = IntegerVariableMatrix("A", rows=2, cols=2)

        v = m.col(0)
        result = sum([v])  # triggers __radd__ with 0

        assert isinstance(result, Expression)
        assert str(result) == f"sum({v})"


    def test_matrix_variable_to_json(self):
        m = IntegerVariableMatrix(
            "A",
            rows=2,
            cols=3,
            domain_low=0,
            domain_high=5,
            branch_var=BranchIntegerVar.VAR_RND,
            branch_val=BranchIntegerVal.VAL_RND,
            branch_order=7,
        )

        data = m.to_json()

        assert data["name"] == m.var_name
        assert data["rows"] == 2
        assert data["cols"] == 3
        assert data["length"] == 6
        assert data["subtype"] == "matrix"
        assert data["domlow"] == 0
        assert data["domup"] == 5
        assert data["branching_order"] == 7


    def test_matrix_variable_from_json_roundtrip(self):
        m = IntegerVariableMatrix(
            "A",
            rows=2,
            cols=2,
            domain_low=1,
            domain_high=9,
        )

        data = m.to_json()
        restored = IntegerVariableMatrix.from_json(data)

        assert restored.var_name == m.var_name
        assert restored.rows == 2
        assert restored.cols == 2
        assert restored.domain_low == 1
        assert restored.domain_high == 9

if __name__ == "__main__":
    unittest.main()
