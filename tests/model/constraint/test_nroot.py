# pylint: skip-file

import unittest

from qaekwy.model.variable.integer import IntegerVariable
from qaekwy.model.constraint.nroot import ConstraintNRoot

class TestConstraintNRoot(unittest.TestCase):

    def setUp(self):
        self.variable_to_root = IntegerVariable("variable_to_root", 0, 10)
        self.n_value = 3
        self.result_variable = IntegerVariable("result_variable", 0, 10)

    def test_constraint_creation(self):
        constraint = ConstraintNRoot(
            self.variable_to_root,
            self.n_value,
            self.result_variable,
            "nroot_constraint"
        )
        self.assertEqual(constraint.var_1, self.variable_to_root)
        self.assertEqual(constraint.var_2, self.n_value)
        self.assertEqual(constraint.var_3, self.result_variable)
        self.assertEqual(constraint.constraint_name, "nroot_constraint")

    def test_constraint_to_json(self):
        constraint = ConstraintNRoot(
            self.variable_to_root,
            self.n_value,
            self.result_variable,
            "nroot_constraint"
        )
        expected_json = {
            "name": "nroot_constraint",
            "v1": "variable_to_root",
            "v2": 3,
            "v3": "result_variable",
            "type": "nroot"
        }
        self.assertEqual(constraint.to_json(), expected_json)

if __name__ == '__main__':
    unittest.main()
