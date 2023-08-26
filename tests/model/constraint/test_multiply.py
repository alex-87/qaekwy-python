# pylint: skip-file

import unittest

from qaekwy.model.variable.integer import IntegerVariable
from qaekwy.model.constraint.multiply import ConstraintMultiply

class TestConstraintMultiply(unittest.TestCase):

    def setUp(self):
        self.variable_1 = IntegerVariable("variable_1", 0, 10)
        self.variable_2 = IntegerVariable("variable_2", 0, 10)
        self.result_variable = IntegerVariable("result_variable", 0, 10)

    def test_constraint_creation(self):
        constraint = ConstraintMultiply(
            self.variable_1,
            self.variable_2,
            self.result_variable,
            "multiply_constraint"
        )
        self.assertEqual(constraint.var_1, self.variable_1)
        self.assertEqual(constraint.var_2, self.variable_2)
        self.assertEqual(constraint.var_3, self.result_variable)
        self.assertEqual(constraint.constraint_name, "multiply_constraint")

    def test_constraint_to_json(self):
        constraint = ConstraintMultiply(
            self.variable_1,
            self.variable_2,
            self.result_variable,
            "multiply_constraint"
        )
        expected_json = {
            "name": "multiply_constraint",
            "v1": "variable_1",
            "v2": "variable_2",
            "v3": "result_variable",
            "type": "mul"
        }
        self.assertEqual(constraint.to_json(), expected_json)

if __name__ == '__main__':
    unittest.main()
