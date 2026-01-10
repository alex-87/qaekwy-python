# pylint: skip-file
import unittest

# Import the classes under test
# Adjust the import path if needed for your project structure
from qaekwy.core.model.constraint.distinct import (
    ConstraintDistinctArray,
    ConstraintDistinctRow,
    ConstraintDistinctCol,
    ConstraintDistinctSlice,
)


# ---------------------------------------------------------------------------
# Minimal mock classes to avoid dependency on the full variable implementation
# ---------------------------------------------------------------------------

class MockArrayVariable:
    def __init__(self, var_name):
        self.var_name = var_name


class MockMatrixVariable:
    def __init__(self, var_name):
        self.var_name = var_name


# ---------------------------------------------------------------------------
# Test cases
# ---------------------------------------------------------------------------

class TestConstraintDistinctArray(unittest.TestCase):
    def setUp(self):
        self.var = MockArrayVariable("x")

    def test_to_json(self):
        constraint = ConstraintDistinctArray(self.var, "c1")

        expected = {
            "name": "c1",
            "type": "distinct",
            "v1": "x",
            "selection": "standard",
        }

        self.assertEqual(constraint.to_json(), expected)

    def test_from_json(self):
        json_data = {
            "name": "c1",
            "type": "distinct",
            "v1": "x",
            "selection": "standard",
        }

        constraint = ConstraintDistinctArray.from_json(json_data, [self.var])

        self.assertIsInstance(constraint, ConstraintDistinctArray)
        self.assertEqual(constraint.var_1, self.var)
        self.assertEqual(constraint.constraint_name, "c1")

    def test_from_json_variable_not_found(self):
        json_data = {"v1": "missing"}

        with self.assertRaises(ValueError):
            ConstraintDistinctArray.from_json(json_data, [])


class TestConstraintDistinctRow(unittest.TestCase):
    def setUp(self):
        self.var = MockMatrixVariable("m")

    def test_to_json(self):
        constraint = ConstraintDistinctRow(self.var, size=4, idx=1, constraint_name="row1")

        expected = {
            "name": "row1",
            "type": "distinct",
            "v1": "m",
            "selection": "row",
            "size": 4,
            "index": 1,
        }

        self.assertEqual(constraint.to_json(), expected)

    def test_from_json(self):
        json_data = {
            "name": "row1",
            "v1": "m",
            "selection": "row",
            "size": 4,
            "index": 1,
        }

        constraint = ConstraintDistinctRow.from_json(json_data, [self.var])

        self.assertIsInstance(constraint, ConstraintDistinctRow)
        self.assertEqual(constraint.var_1, self.var)
        self.assertEqual(constraint.size, 4)
        self.assertEqual(constraint.idx, 1)
        self.assertEqual(constraint.constraint_name, "row1")

    def test_from_json_variable_not_found(self):
        json_data = {"v1": "missing", "size": 3, "index": 0}

        with self.assertRaises(ValueError):
            ConstraintDistinctRow.from_json(json_data, [])


class TestConstraintDistinctCol(unittest.TestCase):
    def setUp(self):
        self.var = MockMatrixVariable("m")

    def test_to_json(self):
        constraint = ConstraintDistinctCol(self.var, size=5, idx=2, constraint_name="col1")

        expected = {
            "name": "col1",
            "type": "distinct",
            "v1": "m",
            "selection": "col",
            "size": 5,
            "index": 2,
        }

        self.assertEqual(constraint.to_json(), expected)

    def test_from_json(self):
        json_data = {
            "name": "col1",
            "v1": "m",
            "selection": "col",
            "size": 5,
            "index": 2,
        }

        constraint = ConstraintDistinctCol.from_json(json_data, [self.var])

        self.assertIsInstance(constraint, ConstraintDistinctCol)
        self.assertEqual(constraint.size, 5)
        self.assertEqual(constraint.idx, 2)
        self.assertEqual(constraint.constraint_name, "col1")

    def test_from_json_variable_not_found(self):
        json_data = {"v1": "missing", "size": 3, "index": 0}

        with self.assertRaises(ValueError):
            ConstraintDistinctCol.from_json(json_data, [])


class TestConstraintDistinctSlice(unittest.TestCase):
    def setUp(self):
        self.var = MockMatrixVariable("m")

    def test_to_json(self):
        constraint = ConstraintDistinctSlice(
            self.var,
            size=6,
            offset_start_x=0,
            offset_start_y=1,
            offset_end_x=2,
            offset_end_y=3,
            constraint_name="slice1",
        )

        expected = {
            "name": "slice1",
            "type": "distinct",
            "v1": "m",
            "selection": "slice",
            "size": 6,
            "offset_start_x": 0,
            "offset_start_y": 1,
            "offset_end_x": 2,
            "offset_end_y": 3,
        }

        self.assertEqual(constraint.to_json(), expected)

    def test_from_json(self):
        json_data = {
            "name": "slice1",
            "v1": "m",
            "selection": "slice",
            "size": 6,
            "offset_start_x": 0,
            "offset_start_y": 1,
            "offset_end_x": 2,
            "offset_end_y": 3,
        }

        constraint = ConstraintDistinctSlice.from_json(json_data, [self.var])

        self.assertIsInstance(constraint, ConstraintDistinctSlice)
        self.assertEqual(constraint.size, 6)
        self.assertEqual(constraint.offset_start_x, 0)
        self.assertEqual(constraint.offset_start_y, 1)
        self.assertEqual(constraint.offset_end_x, 2)
        self.assertEqual(constraint.offset_end_y, 3)
        self.assertEqual(constraint.constraint_name, "slice1")

    def test_from_json_variable_not_found(self):
        json_data = {
            "v1": "missing",
            "size": 4,
            "offset_start_x": 0,
            "offset_start_y": 0,
            "offset_end_x": 1,
            "offset_end_y": 1,
        }

        with self.assertRaises(ValueError):
            ConstraintDistinctSlice.from_json(json_data, [])


if __name__ == "__main__":
    unittest.main()
