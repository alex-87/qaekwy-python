# pylint: skip-file


import unittest

from qaekwy.model.variable.integer import IntegerVariableArray
from qaekwy.model.constraint.distinct import ConstraintDistinctArray, ConstraintDistinctCol, ConstraintDistinctRow, ConstraintDistinctSlice


class TestConstraintDistinctArray(unittest.TestCase):

    def setUp(self):
        self.array_var = IntegerVariableArray("array_var", 10, 0, 30)

    def test_constraint_array_creation(self):
        constraint = ConstraintDistinctArray(self.array_var, "distinct_array_constraint")
        self.assertEqual(constraint.var_1, self.array_var)
        self.assertEqual(constraint.constraint_name, "distinct_array_constraint")

    def test_constraint_array_to_json(self):
        constraint = ConstraintDistinctArray(self.array_var, "distinct_array_constraint")
        expected_json = {
            "name": "distinct_array_constraint",
            "type": "distinct",
            "v1": "array_var",
            "selection": "standard"
        }
        self.assertEqual(constraint.to_json(), expected_json)

class TestConstraintDistinctRow(unittest.TestCase):

    def setUp(self):
        self.array_var = IntegerVariableArray("array_var", 10, 0, 30)

    def test_constraint_row_creation(self):
        constraint = ConstraintDistinctRow(self.array_var, size=3, idx=1, constraint_name="distinct_row_constraint")
        self.assertEqual(constraint.var_1, self.array_var)
        self.assertEqual(constraint.size, 3)
        self.assertEqual(constraint.idx, 1)
        self.assertEqual(constraint.constraint_name, "distinct_row_constraint")

    def test_constraint_row_to_json(self):
        constraint = ConstraintDistinctRow(self.array_var, size=3, idx=1, constraint_name="distinct_row_constraint")
        expected_json = {
            "name": "distinct_row_constraint",
            "type": "distinct",
            "v1": "array_var",
            "selection": "row",
            "size": 3,
            "index": 1
        }
        self.assertEqual(constraint.to_json(), expected_json)

class TestConstraintDistinctCol(unittest.TestCase):

    def setUp(self):
        self.array_var = IntegerVariableArray("array_var", 10, 0, 30)

    def test_constraint_column_creation(self):
        constraint = ConstraintDistinctCol(self.array_var, size=3, idx=0, constraint_name="distinct_col_constraint")
        self.assertEqual(constraint.var_1, self.array_var)
        self.assertEqual(constraint.size, 3)
        self.assertEqual(constraint.idx, 0)
        self.assertEqual(constraint.constraint_name, "distinct_col_constraint")

    def test_constraint_column_to_json(self):
        constraint = ConstraintDistinctCol(self.array_var, size=3, idx=0, constraint_name="distinct_col_constraint")
        expected_json = {
            "name": "distinct_col_constraint",
            "type": "distinct",
            "v1": "array_var",
            "selection": "col",
            "size": 3,
            "index": 0
        }
        self.assertEqual(constraint.to_json(), expected_json)

class TestConstraintDistinctSlice(unittest.TestCase):

    def setUp(self):
        self.array_var = IntegerVariableArray("array_var", 10, 0, 30)

    def test_constraint_slice_creation(self):
        constraint = ConstraintDistinctSlice(self.array_var, size=6, offset_start_x=1, offset_start_y=1, offset_end_x=3, offset_end_y=2, constraint_name="distinct_slice_constraint")
        self.assertEqual(constraint.var_1, self.array_var)
        self.assertEqual(constraint.size, 6)
        self.assertEqual(constraint.offset_start_x, 1)
        self.assertEqual(constraint.offset_start_y, 1)
        self.assertEqual(constraint.offset_end_x, 3)
        self.assertEqual(constraint.offset_end_y, 2)
        self.assertEqual(constraint.constraint_name, "distinct_slice_constraint")

    def test_constraint_slice_to_json(self):
        constraint = ConstraintDistinctSlice(self.array_var, size=6, offset_start_x=1, offset_start_y=1, offset_end_x=3, offset_end_y=2, constraint_name="distinct_slice_constraint")
        expected_json = {
            "name": "distinct_slice_constraint",
            "type": "distinct",
            "v1": "array_var",
            "selection": "slice",
            "size": 6,
            "offset_start_x": 1,
            "offset_start_y": 1,
            "offset_end_x": 3,
            "offset_end_y": 2
        }
        self.assertEqual(constraint.to_json(), expected_json)

if __name__ == '__main__':
    unittest.main()
