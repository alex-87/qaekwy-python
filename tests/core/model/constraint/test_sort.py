# pylint: skip-file

import unittest

from qaekwy.core.model.variable.integer import IntegerVariableArray
from qaekwy.core.model.constraint.sort import ConstraintSorted, ConstraintReverseSorted


class TestConstraintSorted(unittest.TestCase):

    def test_sorted_constraint_creation(self):
        array_var = IntegerVariableArray("array_var", 10, 0, 200)
        sorted_constraint = ConstraintSorted(array_var, "sorted_constraint")

        self.assertEqual(sorted_constraint.var_1, array_var)
        self.assertEqual(sorted_constraint.constraint_name, "sorted_constraint")

    def test_sorted_constraint_to_json(self):
        array_var = IntegerVariableArray("array_var", 10, 0, 200)
        sorted_constraint = ConstraintSorted(array_var, "sorted_constraint")

        expected_json = {
            "name": "sorted_constraint",
            "v1": "array_var",
            "type": "sorted",
        }

        self.assertDictEqual(
            sorted_constraint.to_json(),
            sorted_constraint.from_json(expected_json, [array_var]).to_json(),
            expected_json,
        )


class TestConstraintReverseSorted(unittest.TestCase):

    def test_reverse_sorted_constraint_creation(self):
        array_var = IntegerVariableArray("array_var", 10, 0, 200)
        reverse_sorted_constraint = ConstraintReverseSorted(
            array_var, "reverse_sorted_constraint"
        )

        self.assertEqual(reverse_sorted_constraint.var_1, array_var)
        self.assertEqual(
            reverse_sorted_constraint.constraint_name, "reverse_sorted_constraint"
        )

    def test_reverse_sorted_constraint_to_json(self):
        array_var = IntegerVariableArray("array_var", 10, 0, 200)
        reverse_sorted_constraint = ConstraintReverseSorted(
            array_var, "reverse_sorted_constraint"
        )

        expected_json = {
            "name": "reverse_sorted_constraint",
            "v1": "array_var",
            "type": "rsorted",
        }

        self.assertDictEqual(
            reverse_sorted_constraint.to_json(),
            reverse_sorted_constraint.from_json(expected_json, [array_var]).to_json(),
            expected_json,
        )


if __name__ == "__main__":
    unittest.main()
