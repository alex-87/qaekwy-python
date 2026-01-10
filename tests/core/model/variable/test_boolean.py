# pylint: skip-file

import unittest

from qaekwy.core.model.variable.boolean import (
    BooleanVariable,
    BooleanExpressionVariable,
    BooleanVariableArray,
    BooleanVariableMatrix,
)

from qaekwy.core.model.variable.variable import (
    Expression,
    VariableType,
)

from qaekwy.core.model.variable.branch import (
    BranchBooleanVal,
    BranchBooleanVar,
)


class TestBooleanVariable(unittest.TestCase):

    def test_boolean_variable_basic_init(self):
        v = BooleanVariable("b")

        self.assertEqual(v.var_name, "b")
        self.assertEqual(v.var_type, VariableType.BOOLEAN)
        self.assertEqual(v.domain_low, 0)
        self.assertEqual(v.domain_high, 1)
        self.assertEqual(v.branch_val, BranchBooleanVal.VAL_RND)

    def test_boolean_variable_to_json_and_from_json_roundtrip(self):
        v = BooleanVariable(
            "b1",
            branch_val=BranchBooleanVal.VAL_RND,
            branch_order=5,
        )

        data = v.to_json()
        restored = BooleanVariable.from_json(data)

        self.assertEqual(restored.var_name, v.var_name)
        self.assertEqual(restored.var_type, VariableType.BOOLEAN)
        self.assertEqual(restored.domain_low, 0)
        self.assertEqual(restored.domain_high, 1)
        self.assertEqual(restored.branch_val, BranchBooleanVal.VAL_RND)
        self.assertEqual(restored.branching_order, 5)

    def test_boolean_expression_variable_basic_init(self):
        expr = "x > 5"
        v = BooleanExpressionVariable("be", expression=expr)

        self.assertEqual(v.var_name, "be")
        self.assertEqual(v.var_type, VariableType.BOOLEAN)
        self.assertEqual(str(v.expression), "x > 5")

    def test_boolean_expression_variable_from_json(self):
        json_data = {
            "name": "be_json",
            "expr": "y == 1",
            "type": VariableType.BOOLEAN.value,
            "brancher_value": BranchBooleanVal.VAL_RND.value,
            "branching_order": 2,
        }

        v = BooleanExpressionVariable.from_json(json_data)

        self.assertEqual(v.var_name, "be_json")
        self.assertEqual(str(v.expression), "y == 1")
        self.assertEqual(v.branch_val, BranchBooleanVal.VAL_RND)
        self.assertEqual(v.branching_order, 2)

    def test_boolean_variable_array_basic_init(self):
        arr = BooleanVariableArray("bool_arr", length=10)

        self.assertEqual(arr.var_name, "bool_arr")
        self.assertEqual(arr.length, 10)
        self.assertEqual(arr.var_type, VariableType.BOOLEAN_ARRAY)
        self.assertEqual(arr.domain_low, 0)
        self.assertEqual(arr.domain_high, 1)
        self.assertEqual(arr.branch_var, BranchBooleanVar.VAR_RND)

    def test_boolean_variable_array_to_json_and_from_json_roundtrip(self):
        arr = BooleanVariableArray(
            "arr_json",
            length=3,
            branch_var=BranchBooleanVar.VAR_RND,
            branch_val=BranchBooleanVal.VAL_RND,
            branch_order=1,
        )

        data = arr.to_json()
        restored = BooleanVariableArray.from_json(data)

        self.assertEqual(restored.var_name, arr.var_name)
        self.assertEqual(restored.length, 3)
        self.assertEqual(restored.domain_low, 0)
        self.assertEqual(restored.domain_high, 1)
        self.assertEqual(restored.branch_var, BranchBooleanVar.VAR_RND)
        self.assertEqual(restored.branch_val, BranchBooleanVal.VAL_RND)
        self.assertEqual(restored.branching_order, 1)

    def test_boolean_variable_matrix_basic_init(self):
        m = BooleanVariableMatrix("M", rows=4, cols=5)

        self.assertEqual(m.rows, 4)
        self.assertEqual(m.cols, 5)
        self.assertEqual(m.length, 20)
        self.assertEqual(m.var_type, VariableType.BOOLEAN_ARRAY)
        self.assertEqual(m.domain_low, 0)
        self.assertEqual(m.domain_high, 1)

    def test_boolean_variable_matrix_to_json_and_from_json_roundtrip(self):
        m = BooleanVariableMatrix(
            "mat_json",
            rows=2,
            cols=2,
            branch_var=BranchBooleanVar.VAR_RND,
            branch_val=BranchBooleanVal.VAL_RND,
            branch_order=4,
        )

        data = m.to_json()
        restored = BooleanVariableMatrix.from_json(data)

        self.assertEqual(restored.var_name, m.var_name)
        self.assertEqual(restored.rows, 2)
        self.assertEqual(restored.cols, 2)
        self.assertEqual(restored.length, 4)
        self.assertEqual(restored.branch_var, BranchBooleanVar.VAR_RND)
        self.assertEqual(restored.branch_val, BranchBooleanVal.VAL_RND)
        self.assertEqual(restored.branching_order, 4)


if __name__ == "__main__":
    unittest.main()
