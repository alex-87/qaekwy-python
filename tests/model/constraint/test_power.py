# pylint: skip-file

import unittest

from qaekwy.model.variable.integer import IntegerVariable
from qaekwy.model.constraint.power import ConstraintPower

class TestConstraintPower(unittest.TestCase):

    def setUp(self):
        self.base_variable = IntegerVariable("base_variable", 0, 10)
        self.exponent_value = 2
        self.result_variable = IntegerVariable("result_variable", 0, 10)

    def test_constraint_creation(self):
        constraint = ConstraintPower(
            self.base_variable,
            self.exponent_value,
            self.result_variable,
            "power_constraint"
        )
        self.assertEqual(constraint.var_1, self.base_variable)
        self.assertEqual(constraint.var_2, self.exponent_value)
        self.assertEqual(constraint.var_3, self.result_variable)
        self.assertEqual(constraint.constraint_name, "power_constraint")

    def test_constraint_to_json(self):
        constraint = ConstraintPower(
            self.base_variable,
            self.exponent_value,
            self.result_variable,
            "power_constraint"
        )
        expected_json = {
            "name": "power_constraint",
            "v1": "base_variable",
            "v2": 2,
            "v3": "result_variable",
            "type": "pow"
        }
        self.assertEqual(constraint.to_json(), expected_json)

if __name__ == '__main__':
    unittest.main()
