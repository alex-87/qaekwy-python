# pylint: skip-file

import unittest

from qaekwy.core.model.variable.float import (
    FloatVariable,
    FloatExpressionVariable,
    FloatVariableArray,
    FloatVariableMatrix,
    Expression,
    VariableType,
)
from qaekwy.core.model.variable.branch import (
    BranchFloatVal,
    BranchFloatVar,
)


class TestFloatVariable(unittest.TestCase):

    def test_float_variable_basic_init(self):
        v = FloatVariable("x")

        assert v.var_name == "x"
        assert v.var_type == VariableType.FLOAT
        assert v.domain_low is None
        assert v.domain_high is None
        assert v.branch_val == BranchFloatVal.VAL_RND


    def test_float_variable_with_domain(self):
        v = FloatVariable("x", domain_low=0.0, domain_high=1.0)

        assert v.domain_low == 0.0
        assert v.domain_high == 1.0


    def test_float_variable_to_json_and_from_json_roundtrip(self):
        v = FloatVariable(
            "x",
            domain_low=-1.5,
            domain_high=2.5,
            branch_val=BranchFloatVal.VAL_RND,
            branch_order=3,
        )

        data = v.to_json()
        restored = FloatVariable.from_json(data)

        assert restored.var_name == v.var_name
        assert restored.var_type == VariableType.FLOAT
        assert restored.domain_low == -1.5
        assert restored.domain_high == 2.5
        assert restored.branch_val == BranchFloatVal.VAL_RND
        assert restored.branching_order == 3


    def test_float_expression_variable_basic_init(self):
        expr = Expression("x + 1.5")
        v = FloatExpressionVariable("y", expression=expr.expr)

        assert v.var_name == "y"
        assert v.var_type == VariableType.FLOAT
        assert str(v.expression) == "x + 1.5"


    def test_float_expression_variable_from_json(self):
        json_data = {
            "name": "z",
            "expr": "x * 0.5",
            "type": VariableType.FLOAT.value,
            "brancher_value": BranchFloatVal.VAL_RND.value,
            "branching_order": 2,
        }

        v = FloatExpressionVariable.from_json(json_data)

        assert v.var_name == "z"
        assert v.var_type == VariableType.FLOAT
        assert str(v.expression) == "x * 0.5"
        assert v.branch_val == BranchFloatVal.VAL_RND
        assert v.branching_order == 2


    def test_float_variable_array_basic_init(self):
        arr = FloatVariableArray("arr", length=5)

        assert arr.var_name == "arr"
        assert arr.length == 5
        assert arr.var_type == VariableType.FLOAT_ARRAY
        assert arr.domain_low is None
        assert arr.domain_high is None
        assert arr.branch_var == BranchFloatVar.VAR_RND


    def test_float_variable_array_with_domain(self):
        arr = FloatVariableArray(
            "arr",
            length=3,
            domain_low=0.0,
            domain_high=10.0,
        )

        assert arr.domain_low == 0.0
        assert arr.domain_high == 10.0


    def test_float_variable_array_to_json_and_from_json_roundtrip(self):
        arr = FloatVariableArray(
            "arr",
            length=4,
            domain_low=-2.0,
            domain_high=2.0,
            branch_var=BranchFloatVar.VAR_RND,
            branch_val=BranchFloatVal.VAL_RND,
            branch_order=1,
        )

        data = arr.to_json()
        restored = FloatVariableArray.from_json(data)

        assert restored.var_name == arr.var_name
        assert restored.length == 4
        assert restored.var_type == VariableType.FLOAT_ARRAY
        assert restored.domain_low == -2.0
        assert restored.domain_high == 2.0
        assert restored.branch_var == BranchFloatVar.VAR_RND
        assert restored.branch_val == BranchFloatVal.VAL_RND
        assert restored.branching_order == 1

    def test_float_variable_matrix_basic_init(self):
        m = FloatVariableMatrix("M", rows=2, cols=3)

        assert m.rows == 2
        assert m.cols == 3
        assert m.length == 6
        assert m.var_type == VariableType.FLOAT_ARRAY
        assert m.branch_var == BranchFloatVar.VAR_RND


    def test_float_variable_matrix_with_domain(self):
        m = FloatVariableMatrix(
            "M",
            rows=3,
            cols=3,
            domain_low=0.0,
            domain_high=1.0,
        )

        assert m.domain_low == 0.0
        assert m.domain_high == 1.0


    def test_float_variable_matrix_to_json_and_from_json_roundtrip(self):
        m = FloatVariableMatrix(
            "M",
            rows=2,
            cols=2,
            domain_low=-1.0,
            domain_high=1.0,
            branch_var=BranchFloatVar.VAR_RND,
            branch_val=BranchFloatVal.VAL_RND,
            branch_order=4,
        )

        data = m.to_json()
        restored = FloatVariableMatrix.from_json(data)

        assert restored.var_name == m.var_name
        assert restored.rows == 2
        assert restored.cols == 2
        assert restored.length == 4
        assert restored.domain_low == -1.0
        assert restored.domain_high == 1.0
        assert restored.branch_var == BranchFloatVar.VAR_RND
        assert restored.branch_val == BranchFloatVal.VAL_RND
        assert restored.branching_order == 4

if __name__ == "__main__":
    unittest.main()
